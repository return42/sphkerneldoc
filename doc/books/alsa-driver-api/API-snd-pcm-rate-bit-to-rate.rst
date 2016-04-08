
.. _API-snd-pcm-rate-bit-to-rate:

========================
snd_pcm_rate_bit_to_rate
========================

*man snd_pcm_rate_bit_to_rate(9)*

*4.6.0-rc1*

converts SNDRV_PCM_RATE_xxx bit to sample rate


Synopsis
========

.. c:function:: unsigned int snd_pcm_rate_bit_to_rate( unsigned int rate_bit )

Arguments
=========

``rate_bit``
    the rate bit to convert


Return
======

The sample rate that corresponds to the given SNDRV_PCM_RATE_xxx flag or 0 for an unknown rate bit.
