.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-hw-rule-noresample:

==========================
snd_pcm_hw_rule_noresample
==========================

*man snd_pcm_hw_rule_noresample(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
