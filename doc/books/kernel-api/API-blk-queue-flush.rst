
.. _API-blk-queue-flush:

===============
blk_queue_flush
===============

*man blk_queue_flush(9)*

*4.6.0-rc1*

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

Tell block layer cache flush capability of ``q``. If it supports flushing, REQ_FLUSH should be set. If it supports bypassing write cache for individual writes, REQ_FUA should be
set.
