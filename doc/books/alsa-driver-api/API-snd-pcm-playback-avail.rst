.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-playback-avail:

======================
snd_pcm_playback_avail
======================

*man snd_pcm_playback_avail(9)*

*4.6.0-rc5*

Get the available (writable) space for playback


Synopsis
========

.. c:function:: snd_pcm_uframes_t snd_pcm_playback_avail( struct snd_pcm_runtime * runtime )

Arguments
=========

``runtime``
    PCM runtime instance


Description
===========

Result is between 0 ... (boundary - 1)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
