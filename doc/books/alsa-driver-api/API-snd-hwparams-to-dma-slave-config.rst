
.. _API-snd-hwparams-to-dma-slave-config:

================================
snd_hwparams_to_dma_slave_config
================================

*man snd_hwparams_to_dma_slave_config(9)*

*4.6.0-rc1*

Convert hw_params to dma_slave_config


Synopsis
========

.. c:function:: int snd_hwparams_to_dma_slave_config( const struct snd_pcm_substream * substream, const struct snd_pcm_hw_params * params, struct dma_slave_config * slave_config )

Arguments
=========

``substream``
    PCM substream

``params``
    hw_params

``slave_config``
    DMA slave config


Description
===========

This function can be used to initialize a dma_slave_config from a substream and hw_params in a dmaengine based PCM driver implementation.
