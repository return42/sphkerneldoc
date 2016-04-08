
.. _API-snd-soc-codec-set-sysclk:

========================
snd_soc_codec_set_sysclk
========================

*man snd_soc_codec_set_sysclk(9)*

*4.6.0-rc1*

configure CODEC system or master clock.


Synopsis
========

.. c:function:: int snd_soc_codec_set_sysclk( struct snd_soc_codec * codec, int clk_id, int source, unsigned int freq, int dir )

Arguments
=========

``codec``
    CODEC

``clk_id``
    DAI specific clock ID

``source``
    Source for the clock

``freq``
    new clock frequency in Hz

``dir``
    new clock direction - input/output.


Description
===========

Configures the CODEC master (MCLK) or system (SYSCLK) clocking.
