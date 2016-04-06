
.. _API-blk-limits-io-min:

=================
blk_limits_io_min
=================

*man blk_limits_io_min(9)*

*4.6.0-rc1*

set minimum request size for a device


Synopsis
========

.. c:function:: void blk_limits_io_min( struct queue_limits * limits, unsigned int min )

Arguments
=========

``limits``
    the queue limits

``min``
    smallest I/O size in bytes


Description
===========

Some devices have an internal block size bigger than the reported hardware sector size. This function can be used to signal the smallest I/O the device can perform without
incurring a performance penalty.
