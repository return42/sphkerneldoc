
.. _API-snd-soc-dapm-info-pin-switch:

============================
snd_soc_dapm_info_pin_switch
============================

*man snd_soc_dapm_info_pin_switch(9)*

*4.6.0-rc1*

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
