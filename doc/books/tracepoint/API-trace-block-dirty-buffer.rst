.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-dirty-buffer:

========================
trace_block_dirty_buffer
========================

*man trace_block_dirty_buffer(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
