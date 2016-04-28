.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dmaengine-pcm-close-release-chan:

====================================
snd_dmaengine_pcm_close_release_chan
====================================

*man snd_dmaengine_pcm_close_release_chan(9)*

*4.6.0-rc5*

Close a dmaengine based PCM substream and release channel


Synopsis
========

.. c:function:: int snd_dmaengine_pcm_close_release_chan( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    PCM substream


Description
===========

Releases the DMA channel associated with the PCM substream.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
