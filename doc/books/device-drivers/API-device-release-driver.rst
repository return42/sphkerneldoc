.. -*- coding: utf-8; mode: rst -*-

.. _API-device-release-driver:

=====================
device_release_driver
=====================

*man device_release_driver(9)*

*4.6.0-rc5*

manually detach device from driver.


Synopsis
========

.. c:function:: void device_release_driver( struct device * dev )

Arguments
=========

``dev``
    device.


Description
===========

Manually detach device from driver. When called for a USB interface,
``dev``->parent lock must be held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
