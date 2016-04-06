
.. _API-sysfs-remove-bin-file:

=====================
sysfs_remove_bin_file
=====================

*man sysfs_remove_bin_file(9)*

*4.6.0-rc1*

remove binary file for object.


Synopsis
========

.. c:function:: void sysfs_remove_bin_file( struct kobject * kobj, const struct bin_attribute * attr )

Arguments
=========

``kobj``
    object.

``attr``
    attribute descriptor.
