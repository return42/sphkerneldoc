
.. _API-struct-snd-compr-tstamp:

=======================
struct snd_compr_tstamp
=======================

*man struct snd_compr_tstamp(9)*

*4.6.0-rc1*

timestamp descriptor


Synopsis
========

.. code-block:: c

    struct snd_compr_tstamp {
      __u32 byte_offset;
      __u32 copied_total;
      __u32 pcm_frames;
      __u32 pcm_io_frames;
      __u32 sampling_rate;
    };


Members
=======

byte_offset
    Byte offset in ring buffer to DSP

copied_total
    Total number of bytes copied from/to ring buffer to/by DSP

pcm_frames
    Frames decoded or encoded by DSP. This field will evolve by large steps and should only be used to monitor encoding/decoding progress. It shall not be used for timing
    estimates.

pcm_io_frames
    Frames rendered or received by DSP into a mixer or an audio output/input. This field should be used for A/V sync or time estimates.

sampling_rate
    sampling rate of audio
