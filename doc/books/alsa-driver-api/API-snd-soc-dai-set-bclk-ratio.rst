
.. _API-snd-soc-dai-set-bclk-ratio:

==========================
snd_soc_dai_set_bclk_ratio
==========================

*man snd_soc_dai_set_bclk_ratio(9)*

*4.6.0-rc1*

configure BCLK to sample rate ratio.


Synopsis
========

.. c:function:: int snd_soc_dai_set_bclk_ratio( struct snd_soc_dai * dai, unsigned int ratio )

Arguments
=========

``dai``
    DAI

``ratio``
    Ratio of BCLK to Sample rate.


Description
===========

Configures the DAI for a preset BCLK to sample rate ratio.
