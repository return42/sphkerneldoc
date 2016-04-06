
.. _API---insert-inode-hash:

===================
__insert_inode_hash
===================

*man __insert_inode_hash(9)*

*4.6.0-rc1*

hash an inode


Synopsis
========

.. c:function:: void __insert_inode_hash( struct inode * inode, unsigned long hashval )

Arguments
=========

``inode``
    unhashed inode

``hashval``
    unsigned long value used to locate this object in the inode_hashtable.


Description
===========

Add an inode to the inode hash for this superblock.
