
.. _API---remove-inode-hash:

===================
__remove_inode_hash
===================

*man __remove_inode_hash(9)*

*4.6.0-rc1*

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
