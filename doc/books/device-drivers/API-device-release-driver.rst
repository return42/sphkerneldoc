
.. _API-device-release-driver:

=====================
device_release_driver
=====================

*man device_release_driver(9)*

*4.6.0-rc1*

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

Manually detach device from driver. When called for a USB interface, ``dev``->parent lock must be held.
