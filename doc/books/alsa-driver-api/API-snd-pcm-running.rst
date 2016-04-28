.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-running:

===============
snd_pcm_running
===============

*man snd_pcm_running(9)*

*4.6.0-rc5*

Check whether the substream is in a running state


Synopsis
========

.. c:function:: int snd_pcm_running( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    substream to check


Description
===========

Returns true if the given substream is in the state RUNNING, or in the
state DRAINING for playback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
