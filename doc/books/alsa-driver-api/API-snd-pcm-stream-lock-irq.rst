
.. _API-snd-pcm-stream-lock-irq:

=======================
snd_pcm_stream_lock_irq
=======================

*man snd_pcm_stream_lock_irq(9)*

*4.6.0-rc1*

Lock the PCM stream


Synopsis
========

.. c:function:: void snd_pcm_stream_lock_irq( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    PCM substream


Description
===========

This locks the PCM stream like ``snd_pcm_stream_lock`` and disables the local IRQ (only when nonatomic is false). In nonatomic case, this is identical as ``snd_pcm_stream_lock``.
