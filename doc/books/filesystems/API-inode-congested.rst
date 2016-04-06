
.. _API-inode-congested:

===============
inode_congested
===============

*man inode_congested(9)*

*4.6.0-rc1*

test whether an inode is congested


Synopsis
========

.. c:function:: int inode_congested( struct inode * inode, int cong_bits )

Arguments
=========

``inode``
    inode to test for congestion (may be NULL)

``cong_bits``
    mask of WB_[a]sync_congested bits to test


Description
===========

Tests whether ``inode`` is congested. ``cong_bits`` is the mask of congestion bits to test and the return value is the mask of set bits.

If cgroup writeback is enabled for ``inode``, the congestion state is determined by whether the cgwb (cgroup bdi_writeback) for the blkcg associated with ``inode`` is congested;
otherwise, the root wb's congestion state is used.

``inode`` is allowed to be NULL as this function is often called on mapping->host which is NULL for the swapper space.
