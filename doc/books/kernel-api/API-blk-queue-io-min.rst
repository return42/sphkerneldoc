
.. _API-blk-queue-io-min:

================
blk_queue_io_min
================

*man blk_queue_io_min(9)*

*4.6.0-rc1*

set minimum request size for the queue


Synopsis
========

.. c:function:: void blk_queue_io_min( struct request_queue * q, unsigned int min )

Arguments
=========

``q``
    the request queue for the device

``min``
    smallest I/O size in bytes


Description
===========

Storage devices may report a granularity or preferred minimum I/O size which is the smallest request the device can perform without incurring a performance penalty. For disk drives
this is often the physical block size. For RAID arrays it is often the stripe chunk size. A properly aligned multiple of minimum_io_size is the preferred request size for
workloads where a high number of I/O operations is desired.
