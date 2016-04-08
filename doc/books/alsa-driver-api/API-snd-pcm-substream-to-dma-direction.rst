
.. _API-snd-pcm-substream-to-dma-direction:

==================================
snd_pcm_substream_to_dma_direction
==================================

*man snd_pcm_substream_to_dma_direction(9)*

*4.6.0-rc1*

Get dma_transfer_direction for a PCM substream


Synopsis
========

.. c:function:: enum dma_transfer_direction snd_pcm_substream_to_dma_direction( const struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    PCM substream
