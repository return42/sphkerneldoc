
.. _API-samples-to-bytes:

================
samples_to_bytes
================

*man samples_to_bytes(9)*

*4.6.0-rc1*

Unit conversion of the size from samples to bytes


Synopsis
========

.. c:function:: ssize_t samples_to_bytes( struct snd_pcm_runtime * runtime, ssize_t size )

Arguments
=========

``runtime``
    PCM runtime instance

``size``
    size in samples
