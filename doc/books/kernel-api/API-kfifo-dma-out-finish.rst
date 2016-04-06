
.. _API-kfifo-dma-out-finish:

====================
kfifo_dma_out_finish
====================

*man kfifo_dma_out_finish(9)*

*4.6.0-rc1*

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

This macro finish a DMA OUT operation. The out counter will be updated by the len parameter. No error checking will be done.

Note that with only one concurrent reader and one concurrent writer, you don't need extra locking to use these macros.
