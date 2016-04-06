
.. _API-device-create-bin-file:

======================
device_create_bin_file
======================

*man device_create_bin_file(9)*

*4.6.0-rc1*

create sysfs binary attribute file for device.


Synopsis
========

.. c:function:: int device_create_bin_file( struct device * dev, const struct bin_attribute * attr )

Arguments
=========

``dev``
    device.

``attr``
    device binary attribute descriptor.
