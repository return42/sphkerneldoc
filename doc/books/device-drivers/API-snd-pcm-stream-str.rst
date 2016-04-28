.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-stream-str:

==================
snd_pcm_stream_str
==================

*man snd_pcm_stream_str(9)*

*4.6.0-rc5*

Get a string naming the direction of a stream


Synopsis
========

.. c:function:: const char * snd_pcm_stream_str( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the pcm substream instance


Return
======

A string naming the direction of the stream.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
