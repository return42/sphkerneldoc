.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-kcontrol-dapm:

==========================
snd_soc_dapm_kcontrol_dapm
==========================

*man snd_soc_dapm_kcontrol_dapm(9)*

*4.6.0-rc5*

Returns the dapm context associated to a kcontrol


Synopsis
========

.. c:function:: struct snd_soc_dapm_context * snd_soc_dapm_kcontrol_dapm( struct snd_kcontrol * kcontrol )

Arguments
=========

``kcontrol``
    The kcontrol


Note
====

This function must only be used on kcontrols that are known to have been
registered for a CODEC. Otherwise the behaviour is undefined.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
