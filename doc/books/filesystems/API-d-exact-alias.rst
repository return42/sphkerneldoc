.. -*- coding: utf-8; mode: rst -*-

.. _API-d-exact-alias:

=============
d_exact_alias
=============

*man d_exact_alias(9)*

*4.6.0-rc5*

find and hash an exact unhashed alias


Synopsis
========

.. c:function:: struct dentry * d_exact_alias( struct dentry * entry, struct inode * inode )

Arguments
=========

``entry``
    dentry to add

``inode``
    The inode to go with this dentry


Description
===========

If an unhashed dentry with the same name/parent and desired inode
already exists, hash and return it. Otherwise, return NULL.

Parent directory should be locked.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
