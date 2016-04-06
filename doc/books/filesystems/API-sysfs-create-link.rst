
.. _API-sysfs-create-link:

=================
sysfs_create_link
=================

*man sysfs_create_link(9)*

*4.6.0-rc1*

create symlink between two objects.


Synopsis
========

.. c:function:: int sysfs_create_link( struct kobject * kobj, struct kobject * target, const char * name )

Arguments
=========

``kobj``
    object whose directory we're creating the link in.

``target``
    object we're pointing to.

``name``
    name of the symlink.
