.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-free-tags:

===================
blk_queue_free_tags
===================

*man blk_queue_free_tags(9)*

*4.6.0-rc5*

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

This is used to disable tagged queuing to a device, yet leave queue in
function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
