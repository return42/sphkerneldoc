
.. _API-trace-block-dirty-buffer:

========================
trace_block_dirty_buffer
========================

*man trace_block_dirty_buffer(9)*

*4.6.0-rc1*

mark a buffer dirty


Synopsis
========

.. c:function:: void trace_block_dirty_buffer( struct buffer_head * bh )

Arguments
=========

``bh``
    buffer_head being dirtied


Description
===========

Called from ``mark_buffer_dirty``.
