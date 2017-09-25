.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/sound/compress_offload.h

.. _`snd_compressed_buffer`:

struct snd_compressed_buffer
============================

.. c:type:: struct snd_compressed_buffer

    compressed buffer

.. _`snd_compressed_buffer.definition`:

Definition
----------

.. code-block:: c

    struct snd_compressed_buffer {
        __u32 fragment_size;
        __u32 fragments;
    }

.. _`snd_compressed_buffer.members`:

Members
-------

fragment_size
    size of buffer fragment in bytes

fragments
    number of such fragments

.. _`snd_compr_params`:

struct snd_compr_params
=======================

.. c:type:: struct snd_compr_params

    compressed stream params

.. _`snd_compr_params.definition`:

Definition
----------

.. code-block:: c

    struct snd_compr_params {
        struct snd_compressed_buffer buffer;
        struct snd_codec codec;
        __u8 no_wake_mode;
    }

.. _`snd_compr_params.members`:

Members
-------

buffer
    buffer description

codec
    codec parameters

no_wake_mode
    dont wake on fragment elapsed

.. _`snd_compr_tstamp`:

struct snd_compr_tstamp
=======================

.. c:type:: struct snd_compr_tstamp

    timestamp descriptor

.. _`snd_compr_tstamp.definition`:

Definition
----------

.. code-block:: c

    struct snd_compr_tstamp {
        __u32 byte_offset;
        __u32 copied_total;
        __u32 pcm_frames;
        __u32 pcm_io_frames;
        __u32 sampling_rate;
    }

.. _`snd_compr_tstamp.members`:

Members
-------

byte_offset
    Byte offset in ring buffer to DSP

copied_total
    Total number of bytes copied from/to ring buffer to/by DSP

pcm_frames
    Frames decoded or encoded by DSP. This field will evolve by
    large steps and should only be used to monitor encoding/decoding
    progress. It shall not be used for timing estimates.

pcm_io_frames
    Frames rendered or received by DSP into a mixer or an audio
    output/input. This field should be used for A/V sync or time estimates.

sampling_rate
    sampling rate of audio

.. _`snd_compr_avail`:

struct snd_compr_avail
======================

.. c:type:: struct snd_compr_avail

    avail descriptor

.. _`snd_compr_avail.definition`:

Definition
----------

.. code-block:: c

    struct snd_compr_avail {
        __u64 avail;
        struct snd_compr_tstamp tstamp;
    }

.. _`snd_compr_avail.members`:

Members
-------

avail
    Number of bytes available in ring buffer for writing/reading

tstamp
    timestamp information

.. _`snd_compr_caps`:

struct snd_compr_caps
=====================

.. c:type:: struct snd_compr_caps

    caps descriptor

.. _`snd_compr_caps.definition`:

Definition
----------

.. code-block:: c

    struct snd_compr_caps {
        __u32 num_codecs;
        __u32 direction;
        __u32 min_fragment_size;
        __u32 max_fragment_size;
        __u32 min_fragments;
        __u32 max_fragments;
        __u32 codecs[MAX_NUM_CODECS];
        __u32 reserved[11];
    }

.. _`snd_compr_caps.members`:

Members
-------

num_codecs
    number of codecs supported

direction
    direction supported. Of type snd_compr_direction

min_fragment_size
    minimum fragment supported by DSP

max_fragment_size
    maximum fragment supported by DSP

min_fragments
    min fragments supported by DSP

max_fragments
    max fragments supported by DSP

codecs
    pointer to array of codecs

reserved
    reserved field

.. _`snd_compr_codec_caps`:

struct snd_compr_codec_caps
===========================

.. c:type:: struct snd_compr_codec_caps

    query capability of codec

.. _`snd_compr_codec_caps.definition`:

Definition
----------

.. code-block:: c

    struct snd_compr_codec_caps {
        __u32 codec;
        __u32 num_descriptors;
        struct snd_codec_desc descriptor[MAX_NUM_CODEC_DESCRIPTORS];
    }

.. _`snd_compr_codec_caps.members`:

Members
-------

codec
    codec for which capability is queried

num_descriptors
    number of codec descriptors

descriptor
    array of codec capability descriptor

.. _`sndrv_compress_encoder`:

enum sndrv_compress_encoder
===========================

.. c:type:: enum sndrv_compress_encoder


.. _`sndrv_compress_encoder.definition`:

Definition
----------

.. code-block:: c

    enum sndrv_compress_encoder {
        SNDRV_COMPRESS_ENCODER_PADDING,
        SNDRV_COMPRESS_ENCODER_DELAY
    };

.. _`sndrv_compress_encoder.constants`:

Constants
---------

SNDRV_COMPRESS_ENCODER_PADDING
    no of samples appended by the encoder at the
    end of the track

SNDRV_COMPRESS_ENCODER_DELAY
    no of samples inserted by the encoder at the
    beginning of the track

.. _`snd_compr_metadata`:

struct snd_compr_metadata
=========================

.. c:type:: struct snd_compr_metadata

    compressed stream metadata

.. _`snd_compr_metadata.definition`:

Definition
----------

.. code-block:: c

    struct snd_compr_metadata {
        __u32 key;
        __u32 value[8];
    }

.. _`snd_compr_metadata.members`:

Members
-------

key
    key id

value
    key value

.. _`sndrv_compress_ioctl_version`:

SNDRV_COMPRESS_IOCTL_VERSION
============================

.. c:function::  SNDRV_COMPRESS_IOCTL_VERSION()

    SNDRV_COMPRESS_GET_CAPS: Query capability of DSP SNDRV_COMPRESS_GET_CODEC_CAPS: Query capability of a codec SNDRV_COMPRESS_SET_PARAMS: Set codec and stream parameters

.. _`sndrv_compress_ioctl_version.note`:

Note
----

only codec params can be changed runtime and stream params cant be
SNDRV_COMPRESS_GET_PARAMS: Query codec params
SNDRV_COMPRESS_TSTAMP: get the current timestamp value
SNDRV_COMPRESS_AVAIL: get the current buffer avail value.
This also queries the tstamp properties
SNDRV_COMPRESS_PAUSE: Pause the running stream
SNDRV_COMPRESS_RESUME: resume a paused stream
SNDRV_COMPRESS_START: Start a stream
SNDRV_COMPRESS_STOP: stop a running stream, discarding ring buffer content
and the buffers currently with DSP
SNDRV_COMPRESS_DRAIN: Play till end of buffers and stop after that
SNDRV_COMPRESS_IOCTL_VERSION: Query the API version

.. This file was automatic generated / don't edit.

