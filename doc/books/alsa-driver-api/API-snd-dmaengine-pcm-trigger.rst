.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dmaengine-pcm-trigger:

=========================
snd_dmaengine_pcm_trigger
=========================

*man snd_dmaengine_pcm_trigger(9)*

*4.6.0-rc5*

dmaengine based PCM trigger implementation


Synopsis
========

.. c:function:: int snd_dmaengine_pcm_trigger( struct snd_pcm_substream * substream, int cmd )

Arguments
=========

``substream``
    PCM substream

``cmd``
    Trigger command


Description
===========

Returns 0 on success, a negative error code otherwise.

This function can be used as the PCM trigger callback for dmaengine
based PCM driver implementations.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
