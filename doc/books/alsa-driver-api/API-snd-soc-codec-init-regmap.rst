.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-codec-init-regmap:

=========================
snd_soc_codec_init_regmap
=========================

*man snd_soc_codec_init_regmap(9)*

*4.6.0-rc5*

Initialize regmap instance for the CODEC


Synopsis
========

.. c:function:: void snd_soc_codec_init_regmap( struct snd_soc_codec * codec, struct regmap * regmap )

Arguments
=========

``codec``
    The CODEC for which to initialize the regmap instance

``regmap``
    The regmap instance that should be used by the CODEC


Description
===========

This function allows deferred assignment of the regmap instance that is
associated with the CODEC. Only use this if the regmap instance is not
yet ready when the CODEC is registered. The function must also be called
before the first IO attempt of the CODEC.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
