
.. _API-blk-trace-ioctl:

===============
blk_trace_ioctl
===============

*man blk_trace_ioctl(9)*

*4.6.0-rc1*

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
