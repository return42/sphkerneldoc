
.. _API-snd-soc-put-strobe:

==================
snd_soc_put_strobe
==================

*man snd_soc_put_strobe(9)*

*4.6.0-rc1*

strobe put callback


Synopsis
========

.. c:function:: int snd_soc_put_strobe( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mixer control

``ucontrol``
    control element information


Description
===========

Callback strobe a register bit to high then low (or the inverse) in one pass of a single mixer enum control.

Returns 1 for success.
