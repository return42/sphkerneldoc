
.. _API-snd-soc-get-volsw:

=================
snd_soc_get_volsw
=================

*man snd_soc_get_volsw(9)*

*4.6.0-rc1*

single mixer get callback


Synopsis
========

.. c:function:: int snd_soc_get_volsw( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mixer control

``ucontrol``
    control element information


Description
===========

Callback to get the value of a single mixer control, or a double mixer control that spans 2 registers.

Returns 0 for success.
