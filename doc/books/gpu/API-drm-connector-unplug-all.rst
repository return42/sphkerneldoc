.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-connector-unplug-all:

========================
drm_connector_unplug_all
========================

*man drm_connector_unplug_all(9)*

*4.6.0-rc5*

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

This function unregisters all connector userspace interfaces in sysfs.
Should be call when the device is disconnected, e.g. from an usb
driver's ->disconnect callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
