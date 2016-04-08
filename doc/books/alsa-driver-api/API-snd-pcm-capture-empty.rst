
.. _API-snd-pcm-capture-empty:

=====================
snd_pcm_capture_empty
=====================

*man snd_pcm_capture_empty(9)*

*4.6.0-rc1*

check whether the capture buffer is empty


Synopsis
========

.. c:function:: int snd_pcm_capture_empty( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the pcm substream instance


Description
===========

Checks whether the capture buffer is empty.


Return
======

Non-zero if empty, or zero if not.
