.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-codec-get-dapm:

======================
snd_soc_codec_get_dapm
======================

*man snd_soc_codec_get_dapm(9)*

*4.6.0-rc5*

Returns the DAPM context for the CODEC


Synopsis
========

.. c:function:: struct snd_soc_dapm_context * snd_soc_codec_get_dapm( struct snd_soc_codec * codec )

Arguments
=========

``codec``
    The CODEC for which to get the DAPM context


Note
====

Use this function instead of directly accessing the CODEC's dapm field


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
