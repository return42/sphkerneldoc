
.. _API-snd-soc-dai-set-sysclk:

======================
snd_soc_dai_set_sysclk
======================

*man snd_soc_dai_set_sysclk(9)*

*4.6.0-rc1*

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
