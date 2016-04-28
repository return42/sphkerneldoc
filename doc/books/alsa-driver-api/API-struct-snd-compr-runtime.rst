.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-compr-runtime:

========================
struct snd_compr_runtime
========================

*man struct snd_compr_runtime(9)*

*4.6.0-rc5*


Synopsis
========

.. code-block:: c

    struct snd_compr_runtime {
      snd_pcm_state_t state;
      struct snd_compr_ops * ops;
      void * buffer;
      u64 buffer_size;
      u32 fragment_size;
      u32 fragments;
      u64 total_bytes_available;
      u64 total_bytes_transferred;
      wait_queue_head_t sleep;
      void * private_data;
    };


Members
=======

state
    stream state

ops
    pointer to DSP callbacks

buffer
    pointer to kernel buffer, valid only when not in mmap mode or DSP
    doesn't implement copy

buffer_size
    size of the above buffer

fragment_size
    size of buffer fragment in bytes

fragments
    number of such fragments

total_bytes_available
    cumulative number of bytes made available in the ring buffer

total_bytes_transferred
    cumulative bytes transferred by offload DSP

sleep
    poll sleep

private_data
    driver private data pointer


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
