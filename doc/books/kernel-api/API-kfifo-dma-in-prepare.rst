
.. _API-kfifo-dma-in-prepare:

====================
kfifo_dma_in_prepare
====================

*man kfifo_dma_in_prepare(9)*

*4.6.0-rc1*

setup a scatterlist for DMA input


Synopsis
========

.. c:function:: kfifo_dma_in_prepare( fifo, sgl, nents, len )

Arguments
=========

``fifo``
    address of the fifo to be used

``sgl``
    pointer to the scatterlist array

``nents``
    number of entries in the scatterlist array

``len``
    number of elements to transfer


Description
===========

This macro fills a scatterlist for DMA input. It returns the number entries in the scatterlist array.

Note that with only one concurrent reader and one concurrent writer, you don't need extra locking to use these macros.
