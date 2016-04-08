
.. _API-snd-pcm-hw-rule-noresample:

==========================
snd_pcm_hw_rule_noresample
==========================

*man snd_pcm_hw_rule_noresample(9)*

*4.6.0-rc1*

add a rule to allow disabling hw resampling


Synopsis
========

.. c:function:: int snd_pcm_hw_rule_noresample( struct snd_pcm_runtime * runtime, unsigned int base_rate )

Arguments
=========

``runtime``
    PCM runtime instance

``base_rate``
    the rate at which the hardware does not resample


Return
======

Zero if successful, or a negative error code on failure.
