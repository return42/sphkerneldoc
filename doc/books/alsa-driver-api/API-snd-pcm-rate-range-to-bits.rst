.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-rate-range-to-bits:

==========================
snd_pcm_rate_range_to_bits
==========================

*man snd_pcm_rate_range_to_bits(9)*

*4.6.0-rc5*

converts rate range to SNDRV_PCM_RATE_xxx bit


Synopsis
========

.. c:function:: unsigned int snd_pcm_rate_range_to_bits( unsigned int rate_min, unsigned int rate_max )

Arguments
=========

``rate_min``
    the minimum sample rate

``rate_max``
    the maximum sample rate


This function has an implicit assumption
========================================

the rates in the given range have only the pre-defined rates like 44100
or 16000.


Return
======

The SNDRV_PCM_RATE_xxx flag that corresponds to the given rate range,
or SNDRV_PCM_RATE_KNOT for an unknown range.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
