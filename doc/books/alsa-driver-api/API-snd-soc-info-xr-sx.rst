
.. _API-snd-soc-info-xr-sx:

==================
snd_soc_info_xr_sx
==================

*man snd_soc_info_xr_sx(9)*

*4.6.0-rc1*

signed multi register info callback


Synopsis
========

.. c:function:: int snd_soc_info_xr_sx( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_info * uinfo )

Arguments
=========

``kcontrol``
    mreg control

``uinfo``
    control element information


Description
===========

Callback to provide information of a control that can span multiple codec registers which together forms a single signed value in a MSB/LSB manner.

Returns 0 for success.
