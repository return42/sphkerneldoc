
.. _API-d-inode:

=======
d_inode
=======

*man d_inode(9)*

*4.6.0-rc1*

Get the actual inode of this dentry


Synopsis
========

.. c:function:: struct inode ⋆ d_inode( const struct dentry * dentry )

Arguments
=========

``dentry``
    The dentry to query


Description
===========

This is the helper normal filesystems should use to get at their own inodes in their own dentries and ignore the layering superimposed upon them.
