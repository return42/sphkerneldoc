.. -*- coding: utf-8; mode: rst -*-

.. _API-ilookup5-nowait:

===============
ilookup5_nowait
===============

*man ilookup5_nowait(9)*

*4.6.0-rc5*

search for an inode in the inode cache


Synopsis
========

.. c:function:: struct inode * ilookup5_nowait( struct super_block * sb, unsigned long hashval, int (*test) struct inode *, void *, void * data )

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
cache. If the inode is in the cache, the inode is returned with an
incremented reference count.


Note
====

I_NEW is not waited upon so you have to be very careful what you do
with the returned inode. You probably should be using ``ilookup5``
instead.


Note2
=====

``test`` is called with the inode_hash_lock held, so can't sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
