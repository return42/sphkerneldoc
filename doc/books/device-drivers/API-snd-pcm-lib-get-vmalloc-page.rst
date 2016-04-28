.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-lib-get-vmalloc-page:

============================
snd_pcm_lib_get_vmalloc_page
============================

*man snd_pcm_lib_get_vmalloc_page(9)*

*4.6.0-rc5*

map vmalloc buffer offset to page struct


Synopsis
========

.. c:function:: struct page * snd_pcm_lib_get_vmalloc_page( struct snd_pcm_substream * substream, unsigned long offset )

Arguments
=========

``substream``
    the substream with a buffer allocated by
    ``snd_pcm_lib_alloc_vmalloc_buffer``

``offset``
    offset in the buffer


Description
===========

This function is to be used as the page callback in the PCM ops.


Return
======

The page struct, or ``NULL`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
