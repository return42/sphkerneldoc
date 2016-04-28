.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-kcontrol-codec:

===========================
snd_soc_dapm_kcontrol_codec
===========================

*man snd_soc_dapm_kcontrol_codec(9)*

*4.6.0-rc5*

Returns the codec associated to a kcontrol


Synopsis
========

.. c:function:: struct snd_soc_codec * snd_soc_dapm_kcontrol_codec( struct snd_kcontrol * kcontrol )

Arguments
=========

``kcontrol``
    The kcontrol


Description
===========

This function must only be used on DAPM contexts that are known to be
part of a CODEC (e.g. in a CODEC driver). Otherwise the behavior is
undefined.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
