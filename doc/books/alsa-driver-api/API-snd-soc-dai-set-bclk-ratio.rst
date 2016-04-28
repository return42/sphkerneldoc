.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dai-set-bclk-ratio:

==========================
snd_soc_dai_set_bclk_ratio
==========================

*man snd_soc_dai_set_bclk_ratio(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
