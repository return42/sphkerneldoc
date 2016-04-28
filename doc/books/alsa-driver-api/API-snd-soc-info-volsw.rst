.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-info-volsw:

==================
snd_soc_info_volsw
==================

*man snd_soc_info_volsw(9)*

*4.6.0-rc5*

single mixer info callback


Synopsis
========

.. c:function:: int snd_soc_info_volsw( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_info * uinfo )

Arguments
=========

``kcontrol``
    mixer control

``uinfo``
    control element information


Description
===========

Callback to provide information about a single mixer control, or a
double mixer control that spans 2 registers.

Returns 0 for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
