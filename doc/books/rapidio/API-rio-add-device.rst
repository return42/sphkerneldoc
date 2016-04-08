
.. _API-rio-add-device:

==============
rio_add_device
==============

*man rio_add_device(9)*

*4.6.0-rc1*

Adds a RIO device to the device model


Synopsis
========

.. c:function:: int rio_add_device( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device


Description
===========

Adds the RIO device to the global device list and adds the RIO device to the RIO device list. Creates the generic sysfs nodes for an RIO device.
