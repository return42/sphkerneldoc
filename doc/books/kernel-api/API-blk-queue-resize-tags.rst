.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-resize-tags:

=====================
blk_queue_resize_tags
=====================

*man blk_queue_resize_tags(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
