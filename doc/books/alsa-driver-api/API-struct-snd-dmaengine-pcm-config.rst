.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-dmaengine-pcm-config:

===============================
struct snd_dmaengine_pcm_config
===============================

*man struct snd_dmaengine_pcm_config(9)*

*4.6.0-rc5*

Configuration data for dmaengine based PCM


Synopsis
========

.. code-block:: c

    struct snd_dmaengine_pcm_config {
      int (* prepare_slave_config) (struct snd_pcm_substream *substream,struct snd_pcm_hw_params *params,struct dma_slave_config *slave_config);
      struct dma_chan *(* compat_request_channel) (struct snd_soc_pcm_runtime *rtd,struct snd_pcm_substream *substream);
      dma_filter_fn compat_filter_fn;
      struct device * dma_dev;
      const char * chan_names[SNDRV_PCM_STREAM_LAST + 1];
      const struct snd_pcm_hardware * pcm_hardware;
      unsigned int prealloc_buffer_size;
    };


Members
=======

prepare_slave_config
    Callback used to fill in the DMA slave_config for a PCM substream.
    Will be called from the PCM drivers hwparams callback.

compat_request_channel
    Callback to request a DMA channel for platforms which do not use
    devicetree.

compat_filter_fn
    Will be used as the filter function when requesting a channel for
    platforms which do not use devicetree. The filter parameter will be
    the DAI's DMA data.

dma_dev
    If set, request DMA channel on this device rather than the DAI
    device.

chan_names[SNDRV_PCM_STREAM_LAST + 1]
    If set, these custom DMA channel names will be requested at
    registration time.

pcm_hardware
    snd_pcm_hardware struct to be used for the PCM.

prealloc_buffer_size
    Size of the preallocated audio buffer.


Note
====

If both compat_request_channel and compat_filter_fn are set
compat_request_channel will be used to request the channel and
compat_filter_fn will be ignored. Otherwise the channel will be
requested using dma_request_channel with compat_filter_fn as the
filter function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
