
.. _API-d-backing-inode:

===============
d_backing_inode
===============

*man d_backing_inode(9)*

*4.6.0-rc1*

Get upper or lower inode we should be using


Synopsis
========

.. c:function:: struct inode ⋆ d_backing_inode( const struct dentry * upper )

Arguments
=========

``upper``
    The upper layer


Description
===========

This is the helper that should be used to get at the inode that will be used if this dentry were to be opened as a file. The inode may be on the upper dentry or it may be on a
lower dentry pinned by the upper.

Normal filesystems should not use this to access their own inodes.
