.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-register-codec:

======================
snd_soc_register_codec
======================

*man snd_soc_register_codec(9)*

*4.6.0-rc5*

Register a codec with the ASoC core


Synopsis
========

.. c:function:: int snd_soc_register_codec( struct device * dev, const struct snd_soc_codec_driver * codec_drv, struct snd_soc_dai_driver * dai_drv, int num_dai )

Arguments
=========

``dev``
    The parent device for this codec

``codec_drv``
    Codec driver

``dai_drv``
    The associated DAI driver

``num_dai``
    Number of DAIs


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
