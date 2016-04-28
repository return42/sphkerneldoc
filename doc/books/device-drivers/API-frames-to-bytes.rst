.. -*- coding: utf-8; mode: rst -*-

.. _API-frames-to-bytes:

===============
frames_to_bytes
===============

*man frames_to_bytes(9)*

*4.6.0-rc5*

Unit conversion of the size from frames to bytes


Synopsis
========

.. c:function:: ssize_t frames_to_bytes( struct snd_pcm_runtime * runtime, snd_pcm_sframes_t size )

Arguments
=========

``runtime``
    PCM runtime instance

``size``
    size in frames


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
