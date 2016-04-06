
.. _API-blk-trace-shutdown:

==================
blk_trace_shutdown
==================

*man blk_trace_shutdown(9)*

*4.6.0-rc1*

stop and cleanup trace structures


Synopsis
========

.. c:function:: void blk_trace_shutdown( struct request_queue * q )

Arguments
=========

``q``
    the request queue associated with the device
