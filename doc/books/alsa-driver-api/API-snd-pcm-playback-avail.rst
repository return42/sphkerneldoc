
.. _API-snd-pcm-playback-avail:

======================
snd_pcm_playback_avail
======================

*man snd_pcm_playback_avail(9)*

*4.6.0-rc1*

Get the available (writable) space for playback


Synopsis
========

.. c:function:: snd_pcm_uframes_t snd_pcm_playback_avail( struct snd_pcm_runtime * runtime )

Arguments
=========

``runtime``
    PCM runtime instance


Description
===========

Result is between 0 ... (boundary - 1)
