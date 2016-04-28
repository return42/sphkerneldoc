.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-new:

===========
snd_pcm_new
===========

*man snd_pcm_new(9)*

*4.6.0-rc5*

create a new PCM instance


Synopsis
========

.. c:function:: int snd_pcm_new( struct snd_card * card, const char * id, int device, int playback_count, int capture_count, struct snd_pcm ** rpcm )

Arguments
=========

``card``
    the card instance

``id``
    the id string

``device``
    the device index (zero based)

``playback_count``
    the number of substreams for playback

``capture_count``
    the number of substreams for capture

``rpcm``
    the pointer to store the new pcm instance


Description
===========

Creates a new PCM instance.

The pcm operators have to be set afterwards to the new instance via
``snd_pcm_set_ops``.


Return
======

Zero if successful, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
