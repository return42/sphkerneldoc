
.. _API-snd-pcm-lib-malloc-pages:

========================
snd_pcm_lib_malloc_pages
========================

*man snd_pcm_lib_malloc_pages(9)*

*4.6.0-rc1*

allocate the DMA buffer


Synopsis
========

.. c:function:: int snd_pcm_lib_malloc_pages( struct snd_pcm_substream * substream, size_t size )

Arguments
=========

``substream``
    the substream to allocate the DMA buffer to

``size``
    the requested buffer size in bytes


Description
===========

Allocates the DMA buffer on the BUS type given earlier to ``snd_pcm_lib_preallocate_xxx_pages``.


Return
======

1 if the buffer is changed, 0 if not changed, or a negative code on failure.
