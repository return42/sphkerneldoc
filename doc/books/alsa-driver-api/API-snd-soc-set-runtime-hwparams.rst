
.. _API-snd-soc-set-runtime-hwparams:

============================
snd_soc_set_runtime_hwparams
============================

*man snd_soc_set_runtime_hwparams(9)*

*4.6.0-rc1*

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
