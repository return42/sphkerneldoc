.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-stream-unlock:

=====================
snd_pcm_stream_unlock
=====================

*man snd_pcm_stream_unlock(9)*

*4.6.0-rc5*

Unlock the PCM stream


Synopsis
========

.. c:function:: void snd_pcm_stream_unlock( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    PCM substream


Description
===========

This unlocks the PCM stream that has been locked via
``snd_pcm_stream_lock``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
