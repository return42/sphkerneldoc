
.. _API-sysfs-add-file-to-group:

=======================
sysfs_add_file_to_group
=======================

*man sysfs_add_file_to_group(9)*

*4.6.0-rc1*

add an attribute file to a pre-existing group.


Synopsis
========

.. c:function:: int sysfs_add_file_to_group( struct kobject * kobj, const struct attribute * attr, const char * group )

Arguments
=========

``kobj``
    object we're acting for.

``attr``
    attribute descriptor.

``group``
    group name.
