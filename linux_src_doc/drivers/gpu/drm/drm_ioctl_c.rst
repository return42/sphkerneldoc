.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_ioctl.c

.. _`getunique-and-setversion-story`:

getunique and setversion story
==============================

BEWARE THE DRAGONS! MIND THE TRAPDOORS!

In an attempt to warn anyone else who's trying to figure out what's going
on here, I'll try to summarize the story. First things first, let's clear up
the names, because the kernel internals, libdrm and the ioctls are all named
differently:

 - GET_UNIQUE ioctl, implemented by drm_getunique is wrapped up in libdrm
   through the drmGetBusid function.
 - The libdrm drmSetBusid function is backed by the SET_UNIQUE ioctl. All
   that code is nerved in the kernel with \ :c:func:`drm_invalid_op`\ .
 - The internal set_busid kernel functions and driver callbacks are
   exclusively use by the SET_VERSION ioctl, because only drm 1.0 (which is
   nerved) allowed userspace to set the busid through the above ioctl.
 - Other ioctls and functions involved are named consistently.

For anyone wondering what's the difference between drm 1.1 and 1.4: Correctly
handling pci domains in the busid on ppc. Doing this correctly was only
implemented in libdrm in 2010, hence can't be nerved yet. No one knows what's
special with drm 1.2 and 1.3.

Now the actual horror story of how device lookup in drm works. At large,
there's 2 different ways, either by busid, or by device driver name.

Opening by busid is fairly simple:

1. First call SET_VERSION to make sure pci domains are handled properly. As a
   side-effect this fills out the unique name in the master structure.
2. Call GET_UNIQUE to read out the unique name from the master structure,
   which matches the busid thanks to step 1. If it doesn't, proceed to try
   the next device node.

Opening by name is slightly different:

1. Directly call VERSION to get the version and to match against the driver
   name returned by that ioctl. Note that SET_VERSION is not called, which
   means the the unique name for the master node just opening is _not_ filled
   out. This despite that with current drm device nodes are always bound to
   one device, and can't be runtime assigned like with drm 1.0.
2. Match driver name. If it mismatches, proceed to the next device node.
3. Call GET_UNIQUE, and check whether the unique name has length zero (by
   checking that the first byte in the string is 0). If that's not the case
   libdrm skips and proceeds to the next device node. Probably this is just
   copypasta from drm 1.0 times where a set unique name meant that the driver
   was in use already, but that's just conjecture.

Long story short: To keep the open by name logic working, GET_UNIQUE must
_not_ return a unique string when SET_VERSION hasn't been called yet,
otherwise libdrm breaks. Even when that unique string can't ever change, and
is totally irrelevant for actually opening the device because runtime
assignable device instances were only support in drm 1.0, which is long dead.
But the libdrm code in drmOpenByName somehow survived, hence this can't be
broken.

.. _`drm_noop`:

drm_noop
========

.. c:function:: int drm_noop(struct drm_device *dev, void *data, struct drm_file *file_priv)

    DRM no-op ioctl implemntation

    :param dev:
        DRM device for the ioctl
    :type dev: struct drm_device \*

    :param data:
        data pointer for the ioctl
    :type data: void \*

    :param file_priv:
        DRM file for the ioctl call
    :type file_priv: struct drm_file \*

.. _`drm_noop.description`:

Description
-----------

This no-op implementation for drm ioctls is useful for deprecated
functionality where we can't return a failure code because existing userspace
checks the result of the ioctl, but doesn't care about the action.

Always returns successfully with 0.

.. _`drm_invalid_op`:

drm_invalid_op
==============

.. c:function:: int drm_invalid_op(struct drm_device *dev, void *data, struct drm_file *file_priv)

    DRM invalid ioctl implemntation

    :param dev:
        DRM device for the ioctl
    :type dev: struct drm_device \*

    :param data:
        data pointer for the ioctl
    :type data: void \*

    :param file_priv:
        DRM file for the ioctl call
    :type file_priv: struct drm_file \*

.. _`drm_invalid_op.description`:

Description
-----------

This no-op implementation for drm ioctls is useful for deprecated
functionality where we really don't want to allow userspace to call the ioctl
any more. This is the case for old ums interfaces for drivers that
transitioned to kms gradually and so kept the old legacy tables around. This
only applies to radeon and i915 kms drivers, other drivers shouldn't need to
use this function.

Always fails with a return value of -EINVAL.

.. _`drm_ioctl_permit`:

drm_ioctl_permit
================

.. c:function:: int drm_ioctl_permit(u32 flags, struct drm_file *file_priv)

    Check ioctl permissions against caller

    :param flags:
        ioctl permission flags.
    :type flags: u32

    :param file_priv:
        Pointer to struct drm_file identifying the caller.
    :type file_priv: struct drm_file \*

.. _`drm_ioctl_permit.description`:

Description
-----------

Checks whether the caller is allowed to run an ioctl with the
indicated permissions.

.. _`drm_ioctl_permit.return`:

Return
------

Zero if allowed, -EACCES otherwise.

.. _`driver-specific-ioctls`:

driver specific ioctls
======================

First things first, driver private IOCTLs should only be needed for drivers
supporting rendering. Kernel modesetting is all standardized, and extended
through properties. There are a few exceptions in some existing drivers,
which define IOCTL for use by the display DRM master, but they all predate
properties.

Now if you do have a render driver you always have to support it through
driver private properties. There's a few steps needed to wire all the things
up.

First you need to define the structure for your IOCTL in your driver private
UAPI header in ``include/uapi/drm/my_driver_drm.h``::

    struct my_driver_operation {
            u32 some_thing;
            u32 another_thing;
    };

Please make sure that you follow all the best practices from
``Documentation/ioctl/botching-up-ioctls.txt``. Note that \ :c:func:`drm_ioctl`\ 
automatically zero-extends structures, hence make sure you can add more stuff
at the end, i.e. don't put a variable sized array there.

Then you need to define your IOCTL number, using one of \ :c:func:`DRM_IO`\ , \ :c:func:`DRM_IOR`\ ,
\ :c:func:`DRM_IOW`\  or \ :c:func:`DRM_IOWR`\ . It must start with the DRM_IOCTL\_ prefix::

    ##define DRM_IOCTL_MY_DRIVER_OPERATION \
        DRM_IOW(DRM_COMMAND_BASE, struct my_driver_operation)

DRM driver private IOCTL must be in the range from DRM_COMMAND_BASE to
DRM_COMMAND_END. Finally you need an array of \ :c:type:`struct drm_ioctl_desc <drm_ioctl_desc>`\  to wire
up the handlers and set the access rights::

    static const struct drm_ioctl_desc my_driver_ioctls[] = {
        DRM_IOCTL_DEF_DRV(MY_DRIVER_OPERATION, my_driver_operation,
                DRM_AUTH|DRM_RENDER_ALLOW),
    };

And then assign this to the \ :c:type:`drm_driver.ioctls <drm_driver>`\  field in your driver
structure.

See the separate chapter on :ref:`file operations<drm_driver_fops>` for how
the driver-specific IOCTLs are wired up.

.. _`drm_ioctl`:

drm_ioctl
=========

.. c:function:: long drm_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)

    ioctl callback implementation for DRM drivers

    :param filp:
        file this ioctl is called on
    :type filp: struct file \*

    :param cmd:
        ioctl cmd number
    :type cmd: unsigned int

    :param arg:
        user argument
    :type arg: unsigned long

.. _`drm_ioctl.description`:

Description
-----------

Looks up the ioctl function in the DRM core and the driver dispatch table,
stored in \ :c:type:`drm_driver.ioctls <drm_driver>`\ . It checks for necessary permission by calling
\ :c:func:`drm_ioctl_permit`\ , and dispatches to the respective function.

.. _`drm_ioctl.return`:

Return
------

Zero on success, negative error code on failure.

.. _`drm_ioctl_flags`:

drm_ioctl_flags
===============

.. c:function:: bool drm_ioctl_flags(unsigned int nr, unsigned int *flags)

    Check for core ioctl and return ioctl permission flags

    :param nr:
        ioctl number
    :type nr: unsigned int

    :param flags:
        where to return the ioctl permission flags
    :type flags: unsigned int \*

.. _`drm_ioctl_flags.description`:

Description
-----------

This ioctl is only used by the vmwgfx driver to augment the access checks
done by the drm core and insofar a pretty decent layering violation. This
shouldn't be used by any drivers.

.. _`drm_ioctl_flags.return`:

Return
------

True if the \ ``nr``\  corresponds to a DRM core ioctl number, false otherwise.

.. This file was automatic generated / don't edit.

