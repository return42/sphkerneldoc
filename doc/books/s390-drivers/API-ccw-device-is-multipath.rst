
.. _API-ccw-device-is-multipath:

=======================
ccw_device_is_multipath
=======================

*man ccw_device_is_multipath(9)*

*4.6.0-rc1*

determine if device is operating in multipath mode


Synopsis
========

.. c:function:: int ccw_device_is_multipath( struct ccw_device * cdev )

Arguments
=========

``cdev``
    ccw device


Description
===========

Return non-zero if device is operating in multipath mode, zero otherwise.
