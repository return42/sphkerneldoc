
.. _API-snd-soc-get-strobe:

==================
snd_soc_get_strobe
==================

*man snd_soc_get_strobe(9)*

*4.6.0-rc1*

strobe get callback


Synopsis
========

.. c:function:: int snd_soc_get_strobe( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mixer control

``ucontrol``
    control element information


Description
===========

Callback get the value of a strobe mixer control.

Returns 0 for success.
