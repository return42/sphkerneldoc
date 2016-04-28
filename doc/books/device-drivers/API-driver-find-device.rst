.. -*- coding: utf-8; mode: rst -*-

.. _API-driver-find-device:

==================
driver_find_device
==================

*man driver_find_device(9)*

*4.6.0-rc5*

device iterator for locating a particular device.


Synopsis
========

.. c:function:: struct device * driver_find_device( struct device_driver * drv, struct device * start, void * data, int (*match) struct device *dev, void *data )

Arguments
=========

``drv``
    The device's driver

``start``
    Device to begin with

``data``
    Data to pass to match function

``match``
    Callback function to check device


Description
===========

This is similar to the ``driver_for_each_device`` function above, but it
returns a reference to a device that is 'found' for later use, as
determined by the ``match`` callback.

The callback should return 0 if the device doesn't match and non-zero if
it does. If the callback returns non-zero, this function will return to
the caller and not iterate over any more devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
