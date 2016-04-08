
.. _API-snd-soc-dapm-force-enable-pin:

=============================
snd_soc_dapm_force_enable_pin
=============================

*man snd_soc_dapm_force_enable_pin(9)*

*4.6.0-rc1*

force a pin to be enabled


Synopsis
========

.. c:function:: int snd_soc_dapm_force_enable_pin( struct snd_soc_dapm_context * dapm, const char * pin )

Arguments
=========

``dapm``
    DAPM context

``pin``
    pin name


Description
===========

Enables input/output pin regardless of any other state. This is intended for use with microphone bias supplies used in microphone jack detection.


NOTE
====

``snd_soc_dapm_sync`` needs to be called after this for DAPM to do any widget power switching.
