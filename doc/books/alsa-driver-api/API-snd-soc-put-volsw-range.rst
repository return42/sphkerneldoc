
.. _API-snd-soc-put-volsw-range:

=======================
snd_soc_put_volsw_range
=======================

*man snd_soc_put_volsw_range(9)*

*4.6.0-rc1*

single mixer put value callback with range.


Synopsis
========

.. c:function:: int snd_soc_put_volsw_range( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mixer control

``ucontrol``
    control element information


Description
===========

Callback to set the value, within a range, for a single mixer control.

Returns 0 for success.
