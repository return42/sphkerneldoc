
.. _API-blk-queue-free-tags:

===================
blk_queue_free_tags
===================

*man blk_queue_free_tags(9)*

*4.6.0-rc1*

release tag maintenance info


Synopsis
========

.. c:function:: void blk_queue_free_tags( struct request_queue * q )

Arguments
=========

``q``
    the request queue for the device


Notes
=====

This is used to disable tagged queuing to a device, yet leave queue in function.
