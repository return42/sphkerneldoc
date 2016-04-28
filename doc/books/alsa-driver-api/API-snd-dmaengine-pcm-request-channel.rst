.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dmaengine-pcm-request-channel:

=================================
snd_dmaengine_pcm_request_channel
=================================

*man snd_dmaengine_pcm_request_channel(9)*

*4.6.0-rc5*

Request channel for the dmaengine PCM


Synopsis
========

.. c:function:: struct dma_chan * snd_dmaengine_pcm_request_channel( dma_filter_fn filter_fn, void * filter_data )

Arguments
=========

``filter_fn``
    Filter function used to request the DMA channel

``filter_data``
    Data passed to the DMA filter function


Description
===========

Returns NULL or the requested DMA channel.

This function request a DMA channel for usage with dmaengine PCM.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
