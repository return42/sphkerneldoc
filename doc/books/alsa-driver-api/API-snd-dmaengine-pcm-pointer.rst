
.. _API-snd-dmaengine-pcm-pointer:

=========================
snd_dmaengine_pcm_pointer
=========================

*man snd_dmaengine_pcm_pointer(9)*

*4.6.0-rc1*

dmaengine based PCM pointer implementation


Synopsis
========

.. c:function:: snd_pcm_uframes_t snd_dmaengine_pcm_pointer( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    PCM substream


Description
===========

This function can be used as the PCM pointer callback for dmaengine based PCM driver implementations.
