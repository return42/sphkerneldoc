
.. _API-device-remove-file:

==================
device_remove_file
==================

*man device_remove_file(9)*

*4.6.0-rc1*

remove sysfs attribute file.


Synopsis
========

.. c:function:: void device_remove_file( struct device * dev, const struct device_attribute * attr )

Arguments
=========

``dev``
    device.

``attr``
    device attribute descriptor.
