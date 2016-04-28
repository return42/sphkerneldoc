.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-rate-to-rate-bit:

========================
snd_pcm_rate_to_rate_bit
========================

*man snd_pcm_rate_to_rate_bit(9)*

*4.6.0-rc5*

converts sample rate to SNDRV_PCM_RATE_xxx bit


Synopsis
========

.. c:function:: unsigned int snd_pcm_rate_to_rate_bit( unsigned int rate )

Arguments
=========

``rate``
    the sample rate to convert


Return
======

The SNDRV_PCM_RATE_xxx flag that corresponds to the given rate, or
SNDRV_PCM_RATE_KNOT for an unknown rate.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
