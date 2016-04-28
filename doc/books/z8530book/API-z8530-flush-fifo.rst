.. -*- coding: utf-8; mode: rst -*-

.. _API-z8530-flush-fifo:

================
z8530_flush_fifo
================

*man z8530_flush_fifo(9)*

*4.6.0-rc5*

Flush on chip RX FIFO


Synopsis
========

.. c:function:: void z8530_flush_fifo( struct z8530_channel * c )

Arguments
=========

``c``
    Channel to flush


Description
===========

Flush the receive FIFO. There is no specific option for this, we blindly
read bytes and discard them. Reading when there is no data is harmless.
The 8530 has a 4 byte FIFO, the 85230 has 8 bytes.

All locking is handled for the caller. On return data may still be
present if it arrived during the flush.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
