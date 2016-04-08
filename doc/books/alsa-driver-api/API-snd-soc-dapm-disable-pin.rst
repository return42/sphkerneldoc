
.. _API-snd-soc-dapm-disable-pin:

========================
snd_soc_dapm_disable_pin
========================

*man snd_soc_dapm_disable_pin(9)*

*4.6.0-rc1*

disable pin.


Synopsis
========

.. c:function:: int snd_soc_dapm_disable_pin( struct snd_soc_dapm_context * dapm, const char * pin )

Arguments
=========

``dapm``
    DAPM context

``pin``
    pin name


Description
===========

Disables input/output pin and its parents or children widgets.


NOTE
====

``snd_soc_dapm_sync`` needs to be called after this for DAPM to do any widget power switching.
