.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-capture-ready:

=====================
snd_pcm_capture_ready
=====================

*man snd_pcm_capture_ready(9)*

*4.6.0-rc5*

check whether the capture buffer is available


Synopsis
========

.. c:function:: int snd_pcm_capture_ready( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the pcm substream instance


Description
===========

Checks whether enough capture data is available on the capture buffer.


Return
======

Non-zero if available, or zero if not.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
