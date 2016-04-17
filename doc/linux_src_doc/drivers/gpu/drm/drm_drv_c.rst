.. -*- coding: utf-8; mode: rst -*-

=========
drm_drv.c
=========


.. _`drm_minor_acquire`:

drm_minor_acquire
=================

.. c:function:: struct drm_minor *drm_minor_acquire (unsigned int minor_id)

    Acquire a DRM minor

    :param unsigned int minor_id:
        Minor ID of the DRM-minor



.. _`drm_minor_acquire.description`:

Description
-----------

Looks up the given minor-ID and returns the respective DRM-minor object. The
refence-count of the underlying device is increased so you must release this
object with :c:func:`drm_minor_release`.

As long as you hold this minor, it is guaranteed that the object and the
minor->dev pointer will stay valid! However, the device may get unplugged and
unregistered while you hold the minor.



.. _`drm_minor_acquire.returns`:

Returns
-------

Pointer to minor-object with increased device-refcount, or PTR_ERR on
failure.



.. _`drm_minor_release`:

drm_minor_release
=================

.. c:function:: void drm_minor_release (struct drm_minor *minor)

    Release DRM minor

    :param struct drm_minor \*minor:
        Pointer to DRM minor object



.. _`drm_minor_release.description`:

Description
-----------

Release a minor that was previously acquired via :c:func:`drm_minor_acquire`.



.. _`driver-instance-overview`:

driver instance overview
========================

A device instance for a drm driver is represented by struct :c:type:`struct drm_device <drm_device>`. This
is allocated with :c:func:`drm_dev_alloc`, usually from bus-specific ->:c:func:`probe`
callbacks implemented by the driver. The driver then needs to initialize all
the various subsystems for the drm device like memory management, vblank
handling, modesetting support and intial output configuration plus obviously
initialize all the corresponding hardware bits. An important part of this is
also calling :c:func:`drm_dev_set_unique` to set the userspace-visible unique name of
this device instance. Finally when everything is up and running and ready for
userspace the device instance can be published using :c:func:`drm_dev_register`.

There is also deprecated support for initalizing device instances using
bus-specific helpers and the ->:c:func:`load` callback. But due to
backwards-compatibility needs the device instance have to be published too
early, which requires unpretty global locking to make safe and is therefore
only support for existing drivers not yet converted to the new scheme.

When cleaning up a device instance everything needs to be done in reverse:
First unpublish the device instance with :c:func:`drm_dev_unregister`. Then clean up
any other resources allocated at device initialization and drop the driver's
reference to :c:type:`struct drm_device <drm_device>` using :c:func:`drm_dev_unref`.

Note that the lifetime rules for :c:type:`struct drm_device <drm_device>` instance has still a lot of
historical baggage. Hence use the reference counting provided by
:c:func:`drm_dev_ref` and :c:func:`drm_dev_unref` only carefully.

Also note that embedding of :c:type:`struct drm_device <drm_device>` is currently not (yet) supported (but
it would be easy to add). Drivers can store driver-private data in the
dev_priv field of :c:type:`struct drm_device <drm_device>`.



.. _`drm_put_dev`:

drm_put_dev
===========

.. c:function:: void drm_put_dev (struct drm_device *dev)

    Unregister and release a DRM device

    :param struct drm_device \*dev:
        DRM device



.. _`drm_put_dev.description`:

Description
-----------

Called at module unload time or when a PCI device is unplugged.

Cleans up all DRM device, calling :c:func:`drm_lastclose`.



.. _`drm_put_dev.note`:

Note
----

Use of this function is deprecated. It will eventually go away
completely.  Please use :c:func:`drm_dev_unregister` and :c:func:`drm_dev_unref` explicitly
instead to make sure that the device isn't userspace accessible any more
while teardown is in progress, ensuring that userspace can't access an
inconsistent state.



.. _`drm_dev_alloc`:

drm_dev_alloc
=============

.. c:function:: struct drm_device *drm_dev_alloc (struct drm_driver *driver, struct device *parent)

    Allocate new DRM device

    :param struct drm_driver \*driver:
        DRM driver to allocate device for

    :param struct device \*parent:
        Parent device object



.. _`drm_dev_alloc.description`:

Description
-----------

Allocate and initialize a new DRM device. No device registration is done.
Call :c:func:`drm_dev_register` to advertice the device to user space and register it
with other core subsystems. This should be done last in the device
initialization sequence to make sure userspace can't access an inconsistent
state.

The initial ref-count of the object is 1. Use :c:func:`drm_dev_ref` and
:c:func:`drm_dev_unref` to take and drop further ref-counts.

Note that for purely virtual devices ``parent`` can be NULL.



.. _`drm_dev_alloc.returns`:

RETURNS
-------

Pointer to new DRM device, or NULL if out of memory.



.. _`drm_dev_ref`:

drm_dev_ref
===========

.. c:function:: void drm_dev_ref (struct drm_device *dev)

    Take reference of a DRM device

    :param struct drm_device \*dev:
        device to take reference of or NULL



.. _`drm_dev_ref.description`:

Description
-----------

This increases the ref-count of ``dev`` by one. You \*must\* already own a
reference when calling this. Use :c:func:`drm_dev_unref` to drop this reference
again.

This function never fails. However, this function does not provide \*any*
guarantee whether the device is alive or running. It only provides a
reference to the object and the memory associated with it.



.. _`drm_dev_unref`:

drm_dev_unref
=============

.. c:function:: void drm_dev_unref (struct drm_device *dev)

    Drop reference of a DRM device

    :param struct drm_device \*dev:
        device to drop reference of or NULL



.. _`drm_dev_unref.description`:

Description
-----------

This decreases the ref-count of ``dev`` by one. The device is destroyed if the
ref-count drops to zero.



.. _`drm_dev_register`:

drm_dev_register
================

.. c:function:: int drm_dev_register (struct drm_device *dev, unsigned long flags)

    Register DRM device

    :param struct drm_device \*dev:
        Device to register

    :param unsigned long flags:
        Flags passed to the driver's .:c:func:`load` function



.. _`drm_dev_register.description`:

Description
-----------

Register the DRM device ``dev`` with the system, advertise device to user-space
and start normal device operation. ``dev`` must be allocated via :c:func:`drm_dev_alloc`
previously.

Never call this twice on any device!



.. _`drm_dev_register.note`:

NOTE
----

To ensure backward compatibility with existing drivers method this
function calls the ->:c:func:`load` method after registering the device nodes,
creating race conditions. Usage of the ->:c:func:`load` methods is therefore
deprecated, drivers must perform all initialization before calling
:c:func:`drm_dev_register`.



.. _`drm_dev_register.returns`:

RETURNS
-------

0 on success, negative error code on failure.



.. _`drm_dev_unregister`:

drm_dev_unregister
==================

.. c:function:: void drm_dev_unregister (struct drm_device *dev)

    Unregister DRM device

    :param struct drm_device \*dev:
        Device to unregister



.. _`drm_dev_unregister.description`:

Description
-----------

Unregister the DRM device from the system. This does the reverse of
:c:func:`drm_dev_register` but does not deallocate the device. The caller must call
:c:func:`drm_dev_unref` to drop their final reference.

This should be called first in the device teardown code to make sure
userspace can't access the device instance any more.



.. _`drm_dev_set_unique`:

drm_dev_set_unique
==================

.. c:function:: int drm_dev_set_unique (struct drm_device *dev, const char *name)

    Set the unique name of a DRM device

    :param struct drm_device \*dev:
        device of which to set the unique name

    :param const char \*name:
        unique name



.. _`drm_dev_set_unique.description`:

Description
-----------

Sets the unique name of a DRM device using the specified string. Drivers
can use this at driver probe time if the unique name of the devices they
drive is static.



.. _`drm_dev_set_unique.return`:

Return
------

0 on success or a negative error code on failure.

