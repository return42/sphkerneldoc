
.. _API-snd-soc-dapm-put-volsw:

======================
snd_soc_dapm_put_volsw
======================

*man snd_soc_dapm_put_volsw(9)*

*4.6.0-rc1*

dapm mixer set callback


Synopsis
========

.. c:function:: int snd_soc_dapm_put_volsw( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mixer control

``ucontrol``
    control element information


Description
===========

Callback to set the value of a dapm mixer control.

Returns 0 for success.
