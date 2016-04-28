.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-disable-pin:

========================
snd_soc_dapm_disable_pin
========================

*man snd_soc_dapm_disable_pin(9)*

*4.6.0-rc5*

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

``snd_soc_dapm_sync`` needs to be called after this for DAPM to do any
widget power switching.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
