
.. _API-snd-pcm-stream-lock:

===================
snd_pcm_stream_lock
===================

*man snd_pcm_stream_lock(9)*

*4.6.0-rc1*

Lock the PCM stream


Synopsis
========

.. c:function:: void snd_pcm_stream_lock( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    PCM substream


Description
===========

This locks the PCM stream's spinlock or mutex depending on the nonatomic flag of the given substream. This also takes the global link rw lock (or rw sem), too, for avoiding the
race with linked streams.
