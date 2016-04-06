
.. _API-sysfs-create-file-ns:

====================
sysfs_create_file_ns
====================

*man sysfs_create_file_ns(9)*

*4.6.0-rc1*

create an attribute file for an object with custom ns


Synopsis
========

.. c:function:: int sysfs_create_file_ns( struct kobject * kobj, const struct attribute * attr, const void * ns )

Arguments
=========

``kobj``
    object we're creating for

``attr``
    attribute descriptor

``ns``
    namespace the new file should belong to
