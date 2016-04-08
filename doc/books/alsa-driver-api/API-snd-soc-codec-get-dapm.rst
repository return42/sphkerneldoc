
.. _API-snd-soc-codec-get-dapm:

======================
snd_soc_codec_get_dapm
======================

*man snd_soc_codec_get_dapm(9)*

*4.6.0-rc1*

Returns the DAPM context for the CODEC


Synopsis
========

.. c:function:: struct snd_soc_dapm_context ⋆ snd_soc_codec_get_dapm( struct snd_soc_codec * codec )

Arguments
=========

``codec``
    The CODEC for which to get the DAPM context


Note
====

Use this function instead of directly accessing the CODEC's dapm field
