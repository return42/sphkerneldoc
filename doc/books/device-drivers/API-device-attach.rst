
.. _API-device-attach:

=============
device_attach
=============

*man device_attach(9)*

*4.6.0-rc1*

try to attach device to a driver.


Synopsis
========

.. c:function:: int device_attach( struct device * dev )

Arguments
=========

``dev``
    device.


Description
===========

Walk the list of drivers that the bus has and call ``driver_probe_device`` for each pair. If a compatible pair is found, break out and return.

Returns 1 if the device was bound to a driver; 0 if no matching driver was found; -ENODEV if the device is not registered.

When called for a USB interface, ``dev``->parent lock must be held.
