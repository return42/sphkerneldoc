.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/dmaengine_pcm.h

.. _`snd_pcm_substream_to_dma_direction`:

snd_pcm_substream_to_dma_direction
==================================

.. c:function:: enum dma_transfer_direction snd_pcm_substream_to_dma_direction(const struct snd_pcm_substream *substream)

    Get dma_transfer_direction for a PCM substream

    :param const struct snd_pcm_substream \*substream:
        PCM substream

.. _`snd_dmaengine_dai_dma_data`:

struct snd_dmaengine_dai_dma_data
=================================

.. c:type:: struct snd_dmaengine_dai_dma_data

    DAI DMA configuration data

.. _`snd_dmaengine_dai_dma_data.definition`:

Definition
----------

.. code-block:: c

    struct snd_dmaengine_dai_dma_data {
        dma_addr_t addr;
        enum dma_slave_buswidth addr_width;
        u32 maxburst;
        unsigned int slave_id;
        void *filter_data;
        unsigned int fifo_size;
        unsigned int flags;
    }

.. _`snd_dmaengine_dai_dma_data.members`:

Members
-------

addr
    Address of the DAI data source or destination register.

addr_width
    Width of the DAI data source or destination register.

maxburst
    Maximum number of words(note: words, as in units of the
    src_addr_width member, not bytes) that can be send to or received from the
    DAI in one burst.

slave_id
    Slave requester id for the DMA channel.

filter_data
    Custom DMA channel filter data, this will usually be used when
    requesting the DMA channel.

fifo_size
    FIFO size of the DAI controller in bytes

flags
    PCM_DAI flags, only SND_DMAENGINE_PCM_DAI_FLAG_PACK for now

.. _`snd_dmaengine_pcm_config`:

struct snd_dmaengine_pcm_config
===============================

.. c:type:: struct snd_dmaengine_pcm_config

    Configuration data for dmaengine based PCM

.. _`snd_dmaengine_pcm_config.definition`:

Definition
----------

.. code-block:: c

    struct snd_dmaengine_pcm_config {
        int (*prepare_slave_config)(struct snd_pcm_substream *substream,struct snd_pcm_hw_params *params,struct dma_slave_config *slave_config);
        struct dma_chan *(*compat_request_channel)(struct snd_soc_pcm_runtime *rtd,struct snd_pcm_substream *substream);
        dma_filter_fn compat_filter_fn;
        struct device *dma_dev;
        const char  *chan_names[SNDRV_PCM_STREAM_LAST + 1];
        const struct snd_pcm_hardware *pcm_hardware;
        unsigned int prealloc_buffer_size;
    }

.. _`snd_dmaengine_pcm_config.members`:

Members
-------

prepare_slave_config
    Callback used to fill in the DMA slave_config for a
    PCM substream. Will be called from the PCM drivers hwparams callback.

compat_request_channel
    Callback to request a DMA channel for platforms
    which do not use devicetree.

compat_filter_fn
    Will be used as the filter function when requesting a
    channel for platforms which do not use devicetree. The filter parameter
    will be the DAI's DMA data.

dma_dev
    If set, request DMA channel on this device rather than the DAI
    device.

chan_names
    If set, these custom DMA channel names will be requested at
    registration time.

pcm_hardware
    snd_pcm_hardware struct to be used for the PCM.

prealloc_buffer_size
    Size of the preallocated audio buffer.

.. _`snd_dmaengine_pcm_config.note`:

Note
----

If both compat_request_channel and compat_filter_fn are set
compat_request_channel will be used to request the channel and
compat_filter_fn will be ignored. Otherwise the channel will be requested
using dma_request_channel with compat_filter_fn as the filter function.

.. This file was automatic generated / don't edit.

