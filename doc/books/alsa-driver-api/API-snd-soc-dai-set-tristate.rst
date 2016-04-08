
.. _API-snd-soc-dai-set-tristate:

========================
snd_soc_dai_set_tristate
========================

*man snd_soc_dai_set_tristate(9)*

*4.6.0-rc1*

configure DAI system or master clock.


Synopsis
========

.. c:function:: int snd_soc_dai_set_tristate( struct snd_soc_dai * dai, int tristate )

Arguments
=========

``dai``
    DAI

``tristate``
    tristate enable


Description
===========

Tristates the DAI so that others can use it.
