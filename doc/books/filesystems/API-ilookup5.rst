.. -*- coding: utf-8; mode: rst -*-

.. _API-ilookup5:

========
ilookup5
========

*man ilookup5(9)*

*4.6.0-rc5*

search for an inode in the inode cache


Synopsis
========

.. c:function:: struct inode * ilookup5( struct super_block * sb, unsigned long hashval, int (*test) struct inode *, void *, void * data )

Arguments
=========

``sb``
    super block of file system to search

``hashval``
    hash value (usually inode number) to search for

``test``
    callback used for comparisons between inodes

``data``
    opaque data pointer to pass to ``test``


Description
===========

Search for the inode specified by ``hashval`` and ``data`` in the inode
cache, and if the inode is in the cache, return the inode with an
incremented reference count. Waits on I_NEW before returning the inode.
returned with an incremented reference count.

This is a generalized version of ``ilookup`` for file systems where the
inode number is not sufficient for unique identification of an inode.


Note
====

``test`` is called with the inode_hash_lock held, so can't sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
