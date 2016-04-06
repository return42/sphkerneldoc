
.. _API-kfifo-dma-in-finish:

===================
kfifo_dma_in_finish
===================

*man kfifo_dma_in_finish(9)*

*4.6.0-rc1*

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

This macro finish a DMA IN operation. The in counter will be updated by the len parameter. No error checking will be done.

Note that with only one concurrent reader and one concurrent writer, you don't need extra locking to use these macros.
