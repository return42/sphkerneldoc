.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-stream-unlock-irqrestore:

================================
snd_pcm_stream_unlock_irqrestore
================================

*man snd_pcm_stream_unlock_irqrestore(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
