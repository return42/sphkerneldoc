
.. _API-blk-start-queue-async:

=====================
blk_start_queue_async
=====================

*man blk_start_queue_async(9)*

*4.6.0-rc1*

asynchronously restart a previously stopped queue


Synopsis
========

.. c:function:: void blk_start_queue_async( struct request_queue * q )

Arguments
=========

``q``
    The ``struct request_queue`` in question


Description
===========

``blk_start_queue_async`` will clear the stop flag on the queue, and ensure that the request_fn for the queue is run from an async context.
