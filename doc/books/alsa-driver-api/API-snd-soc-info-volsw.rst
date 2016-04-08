
.. _API-snd-soc-info-volsw:

==================
snd_soc_info_volsw
==================

*man snd_soc_info_volsw(9)*

*4.6.0-rc1*

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

Callback to provide information about a single mixer control, or a double mixer control that spans 2 registers.

Returns 0 for success.
