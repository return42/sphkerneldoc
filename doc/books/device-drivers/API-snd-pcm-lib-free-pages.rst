
.. _API-snd-pcm-lib-free-pages:

======================
snd_pcm_lib_free_pages
======================

*man snd_pcm_lib_free_pages(9)*

*4.6.0-rc1*

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
