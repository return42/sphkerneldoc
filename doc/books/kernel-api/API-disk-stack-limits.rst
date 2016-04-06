
.. _API-disk-stack-limits:

=================
disk_stack_limits
=================

*man disk_stack_limits(9)*

*4.6.0-rc1*

adjust queue limits for stacked drivers


Synopsis
========

.. c:function:: void disk_stack_limits( struct gendisk * disk, struct block_device * bdev, sector_t offset )

Arguments
=========

``disk``
    MD/DM gendisk (top)

``bdev``
    the underlying block device (bottom)

``offset``
    offset to beginning of data within component device


Description
===========

Merges the limits for a top level gendisk and a bottom level block_device.
