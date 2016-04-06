
.. _API-snd-pcm-stream-lock-irqsave:

===========================
snd_pcm_stream_lock_irqsave
===========================

*man snd_pcm_stream_lock_irqsave(9)*

*4.6.0-rc1*

Lock the PCM stream


Synopsis
========

.. c:function:: snd_pcm_stream_lock_irqsave( substream, flags )

Arguments
=========

``substream``
    PCM substream

``flags``
    irq flags


Description
===========

This locks the PCM stream like ``snd_pcm_stream_lock`` but with the local IRQ (only when nonatomic is false). In nonatomic case, this is identical as ``snd_pcm_stream_lock``.
