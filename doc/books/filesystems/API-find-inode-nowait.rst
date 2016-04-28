.. -*- coding: utf-8; mode: rst -*-

.. _API-find-inode-nowait:

=================
find_inode_nowait
=================

*man find_inode_nowait(9)*

*4.6.0-rc5*

find an inode in the inode cache


Synopsis
========

.. c:function:: struct inode * find_inode_nowait( struct super_block * sb, unsigned long hashval, int (*match) struct inode *, unsigned long, void *, void * data )

Arguments
=========

``sb``
    super block of file system to search

``hashval``
    hash value (usually inode number) to search for

``match``
    callback used for comparisons between inodes

``data``
    opaque data pointer to pass to ``match``


Description
===========

Search for the inode specified by ``hashval`` and ``data`` in the inode
cache, where the helper function ``match`` will return 0 if the inode
does not match, 1 if the inode does match, and -1 if the search should
be stopped. The ``match`` function must be responsible for taking the
i_lock spin_lock and checking i_state for an inode being freed or
being initialized, and incrementing the reference count before returning
1. It also must not sleep, since it is called with the inode_hash_lock
spinlock held.

This is a even more generalized version of ``ilookup5`` when the
function must never block --- ``find_inode`` can block in
``__wait_on_freeing_inode`` --- or when the caller can not increment the
reference count because the resulting ``iput`` might cause an inode
eviction. The tradeoff is that the ``match`` funtion must be very
carefully implemented.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
