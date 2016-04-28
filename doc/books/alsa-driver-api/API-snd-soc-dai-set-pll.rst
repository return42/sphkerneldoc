.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dai-set-pll:

===================
snd_soc_dai_set_pll
===================

*man snd_soc_dai_set_pll(9)*

*4.6.0-rc5*

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

Configures and enables PLL to generate output clock based on input
clock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
