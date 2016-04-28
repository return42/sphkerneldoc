.. -*- coding: utf-8; mode: rst -*-

.. _API-d-splice-alias:

==============
d_splice_alias
==============

*man d_splice_alias(9)*

*4.6.0-rc5*

splice a disconnected dentry into the tree if one exists


Synopsis
========

.. c:function:: struct dentry * d_splice_alias( struct inode * inode, struct dentry * dentry )

Arguments
=========

``inode``
    the inode which may have a disconnected dentry

``dentry``
    a negative dentry which we want to point to the inode.


Description
===========

If inode is a directory and has an IS_ROOT alias, then d_move that in
place of the given dentry and return it, else simply d_add the inode to
the dentry and return NULL.

If a non-IS_ROOT directory is found, the filesystem is corrupt, and


we should error out
===================

directories can't have multiple aliases.

This is needed in the lookup routine of any filesystem that is
exportable (via knfsd) so that we can build dcache paths to directories
effectively.

If a dentry was found and moved, then it is returned. Otherwise NULL is
returned. This matches the expected return value of ->lookup.

Cluster filesystems may call this function with a negative, hashed
dentry. In that case, we know that the inode will be a regular file, and
also this will only occur during atomic_open. So we need to check for
the dentry being already hashed only in the final case.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
