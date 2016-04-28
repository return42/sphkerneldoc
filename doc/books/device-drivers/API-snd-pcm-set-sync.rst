.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-set-sync:

================
snd_pcm_set_sync
================

*man snd_pcm_set_sync(9)*

*4.6.0-rc5*

set the PCM sync id


Synopsis
========

.. c:function:: void snd_pcm_set_sync( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the pcm substream


Description
===========

Sets the PCM sync identifier for the card.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
