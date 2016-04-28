.. -*- coding: utf-8; mode: rst -*-

.. _API---remove-inode-hash:

===================
__remove_inode_hash
===================

*man __remove_inode_hash(9)*

*4.6.0-rc5*

remove an inode from the hash


Synopsis
========

.. c:function:: void __remove_inode_hash( struct inode * inode )

Arguments
=========

``inode``
    inode to unhash


Description
===========

Remove an inode from the superblock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
