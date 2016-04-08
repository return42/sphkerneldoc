
.. _API-snd-pcm-capture-avail:

=====================
snd_pcm_capture_avail
=====================

*man snd_pcm_capture_avail(9)*

*4.6.0-rc1*

Get the available (readable) space for capture


Synopsis
========

.. c:function:: snd_pcm_uframes_t snd_pcm_capture_avail( struct snd_pcm_runtime * runtime )

Arguments
=========

``runtime``
    PCM runtime instance


Description
===========

Result is between 0 ... (boundary - 1)
