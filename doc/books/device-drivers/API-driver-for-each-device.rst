.. -*- coding: utf-8; mode: rst -*-

.. _API-driver-for-each-device:

======================
driver_for_each_device
======================

*man driver_for_each_device(9)*

*4.6.0-rc5*

Iterator for devices bound to a driver.


Synopsis
========

.. c:function:: int driver_for_each_device( struct device_driver * drv, struct device * start, void * data, int (*fn) struct device *, void * )

Arguments
=========

``drv``
    Driver we're iterating.

``start``
    Device to begin with

``data``
    Data to pass to the callback.

``fn``
    Function to call for each device.


Description
===========

Iterate over the ``drv``'s list of devices calling ``fn`` for each one.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
