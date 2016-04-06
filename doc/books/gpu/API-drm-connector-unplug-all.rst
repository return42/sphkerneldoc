
.. _API-drm-connector-unplug-all:

========================
drm_connector_unplug_all
========================

*man drm_connector_unplug_all(9)*

*4.6.0-rc1*

unregister connector userspace interfaces


Synopsis
========

.. c:function:: void drm_connector_unplug_all( struct drm_device * dev )

Arguments
=========

``dev``
    drm device


Description
===========

This function unregisters all connector userspace interfaces in sysfs. Should be call when the device is disconnected, e.g. from an usb driver's ->disconnect callback.
