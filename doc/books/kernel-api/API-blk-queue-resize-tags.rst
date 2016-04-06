
.. _API-blk-queue-resize-tags:

=====================
blk_queue_resize_tags
=====================

*man blk_queue_resize_tags(9)*

*4.6.0-rc1*

change the queueing depth


Synopsis
========

.. c:function:: int blk_queue_resize_tags( struct request_queue * q, int new_depth )

Arguments
=========

``q``
    the request queue for the device

``new_depth``
    the new max command queueing depth


Notes
=====

Must be called with the queue lock held.
