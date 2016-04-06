
.. _API-snd-pcm-stream-linked:

=====================
snd_pcm_stream_linked
=====================

*man snd_pcm_stream_linked(9)*

*4.6.0-rc1*

Check whether the substream is linked with others


Synopsis
========

.. c:function:: int snd_pcm_stream_linked( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    substream to check


Description
===========

Returns true if the given substream is being linked with others.
