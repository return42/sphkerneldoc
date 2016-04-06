
.. _API-device-remove-file-self:

=======================
device_remove_file_self
=======================

*man device_remove_file_self(9)*

*4.6.0-rc1*

remove sysfs attribute file from its own method.


Synopsis
========

.. c:function:: bool device_remove_file_self( struct device * dev, const struct device_attribute * attr )

Arguments
=========

``dev``
    device.

``attr``
    device attribute descriptor.


Description
===========

See ``kernfs_remove_self`` for details.
