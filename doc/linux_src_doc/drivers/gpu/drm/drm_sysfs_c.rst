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

.. _`drm_sysfs_connector_add`:

drm_sysfs_connector_add
=======================

.. c:function:: int drm_sysfs_connector_add(struct drm_connector *connector)

    add a connector to sysfs

    :param struct drm_connector \*connector:
        connector to add

.. _`drm_sysfs_connector_add.description`:

Description
-----------

Create a connector device in sysfs, along with its associated connector
properties (so far, connection status, dpms, mode list & edid) and
generate a hotplug event so userspace knows there's a new connector
available.

.. _`drm_sysfs_connector_remove`:

drm_sysfs_connector_remove
==========================

.. c:function:: void drm_sysfs_connector_remove(struct drm_connector *connector)

    remove an connector device from sysfs

    :param struct drm_connector \*connector:
        connector to remove

.. _`drm_sysfs_connector_remove.description`:

Description
-----------

Remove \ ``connector``\  and its associated attributes from sysfs.  Note that
the device model core will take care of sending the "remove" uevent
at this time, so we don't need to do it.

.. _`drm_sysfs_connector_remove.note`:

Note
----

This routine should only be called if the connector was previously
successfully registered.  If \ ``connector``\  hasn't been registered yet,
you'll likely see a panic somewhere deep in sysfs code when called.

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

.. _`drm_sysfs_minor_alloc`:

drm_sysfs_minor_alloc
=====================

.. c:function:: struct device *drm_sysfs_minor_alloc(struct drm_minor *minor)

    Allocate sysfs device for given minor

    :param struct drm_minor \*minor:
        minor to allocate sysfs device for

.. _`drm_sysfs_minor_alloc.description`:

Description
-----------

This allocates a new sysfs device for \ ``minor``\  and returns it. The device is
not registered nor linked. The caller has to use \ :c:func:`device_add`\  and
\ :c:func:`device_del`\  to register and unregister it.

Note that \ :c:func:`dev_get_drvdata`\  on the new device will return the minor.
However, the device does not hold a ref-count to the minor nor to the
underlying drm_device. This is unproblematic as long as you access the
private data only in sysfs callbacks. \ :c:func:`device_del`\  disables those
synchronously, so they cannot be called after you cleanup a minor.

.. _`drm_class_device_register`:

drm_class_device_register
=========================

.. c:function:: int drm_class_device_register(struct device *dev)

    Register a struct device in the drm class.

    :param struct device \*dev:
        pointer to struct device to register.

.. _`drm_class_device_register.description`:

Description
-----------

\ ``dev``\  should have all relevant members pre-filled with the exception
of the class member. In particular, the device_type member must
be set.

.. This file was automatic generated / don't edit.

