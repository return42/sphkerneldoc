
.. _API-snd-soc-kcontrol-codec:

======================
snd_soc_kcontrol_codec
======================

*man snd_soc_kcontrol_codec(9)*

*4.6.0-rc1*

Returns the CODEC that registered the control


Synopsis
========

.. c:function:: struct snd_soc_codec ⋆ snd_soc_kcontrol_codec( struct snd_kcontrol * kcontrol )

Arguments
=========

``kcontrol``
    The control for which to get the CODEC


Note
====

This function will only work correctly if the control has been registered with ``snd_soc_add_codec_controls`` or via table based setup of snd_soc_codec_driver. Otherwise the
behavior is undefined.
