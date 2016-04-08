
.. _API-snd-pcm-rate-to-rate-bit:

========================
snd_pcm_rate_to_rate_bit
========================

*man snd_pcm_rate_to_rate_bit(9)*

*4.6.0-rc1*

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

The SNDRV_PCM_RATE_xxx flag that corresponds to the given rate, or SNDRV_PCM_RATE_KNOT for an unknown rate.
