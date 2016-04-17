.. -*- coding: utf-8; mode: rst -*-

=================
compress_driver.h
=================


.. _`snd_compr_runtime`:

struct snd_compr_runtime
========================

.. c:type:: snd_compr_runtime

    


.. _`snd_compr_runtime.definition`:

Definition
----------

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


.. _`snd_compr_runtime.members`:

Members
-------

:``state``:
    stream state

:``ops``:
    pointer to DSP callbacks

:``buffer``:
    pointer to kernel buffer, valid only when not in mmap mode or
    DSP doesn't implement copy

:``buffer_size``:
    size of the above buffer

:``fragment_size``:
    size of buffer fragment in bytes

:``fragments``:
    number of such fragments

:``total_bytes_available``:
    cumulative number of bytes made available in
    the ring buffer

:``total_bytes_transferred``:
    cumulative bytes transferred by offload DSP

:``sleep``:
    poll sleep

:``private_data``:
    driver private data pointer




.. _`snd_compr_stream`:

struct snd_compr_stream
=======================

.. c:type:: snd_compr_stream

    


.. _`snd_compr_stream.definition`:

Definition
----------

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


.. _`snd_compr_stream.members`:

Members
-------

:``name``:
    device name

:``ops``:
    pointer to DSP callbacks

:``runtime``:
    pointer to runtime structure

:``device``:
    device pointer

:``direction``:
    stream direction, playback/recording

:``metadata_set``:
    metadata set flag, true when set

:``next_track``:
    has userspace signal next track transition, true when set

:``private_data``:
    pointer to DSP private data




.. _`snd_compr_ops`:

struct snd_compr_ops
====================

.. c:type:: snd_compr_ops

    


.. _`snd_compr_ops.definition`:

Definition
----------

.. code-block:: c

  struct snd_compr_ops {
    int (* open) (struct snd_compr_stream *stream);
    int (* free) (struct snd_compr_stream *stream);
    int (* set_params) (struct snd_compr_stream *stream,struct snd_compr_params *params);
    int (* get_params) (struct snd_compr_stream *stream,struct snd_codec *params);
    int (* set_metadata) (struct snd_compr_stream *stream,struct snd_compr_metadata *metadata);
    int (* get_metadata) (struct snd_compr_stream *stream,struct snd_compr_metadata *metadata);
    int (* trigger) (struct snd_compr_stream *stream, int cmd);
    int (* pointer) (struct snd_compr_stream *stream,struct snd_compr_tstamp *tstamp);
    int (* copy) (struct snd_compr_stream *stream, char __user *buf,size_t count);
    int (* mmap) (struct snd_compr_stream *stream,struct vm_area_struct *vma);
    int (* ack) (struct snd_compr_stream *stream, size_t bytes);
    int (* get_caps) (struct snd_compr_stream *stream,struct snd_compr_caps *caps);
    int (* get_codec_caps) (struct snd_compr_stream *stream,struct snd_compr_codec_caps *codec);
  };


.. _`snd_compr_ops.members`:

Members
-------

:``open``:
    Open the compressed stream
    This callback is mandatory and shall keep dsp ready to receive the stream
    parameter

:``free``:
    Close the compressed stream, mandatory

:``set_params``:
    Sets the compressed stream parameters, mandatory
    This can be called in during stream creation only to set codec params
    and the stream properties

:``get_params``:
    retrieve the codec parameters, mandatory

:``set_metadata``:
    Set the metadata values for a stream

:``get_metadata``:
    retrieves the requested metadata values from stream

:``trigger``:
    Trigger operations like start, pause, resume, drain, stop.
    This callback is mandatory

:``pointer``:
    Retrieve current h/w pointer information. Mandatory

:``copy``:
    Copy the compressed data to/from userspace, Optional
    Can't be implemented if DSP supports mmap

:``mmap``:
    DSP mmap method to mmap DSP memory

:``ack``:
    Ack for DSP when data is written to audio buffer, Optional
    Not valid if copy is implemented

:``get_caps``:
    Retrieve DSP capabilities, mandatory

:``get_codec_caps``:
    Retrieve capabilities for a specific codec, mandatory




.. _`snd_compr`:

struct snd_compr
================

.. c:type:: snd_compr

    


.. _`snd_compr.definition`:

Definition
----------

.. code-block:: c

  struct snd_compr {
    const char * name;
    struct device dev;
    struct snd_compr_ops * ops;
    void * private_data;
    struct snd_card * card;
    unsigned int direction;
    struct mutex lock;
    int device;
    #ifdef CONFIG_SND_VERBOSE_PROCFS
    #endif
  };


.. _`snd_compr.members`:

Members
-------

:``name``:
    DSP device name

:``dev``:
    associated device instance

:``ops``:
    pointer to DSP callbacks

:``private_data``:
    pointer to DSP pvt data

:``card``:
    sound card pointer

:``direction``:
    Playback or capture direction

:``lock``:
    device lock

:``device``:
    device id


