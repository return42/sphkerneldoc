
.. _API-snd-pcm-gettime:

===============
snd_pcm_gettime
===============

*man snd_pcm_gettime(9)*

*4.6.0-rc1*

Fill the timespec depending on the timestamp mode


Synopsis
========

.. c:function:: void snd_pcm_gettime( struct snd_pcm_runtime * runtime, struct timespec * tv )

Arguments
=========

``runtime``
    PCM runtime instance

``tv``
    timespec to fill
