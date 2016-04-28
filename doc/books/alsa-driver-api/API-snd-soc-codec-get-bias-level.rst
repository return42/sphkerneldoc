.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-codec-get-bias-level:

============================
snd_soc_codec_get_bias_level
============================

*man snd_soc_codec_get_bias_level(9)*

*4.6.0-rc5*

Get current CODEC DAPM bias level


Synopsis
========

.. c:function:: enum snd_soc_bias_level snd_soc_codec_get_bias_level( struct snd_soc_codec * codec )

Arguments
=========

``codec``
    The CODEC for which to get the DAPM bias level


Returns
=======

The current DAPM bias level of the CODEC.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
