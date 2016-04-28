.. -*- coding: utf-8; mode: rst -*-

.. _API-debugfs-create-dir:

==================
debugfs_create_dir
==================

*man debugfs_create_dir(9)*

*4.6.0-rc5*

create a directory in the debugfs filesystem


Synopsis
========

.. c:function:: struct dentry * debugfs_create_dir( const char * name, struct dentry * parent )

Arguments
=========

``name``
    a pointer to a string containing the name of the directory to
    create.

``parent``
    a pointer to the parent dentry for this file. This should be a
    directory dentry if set. If this parameter is NULL, then the
    directory will be created in the root of the debugfs filesystem.


Description
===========

This function creates a directory in debugfs with the given name.

This function will return a pointer to a dentry if it succeeds. This
pointer must be passed to the ``debugfs_remove`` function when the file
is to be removed (no automatic cleanup happens if your module is
unloaded, you are responsible here.) If an error occurs, ``NULL`` will
be returned.

If debugfs is not enabled in the kernel, the value -``ENODEV`` will be
returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
