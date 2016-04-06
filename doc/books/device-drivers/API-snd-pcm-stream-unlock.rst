
.. _API-snd-pcm-stream-unlock:

=====================
snd_pcm_stream_unlock
=====================

*man snd_pcm_stream_unlock(9)*

*4.6.0-rc1*

Unlock the PCM stream


Synopsis
========

.. c:function:: void snd_pcm_stream_unlock( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    PCM substream


Description
===========

This unlocks the PCM stream that has been locked via ``snd_pcm_stream_lock``.
