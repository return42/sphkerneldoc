
.. _API-sysfs-remove-file-from-group:

============================
sysfs_remove_file_from_group
============================

*man sysfs_remove_file_from_group(9)*

*4.6.0-rc1*

remove an attribute file from a group.


Synopsis
========

.. c:function:: void sysfs_remove_file_from_group( struct kobject * kobj, const struct attribute * attr, const char * group )

Arguments
=========

``kobj``
    object we're acting for.

``attr``
    attribute descriptor.

``group``
    group name.
