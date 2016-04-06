
.. _API-frame-aligned:

=============
frame_aligned
=============

*man frame_aligned(9)*

*4.6.0-rc1*

Check whether the byte size is aligned to frames


Synopsis
========

.. c:function:: int frame_aligned( struct snd_pcm_runtime * runtime, ssize_t bytes )

Arguments
=========

``runtime``
    PCM runtime instance

``bytes``
    size in bytes
