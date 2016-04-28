.. -*- coding: utf-8; mode: rst -*-

.. _API-securityfs-create-file:

======================
securityfs_create_file
======================

*man securityfs_create_file(9)*

*4.6.0-rc5*

create a file in the securityfs filesystem


Synopsis
========

.. c:function:: struct dentry * securityfs_create_file( const char * name, umode_t mode, struct dentry * parent, void * data, const struct file_operations * fops )

Arguments
=========

``name``
    a pointer to a string containing the name of the file to create.

``mode``
    the permission that the file should have

``parent``
    a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is ``NULL``, then the
    file will be created in the root of the securityfs filesystem.

``data``
    a pointer to something that the caller will want to get to later on.
    The inode.i_private pointer will point to this value on the
    ``open`` call.

``fops``
    a pointer to a struct file_operations that should be used for this
    file.


Description
===========

This is the basic “create a file” function for securityfs. It allows for
a wide range of flexibility in creating a file, or a directory (if you
want to create a directory, the ``securityfs_create_dir`` function is
recommended to be used instead).

This function returns a pointer to a dentry if it succeeds. This pointer
must be passed to the ``securityfs_remove`` function when the file is to
be removed (no automatic cleanup happens if your module is unloaded, you
are responsible here). If an error occurs, the function will return the
error value (via ERR_PTR).

If securityfs is not enabled in the kernel, the value ``-ENODEV`` is
returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
