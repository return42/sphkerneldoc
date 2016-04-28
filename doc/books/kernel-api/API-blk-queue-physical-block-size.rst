.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-physical-block-size:

=============================
blk_queue_physical_block_size
=============================

*man blk_queue_physical_block_size(9)*

*4.6.0-rc5*

set physical block size for the queue


Synopsis
========

.. c:function:: void blk_queue_physical_block_size( struct request_queue * q, unsigned int size )

Arguments
=========

``q``
    the request queue for the device

``size``
    the physical block size, in bytes


Description
===========

This should be set to the lowest possible sector size that the hardware
can operate on without reverting to read-modify-write operations.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
