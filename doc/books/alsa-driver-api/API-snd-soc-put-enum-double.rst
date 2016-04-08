
.. _API-snd-soc-put-enum-double:

=======================
snd_soc_put_enum_double
=======================

*man snd_soc_put_enum_double(9)*

*4.6.0-rc1*

enumerated double mixer put callback


Synopsis
========

.. c:function:: int snd_soc_put_enum_double( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mixer control

``ucontrol``
    control element information


Description
===========

Callback to set the value of a double enumerated mixer.

Returns 0 for success.
