
.. _API-snd-pcm-sgbuf-get-addr:

======================
snd_pcm_sgbuf_get_addr
======================

*man snd_pcm_sgbuf_get_addr(9)*

*4.6.0-rc1*

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
