.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dmaengine-pcm-prepare-slave-config:

======================================
snd_dmaengine_pcm_prepare_slave_config
======================================

*man snd_dmaengine_pcm_prepare_slave_config(9)*

*4.6.0-rc5*

Generic prepare_slave_config callback


Synopsis
========

.. c:function:: int snd_dmaengine_pcm_prepare_slave_config( struct snd_pcm_substream * substream, struct snd_pcm_hw_params * params, struct dma_slave_config * slave_config )

Arguments
=========

``substream``
    PCM substream

``params``
    hw_params

``slave_config``
    DMA slave config to prepare


Description
===========

This function can be used as a generic prepare_slave_config callback
for platforms which make use of the snd_dmaengine_dai_dma_data
struct for their DAI DMA data. Internally the function will first call
snd_hwparams_to_dma_slave_config to fill in the slave config based
on the hw_params, followed by
snd_dmaengine_set_config_from_dai_data to fill in the remaining
fields based on the DAI DMA data.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
