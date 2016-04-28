.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dai-set-tristate:

========================
snd_soc_dai_set_tristate
========================

*man snd_soc_dai_set_tristate(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
