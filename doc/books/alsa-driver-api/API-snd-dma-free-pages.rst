
.. _API-snd-dma-free-pages:

==================
snd_dma_free_pages
==================

*man snd_dma_free_pages(9)*

*4.6.0-rc1*

release the allocated buffer


Synopsis
========

.. c:function:: void snd_dma_free_pages( struct snd_dma_buffer * dmab )

Arguments
=========

``dmab``
    the buffer allocation record to release


Description
===========

Releases the allocated buffer via ``snd_dma_alloc_pages``.
