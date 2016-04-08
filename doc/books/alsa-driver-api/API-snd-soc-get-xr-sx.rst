
.. _API-snd-soc-get-xr-sx:

=================
snd_soc_get_xr_sx
=================

*man snd_soc_get_xr_sx(9)*

*4.6.0-rc1*

signed multi register get callback


Synopsis
========

.. c:function:: int snd_soc_get_xr_sx( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mreg control

``ucontrol``
    control element information


Description
===========

Callback to get the value of a control that can span multiple codec registers which together forms a single signed value in a MSB/LSB manner. The control supports specifying total
no of bits used to allow for bitfields across the multiple codec registers.

Returns 0 for success.
