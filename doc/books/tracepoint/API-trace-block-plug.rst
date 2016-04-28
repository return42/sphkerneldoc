.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-plug:

================
trace_block_plug
================

*man trace_block_plug(9)*

*4.6.0-rc5*

keep operations requests in request queue


Synopsis
========

.. c:function:: void trace_block_plug( struct request_queue * q )

Arguments
=========

``q``
    request queue to plug


Description
===========

Plug the request queue ``q``. Do not allow block operation requests to
be sent to the device driver. Instead, accumulate requests in the queue
to improve throughput performance of the block device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
