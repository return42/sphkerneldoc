.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-info-volsw-sx:

=====================
snd_soc_info_volsw_sx
=====================

*man snd_soc_info_volsw_sx(9)*

*4.6.0-rc5*

Mixer info callback for SX TLV controls


Synopsis
========

.. c:function:: int snd_soc_info_volsw_sx( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_info * uinfo )

Arguments
=========

``kcontrol``
    mixer control

``uinfo``
    control element information


Description
===========

Callback to provide information about a single mixer control, or a
double mixer control that spans 2 registers of the SX TLV type. SX TLV
controls have a range that represents both positive and negative values
either side of zero but without a sign bit.

Returns 0 for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
