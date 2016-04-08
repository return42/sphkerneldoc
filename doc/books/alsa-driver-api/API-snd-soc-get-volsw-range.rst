
.. _API-snd-soc-get-volsw-range:

=======================
snd_soc_get_volsw_range
=======================

*man snd_soc_get_volsw_range(9)*

*4.6.0-rc1*

single mixer get callback with range


Synopsis
========

.. c:function:: int snd_soc_get_volsw_range( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mixer control

``ucontrol``
    control element information


Description
===========

Callback to get the value, within a range, of a single mixer control.

Returns 0 for success.
