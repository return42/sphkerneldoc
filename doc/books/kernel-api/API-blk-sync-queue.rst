
.. _API-blk-sync-queue:

==============
blk_sync_queue
==============

*man blk_sync_queue(9)*

*4.6.0-rc1*

cancel any pending callbacks on a queue


Synopsis
========

.. c:function:: void blk_sync_queue( struct request_queue * q )

Arguments
=========

``q``
    the queue


Description
===========

The block layer may perform asynchronous callback activity on a queue, such as calling the unplug function after a timeout. A block device may call blk_sync_queue to ensure that
any such activity is cancelled, thus allowing it to release resources that the callbacks might use. The caller must already have made sure that its ->make_request_fn will not
re-add plugging prior to calling this function.

This function does not cancel any asynchronous activity arising out of elevator or throttling code. That would require ``elevator_exit`` and ``blkcg_exit_queue`` to be called with
queue lock initialized.
