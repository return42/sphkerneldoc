
.. _API-snd-soc-dapm-get-enum-double:

============================
snd_soc_dapm_get_enum_double
============================

*man snd_soc_dapm_get_enum_double(9)*

*4.6.0-rc1*

dapm enumerated double mixer get callback


Synopsis
========

.. c:function:: int snd_soc_dapm_get_enum_double( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mixer control

``ucontrol``
    control element information


Description
===========

Callback to get the value of a dapm enumerated double mixer control.

Returns 0 for success.
