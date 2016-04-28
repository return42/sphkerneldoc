.. -*- coding: utf-8; mode: rst -*-

.. _API-check-disk-size-change:

======================
check_disk_size_change
======================

*man check_disk_size_change(9)*

*4.6.0-rc5*

checks for disk size change and adjusts bdev size.


Synopsis
========

.. c:function:: void check_disk_size_change( struct gendisk * disk, struct block_device * bdev )

Arguments
=========

``disk``
    struct gendisk to check

``bdev``
    struct bdev to adjust.


Description
===========

This routine checks to see if the bdev size does not match the disk size
and adjusts it if it differs.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
