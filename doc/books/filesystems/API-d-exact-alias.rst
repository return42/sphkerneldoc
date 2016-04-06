
.. _API-d-exact-alias:

=============
d_exact_alias
=============

*man d_exact_alias(9)*

*4.6.0-rc1*

find and hash an exact unhashed alias


Synopsis
========

.. c:function:: struct dentry ⋆ d_exact_alias( struct dentry * entry, struct inode * inode )

Arguments
=========

``entry``
    dentry to add

``inode``
    The inode to go with this dentry


Description
===========

If an unhashed dentry with the same name/parent and desired inode already exists, hash and return it. Otherwise, return NULL.

Parent directory should be locked.
