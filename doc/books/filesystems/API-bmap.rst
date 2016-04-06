
.. _API-bmap:

====
bmap
====

*man bmap(9)*

*4.6.0-rc1*

find a block number in a file


Synopsis
========

.. c:function:: sector_t bmap( struct inode * inode, sector_t block )

Arguments
=========

``inode``
    inode of file

``block``
    block to find


Description
===========

Returns the block number on the device holding the inode that is the disk block number for the block of the file requested. That is, asked for block 4 of inode 1 the function will
return the disk block relative to the disk start that holds that block of the file.
