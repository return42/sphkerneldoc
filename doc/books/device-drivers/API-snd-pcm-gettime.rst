.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-gettime:

===============
snd_pcm_gettime
===============

*man snd_pcm_gettime(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
