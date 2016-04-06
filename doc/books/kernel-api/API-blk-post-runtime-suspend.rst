
.. _API-blk-post-runtime-suspend:

========================
blk_post_runtime_suspend
========================

*man blk_post_runtime_suspend(9)*

*4.6.0-rc1*

Post runtime suspend processing


Synopsis
========

.. c:function:: void blk_post_runtime_suspend( struct request_queue * q, int err )

Arguments
=========

``q``
    the queue of the device

``err``
    return value of the device's runtime_suspend function


Description
===========

Update the queue's runtime status according to the return value of the device's runtime suspend function and mark last busy for the device so that PM core will try to auto suspend
the device at a later time.

This function should be called near the end of the device's runtime_suspend callback.
