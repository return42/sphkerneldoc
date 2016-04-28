.. -*- coding: utf-8; mode: rst -*-

.. _API-debugfs-create-blob:

===================
debugfs_create_blob
===================

*man debugfs_create_blob(9)*

*4.6.0-rc5*

create a debugfs file that is used to read a binary blob


Synopsis
========

.. c:function:: struct dentry * debugfs_create_blob( const char * name, umode_t mode, struct dentry * parent, struct debugfs_blob_wrapper * blob )

Arguments
=========

``name``
    a pointer to a string containing the name of the file to create.

``mode``
    the permission that the file should have

``parent``
    a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is ``NULL``, then the
    file will be created in the root of the debugfs filesystem.

``blob``
    a pointer to a struct debugfs_blob_wrapper which contains a
    pointer to the blob data and the size of the data.


Description
===========

This function creates a file in debugfs with the given name that exports
``blob``->data as a binary blob. If the ``mode`` variable is so set it
can be read from. Writing is not supported.

This function will return a pointer to a dentry if it succeeds. This
pointer must be passed to the ``debugfs_remove`` function when the file
is to be removed (no automatic cleanup happens if your module is
unloaded, you are responsible here.) If an error occurs, ``NULL`` will
be returned.

If debugfs is not enabled in the kernel, the value -``ENODEV`` will be
returned. It is not wise to check for this value, but rather, check for
``NULL`` or !\ ``NULL`` instead as to eliminate the need for #ifdef in
the calling code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
