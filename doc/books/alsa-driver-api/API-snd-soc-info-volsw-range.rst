.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-info-volsw-range:

========================
snd_soc_info_volsw_range
========================

*man snd_soc_info_volsw_range(9)*

*4.6.0-rc5*

single mixer info callback with range.


Synopsis
========

.. c:function:: int snd_soc_info_volsw_range( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_info * uinfo )

Arguments
=========

``kcontrol``
    mixer control

``uinfo``
    control element information


Description
===========

Callback to provide information, within a range, about a single mixer
control.

returns 0 for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
