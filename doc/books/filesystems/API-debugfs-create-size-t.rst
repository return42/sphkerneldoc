
.. _API-debugfs-create-size-t:

=====================
debugfs_create_size_t
=====================

*man debugfs_create_size_t(9)*

*4.6.0-rc1*

create a debugfs file that is used to read and write an size_t value


Synopsis
========

.. c:function:: struct dentry ⋆ debugfs_create_size_t( const char * name, umode_t mode, struct dentry * parent, size_t * value )

Arguments
=========

``name``
    a pointer to a string containing the name of the file to create.

``mode``
    the permission that the file should have

``parent``
    a pointer to the parent dentry for this file. This should be a directory dentry if set. If this parameter is ``NULL``, then the file will be created in the root of the debugfs
    filesystem.

``value``
    a pointer to the variable that the file should read to and write from.
