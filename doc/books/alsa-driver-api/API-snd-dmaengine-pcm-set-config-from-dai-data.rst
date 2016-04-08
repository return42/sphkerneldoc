
.. _API-snd-dmaengine-pcm-set-config-from-dai-data:

==========================================
snd_dmaengine_pcm_set_config_from_dai_data
==========================================

*man snd_dmaengine_pcm_set_config_from_dai_data(9)*

*4.6.0-rc1*

Initializes a dma slave config using DAI DMA data.


Synopsis
========

.. c:function:: void snd_dmaengine_pcm_set_config_from_dai_data( const struct snd_pcm_substream * substream, const struct snd_dmaengine_dai_dma_data * dma_data, struct dma_slave_config * slave_config )

Arguments
=========

``substream``
    PCM substream

``dma_data``
    DAI DMA data

``slave_config``
    DMA slave configuration


Description
===========

Initializes the {dst,src}_addr, {dst,src}_maxburst, {dst,src}_addr_width and slave_id fields of the DMA slave config from the same fields of the DAI DMA data struct. The src
and dst fields will be initialized depending on the direction of the substream. If the substream is a playback stream the dst fields will be initialized, if it is a capture stream
the src fields will be initialized. The {dst,src}_addr_width field will only be initialized if the addr_width field of the DAI DMA data struct is not equal to
DMA_SLAVE_BUSWIDTH_UNDEFINED.
