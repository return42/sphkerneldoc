
.. _API-sysfs-chmod-file:

================
sysfs_chmod_file
================

*man sysfs_chmod_file(9)*

*4.6.0-rc1*

update the modified mode value on an object attribute.


Synopsis
========

.. c:function:: int sysfs_chmod_file( struct kobject * kobj, const struct attribute * attr, umode_t mode )

Arguments
=========

``kobj``
    object we're acting for.

``attr``
    attribute descriptor.

``mode``
    file permissions.
