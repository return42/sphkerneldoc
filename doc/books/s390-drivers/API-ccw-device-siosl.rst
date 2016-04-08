
.. _API-ccw-device-siosl:

================
ccw_device_siosl
================

*man ccw_device_siosl(9)*

*4.6.0-rc1*

initiate logging


Synopsis
========

.. c:function:: int ccw_device_siosl( struct ccw_device * cdev )

Arguments
=========

``cdev``
    ccw device


Description
===========

This function is used to invoke model-dependent logging within the channel subsystem.
