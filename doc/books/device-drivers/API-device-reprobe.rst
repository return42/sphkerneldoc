.. -*- coding: utf-8; mode: rst -*-

.. _API-device-reprobe:

==============
device_reprobe
==============

*man device_reprobe(9)*

*4.6.0-rc5*

remove driver for a device and probe for a new driver


Synopsis
========

.. c:function:: int device_reprobe( struct device * dev )

Arguments
=========

``dev``
    the device to reprobe


Description
===========

This function detaches the attached driver (if any) for the given device
and restarts the driver probing process. It is intended to use if
probing criteria changed during a devices lifetime and driver attachment
should change accordingly.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
