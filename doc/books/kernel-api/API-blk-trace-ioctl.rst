.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-trace-ioctl:

===============
blk_trace_ioctl
===============

*man blk_trace_ioctl(9)*

*4.6.0-rc5*

handle the ioctls associated with tracing


Synopsis
========

.. c:function:: int blk_trace_ioctl( struct block_device * bdev, unsigned cmd, char __user * arg )

Arguments
=========

``bdev``
    the block device

``cmd``
    the ioctl cmd

``arg``
    the argument data, if any


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
