
.. _API-bytes-to-frames:

===============
bytes_to_frames
===============

*man bytes_to_frames(9)*

*4.6.0-rc1*

Unit conversion of the size from bytes to frames


Synopsis
========

.. c:function:: snd_pcm_sframes_t bytes_to_frames( struct snd_pcm_runtime * runtime, ssize_t size )

Arguments
=========

``runtime``
    PCM runtime instance

``size``
    size in bytes
