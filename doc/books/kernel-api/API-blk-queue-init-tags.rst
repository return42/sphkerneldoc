
.. _API-blk-queue-init-tags:

===================
blk_queue_init_tags
===================

*man blk_queue_init_tags(9)*

*4.6.0-rc1*

initialize the queue tag info


Synopsis
========

.. c:function:: int blk_queue_init_tags( struct request_queue * q, int depth, struct blk_queue_tag * tags, int alloc_policy )

Arguments
=========

``q``
    the request queue for the device

``depth``
    the maximum queue depth supported

``tags``
    the tag to use

``alloc_policy``
    tag allocation policy


Description
===========

Queue lock must be held here if the function is called to resize an existing map.
