.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_ioctl.h

.. _`drm_ioctl_t`:

drm_ioctl_t
===========

.. c:function:: int drm_ioctl_t(struct drm_device *dev, void *data, struct drm_file *file_priv)

    DRM ioctl function type.

    :param dev:
        DRM device inode
    :type dev: struct drm_device \*

    :param data:
        private pointer of the ioctl call
    :type data: void \*

    :param file_priv:
        DRM file this ioctl was made on
    :type file_priv: struct drm_file \*

.. _`drm_ioctl_t.description`:

Description
-----------

This is the DRM ioctl typedef. Note that \ :c:func:`drm_ioctl`\  has alrady copied \ ``data``\ 
into kernel-space, and will also copy it back, depending upon the read/write
settings in the ioctl command code.

.. _`drm_ioctl_compat_t`:

drm_ioctl_compat_t
==================

.. c:function:: int drm_ioctl_compat_t(struct file *filp, unsigned int cmd, unsigned long arg)

    compatibility DRM ioctl function type.

    :param filp:
        file pointer
    :type filp: struct file \*

    :param cmd:
        ioctl command code
    :type cmd: unsigned int

    :param arg:
        DRM file this ioctl was made on
    :type arg: unsigned long

.. _`drm_ioctl_compat_t.description`:

Description
-----------

Just a typedef to make declaring an array of compatibility handlers easier.
New drivers shouldn't screw up the structure layout for their ioctl
structures and hence never need this.

.. _`drm_ioctl_flags`:

enum drm_ioctl_flags
====================

.. c:type:: enum drm_ioctl_flags

    DRM ioctl flags

.. _`drm_ioctl_flags.definition`:

Definition
----------

.. code-block:: c

    enum drm_ioctl_flags {
        DRM_AUTH,
        DRM_MASTER,
        DRM_ROOT_ONLY,
        DRM_UNLOCKED,
        DRM_RENDER_ALLOW
    };

.. _`drm_ioctl_flags.constants`:

Constants
---------

DRM_AUTH

    This is for ioctl which are used for rendering, and require that the
    file descriptor is either for a render node, or if it's a
    legacy/primary node, then it must be authenticated.

DRM_MASTER

    This must be set for any ioctl which can change the modeset or
    display state. Userspace must call the ioctl through a primary node,
    while it is the active master.

    Note that read-only modeset ioctl can also be called by
    unauthenticated clients, or when a master is not the currently active
    one.

DRM_ROOT_ONLY

    Anything that could potentially wreak a master file descriptor needs
    to have this flag set. Current that's only for the SETMASTER and
    DROPMASTER ioctl, which e.g. logind can call to force a non-behaving
    master (display compositor) into compliance.

    This is equivalent to callers with the SYSADMIN capability.

DRM_UNLOCKED

    Whether \ :c:type:`drm_ioctl_desc.func <drm_ioctl_desc>`\  should be called with the DRM BKL held
    or not. Enforced as the default for all modern drivers, hence there
    should never be a need to set this flag.

DRM_RENDER_ALLOW

    This is used for all ioctl needed for rendering only, for drivers
    which support render nodes. This should be all new render drivers,
    and hence it should be always set for any ioctl with DRM_AUTH set.
    Note though that read-only query ioctl might have this set, but have
    not set DRM_AUTH because they do not require authentication.

.. _`drm_ioctl_flags.description`:

Description
-----------

Various flags that can be set in \ :c:type:`drm_ioctl_desc.flags <drm_ioctl_desc>`\  to control how
userspace can use a given ioctl.

.. _`drm_ioctl_desc`:

struct drm_ioctl_desc
=====================

.. c:type:: struct drm_ioctl_desc

    DRM driver ioctl entry

.. _`drm_ioctl_desc.definition`:

Definition
----------

.. code-block:: c

    struct drm_ioctl_desc {
        unsigned int cmd;
        enum drm_ioctl_flags flags;
        drm_ioctl_t *func;
        const char *name;
    }

.. _`drm_ioctl_desc.members`:

Members
-------

cmd
    ioctl command number, without flags

flags
    a bitmask of \ :c:type:`enum drm_ioctl_flags <drm_ioctl_flags>`\ 

func
    handler for this ioctl

name
    user-readable name for debug output

.. _`drm_ioctl_desc.description`:

Description
-----------

For convenience it's easier to create these using the \ :c:func:`DRM_IOCTL_DEF_DRV`\ 
macro.

.. _`drm_ioctl_def_drv`:

DRM_IOCTL_DEF_DRV
=================

.. c:function::  DRM_IOCTL_DEF_DRV( ioctl,  _func,  _flags)

    helper macro to fill out a \ :c:type:`struct drm_ioctl_desc <drm_ioctl_desc>`\ 

    :param ioctl:
        ioctl command suffix
    :type ioctl: 

    :param _func:
        handler for the ioctl
    :type _func: 

    :param _flags:
        a bitmask of \ :c:type:`enum drm_ioctl_flags <drm_ioctl_flags>`\ 
    :type _flags: 

.. _`drm_ioctl_def_drv.description`:

Description
-----------

Small helper macro to create a \ :c:type:`struct drm_ioctl_desc <drm_ioctl_desc>`\  entry. The ioctl
command number is constructed by prepending ``DRM_IOCTL\_`` and passing that
to \ :c:func:`DRM_IOCTL_NR`\ .

.. This file was automatic generated / don't edit.

