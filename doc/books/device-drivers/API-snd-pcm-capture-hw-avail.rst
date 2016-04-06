
.. _API-snd-pcm-capture-hw-avail:

========================
snd_pcm_capture_hw_avail
========================

*man snd_pcm_capture_hw_avail(9)*

*4.6.0-rc1*

Get the free space for capture


Synopsis
========

.. c:function:: snd_pcm_sframes_t snd_pcm_capture_hw_avail( struct snd_pcm_runtime * runtime )

Arguments
=========

``runtime``
    PCM runtime instance
