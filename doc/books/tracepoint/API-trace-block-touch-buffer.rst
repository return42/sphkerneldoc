
.. _API-trace-block-touch-buffer:

========================
trace_block_touch_buffer
========================

*man trace_block_touch_buffer(9)*

*4.6.0-rc1*

mark a buffer accessed


Synopsis
========

.. c:function:: void trace_block_touch_buffer( struct buffer_head * bh )

Arguments
=========

``bh``
    buffer_head being touched


Description
===========

Called from ``touch_buffer``.
