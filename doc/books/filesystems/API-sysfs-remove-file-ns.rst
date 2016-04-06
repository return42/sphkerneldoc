
.. _API-sysfs-remove-file-ns:

====================
sysfs_remove_file_ns
====================

*man sysfs_remove_file_ns(9)*

*4.6.0-rc1*

remove an object attribute with a custom ns tag


Synopsis
========

.. c:function:: void sysfs_remove_file_ns( struct kobject * kobj, const struct attribute * attr, const void * ns )

Arguments
=========

``kobj``
    object we're acting for

``attr``
    attribute descriptor

``ns``
    namespace tag of the file to remove


Description
===========

Hash the attribute name and namespace tag and kill the victim.
