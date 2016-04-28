.. -*- coding: utf-8; mode: rst -*-

.. _API-sync-inode-metadata:

===================
sync_inode_metadata
===================

*man sync_inode_metadata(9)*

*4.6.0-rc5*

write an inode to disk


Synopsis
========

.. c:function:: int sync_inode_metadata( struct inode * inode, int wait )

Arguments
=========

``inode``
    the inode to sync

``wait``
    wait for I/O to complete.


Description
===========

Write an inode to disk and adjust its dirty state after completion.


Note
====

only writes the actual inode, no associated data or other metadata.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
