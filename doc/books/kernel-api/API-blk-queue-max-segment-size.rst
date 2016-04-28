.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-max-segment-size:

==========================
blk_queue_max_segment_size
==========================

*man blk_queue_max_segment_size(9)*

*4.6.0-rc5*

set max segment size for blk_rq_map_sg


Synopsis
========

.. c:function:: void blk_queue_max_segment_size( struct request_queue * q, unsigned int max_size )

Arguments
=========

``q``
    the request queue for the device

``max_size``
    max size of segment in bytes


Description
===========

Enables a low level driver to set an upper limit on the size of a
coalesced segment


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
