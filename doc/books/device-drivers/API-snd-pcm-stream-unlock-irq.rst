.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-stream-unlock-irq:

=========================
snd_pcm_stream_unlock_irq
=========================

*man snd_pcm_stream_unlock_irq(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
