
.. _API-snd-pcm-playback-data:

=====================
snd_pcm_playback_data
=====================

*man snd_pcm_playback_data(9)*

*4.6.0-rc1*

check whether any data exists on the playback buffer


Synopsis
========

.. c:function:: int snd_pcm_playback_data( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the pcm substream instance


Description
===========

Checks whether any data exists on the playback buffer.


Return
======

Non-zero if any data exists, or zero if not. If stop_threshold is bigger or equal to boundary, then this function returns always non-zero.
