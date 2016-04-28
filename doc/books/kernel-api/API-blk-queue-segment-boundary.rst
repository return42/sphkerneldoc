.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-segment-boundary:

==========================
blk_queue_segment_boundary
==========================

*man blk_queue_segment_boundary(9)*

*4.6.0-rc5*

set boundary rules for segment merging


Synopsis
========

.. c:function:: void blk_queue_segment_boundary( struct request_queue * q, unsigned long mask )

Arguments
=========

``q``
    the request queue for the device

``mask``
    the memory boundary mask


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
