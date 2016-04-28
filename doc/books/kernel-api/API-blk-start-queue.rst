.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-start-queue:

===============
blk_start_queue
===============

*man blk_start_queue(9)*

*4.6.0-rc5*

restart a previously stopped queue


Synopsis
========

.. c:function:: void blk_start_queue( struct request_queue * q )

Arguments
=========

``q``
    The ``struct request_queue`` in question


Description
===========

``blk_start_queue`` will clear the stop flag on the queue, and call the
request_fn for the queue if it was in a stopped state when entered.
Also see ``blk_stop_queue``. Queue lock must be held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
