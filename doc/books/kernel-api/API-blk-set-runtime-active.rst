
.. _API-blk-set-runtime-active:

======================
blk_set_runtime_active
======================

*man blk_set_runtime_active(9)*

*4.6.0-rc1*

Force runtime status of the queue to be active


Synopsis
========

.. c:function:: void blk_set_runtime_active( struct request_queue * q )

Arguments
=========

``q``
    the queue of the device


Description
===========

If the device is left runtime suspended during system suspend the resume hook typically resumes the device and corrects runtime status accordingly. However, that does not affect
the queue runtime PM status which is still “suspended”. This prevents processing requests from the queue.

This function can be used in driver's resume hook to correct queue runtime PM status and re-enable peeking requests from the queue. It should be called before first request is
added to the queue.
