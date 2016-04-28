.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-run-queue-async:

===================
blk_run_queue_async
===================

*man blk_run_queue_async(9)*

*4.6.0-rc5*

run a single device queue in workqueue context


Synopsis
========

.. c:function:: void blk_run_queue_async( struct request_queue * q )

Arguments
=========

``q``
    The queue to run


Description
===========

Tells kblockd to perform the equivalent of ``blk_run_queue`` on behalf
of us. The caller must hold the queue lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
