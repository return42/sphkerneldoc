
.. _API-blk-queue-invalidate-tags:

=========================
blk_queue_invalidate_tags
=========================

*man blk_queue_invalidate_tags(9)*

*4.6.0-rc1*

invalidate all pending tags


Synopsis
========

.. c:function:: void blk_queue_invalidate_tags( struct request_queue * q )

Arguments
=========

``q``
    the request queue for the device


Description
===========

Hardware conditions may dictate a need to stop all pending requests. In this case, we will safely clear the block side of the tag queue and readd all requests to the request queue
in the right order.


Notes
=====

queue lock must be held.
