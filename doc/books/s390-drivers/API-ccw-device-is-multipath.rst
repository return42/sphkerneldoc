.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-is-multipath:

=======================
ccw_device_is_multipath
=======================

*man ccw_device_is_multipath(9)*

*4.6.0-rc5*

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

Return non-zero if device is operating in multipath mode, zero
otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
