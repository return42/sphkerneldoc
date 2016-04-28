.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-info-pin-switch:

============================
snd_soc_dapm_info_pin_switch
============================

*man snd_soc_dapm_info_pin_switch(9)*

*4.6.0-rc5*

Info for a pin switch


Synopsis
========

.. c:function:: int snd_soc_dapm_info_pin_switch( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_info * uinfo )

Arguments
=========

``kcontrol``
    mixer control

``uinfo``
    control element information


Description
===========

Callback to provide information about a pin switch control.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
