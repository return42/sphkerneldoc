
.. _API-blk-requeue-request:

===================
blk_requeue_request
===================

*man blk_requeue_request(9)*

*4.6.0-rc1*

put a request back on queue


Synopsis
========

.. c:function:: void blk_requeue_request( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    request queue where request should be inserted

``rq``
    request to be inserted


Description
===========

Drivers often keep queueing requests until the hardware cannot accept more, when that condition happens we need to put the request back on the queue. Must be called with queue lock
held.
