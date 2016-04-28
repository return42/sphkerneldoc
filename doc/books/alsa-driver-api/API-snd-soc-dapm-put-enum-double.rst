.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-put-enum-double:

============================
snd_soc_dapm_put_enum_double
============================

*man snd_soc_dapm_put_enum_double(9)*

*4.6.0-rc5*

dapm enumerated double mixer set callback


Synopsis
========

.. c:function:: int snd_soc_dapm_put_enum_double( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_value * ucontrol )

Arguments
=========

``kcontrol``
    mixer control

``ucontrol``
    control element information


Description
===========

Callback to set the value of a dapm enumerated double mixer control.

Returns 0 for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
