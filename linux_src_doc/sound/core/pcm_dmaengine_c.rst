.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/pcm_dmaengine.c

.. _`snd_hwparams_to_dma_slave_config`:

snd_hwparams_to_dma_slave_config
================================

.. c:function:: int snd_hwparams_to_dma_slave_config(const struct snd_pcm_substream *substream, const struct snd_pcm_hw_params *params, struct dma_slave_config *slave_config)

    Convert hw_params to dma_slave_config

    :param substream:
        PCM substream
    :type substream: const struct snd_pcm_substream \*

    :param params:
        hw_params
    :type params: const struct snd_pcm_hw_params \*

    :param slave_config:
        DMA slave config
    :type slave_config: struct dma_slave_config \*

.. _`snd_hwparams_to_dma_slave_config.description`:

Description
-----------

This function can be used to initialize a dma_slave_config from a substream
and hw_params in a dmaengine based PCM driver implementation.

.. _`snd_dmaengine_pcm_set_config_from_dai_data`:

snd_dmaengine_pcm_set_config_from_dai_data
==========================================

.. c:function:: void snd_dmaengine_pcm_set_config_from_dai_data(const struct snd_pcm_substream *substream, const struct snd_dmaengine_dai_dma_data *dma_data, struct dma_slave_config *slave_config)

    Initializes a dma slave config using DAI DMA data.

    :param substream:
        PCM substream
    :type substream: const struct snd_pcm_substream \*

    :param dma_data:
        DAI DMA data
    :type dma_data: const struct snd_dmaengine_dai_dma_data \*

    :param slave_config:
        DMA slave configuration
    :type slave_config: struct dma_slave_config \*

.. _`snd_dmaengine_pcm_set_config_from_dai_data.description`:

Description
-----------

Initializes the {dst,src}_addr, {dst,src}_maxburst, {dst,src}_addr_width and
slave_id fields of the DMA slave config from the same fields of the DAI DMA
data struct. The src and dst fields will be initialized depending on the
direction of the substream. If the substream is a playback stream the dst
fields will be initialized, if it is a capture stream the src fields will be
initialized. The {dst,src}_addr_width field will only be initialized if the
SND_DMAENGINE_PCM_DAI_FLAG_PACK flag is set or if the addr_width field of
the DAI DMA data struct is not equal to DMA_SLAVE_BUSWIDTH_UNDEFINED. If
both conditions are met the latter takes priority.

.. _`snd_dmaengine_pcm_trigger`:

snd_dmaengine_pcm_trigger
=========================

.. c:function:: int snd_dmaengine_pcm_trigger(struct snd_pcm_substream *substream, int cmd)

    dmaengine based PCM trigger implementation

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

    :param cmd:
        Trigger command
    :type cmd: int

.. _`snd_dmaengine_pcm_trigger.description`:

Description
-----------

Returns 0 on success, a negative error code otherwise.

This function can be used as the PCM trigger callback for dmaengine based PCM
driver implementations.

.. _`snd_dmaengine_pcm_pointer_no_residue`:

snd_dmaengine_pcm_pointer_no_residue
====================================

.. c:function:: snd_pcm_uframes_t snd_dmaengine_pcm_pointer_no_residue(struct snd_pcm_substream *substream)

    dmaengine based PCM pointer implementation

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_dmaengine_pcm_pointer_no_residue.description`:

Description
-----------

This function is deprecated and should not be used by new drivers, as its
results may be unreliable.

.. _`snd_dmaengine_pcm_pointer`:

snd_dmaengine_pcm_pointer
=========================

.. c:function:: snd_pcm_uframes_t snd_dmaengine_pcm_pointer(struct snd_pcm_substream *substream)

    dmaengine based PCM pointer implementation

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_dmaengine_pcm_pointer.description`:

Description
-----------

This function can be used as the PCM pointer callback for dmaengine based PCM
driver implementations.

.. _`snd_dmaengine_pcm_request_channel`:

snd_dmaengine_pcm_request_channel
=================================

.. c:function:: struct dma_chan *snd_dmaengine_pcm_request_channel(dma_filter_fn filter_fn, void *filter_data)

    Request channel for the dmaengine PCM

    :param filter_fn:
        Filter function used to request the DMA channel
    :type filter_fn: dma_filter_fn

    :param filter_data:
        Data passed to the DMA filter function
    :type filter_data: void \*

.. _`snd_dmaengine_pcm_request_channel.description`:

Description
-----------

Returns NULL or the requested DMA channel.

This function request a DMA channel for usage with dmaengine PCM.

.. _`snd_dmaengine_pcm_open`:

snd_dmaengine_pcm_open
======================

.. c:function:: int snd_dmaengine_pcm_open(struct snd_pcm_substream *substream, struct dma_chan *chan)

    Open a dmaengine based PCM substream

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

    :param chan:
        DMA channel to use for data transfers
    :type chan: struct dma_chan \*

.. _`snd_dmaengine_pcm_open.description`:

Description
-----------

Returns 0 on success, a negative error code otherwise.

The function should usually be called from the pcm open callback. Note that
this function will use private_data field of the substream's runtime. So it
is not available to your pcm driver implementation.

.. _`snd_dmaengine_pcm_open_request_chan`:

snd_dmaengine_pcm_open_request_chan
===================================

.. c:function:: int snd_dmaengine_pcm_open_request_chan(struct snd_pcm_substream *substream, dma_filter_fn filter_fn, void *filter_data)

    Open a dmaengine based PCM substream and request channel

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

    :param filter_fn:
        Filter function used to request the DMA channel
    :type filter_fn: dma_filter_fn

    :param filter_data:
        Data passed to the DMA filter function
    :type filter_data: void \*

.. _`snd_dmaengine_pcm_open_request_chan.description`:

Description
-----------

Returns 0 on success, a negative error code otherwise.

This function will request a DMA channel using the passed filter function and
data. The function should usually be called from the pcm open callback. Note
that this function will use private_data field of the substream's runtime. So
it is not available to your pcm driver implementation.

.. _`snd_dmaengine_pcm_close`:

snd_dmaengine_pcm_close
=======================

.. c:function:: int snd_dmaengine_pcm_close(struct snd_pcm_substream *substream)

    Close a dmaengine based PCM substream

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_dmaengine_pcm_close_release_chan`:

snd_dmaengine_pcm_close_release_chan
====================================

.. c:function:: int snd_dmaengine_pcm_close_release_chan(struct snd_pcm_substream *substream)

    Close a dmaengine based PCM substream and release channel

    :param substream:
        PCM substream
    :type substream: struct snd_pcm_substream \*

.. _`snd_dmaengine_pcm_close_release_chan.description`:

Description
-----------

Releases the DMA channel associated with the PCM substream.

.. This file was automatic generated / don't edit.

