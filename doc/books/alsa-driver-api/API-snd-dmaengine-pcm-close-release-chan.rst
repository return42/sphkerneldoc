
.. _API-snd-dmaengine-pcm-close-release-chan:

====================================
snd_dmaengine_pcm_close_release_chan
====================================

*man snd_dmaengine_pcm_close_release_chan(9)*

*4.6.0-rc1*

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
