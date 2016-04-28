.. -*- coding: utf-8; mode: rst -*-

.. _API-sync-inode:

==========
sync_inode
==========

*man sync_inode(9)*

*4.6.0-rc5*

write an inode and its pages to disk.


Synopsis
========

.. c:function:: int sync_inode( struct inode * inode, struct writeback_control * wbc )

Arguments
=========

``inode``
    the inode to sync

``wbc``
    controls the writeback mode


Description
===========

``sync_inode`` will write an inode and its pages to disk. It will also
correctly update the inode on its superblock's dirty inode lists and
will update inode->i_state.

The caller must have a ref on the inode.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
