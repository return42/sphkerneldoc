
.. _API-snd-pcm-stream-str:

==================
snd_pcm_stream_str
==================

*man snd_pcm_stream_str(9)*

*4.6.0-rc1*

Get a string naming the direction of a stream


Synopsis
========

.. c:function:: const char ⋆ snd_pcm_stream_str( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the pcm substream instance


Return
======

A string naming the direction of the stream.
