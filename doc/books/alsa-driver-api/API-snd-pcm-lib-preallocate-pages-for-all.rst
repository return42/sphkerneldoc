
.. _API-snd-pcm-lib-preallocate-pages-for-all:

=====================================
snd_pcm_lib_preallocate_pages_for_all
=====================================

*man snd_pcm_lib_preallocate_pages_for_all(9)*

*4.6.0-rc1*

pre-allocation for continuous memory type (all substreams)


Synopsis
========

.. c:function:: int snd_pcm_lib_preallocate_pages_for_all( struct snd_pcm * pcm, int type, void * data, size_t size, size_t max )

Arguments
=========

``pcm``
    the pcm instance

``type``
    DMA type (SNDRV_DMA_TYPE_⋆)

``data``
    DMA type dependent data

``size``
    the requested pre-allocation size in bytes

``max``
    the max. allowed pre-allocation size


Description
===========

Do pre-allocation to all substreams of the given pcm for the specified DMA type.


Return
======

Zero if successful, or a negative error code on failure.
