.. -*- coding: utf-8; mode: rst -*-

.. _API-iget5-locked:

============
iget5_locked
============

*man iget5_locked(9)*

*4.6.0-rc5*

obtain an inode from a mounted file system


Synopsis
========

.. c:function:: struct inode * iget5_locked( struct super_block * sb, unsigned long hashval, int (*test) struct inode *, void *, int (*set) struct inode *, void *, void * data )

Arguments
=========

``sb``
    super block of file system

``hashval``
    hash value (usually inode number) to get

``test``
    callback used for comparisons between inodes

``set``
    callback used to initialize a new struct inode

``data``
    opaque data pointer to pass to ``test`` and ``set``


Description
===========

Search for the inode specified by ``hashval`` and ``data`` in the inode
cache, and if present it is return it with an increased reference count.
This is a generalized version of ``iget_locked`` for file systems where
the inode number is not sufficient for unique identification of an
inode.

If the inode is not in cache, allocate a new inode and return it locked,
hashed, and with the I_NEW flag set. The file system gets to fill it in
before unlocking it via ``unlock_new_inode``.

Note both ``test`` and ``set`` are called with the inode_hash_lock
held, so can't sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
