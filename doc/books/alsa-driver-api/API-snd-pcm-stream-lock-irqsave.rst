.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-stream-lock-irqsave:

===========================
snd_pcm_stream_lock_irqsave
===========================

*man snd_pcm_stream_lock_irqsave(9)*

*4.6.0-rc5*

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

This locks the PCM stream like ``snd_pcm_stream_lock`` but with the
local IRQ (only when nonatomic is false). In nonatomic case, this is
identical as ``snd_pcm_stream_lock``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
