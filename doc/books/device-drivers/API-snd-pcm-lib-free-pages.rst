.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-lib-free-pages:

======================
snd_pcm_lib_free_pages
======================

*man snd_pcm_lib_free_pages(9)*

*4.6.0-rc5*

release the allocated DMA buffer.


Synopsis
========

.. c:function:: int snd_pcm_lib_free_pages( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the substream to release the DMA buffer


Description
===========

Releases the DMA buffer allocated via ``snd_pcm_lib_malloc_pages``.


Return
======

Zero if successful, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
