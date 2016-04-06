
.. _API-blk-queue-bounce-limit:

======================
blk_queue_bounce_limit
======================

*man blk_queue_bounce_limit(9)*

*4.6.0-rc1*

set bounce buffer limit for queue


Synopsis
========

.. c:function:: void blk_queue_bounce_limit( struct request_queue * q, u64 max_addr )

Arguments
=========

``q``
    the request queue for the device

``max_addr``
    the maximum address the device can handle


Description
===========

Different hardware can have different requirements as to what pages it can do I/O directly to. A low level driver can call blk_queue_bounce_limit to have lower memory pages
allocated as bounce buffers for doing I/O to pages residing above ``max_addr``.
