
.. _API-sync-inodes-sb:

==============
sync_inodes_sb
==============

*man sync_inodes_sb(9)*

*4.6.0-rc1*

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

This function writes and waits on any dirty inode belonging to this super_block.
