
.. _API-snd-pcm-stop:

============
snd_pcm_stop
============

*man snd_pcm_stop(9)*

*4.6.0-rc1*

try to stop all running streams in the substream group


Synopsis
========

.. c:function:: int snd_pcm_stop( struct snd_pcm_substream * substream, snd_pcm_state_t state )

Arguments
=========

``substream``
    the PCM substream instance

``state``
    PCM state after stopping the stream


Description
===========

The state of each stream is then changed to the given state unconditionally.


Return
======

Zero if successful, or a negative error code.
