
.. _API-blk-queue-prep-rq:

=================
blk_queue_prep_rq
=================

*man blk_queue_prep_rq(9)*

*4.6.0-rc1*

set a prepare_request function for queue


Synopsis
========

.. c:function:: void blk_queue_prep_rq( struct request_queue * q, prep_rq_fn * pfn )

Arguments
=========

``q``
    queue

``pfn``
    prepare_request function


Description
===========

It's possible for a queue to register a prepare_request callback which is invoked before the request is handed to the request_fn. The goal of the function is to prepare a request
for I/O, it can be used to build a cdb from the request data for instance.
