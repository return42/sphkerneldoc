
.. _API-snd-pcm-playback-hw-avail:

=========================
snd_pcm_playback_hw_avail
=========================

*man snd_pcm_playback_hw_avail(9)*

*4.6.0-rc1*

Get the queued space for playback


Synopsis
========

.. c:function:: snd_pcm_sframes_t snd_pcm_playback_hw_avail( struct snd_pcm_runtime * runtime )

Arguments
=========

``runtime``
    PCM runtime instance
