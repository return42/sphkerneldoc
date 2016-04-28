.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-set-offline:

======================
ccw_device_set_offline
======================

*man ccw_device_set_offline(9)*

*4.6.0-rc5*

disable a ccw device for I/O


Synopsis
========

.. c:function:: int ccw_device_set_offline( struct ccw_device * cdev )

Arguments
=========

``cdev``
    target ccw device


Description
===========

This function calls the driver's ``set_offline`` function for ``cdev``,
if given, and then disables ``cdev``.


Returns
=======

``0`` on success and a negative error value on failure.


Context
=======

enabled, ccw device lock not held


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
