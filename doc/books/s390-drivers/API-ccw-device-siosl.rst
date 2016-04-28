.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-siosl:

================
ccw_device_siosl
================

*man ccw_device_siosl(9)*

*4.6.0-rc5*

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

This function is used to invoke model-dependent logging within the
channel subsystem.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
