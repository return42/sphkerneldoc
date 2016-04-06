
.. _API-snd-pcm-new-stream:

==================
snd_pcm_new_stream
==================

*man snd_pcm_new_stream(9)*

*4.6.0-rc1*

create a new PCM stream


Synopsis
========

.. c:function:: int snd_pcm_new_stream( struct snd_pcm * pcm, int stream, int substream_count )

Arguments
=========

``pcm``
    the pcm instance

``stream``
    the stream direction, SNDRV_PCM_STREAM_XXX

``substream_count``
    the number of substreams


Description
===========

Creates a new stream for the pcm. The corresponding stream on the pcm must have been empty before calling this, i.e. zero must be given to the argument of ``snd_pcm_new``.


Return
======

Zero if successful, or a negative error code on failure.
