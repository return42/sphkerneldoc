.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-unplug:

==================
trace_block_unplug
==================

*man trace_block_unplug(9)*

*4.6.0-rc5*

release of operations requests in request queue


Synopsis
========

.. c:function:: void trace_block_unplug( struct request_queue * q, unsigned int depth, bool explicit )

Arguments
=========

``q``
    request queue to unplug

``depth``
    number of requests just added to the queue

``explicit``
    whether this was an explicit unplug, or one from ``schedule``


Description
===========

Unplug request queue ``q`` because device driver is scheduled to work on
elements in the request queue.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
