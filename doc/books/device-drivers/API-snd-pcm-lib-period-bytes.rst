
.. _API-snd-pcm-lib-period-bytes:

========================
snd_pcm_lib_period_bytes
========================

*man snd_pcm_lib_period_bytes(9)*

*4.6.0-rc1*

Get the period size of the current PCM in bytes


Synopsis
========

.. c:function:: size_t snd_pcm_lib_period_bytes( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    PCM substream
