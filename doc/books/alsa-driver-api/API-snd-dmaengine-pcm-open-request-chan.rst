.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dmaengine-pcm-open-request-chan:

===================================
snd_dmaengine_pcm_open_request_chan
===================================

*man snd_dmaengine_pcm_open_request_chan(9)*

*4.6.0-rc5*

Open a dmaengine based PCM substream and request channel


Synopsis
========

.. c:function:: int snd_dmaengine_pcm_open_request_chan( struct snd_pcm_substream * substream, dma_filter_fn filter_fn, void * filter_data )

Arguments
=========

``substream``
    PCM substream

``filter_fn``
    Filter function used to request the DMA channel

``filter_data``
    Data passed to the DMA filter function


Description
===========

Returns 0 on success, a negative error code otherwise.

This function will request a DMA channel using the passed filter
function and data. The function should usually be called from the pcm
open callback. Note that this function will use private_data field of
the substream's runtime. So it is not available to your pcm driver
implementation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
