
.. _API-snd-soc-codec-get-bias-level:

============================
snd_soc_codec_get_bias_level
============================

*man snd_soc_codec_get_bias_level(9)*

*4.6.0-rc1*

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
