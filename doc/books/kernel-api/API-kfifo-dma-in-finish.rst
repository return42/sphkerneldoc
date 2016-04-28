.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-dma-in-finish:

===================
kfifo_dma_in_finish
===================

*man kfifo_dma_in_finish(9)*

*4.6.0-rc5*

finish a DMA IN operation


Synopsis
========

.. c:function:: kfifo_dma_in_finish( fifo, len )

Arguments
=========

``fifo``
    address of the fifo to be used

``len``
    number of bytes to received


Description
===========

This macro finish a DMA IN operation. The in counter will be updated by
the len parameter. No error checking will be done.

Note that with only one concurrent reader and one concurrent writer, you
don't need extra locking to use these macros.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
