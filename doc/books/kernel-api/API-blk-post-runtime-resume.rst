
.. _API-blk-post-runtime-resume:

=======================
blk_post_runtime_resume
=======================

*man blk_post_runtime_resume(9)*

*4.6.0-rc1*

Post runtime resume processing


Synopsis
========

.. c:function:: void blk_post_runtime_resume( struct request_queue * q, int err )

Arguments
=========

``q``
    the queue of the device

``err``
    return value of the device's runtime_resume function


Description
===========

Update the queue's runtime status according to the return value of the device's runtime_resume function. If it is successfully resumed, process the requests that are queued into
the device's queue when it is resuming and then mark last busy and initiate autosuspend for it.

This function should be called near the end of the device's runtime_resume callback.
