
.. _API-snd-soc-dapm-enable-pin:

=======================
snd_soc_dapm_enable_pin
=======================

*man snd_soc_dapm_enable_pin(9)*

*4.6.0-rc1*

enable pin.


Synopsis
========

.. c:function:: int snd_soc_dapm_enable_pin( struct snd_soc_dapm_context * dapm, const char * pin )

Arguments
=========

``dapm``
    DAPM context

``pin``
    pin name


Description
===========

Enables input/output pin and its parents or children widgets iff there is a valid audio route and active audio stream.


NOTE
====

``snd_soc_dapm_sync`` needs to be called after this for DAPM to do any widget power switching.
