
.. _API-blk-run-queue-async:

===================
blk_run_queue_async
===================

*man blk_run_queue_async(9)*

*4.6.0-rc1*

run a single device queue in workqueue context


Synopsis
========

.. c:function:: void blk_run_queue_async( struct request_queue * q )

Arguments
=========

``q``
    The queue to run


Description
===========

Tells kblockd to perform the equivalent of ``blk_run_queue`` on behalf of us. The caller must hold the queue lock.
