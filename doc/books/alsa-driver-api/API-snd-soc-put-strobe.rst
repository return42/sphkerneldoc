.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-put-strobe:

==================
snd_soc_put_strobe
==================

*man snd_soc_put_strobe(9)*

*4.6.0-rc5*

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

Callback strobe a register bit to high then low (or the inverse) in one
pass of a single mixer enum control.

Returns 1 for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
