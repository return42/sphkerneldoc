
.. _API-get-super-thawed:

================
get_super_thawed
================

*man get_super_thawed(9)*

*4.6.0-rc1*

get thawed superblock of a device


Synopsis
========

.. c:function:: struct super_block ⋆ get_super_thawed( struct block_device * bdev )

Arguments
=========

``bdev``
    device to get the superblock for


Description
===========

Scans the superblock list and finds the superblock of the file system mounted on the device. The superblock is returned once it is thawed (or immediately if it was not frozen).
``NULL`` is returned if no match is found.
