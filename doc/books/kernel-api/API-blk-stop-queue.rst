.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-stop-queue:

==============
blk_stop_queue
==============

*man blk_stop_queue(9)*

*4.6.0-rc5*

stop a queue


Synopsis
========

.. c:function:: void blk_stop_queue( struct request_queue * q )

Arguments
=========

``q``
    The ``struct request_queue`` in question


Description
===========

The Linux block layer assumes that a block driver will consume all
entries on the request queue when the request_fn strategy is called.
Often this will not happen, because of hardware limitations (queue depth
settings). If a device driver gets a 'queue full' response, or if it
simply chooses not to queue more I/O at one point, it can call this
function to prevent the request_fn from being called until the driver
has signalled it's ready to go again. This happens by calling
``blk_start_queue`` to restart queue operations. Queue lock must be
held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
