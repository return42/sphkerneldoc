.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-put-volsw-sx:

====================
snd_soc_put_volsw_sx
====================

*man snd_soc_put_volsw_sx(9)*

*4.6.0-rc5*

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

Callback to set the value of a double mixer control that spans 2
registers.

Returns 0 for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
