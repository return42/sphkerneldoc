
.. _API-snd-pcm-set-sync:

================
snd_pcm_set_sync
================

*man snd_pcm_set_sync(9)*

*4.6.0-rc1*

set the PCM sync id


Synopsis
========

.. c:function:: void snd_pcm_set_sync( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the pcm substream


Description
===========

Sets the PCM sync identifier for the card.
