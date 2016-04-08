
.. _API-snd-soc-dapm-to-codec:

=====================
snd_soc_dapm_to_codec
=====================

*man snd_soc_dapm_to_codec(9)*

*4.6.0-rc1*

Casts a DAPM context to the CODEC it is embedded in


Synopsis
========

.. c:function:: struct snd_soc_codec ⋆ snd_soc_dapm_to_codec( struct snd_soc_dapm_context * dapm )

Arguments
=========

``dapm``
    The DAPM context to cast to the CODEC


Description
===========

This function must only be used on DAPM contexts that are known to be part of a CODEC (e.g. in a CODEC driver). Otherwise the behavior is undefined.
