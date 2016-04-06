
.. _API-snd-pcm-playback-ready:

======================
snd_pcm_playback_ready
======================

*man snd_pcm_playback_ready(9)*

*4.6.0-rc1*

check whether the playback buffer is available


Synopsis
========

.. c:function:: int snd_pcm_playback_ready( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the pcm substream instance


Description
===========

Checks whether enough free space is available on the playback buffer.


Return
======

Non-zero if available, or zero if not.
