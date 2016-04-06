
.. _API-kfifo-dma-out-prepare:

=====================
kfifo_dma_out_prepare
=====================

*man kfifo_dma_out_prepare(9)*

*4.6.0-rc1*

setup a scatterlist for DMA output


Synopsis
========

.. c:function:: kfifo_dma_out_prepare( fifo, sgl, nents, len )

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

This macro fills a scatterlist for DMA output which at most ``len`` bytes to transfer. It returns the number entries in the scatterlist array. A zero means there is no space
available and the scatterlist is not filled.

Note that with only one concurrent reader and one concurrent writer, you don't need extra locking to use these macros.
