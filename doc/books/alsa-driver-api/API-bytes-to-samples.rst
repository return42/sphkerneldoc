
.. _API-bytes-to-samples:

================
bytes_to_samples
================

*man bytes_to_samples(9)*

*4.6.0-rc1*

Unit conversion of the size from bytes to samples


Synopsis
========

.. c:function:: ssize_t bytes_to_samples( struct snd_pcm_runtime * runtime, ssize_t size )

Arguments
=========

``runtime``
    PCM runtime instance

``size``
    size in bytes
