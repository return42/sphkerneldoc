
.. _API-snd-pcm-lib-free-vmalloc-buffer:

===============================
snd_pcm_lib_free_vmalloc_buffer
===============================

*man snd_pcm_lib_free_vmalloc_buffer(9)*

*4.6.0-rc1*

free vmalloc buffer


Synopsis
========

.. c:function:: int snd_pcm_lib_free_vmalloc_buffer( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the substream with a buffer allocated by ``snd_pcm_lib_alloc_vmalloc_buffer``


Return
======

Zero if successful, or a negative error code on failure.
