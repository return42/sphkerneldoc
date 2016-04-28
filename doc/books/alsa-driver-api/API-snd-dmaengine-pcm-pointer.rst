.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-dmaengine-pcm-pointer:

=========================
snd_dmaengine_pcm_pointer
=========================

*man snd_dmaengine_pcm_pointer(9)*

*4.6.0-rc5*

dmaengine based PCM pointer implementation


Synopsis
========

.. c:function:: snd_pcm_uframes_t snd_dmaengine_pcm_pointer( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    PCM substream


Description
===========

This function can be used as the PCM pointer callback for dmaengine
based PCM driver implementations.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
