
.. _API-snd-pcm-stream-unlock-irqrestore:

================================
snd_pcm_stream_unlock_irqrestore
================================

*man snd_pcm_stream_unlock_irqrestore(9)*

*4.6.0-rc1*

Unlock the PCM stream


Synopsis
========

.. c:function:: void snd_pcm_stream_unlock_irqrestore( struct snd_pcm_substream * substream, unsigned long flags )

Arguments
=========

``substream``
    PCM substream

``flags``
    irq flags


Description
===========

This is a counter-part of ``snd_pcm_stream_lock_irqsave``.
