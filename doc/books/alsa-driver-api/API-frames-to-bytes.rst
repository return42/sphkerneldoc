
.. _API-frames-to-bytes:

===============
frames_to_bytes
===============

*man frames_to_bytes(9)*

*4.6.0-rc1*

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
