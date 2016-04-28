.. -*- coding: utf-8; mode: rst -*-

.. _API-debugfs-create-symlink:

======================
debugfs_create_symlink
======================

*man debugfs_create_symlink(9)*

*4.6.0-rc5*

create a symbolic link in the debugfs filesystem


Synopsis
========

.. c:function:: struct dentry * debugfs_create_symlink( const char * name, struct dentry * parent, const char * target )

Arguments
=========

``name``
    a pointer to a string containing the name of the symbolic link to
    create.

``parent``
    a pointer to the parent dentry for this symbolic link. This should
    be a directory dentry if set. If this parameter is NULL, then the
    symbolic link will be created in the root of the debugfs filesystem.

``target``
    a pointer to a string containing the path to the target of the
    symbolic link.


Description
===========

This function creates a symbolic link with the given name in debugfs
that links to the given target path.

This function will return a pointer to a dentry if it succeeds. This
pointer must be passed to the ``debugfs_remove`` function when the
symbolic link is to be removed (no automatic cleanup happens if your
module is unloaded, you are responsible here.) If an error occurs,
``NULL`` will be returned.

If debugfs is not enabled in the kernel, the value -``ENODEV`` will be
returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
