.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-codec-force-bias-level:

==============================
snd_soc_codec_force_bias_level
==============================

*man snd_soc_codec_force_bias_level(9)*

*4.6.0-rc5*

Set the CODEC DAPM bias level


Synopsis
========

.. c:function:: int snd_soc_codec_force_bias_level( struct snd_soc_codec * codec, enum snd_soc_bias_level level )

Arguments
=========

``codec``
    The CODEC for which to set the level

``level``
    The level to set to


Description
===========

Forces the CODEC bias level to a specific state. See
``snd_soc_dapm_force_bias_level``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
