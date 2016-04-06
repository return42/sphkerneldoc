
.. _API-device-remove-bin-file:

======================
device_remove_bin_file
======================

*man device_remove_bin_file(9)*

*4.6.0-rc1*

remove sysfs binary attribute file


Synopsis
========

.. c:function:: void device_remove_bin_file( struct device * dev, const struct bin_attribute * attr )

Arguments
=========

``dev``
    device.

``attr``
    device binary attribute descriptor.
