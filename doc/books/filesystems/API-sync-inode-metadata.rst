
.. _API-sync-inode-metadata:

===================
sync_inode_metadata
===================

*man sync_inode_metadata(9)*

*4.6.0-rc1*

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
