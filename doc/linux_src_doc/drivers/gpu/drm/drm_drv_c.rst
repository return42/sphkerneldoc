.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_drv.c

.. _`drm_minor_acquire`:

drm_minor_acquire
=================

.. c:function:: struct drm_minor *drm_minor_acquire(unsigned int minor_id)

    Acquire a DRM minor

    :param unsigned int minor_id:
        Minor ID of the DRM-minor

.. _`drm_minor_acquire.description`:

Description
-----------

Looks up the given minor-ID and returns the respective DRM-minor object. The
refence-count of the underlying device is increased so you must release this
object with \ :c:func:`drm_minor_release`\ .

As long as you hold this minor, it is guaranteed that the object and the
minor->dev pointer will stay valid! However, the device may get unplugged and
unregistered while you hold the minor.

.. _`drm_minor_acquire.return`:

Return
------

Pointer to minor-object with increased device-refcount, or PTR_ERR on
failure.

.. _`drm_minor_release`:

drm_minor_release
=================

.. c:function:: void drm_minor_release(struct drm_minor *minor)

    Release DRM minor

    :param struct drm_minor \*minor:
        Pointer to DRM minor object

.. _`drm_minor_release.description`:

Description
-----------

Release a minor that was previously acquired via \ :c:func:`drm_minor_acquire`\ .

.. _`drm_put_dev`:

drm_put_dev
===========

.. c:function:: void drm_put_dev(struct drm_device *dev)

    Unregister and release a DRM device

    :param struct drm_device \*dev:
        DRM device

.. _`drm_put_dev.description`:

Description
-----------

Called at module unload time or when a PCI device is unplugged.

Cleans up all DRM device, calling \ :c:func:`drm_lastclose`\ .

.. _`drm_put_dev.note`:

Note
----

Use of this function is deprecated. It will eventually go away
completely.  Please use \ :c:func:`drm_dev_unregister`\  and \ :c:func:`drm_dev_unref`\  explicitly
instead to make sure that the device isn't userspace accessible any more
while teardown is in progress, ensuring that userspace can't access an
inconsistent state.

.. _`drm_dev_init`:

drm_dev_init
============

.. c:function:: int drm_dev_init(struct drm_device *dev, struct drm_driver *driver, struct device *parent)

    Initialise new DRM device

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_driver \*driver:
        DRM driver

    :param struct device \*parent:
        Parent device object

.. _`drm_dev_init.description`:

Description
-----------

Initialize a new DRM device. No device registration is done.
Call \ :c:func:`drm_dev_register`\  to advertice the device to user space and register it
with other core subsystems. This should be done last in the device
initialization sequence to make sure userspace can't access an inconsistent
state.

The initial ref-count of the object is 1. Use \ :c:func:`drm_dev_ref`\  and
\ :c:func:`drm_dev_unref`\  to take and drop further ref-counts.

Note that for purely virtual devices \ ``parent``\  can be NULL.

Drivers that do not want to allocate their own device struct
embedding struct \ :c:type:`struct drm_device <drm_device>` can call \ :c:func:`drm_dev_alloc`\  instead.

.. _`drm_dev_init.return`:

Return
------

0 on success, or error code on failure.

.. _`drm_dev_alloc`:

drm_dev_alloc
=============

.. c:function:: struct drm_device *drm_dev_alloc(struct drm_driver *driver, struct device *parent)

    Allocate new DRM device

    :param struct drm_driver \*driver:
        DRM driver to allocate device for

    :param struct device \*parent:
        Parent device object

.. _`drm_dev_alloc.description`:

Description
-----------

Allocate and initialize a new DRM device. No device registration is done.
Call \ :c:func:`drm_dev_register`\  to advertice the device to user space and register it
with other core subsystems. This should be done last in the device
initialization sequence to make sure userspace can't access an inconsistent
state.

The initial ref-count of the object is 1. Use \ :c:func:`drm_dev_ref`\  and
\ :c:func:`drm_dev_unref`\  to take and drop further ref-counts.

Note that for purely virtual devices \ ``parent``\  can be NULL.

Drivers that wish to subclass or embed struct \ :c:type:`struct drm_device <drm_device>` into their
own struct should look at using \ :c:func:`drm_dev_init`\  instead.

.. _`drm_dev_alloc.return`:

Return
------

Pointer to new DRM device, or NULL if out of memory.

.. _`drm_dev_ref`:

drm_dev_ref
===========

.. c:function:: void drm_dev_ref(struct drm_device *dev)

    Take reference of a DRM device

    :param struct drm_device \*dev:
        device to take reference of or NULL

.. _`drm_dev_ref.description`:

Description
-----------

This increases the ref-count of \ ``dev``\  by one. You \*must\* already own a
reference when calling this. Use \ :c:func:`drm_dev_unref`\  to drop this reference
again.

This function never fails. However, this function does not provide \*any\*
guarantee whether the device is alive or running. It only provides a
reference to the object and the memory associated with it.

.. _`drm_dev_unref`:

drm_dev_unref
=============

.. c:function:: void drm_dev_unref(struct drm_device *dev)

    Drop reference of a DRM device

    :param struct drm_device \*dev:
        device to drop reference of or NULL

.. _`drm_dev_unref.description`:

Description
-----------

This decreases the ref-count of \ ``dev``\  by one. The device is destroyed if the
ref-count drops to zero.

.. _`drm_dev_register`:

drm_dev_register
================

.. c:function:: int drm_dev_register(struct drm_device *dev, unsigned long flags)

    Register DRM device

    :param struct drm_device \*dev:
        Device to register

    :param unsigned long flags:
        Flags passed to the driver's .\ :c:func:`load`\  function

.. _`drm_dev_register.description`:

Description
-----------

Register the DRM device \ ``dev``\  with the system, advertise device to user-space
and start normal device operation. \ ``dev``\  must be allocated via \ :c:func:`drm_dev_alloc`\ 
previously.

Never call this twice on any device!

.. _`drm_dev_register.note`:

NOTE
----

To ensure backward compatibility with existing drivers method this
function calls the ->\ :c:func:`load`\  method after registering the device nodes,
creating race conditions. Usage of the ->\ :c:func:`load`\  methods is therefore
deprecated, drivers must perform all initialization before calling
\ :c:func:`drm_dev_register`\ .

.. _`drm_dev_register.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_dev_unregister`:

drm_dev_unregister
==================

.. c:function:: void drm_dev_unregister(struct drm_device *dev)

    Unregister DRM device

    :param struct drm_device \*dev:
        Device to unregister

.. _`drm_dev_unregister.description`:

Description
-----------

Unregister the DRM device from the system. This does the reverse of
\ :c:func:`drm_dev_register`\  but does not deallocate the device. The caller must call
\ :c:func:`drm_dev_unref`\  to drop their final reference.

This should be called first in the device teardown code to make sure
userspace can't access the device instance any more.

.. This file was automatic generated / don't edit.

