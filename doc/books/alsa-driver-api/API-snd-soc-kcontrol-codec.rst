.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-kcontrol-codec:

======================
snd_soc_kcontrol_codec
======================

*man snd_soc_kcontrol_codec(9)*

*4.6.0-rc5*

Returns the CODEC that registered the control


Synopsis
========

.. c:function:: struct snd_soc_codec * snd_soc_kcontrol_codec( struct snd_kcontrol * kcontrol )

Arguments
=========

``kcontrol``
    The control for which to get the CODEC


Note
====

This function will only work correctly if the control has been
registered with ``snd_soc_add_codec_controls`` or via table based setup
of snd_soc_codec_driver. Otherwise the behavior is undefined.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
