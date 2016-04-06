
.. _API-sysfs-remove-link:

=================
sysfs_remove_link
=================

*man sysfs_remove_link(9)*

*4.6.0-rc1*

remove symlink in object's directory.


Synopsis
========

.. c:function:: void sysfs_remove_link( struct kobject * kobj, const char * name )

Arguments
=========

``kobj``
    object we're acting for.

``name``
    name of the symlink to remove.
