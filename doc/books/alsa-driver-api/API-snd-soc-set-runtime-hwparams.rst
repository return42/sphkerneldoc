.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-set-runtime-hwparams:

============================
snd_soc_set_runtime_hwparams
============================

*man snd_soc_set_runtime_hwparams(9)*

*4.6.0-rc5*

set the runtime hardware parameters


Synopsis
========

.. c:function:: int snd_soc_set_runtime_hwparams( struct snd_pcm_substream * substream, const struct snd_pcm_hardware * hw )

Arguments
=========

``substream``
    the pcm substream

``hw``
    the hardware parameters


Description
===========

Sets the substream runtime hardware parameters.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
