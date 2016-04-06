
.. _API-blk-lld-busy:

============
blk_lld_busy
============

*man blk_lld_busy(9)*

*4.6.0-rc1*

Check if underlying low-level drivers of a device are busy


Synopsis
========

.. c:function:: int blk_lld_busy( struct request_queue * q )

Arguments
=========

``q``
    the queue of the device being checked


Description
===========

Check if underlying low-level drivers of a device are busy. If the drivers want to export their busy state, they must set own exporting function using ``blk_queue_lld_busy`` first.

Basically, this function is used only by request stacking drivers to stop dispatching requests to underlying devices when underlying devices are busy. This behavior helps more I/O
merging on the queue of the request stacking driver and prevents I/O throughput regression on burst I/O load.


Return
======

0 - Not busy (The request stacking driver should dispatch request) 1 - Busy (The request stacking driver should stop dispatching request)
