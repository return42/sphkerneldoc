.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-lib-preallocate-pages:

=============================
snd_pcm_lib_preallocate_pages
=============================

*man snd_pcm_lib_preallocate_pages(9)*

*4.6.0-rc5*

pre-allocation for the given DMA type


Synopsis
========

.. c:function:: int snd_pcm_lib_preallocate_pages( struct snd_pcm_substream * substream, int type, struct device * data, size_t size, size_t max )

Arguments
=========

``substream``
    the pcm substream instance

``type``
    DMA type (SNDRV_DMA_TYPE_*)

``data``
    DMA type dependent data

``size``
    the requested pre-allocation size in bytes

``max``
    the max. allowed pre-allocation size


Description
===========

Do pre-allocation for the given DMA buffer type.


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
