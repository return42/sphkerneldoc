.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dai-set-sysclk:

======================
snd_soc_dai_set_sysclk
======================

*man snd_soc_dai_set_sysclk(9)*

*4.6.0-rc5*

configure DAI system or master clock.


Synopsis
========

.. c:function:: int snd_soc_dai_set_sysclk( struct snd_soc_dai * dai, int clk_id, unsigned int freq, int dir )

Arguments
=========

``dai``
    DAI

``clk_id``
    DAI specific clock ID

``freq``
    new clock frequency in Hz

``dir``
    new clock direction - input/output.


Description
===========

Configures the DAI master (MCLK) or system (SYSCLK) clocking.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
