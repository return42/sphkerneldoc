.. -*- coding: utf-8; mode: rst -*-

.. _API---blk-run-queue-uncond:

======================
__blk_run_queue_uncond
======================

*man __blk_run_queue_uncond(9)*

*4.6.0-rc5*

run a queue whether or not it has been stopped


Synopsis
========

.. c:function:: void __blk_run_queue_uncond( struct request_queue * q )

Arguments
=========

``q``
    The queue to run


Description
===========

Invoke request handling on a queue if there are any pending requests.
May be used to restart request handling after a request has completed.
This variant runs the queue whether or not the queue has been stopped.
Must be called with the queue lock held and interrupts disabled. See
also ``blk_run_queue``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
