.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-get-strobe:

==================
snd_soc_get_strobe
==================

*man snd_soc_get_strobe(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
