
.. _API-snd-pcm-lib-get-vmalloc-page:

============================
snd_pcm_lib_get_vmalloc_page
============================

*man snd_pcm_lib_get_vmalloc_page(9)*

*4.6.0-rc1*

map vmalloc buffer offset to page struct


Synopsis
========

.. c:function:: struct page ⋆ snd_pcm_lib_get_vmalloc_page( struct snd_pcm_substream * substream, unsigned long offset )

Arguments
=========

``substream``
    the substream with a buffer allocated by ``snd_pcm_lib_alloc_vmalloc_buffer``

``offset``
    offset in the buffer


Description
===========

This function is to be used as the page callback in the PCM ops.


Return
======

The page struct, or ``NULL`` on failure.
