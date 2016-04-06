
.. _API-blk-queue-start-tag:

===================
blk_queue_start_tag
===================

*man blk_queue_start_tag(9)*

*4.6.0-rc1*

find a free tag and assign it


Synopsis
========

.. c:function:: int blk_queue_start_tag( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    the request queue for the device

``rq``
    the block request that needs tagging


Description
===========

This can either be used as a stand-alone helper, or possibly be assigned as the queue ``prep_rq_fn`` (in which case ``struct request`` automagically gets a tag assigned). Note that
this function assumes that any type of request can be queued! if this is not true for your device, you must check the request type before calling this function. The request will
also be removed from the request queue, so it's the drivers responsibility to readd it if it should need to be restarted for some reason.


Notes
=====

queue lock must be held.
