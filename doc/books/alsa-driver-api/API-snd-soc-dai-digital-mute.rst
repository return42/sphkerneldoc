
.. _API-snd-soc-dai-digital-mute:

========================
snd_soc_dai_digital_mute
========================

*man snd_soc_dai_digital_mute(9)*

*4.6.0-rc1*

configure DAI system or master clock.


Synopsis
========

.. c:function:: int snd_soc_dai_digital_mute( struct snd_soc_dai * dai, int mute, int direction )

Arguments
=========

``dai``
    DAI

``mute``
    mute enable

``direction``
    stream to mute


Description
===========

Mutes the DAI DAC.
