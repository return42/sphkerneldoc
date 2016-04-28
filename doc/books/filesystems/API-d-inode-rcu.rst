.. -*- coding: utf-8; mode: rst -*-

.. _API-d-inode-rcu:

===========
d_inode_rcu
===========

*man d_inode_rcu(9)*

*4.6.0-rc5*

Get the actual inode of this dentry with ``ACCESS_ONCE``


Synopsis
========

.. c:function:: struct inode * d_inode_rcu( const struct dentry * dentry )

Arguments
=========

``dentry``
    The dentry to query


Description
===========

This is the helper normal filesystems should use to get at their own
inodes in their own dentries and ignore the layering superimposed upon
them.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
