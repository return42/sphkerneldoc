.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-compr-stream:

=======================
struct snd_compr_stream
=======================

*man struct snd_compr_stream(9)*

*4.6.0-rc5*


Synopsis
========

.. code-block:: c

    struct snd_compr_stream {
      const char * name;
      struct snd_compr_ops * ops;
      struct snd_compr_runtime * runtime;
      struct snd_compr * device;
      enum snd_compr_direction direction;
      bool metadata_set;
      bool next_track;
      void * private_data;
    };


Members
=======

name
    device name

ops
    pointer to DSP callbacks

runtime
    pointer to runtime structure

device
    device pointer

direction
    stream direction, playback/recording

metadata_set
    metadata set flag, true when set

next_track
    has userspace signal next track transition, true when set

private_data
    pointer to DSP private data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
