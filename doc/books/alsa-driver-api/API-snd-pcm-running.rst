
.. _API-snd-pcm-running:

===============
snd_pcm_running
===============

*man snd_pcm_running(9)*

*4.6.0-rc1*

Check whether the substream is in a running state


Synopsis
========

.. c:function:: int snd_pcm_running( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    substream to check


Description
===========

Returns true if the given substream is in the state RUNNING, or in the state DRAINING for playback.
