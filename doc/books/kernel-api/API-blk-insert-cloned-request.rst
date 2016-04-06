
.. _API-blk-insert-cloned-request:

=========================
blk_insert_cloned_request
=========================

*man blk_insert_cloned_request(9)*

*4.6.0-rc1*

Helper for stacking drivers to submit a request


Synopsis
========

.. c:function:: int blk_insert_cloned_request( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    the queue to submit the request

``rq``
    the request being queued
