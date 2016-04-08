
.. _API-snd-soc-dapm-to-platform:

========================
snd_soc_dapm_to_platform
========================

*man snd_soc_dapm_to_platform(9)*

*4.6.0-rc1*

Casts a DAPM context to the platform it is embedded in


Synopsis
========

.. c:function:: struct snd_soc_platform ⋆ snd_soc_dapm_to_platform( struct snd_soc_dapm_context * dapm )

Arguments
=========

``dapm``
    The DAPM context to cast to the platform.


Description
===========

This function must only be used on DAPM contexts that are known to be part of a platform (e.g. in a platform driver). Otherwise the behavior is undefined.
