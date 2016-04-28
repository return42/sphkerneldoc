.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-touch-buffer:

========================
trace_block_touch_buffer
========================

*man trace_block_touch_buffer(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
