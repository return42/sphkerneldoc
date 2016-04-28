.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-lib-alloc-vmalloc-buffer:

================================
snd_pcm_lib_alloc_vmalloc_buffer
================================

*man snd_pcm_lib_alloc_vmalloc_buffer(9)*

*4.6.0-rc5*

allocate virtual DMA buffer


Synopsis
========

.. c:function:: int snd_pcm_lib_alloc_vmalloc_buffer( struct snd_pcm_substream * substream, size_t size )

Arguments
=========

``substream``
    the substream to allocate the buffer to

``size``
    the requested buffer size, in bytes


Description
===========

Allocates the PCM substream buffer using ``vmalloc``, i.e., the memory
is contiguous in kernel virtual space, but not in physical memory. Use
this if the buffer is accessed by kernel code but not by device DMA.


Return
======

1 if the buffer was changed, 0 if not changed, or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
