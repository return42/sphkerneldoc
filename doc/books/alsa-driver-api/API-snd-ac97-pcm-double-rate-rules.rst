.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-pcm-double-rate-rules:

==============================
snd_ac97_pcm_double_rate_rules
==============================

*man snd_ac97_pcm_double_rate_rules(9)*

*4.6.0-rc5*

set double rate constraints


Synopsis
========

.. c:function:: int snd_ac97_pcm_double_rate_rules( struct snd_pcm_runtime * runtime )

Arguments
=========

``runtime``
    the runtime of the ac97 front playback pcm


Description
===========

Installs the hardware constraint rules to prevent using double rates and
more than two channels at the same time.


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
