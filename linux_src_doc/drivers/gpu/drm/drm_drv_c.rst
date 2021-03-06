.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_drv.c

.. _`driver-instance-overview`:

driver instance overview
========================

A device instance for a drm driver is represented by \ :c:type:`struct drm_device <drm_device>`\ . This
is allocated with \ :c:func:`drm_dev_alloc`\ , usually from bus-specific ->probe()
callbacks implemented by the driver. The driver then needs to initialize all
the various subsystems for the drm device like memory management, vblank
handling, modesetting support and intial output configuration plus obviously
initialize all the corresponding hardware bits. An important part of this is
also calling \ :c:func:`drm_dev_set_unique`\  to set the userspace-visible unique name of
this device instance. Finally when everything is up and running and ready for
userspace the device instance can be published using \ :c:func:`drm_dev_register`\ .

There is also deprecated support for initalizing device instances using
bus-specific helpers and the \ :c:type:`drm_driver.load <drm_driver>`\  callback. But due to
backwards-compatibility needs the device instance have to be published too
early, which requires unpretty global locking to make safe and is therefore
only support for existing drivers not yet converted to the new scheme.

When cleaning up a device instance everything needs to be done in reverse:
First unpublish the device instance with \ :c:func:`drm_dev_unregister`\ . Then clean up
any other resources allocated at device initialization and drop the driver's
reference to \ :c:type:`struct drm_device <drm_device>`\  using \ :c:func:`drm_dev_put`\ .

Note that the lifetime rules for \ :c:type:`struct drm_device <drm_device>`\  instance has still a lot of
historical baggage. Hence use the reference counting provided by
\ :c:func:`drm_dev_get`\  and \ :c:func:`drm_dev_put`\  only carefully.

It is recommended that drivers embed \ :c:type:`struct drm_device <drm_device>`\  into their own device
structure, which is supported through \ :c:func:`drm_dev_init`\ .

.. _`drm_put_dev`:

drm_put_dev
===========

.. c:function:: void drm_put_dev(struct drm_device *dev)

    Unregister and release a DRM device

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_put_dev.description`:

Description
-----------

Called at module unload time or when a PCI device is unplugged.

Cleans up all DRM device, calling \ :c:func:`drm_lastclose`\ .

.. _`drm_put_dev.note`:

Note
----

Use of this function is deprecated. It will eventually go away
completely.  Please use \ :c:func:`drm_dev_unregister`\  and \ :c:func:`drm_dev_put`\  explicitly
instead to make sure that the device isn't userspace accessible any more
while teardown is in progress, ensuring that userspace can't access an
inconsistent state.

.. _`drm_dev_enter`:

drm_dev_enter
=============

.. c:function:: bool drm_dev_enter(struct drm_device *dev, int *idx)

    Enter device critical section

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param idx:
        Pointer to index that will be passed to the matching \ :c:func:`drm_dev_exit`\ 
    :type idx: int \*

.. _`drm_dev_enter.description`:

Description
-----------

This function marks and protects the beginning of a section that should not
be entered after the device has been unplugged. The section end is marked
with \ :c:func:`drm_dev_exit`\ . Calls to this function can be nested.

.. _`drm_dev_enter.return`:

Return
------

True if it is OK to enter the section, false otherwise.

.. _`drm_dev_exit`:

drm_dev_exit
============

.. c:function:: void drm_dev_exit(int idx)

    Exit device critical section

    :param idx:
        index returned from \ :c:func:`drm_dev_enter`\ 
    :type idx: int

.. _`drm_dev_exit.description`:

Description
-----------

This function marks the end of a section that should not be entered after
the device has been unplugged.

.. _`drm_dev_unplug`:

drm_dev_unplug
==============

.. c:function:: void drm_dev_unplug(struct drm_device *dev)

    unplug a DRM device

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_dev_unplug.description`:

Description
-----------

This unplugs a hotpluggable DRM device, which makes it inaccessible to
userspace operations. Entry-points can use \ :c:func:`drm_dev_enter`\  and
\ :c:func:`drm_dev_exit`\  to protect device resources in a race free manner. This
essentially unregisters the device like \ :c:func:`drm_dev_unregister`\ , but can be
called while there are still open users of \ ``dev``\ .

.. _`drm_dev_init`:

drm_dev_init
============

.. c:function:: int drm_dev_init(struct drm_device *dev, struct drm_driver *driver, struct device *parent)

    Initialise new DRM device

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param driver:
        DRM driver
    :type driver: struct drm_driver \*

    :param parent:
        Parent device object
    :type parent: struct device \*

.. _`drm_dev_init.description`:

Description
-----------

Initialize a new DRM device. No device registration is done.
Call \ :c:func:`drm_dev_register`\  to advertice the device to user space and register it
with other core subsystems. This should be done last in the device
initialization sequence to make sure userspace can't access an inconsistent
state.

The initial ref-count of the object is 1. Use \ :c:func:`drm_dev_get`\  and
\ :c:func:`drm_dev_put`\  to take and drop further ref-counts.

Note that for purely virtual devices \ ``parent``\  can be NULL.

Drivers that do not want to allocate their own device struct
embedding \ :c:type:`struct drm_device <drm_device>`\  can call \ :c:func:`drm_dev_alloc`\  instead. For drivers
that do embed \ :c:type:`struct drm_device <drm_device>`\  it must be placed first in the overall
structure, and the overall structure must be allocated using \ :c:func:`kmalloc`\ : The
drm core's release function unconditionally calls \ :c:func:`kfree`\  on the \ ``dev``\  pointer
when the final reference is released. To override this behaviour, and so
allow embedding of the drm_device inside the driver's device struct at an
arbitrary offset, you must supply a \ :c:type:`drm_driver.release <drm_driver>`\  callback and control
the finalization explicitly.

.. _`drm_dev_init.return`:

Return
------

0 on success, or error code on failure.

.. _`drm_dev_fini`:

drm_dev_fini
============

.. c:function:: void drm_dev_fini(struct drm_device *dev)

    Finalize a dead DRM device

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_dev_fini.description`:

Description
-----------

Finalize a dead DRM device. This is the converse to \ :c:func:`drm_dev_init`\  and
frees up all data allocated by it. All driver private data should be
finalized first. Note that this function does not free the \ ``dev``\ , that is
left to the caller.

The ref-count of \ ``dev``\  must be zero, and \ :c:func:`drm_dev_fini`\  should only be called
from a \ :c:type:`drm_driver.release <drm_driver>`\  callback.

.. _`drm_dev_alloc`:

drm_dev_alloc
=============

.. c:function:: struct drm_device *drm_dev_alloc(struct drm_driver *driver, struct device *parent)

    Allocate new DRM device

    :param driver:
        DRM driver to allocate device for
    :type driver: struct drm_driver \*

    :param parent:
        Parent device object
    :type parent: struct device \*

.. _`drm_dev_alloc.description`:

Description
-----------

Allocate and initialize a new DRM device. No device registration is done.
Call \ :c:func:`drm_dev_register`\  to advertice the device to user space and register it
with other core subsystems. This should be done last in the device
initialization sequence to make sure userspace can't access an inconsistent
state.

The initial ref-count of the object is 1. Use \ :c:func:`drm_dev_get`\  and
\ :c:func:`drm_dev_put`\  to take and drop further ref-counts.

Note that for purely virtual devices \ ``parent``\  can be NULL.

Drivers that wish to subclass or embed \ :c:type:`struct drm_device <drm_device>`\  into their
own struct should look at using \ :c:func:`drm_dev_init`\  instead.

.. _`drm_dev_alloc.return`:

Return
------

Pointer to new DRM device, or ERR_PTR on failure.

.. _`drm_dev_get`:

drm_dev_get
===========

.. c:function:: void drm_dev_get(struct drm_device *dev)

    Take reference of a DRM device

    :param dev:
        device to take reference of or NULL
    :type dev: struct drm_device \*

.. _`drm_dev_get.description`:

Description
-----------

This increases the ref-count of \ ``dev``\  by one. You *must* already own a
reference when calling this. Use \ :c:func:`drm_dev_put`\  to drop this reference
again.

This function never fails. However, this function does not provide *any*
guarantee whether the device is alive or running. It only provides a
reference to the object and the memory associated with it.

.. _`drm_dev_put`:

drm_dev_put
===========

.. c:function:: void drm_dev_put(struct drm_device *dev)

    Drop reference of a DRM device

    :param dev:
        device to drop reference of or NULL
    :type dev: struct drm_device \*

.. _`drm_dev_put.description`:

Description
-----------

This decreases the ref-count of \ ``dev``\  by one. The device is destroyed if the
ref-count drops to zero.

.. _`drm_dev_unref`:

drm_dev_unref
=============

.. c:function:: void drm_dev_unref(struct drm_device *dev)

    Drop reference of a DRM device

    :param dev:
        device to drop reference of or NULL
    :type dev: struct drm_device \*

.. _`drm_dev_unref.description`:

Description
-----------

This is a compatibility alias for \ :c:func:`drm_dev_put`\  and should not be used by new
code.

.. _`drm_dev_register`:

drm_dev_register
================

.. c:function:: int drm_dev_register(struct drm_device *dev, unsigned long flags)

    Register DRM device

    :param dev:
        Device to register
    :type dev: struct drm_device \*

    :param flags:
        Flags passed to the driver's .load() function
    :type flags: unsigned long

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
function calls the \ :c:type:`drm_driver.load <drm_driver>`\  method after registering the device
nodes, creating race conditions. Usage of the \ :c:type:`drm_driver.load <drm_driver>`\  methods is
therefore deprecated, drivers must perform all initialization before calling
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

    :param dev:
        Device to unregister
    :type dev: struct drm_device \*

.. _`drm_dev_unregister.description`:

Description
-----------

Unregister the DRM device from the system. This does the reverse of
\ :c:func:`drm_dev_register`\  but does not deallocate the device. The caller must call
\ :c:func:`drm_dev_put`\  to drop their final reference.

A special form of unregistering for hotpluggable devices is \ :c:func:`drm_dev_unplug`\ ,
which can be called while there are still open users of \ ``dev``\ .

This should be called first in the device teardown code to make sure
userspace can't access the device instance any more.

.. _`drm_dev_set_unique`:

drm_dev_set_unique
==================

.. c:function:: int drm_dev_set_unique(struct drm_device *dev, const char *name)

    Set the unique name of a DRM device

    :param dev:
        device of which to set the unique name
    :type dev: struct drm_device \*

    :param name:
        unique name
    :type name: const char \*

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

.. This file was automatic generated / don't edit.

