
.. _API-struct-snd-compressed-buffer:

============================
struct snd_compressed_buffer
============================

*man struct snd_compressed_buffer(9)*

*4.6.0-rc1*

compressed buffer


Synopsis
========

.. code-block:: c

    struct snd_compressed_buffer {
      __u32 fragment_size;
      __u32 fragments;
    };


Members
=======

fragment_size
    size of buffer fragment in bytes

fragments
    number of such fragments
