.. -*- coding: utf-8; mode: rst -*-

.. _API-get-super-thawed:

================
get_super_thawed
================

*man get_super_thawed(9)*

*4.6.0-rc5*

get thawed superblock of a device


Synopsis
========

.. c:function:: struct super_block * get_super_thawed( struct block_device * bdev )

Arguments
=========

``bdev``
    device to get the superblock for


Description
===========

Scans the superblock list and finds the superblock of the file system
mounted on the device. The superblock is returned once it is thawed (or
immediately if it was not frozen). ``NULL`` is returned if no match is
found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
