
.. _API-snd-dmaengine-pcm-trigger:

=========================
snd_dmaengine_pcm_trigger
=========================

*man snd_dmaengine_pcm_trigger(9)*

*4.6.0-rc1*

dmaengine based PCM trigger implementation


Synopsis
========

.. c:function:: int snd_dmaengine_pcm_trigger( struct snd_pcm_substream * substream, int cmd )

Arguments
=========

``substream``
    PCM substream

``cmd``
    Trigger command


Description
===========

Returns 0 on success, a negative error code otherwise.

This function can be used as the PCM trigger callback for dmaengine based PCM driver implementations.
