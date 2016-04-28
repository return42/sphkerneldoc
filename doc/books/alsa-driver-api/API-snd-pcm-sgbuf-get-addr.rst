.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-sgbuf-get-addr:

======================
snd_pcm_sgbuf_get_addr
======================

*man snd_pcm_sgbuf_get_addr(9)*

*4.6.0-rc5*

Get the DMA address at the corresponding offset


Synopsis
========

.. c:function:: dma_addr_t snd_pcm_sgbuf_get_addr( struct snd_pcm_substream * substream, unsigned int ofs )

Arguments
=========

``substream``
    PCM substream

``ofs``
    byte offset


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
