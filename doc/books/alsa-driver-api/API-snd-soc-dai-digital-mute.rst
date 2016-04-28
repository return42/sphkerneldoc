.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dai-digital-mute:

========================
snd_soc_dai_digital_mute
========================

*man snd_soc_dai_digital_mute(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
