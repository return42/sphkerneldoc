
.. _API-snd-pcm-rate-mask-intersect:

===========================
snd_pcm_rate_mask_intersect
===========================

*man snd_pcm_rate_mask_intersect(9)*

*4.6.0-rc1*

computes the intersection between two rate masks


Synopsis
========

.. c:function:: unsigned int snd_pcm_rate_mask_intersect( unsigned int rates_a, unsigned int rates_b )

Arguments
=========

``rates_a``
    The first rate mask

``rates_b``
    The second rate mask


Description
===========

This function computes the rates that are supported by both rate masks passed to the function. It will take care of the special handling of SNDRV_PCM_RATE_CONTINUOUS and
SNDRV_PCM_RATE_KNOT.


Return
======

A rate mask containing the rates that are supported by both rates_a and rates_b.
