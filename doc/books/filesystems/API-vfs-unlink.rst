.. -*- coding: utf-8; mode: rst -*-

.. _API-vfs-unlink:

==========
vfs_unlink
==========

*man vfs_unlink(9)*

*4.6.0-rc5*

unlink a filesystem object


Synopsis
========

.. c:function:: int vfs_unlink( struct inode * dir, struct dentry * dentry, struct inode ** delegated_inode )

Arguments
=========

``dir``
    parent directory

``dentry``
    victim

``delegated_inode``
    returns victim inode, if the inode is delegated.


Description
===========

The caller must hold dir->i_mutex.

If vfs_unlink discovers a delegation, it will return -EWOULDBLOCK and
return a reference to the inode in delegated_inode. The caller should
then break the delegation on that inode and retry. Because breaking a
delegation may take a long time, the caller should drop dir->i_mutex
before doing so.

Alternatively, a caller may pass NULL for delegated_inode. This may be
appropriate for callers that expect the underlying filesystem not to be
NFS exported.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
