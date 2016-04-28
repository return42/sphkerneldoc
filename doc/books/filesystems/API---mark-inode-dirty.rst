.. -*- coding: utf-8; mode: rst -*-

.. _API---mark-inode-dirty:

==================
__mark_inode_dirty
==================

*man __mark_inode_dirty(9)*

*4.6.0-rc5*

internal function


Synopsis
========

.. c:function:: void __mark_inode_dirty( struct inode * inode, int flags )

Arguments
=========

``inode``
    inode to mark

``flags``
    what kind of dirty (i.e. I_DIRTY_SYNC) Mark an inode as dirty.
    Callers should use mark_inode_dirty or mark_inode_dirty_sync.


Description
===========

Put the inode on the super block's dirty list.

CAREFUL! We mark it dirty unconditionally, but move it onto the dirty
list only if it is hashed or if it refers to a blockdev. If it was not
hashed, it will never be added to the dirty list even if it is later
hashed, as it will have been marked dirty already.

In short, make sure you hash any inodes _before_ you start marking
them dirty.

Note that for blockdevs, inode->dirtied_when represents the dirtying
time of the block-special inode (/dev/hda1) itself. And the
->dirtied_when field of the kernel-internal blockdev inode represents
the dirtying time of the blockdev's pages. This is why for
I_DIRTY_PAGES we always use page->mapping->host, so the page-dirtying
time is recorded in the internal blockdev inode.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
