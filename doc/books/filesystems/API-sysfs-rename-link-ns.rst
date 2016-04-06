
.. _API-sysfs-rename-link-ns:

====================
sysfs_rename_link_ns
====================

*man sysfs_rename_link_ns(9)*

*4.6.0-rc1*

rename symlink in object's directory.


Synopsis
========

.. c:function:: int sysfs_rename_link_ns( struct kobject * kobj, struct kobject * targ, const char * old, const char * new, const void * new_ns )

Arguments
=========

``kobj``
    object we're acting for.

``targ``
    object we're pointing to.

``old``
    previous name of the symlink.

``new``
    new name of the symlink.

``new_ns``
    new namespace of the symlink.


Description
===========

A helper function for the common rename symlink idiom.
