.. -*- coding: utf-8; mode: rst -*-

.. _API-bdev-stack-limits:

=================
bdev_stack_limits
=================

*man bdev_stack_limits(9)*

*4.6.0-rc5*

adjust queue limits for stacked drivers


Synopsis
========

.. c:function:: int bdev_stack_limits( struct queue_limits * t, struct block_device * bdev, sector_t start )

Arguments
=========

``t``
    the stacking driver limits (top device)

``bdev``
    the component block_device (bottom)

``start``
    first data sector within component device


Description
===========

Merges queue limits for a top device and a block_device. Returns 0 if
alignment didn't change. Returns -1 if adding the bottom device caused
misalignment.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
