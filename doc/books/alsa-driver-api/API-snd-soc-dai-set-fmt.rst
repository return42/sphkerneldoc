
.. _API-snd-soc-dai-set-fmt:

===================
snd_soc_dai_set_fmt
===================

*man snd_soc_dai_set_fmt(9)*

*4.6.0-rc1*

configure DAI hardware audio format.


Synopsis
========

.. c:function:: int snd_soc_dai_set_fmt( struct snd_soc_dai * dai, unsigned int fmt )

Arguments
=========

``dai``
    DAI

``fmt``
    SND_SOC_DAIFMT_ format value.


Description
===========

Configures the DAI hardware format and clocking.
