.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-dma-out-finish:

====================
kfifo_dma_out_finish
====================

*man kfifo_dma_out_finish(9)*

*4.6.0-rc5*

finish a DMA OUT operation


Synopsis
========

.. c:function:: kfifo_dma_out_finish( fifo, len )

Arguments
=========

``fifo``
    address of the fifo to be used

``len``
    number of bytes transferred


Description
===========

This macro finish a DMA OUT operation. The out counter will be updated
by the len parameter. No error checking will be done.

Note that with only one concurrent reader and one concurrent writer, you
don't need extra locking to use these macros.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
