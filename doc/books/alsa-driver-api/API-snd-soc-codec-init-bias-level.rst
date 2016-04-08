
.. _API-snd-soc-codec-init-bias-level:

=============================
snd_soc_codec_init_bias_level
=============================

*man snd_soc_codec_init_bias_level(9)*

*4.6.0-rc1*

Initialize CODEC DAPM bias level


Synopsis
========

.. c:function:: void snd_soc_codec_init_bias_level( struct snd_soc_codec * codec, enum snd_soc_bias_level level )

Arguments
=========

``codec``
    The CODEC for which to initialize the DAPM bias level

``level``
    The DAPM level to initialize to


Description
===========

Initializes the CODEC DAPM bias level. See ``snd_soc_dapm_init_bias_level``.
