
.. _API-snd-soc-put-volsw-sx:

====================
snd_soc_put_volsw_sx
====================

*man snd_soc_put_volsw_sx(9)*

*4.6.0-rc1*

double mixer set callback


Synopsis
========

.. c:function:: int snd_soc_put_volsw_sx( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mixer control

``ucontrol``
    control element information


Description
===========

Callback to set the value of a double mixer control that spans 2 registers.

Returns 0 for success.
