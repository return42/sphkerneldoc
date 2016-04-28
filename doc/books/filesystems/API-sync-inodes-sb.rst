.. -*- coding: utf-8; mode: rst -*-

.. _API-sync-inodes-sb:

==============
sync_inodes_sb
==============

*man sync_inodes_sb(9)*

*4.6.0-rc5*

sync sb inode pages


Synopsis
========

.. c:function:: void sync_inodes_sb( struct super_block * sb )

Arguments
=========

``sb``
    the superblock


Description
===========

This function writes and waits on any dirty inode belonging to this
super_block.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
