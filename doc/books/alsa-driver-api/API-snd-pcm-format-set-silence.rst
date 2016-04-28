.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-format-set-silence:

==========================
snd_pcm_format_set_silence
==========================

*man snd_pcm_format_set_silence(9)*

*4.6.0-rc5*

set the silence data on the buffer


Synopsis
========

.. c:function:: int snd_pcm_format_set_silence( snd_pcm_format_t format, void * data, unsigned int samples )

Arguments
=========

``format``
    the PCM format

``data``
    the buffer pointer

``samples``
    the number of samples to set silence


Description
===========

Sets the silence data on the buffer for the given samples.


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
