.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-lib-default-mmap:

========================
snd_pcm_lib_default_mmap
========================

*man snd_pcm_lib_default_mmap(9)*

*4.6.0-rc5*

Default PCM data mmap function


Synopsis
========

.. c:function:: int snd_pcm_lib_default_mmap( struct snd_pcm_substream * substream, struct vm_area_struct * area )

Arguments
=========

``substream``
    PCM substream

``area``
    VMA


Description
===========

This is the default mmap handler for PCM data. When mmap pcm_ops is
NULL, this function is invoked implicitly.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
