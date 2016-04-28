.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-runtime-set-dai-fmt:

===========================
snd_soc_runtime_set_dai_fmt
===========================

*man snd_soc_runtime_set_dai_fmt(9)*

*4.6.0-rc5*

Change DAI link format for a ASoC runtime


Synopsis
========

.. c:function:: int snd_soc_runtime_set_dai_fmt( struct snd_soc_pcm_runtime * rtd, unsigned int dai_fmt )

Arguments
=========

``rtd``
    The runtime for which the DAI link format should be changed

``dai_fmt``
    The new DAI link format


Description
===========

This function updates the DAI link format for all DAIs connected to the
DAI link for the specified runtime.


Note
====

For setups with a static format set the dai_fmt field in the
corresponding snd_dai_link struct instead of using this function.

Returns 0 on success, otherwise a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
