.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dma-free-pages:

==================
snd_dma_free_pages
==================

*man snd_dma_free_pages(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
