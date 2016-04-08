
.. _API-snd-soc-dapm-disable-pin-unlocked:

=================================
snd_soc_dapm_disable_pin_unlocked
=================================

*man snd_soc_dapm_disable_pin_unlocked(9)*

*4.6.0-rc1*

disable pin.


Synopsis
========

.. c:function:: int snd_soc_dapm_disable_pin_unlocked( struct snd_soc_dapm_context * dapm, const char * pin )

Arguments
=========

``dapm``
    DAPM context

``pin``
    pin name


Description
===========

Disables input/output pin and its parents or children widgets.

Requires external locking.


NOTE
====

``snd_soc_dapm_sync`` needs to be called after this for DAPM to do any widget power switching.
