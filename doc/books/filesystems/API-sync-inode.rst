
.. _API-sync-inode:

==========
sync_inode
==========

*man sync_inode(9)*

*4.6.0-rc1*

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

``sync_inode`` will write an inode and its pages to disk. It will also correctly update the inode on its superblock's dirty inode lists and will update inode->i_state.

The caller must have a ref on the inode.
