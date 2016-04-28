.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dai-set-fmt:

===================
snd_soc_dai_set_fmt
===================

*man snd_soc_dai_set_fmt(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
