
.. _API-snd-pcm-limit-hw-rates:

======================
snd_pcm_limit_hw_rates
======================

*man snd_pcm_limit_hw_rates(9)*

*4.6.0-rc1*

determine rate_min/rate_max fields


Synopsis
========

.. c:function:: int snd_pcm_limit_hw_rates( struct snd_pcm_runtime * runtime )

Arguments
=========

``runtime``
    the runtime instance


Description
===========

Determines the rate_min and rate_max fields from the rates bits of the given runtime->hw.


Return
======

Zero if successful.
