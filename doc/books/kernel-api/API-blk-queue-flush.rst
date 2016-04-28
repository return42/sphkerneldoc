.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-flush:

===============
blk_queue_flush
===============

*man blk_queue_flush(9)*

*4.6.0-rc5*

configure queue's cache flush capability


Synopsis
========

.. c:function:: void blk_queue_flush( struct request_queue * q, unsigned int flush )

Arguments
=========

``q``
    the request queue for the device

``flush``
    0, REQ_FLUSH or REQ_FLUSH | REQ_FUA


Description
===========

Tell block layer cache flush capability of ``q``. If it supports
flushing, REQ_FLUSH should be set. If it supports bypassing write cache
for individual writes, REQ_FUA should be set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
