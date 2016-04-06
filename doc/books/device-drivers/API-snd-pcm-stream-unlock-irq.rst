
.. _API-snd-pcm-stream-unlock-irq:

=========================
snd_pcm_stream_unlock_irq
=========================

*man snd_pcm_stream_unlock_irq(9)*

*4.6.0-rc1*

Unlock the PCM stream


Synopsis
========

.. c:function:: void snd_pcm_stream_unlock_irq( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    PCM substream


Description
===========

This is a counter-part of ``snd_pcm_stream_lock_irq``.
