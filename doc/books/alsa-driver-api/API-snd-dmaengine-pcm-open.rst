
.. _API-snd-dmaengine-pcm-open:

======================
snd_dmaengine_pcm_open
======================

*man snd_dmaengine_pcm_open(9)*

*4.6.0-rc1*

Open a dmaengine based PCM substream


Synopsis
========

.. c:function:: int snd_dmaengine_pcm_open( struct snd_pcm_substream * substream, struct dma_chan * chan )

Arguments
=========

``substream``
    PCM substream

``chan``
    DMA channel to use for data transfers


Description
===========

Returns 0 on success, a negative error code otherwise.

The function should usually be called from the pcm open callback. Note that this function will use private_data field of the substream's runtime. So it is not available to your
pcm driver implementation.
