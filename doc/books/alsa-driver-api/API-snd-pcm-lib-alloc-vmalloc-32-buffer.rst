.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-lib-alloc-vmalloc-32-buffer:

===================================
snd_pcm_lib_alloc_vmalloc_32_buffer
===================================

*man snd_pcm_lib_alloc_vmalloc_32_buffer(9)*

*4.6.0-rc5*

allocate 32-bit-addressable buffer


Synopsis
========

.. c:function:: int snd_pcm_lib_alloc_vmalloc_32_buffer( struct snd_pcm_substream * substream, size_t size )

Arguments
=========

``substream``
    the substream to allocate the buffer to

``size``
    the requested buffer size, in bytes


Description
===========

This function works like ``snd_pcm_lib_alloc_vmalloc_buffer``, but uses
``vmalloc_32``, i.e., the pages are allocated from 32-bit-addressable
memory.


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
