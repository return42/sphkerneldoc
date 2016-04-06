
.. _API-sysfs-create-bin-file:

=====================
sysfs_create_bin_file
=====================

*man sysfs_create_bin_file(9)*

*4.6.0-rc1*

create binary file for object.


Synopsis
========

.. c:function:: int sysfs_create_bin_file( struct kobject * kobj, const struct bin_attribute * attr )

Arguments
=========

``kobj``
    object.

``attr``
    attribute descriptor.
