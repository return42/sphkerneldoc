
.. _API-device-create-file:

==================
device_create_file
==================

*man device_create_file(9)*

*4.6.0-rc1*

create sysfs attribute file for device.


Synopsis
========

.. c:function:: int device_create_file( struct device * dev, const struct device_attribute * attr )

Arguments
=========

``dev``
    device.

``attr``
    device attribute descriptor.
