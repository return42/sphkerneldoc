.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-stream-lock:

===================
snd_pcm_stream_lock
===================

*man snd_pcm_stream_lock(9)*

*4.6.0-rc5*

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

This locks the PCM stream's spinlock or mutex depending on the nonatomic
flag of the given substream. This also takes the global link rw lock (or
rw sem), too, for avoiding the race with linked streams.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
