
.. _API-trace-block-plug:

================
trace_block_plug
================

*man trace_block_plug(9)*

*4.6.0-rc1*

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

Plug the request queue ``q``. Do not allow block operation requests to be sent to the device driver. Instead, accumulate requests in the queue to improve throughput performance of
the block device.
