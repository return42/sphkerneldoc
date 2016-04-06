
.. _API-snd-pcm-limit-isa-dma-size:

==========================
snd_pcm_limit_isa_dma_size
==========================

*man snd_pcm_limit_isa_dma_size(9)*

*4.6.0-rc1*

Get the max size fitting with ISA DMA transfer


Synopsis
========

.. c:function:: void snd_pcm_limit_isa_dma_size( int dma, size_t * max )

Arguments
=========

``dma``
    DMA number

``max``
    pointer to store the max size
