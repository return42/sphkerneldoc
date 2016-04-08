
.. _API-struct-snd-compr-ops:

====================
struct snd_compr_ops
====================

*man struct snd_compr_ops(9)*

*4.6.0-rc1*


Synopsis
========

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


Members
=======

open
    Open the compressed stream This callback is mandatory and shall keep dsp ready to receive the stream parameter

free
    Close the compressed stream, mandatory

set_params
    Sets the compressed stream parameters, mandatory This can be called in during stream creation only to set codec params and the stream properties

get_params
    retrieve the codec parameters, mandatory

set_metadata
    Set the metadata values for a stream

get_metadata
    retrieves the requested metadata values from stream

trigger
    Trigger operations like start, pause, resume, drain, stop. This callback is mandatory

pointer
    Retrieve current h/w pointer information. Mandatory

copy
    Copy the compressed data to/from userspace, Optional Can't be implemented if DSP supports mmap

mmap
    DSP mmap method to mmap DSP memory

ack
    Ack for DSP when data is written to audio buffer, Optional Not valid if copy is implemented

get_caps
    Retrieve DSP capabilities, mandatory

get_codec_caps
    Retrieve capabilities for a specific codec, mandatory
