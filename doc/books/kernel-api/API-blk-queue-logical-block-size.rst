
.. _API-blk-queue-logical-block-size:

============================
blk_queue_logical_block_size
============================

*man blk_queue_logical_block_size(9)*

*4.6.0-rc1*

set logical block size for the queue


Synopsis
========

.. c:function:: void blk_queue_logical_block_size( struct request_queue * q, unsigned short size )

Arguments
=========

``q``
    the request queue for the device

``size``
    the logical block size, in bytes


Description
===========

This should be set to the lowest possible block size that the storage device can address. The default of 512 covers most hardware.
