.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-lib-mmap-iomem:

======================
snd_pcm_lib_mmap_iomem
======================

*man snd_pcm_lib_mmap_iomem(9)*

*4.6.0-rc5*

Default PCM data mmap function for I/O mem


Synopsis
========

.. c:function:: int snd_pcm_lib_mmap_iomem( struct snd_pcm_substream * substream, struct vm_area_struct * area )

Arguments
=========

``substream``
    PCM substream

``area``
    VMA


Description
===========

When your hardware uses the iomapped pages as the hardware buffer and
wants to mmap it, pass this function as mmap pcm_ops. Note that this is
supposed to work only on limited architectures.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
