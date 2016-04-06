
.. _API-device-bind-driver:

==================
device_bind_driver
==================

*man device_bind_driver(9)*

*4.6.0-rc1*

bind a driver to one device.


Synopsis
========

.. c:function:: int device_bind_driver( struct device * dev )

Arguments
=========

``dev``
    device.


Description
===========

Allow manual attachment of a driver to a device. Caller must have already set ``dev``->driver.

Note that this does not modify the bus reference count nor take the bus's rwsem. Please verify those are accounted for before calling this. (It is ok to call with no other effort
from a driver's ``probe`` method.)

This function must be called with the device lock held.
