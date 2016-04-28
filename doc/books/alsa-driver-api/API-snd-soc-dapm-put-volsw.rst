.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-put-volsw:

======================
snd_soc_dapm_put_volsw
======================

*man snd_soc_dapm_put_volsw(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
