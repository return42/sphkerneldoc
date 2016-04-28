.. -*- coding: utf-8; mode: rst -*-

.. _API-get-super:

=========
get_super
=========

*man get_super(9)*

*4.6.0-rc5*

get the superblock of a device


Synopsis
========

.. c:function:: struct super_block * get_super( struct block_device * bdev )

Arguments
=========

``bdev``
    device to get the superblock for

    Scans the superblock list and finds the superblock of the file
    system mounted on the device given. ``NULL`` is returned if no match
    is found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
