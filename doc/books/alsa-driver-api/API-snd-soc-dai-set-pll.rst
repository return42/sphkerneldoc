
.. _API-snd-soc-dai-set-pll:

===================
snd_soc_dai_set_pll
===================

*man snd_soc_dai_set_pll(9)*

*4.6.0-rc1*

configure DAI PLL.


Synopsis
========

.. c:function:: int snd_soc_dai_set_pll( struct snd_soc_dai * dai, int pll_id, int source, unsigned int freq_in, unsigned int freq_out )

Arguments
=========

``dai``
    DAI

``pll_id``
    DAI specific PLL ID

``source``
    DAI specific source for the PLL

``freq_in``
    PLL input clock frequency in Hz

``freq_out``
    requested PLL output clock frequency in Hz


Description
===========

Configures and enables PLL to generate output clock based on input clock.
