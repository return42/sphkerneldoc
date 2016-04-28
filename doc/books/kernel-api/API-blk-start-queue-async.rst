.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-start-queue-async:

=====================
blk_start_queue_async
=====================

*man blk_start_queue_async(9)*

*4.6.0-rc5*

asynchronously restart a previously stopped queue


Synopsis
========

.. c:function:: void blk_start_queue_async( struct request_queue * q )

Arguments
=========

``q``
    The ``struct request_queue`` in question


Description
===========

``blk_start_queue_async`` will clear the stop flag on the queue, and
ensure that the request_fn for the queue is run from an async context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
