.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_sysfs.c

.. _`drm_sysfs_init`:

drm_sysfs_init
==============

.. c:function:: int drm_sysfs_init( void)

    initialize sysfs helpers

    :param  void:
        no arguments

.. _`drm_sysfs_init.description`:

Description
-----------

This is used to create the DRM class, which is the implicit parent of any
other top-level DRM sysfs objects.

You must call \ :c:func:`drm_sysfs_destroy`\  to release the allocated resources.

.. _`drm_sysfs_init.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_sysfs_destroy`:

drm_sysfs_destroy
=================

.. c:function:: void drm_sysfs_destroy( void)

    destroys DRM class

    :param  void:
        no arguments

.. _`drm_sysfs_destroy.description`:

Description
-----------

Destroy the DRM device class.

.. _`drm_sysfs_hotplug_event`:

drm_sysfs_hotplug_event
=======================

.. c:function:: void drm_sysfs_hotplug_event(struct drm_device *dev)

    generate a DRM uevent

    :param struct drm_device \*dev:
        DRM device

.. _`drm_sysfs_hotplug_event.description`:

Description
-----------

Send a uevent for the DRM device specified by \ ``dev``\ .  Currently we only
set HOTPLUG=1 in the uevent environment, but this could be expanded to
deal with other types of events.

.. _`drm_class_device_register`:

drm_class_device_register
=========================

.. c:function:: int drm_class_device_register(struct device *dev)

    register new device with the DRM sysfs class

    :param struct device \*dev:
        device to register

.. _`drm_class_device_register.description`:

Description
-----------

Registers a new \ :c:type:`struct device <device>`\  within the DRM sysfs class. Essentially only
used by ttm to have a place for its global settings. Drivers should never use
this.

.. _`drm_class_device_unregister`:

drm_class_device_unregister
===========================

.. c:function:: void drm_class_device_unregister(struct device *dev)

    unregister device with the DRM sysfs class

    :param struct device \*dev:
        device to unregister

.. _`drm_class_device_unregister.description`:

Description
-----------

Unregisters a \ :c:type:`struct device <device>`\  from the DRM sysfs class. Essentially only used
by ttm to have a place for its global settings. Drivers should never use
this.

.. This file was automatic generated / don't edit.

