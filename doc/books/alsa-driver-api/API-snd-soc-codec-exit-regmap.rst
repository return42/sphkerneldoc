
.. _API-snd-soc-codec-exit-regmap:

=========================
snd_soc_codec_exit_regmap
=========================

*man snd_soc_codec_exit_regmap(9)*

*4.6.0-rc1*

De-initialize regmap instance for the CODEC


Synopsis
========

.. c:function:: void snd_soc_codec_exit_regmap( struct snd_soc_codec * codec )

Arguments
=========

``codec``
    The CODEC for which to de-initialize the regmap instance


Description
===========

Calls ``regmap_exit`` on the regmap instance associated to the CODEC and removes the regmap instance from the CODEC.

This function should only be used if ``snd_soc_codec_init_regmap`` was used to initialize the regmap instance.
