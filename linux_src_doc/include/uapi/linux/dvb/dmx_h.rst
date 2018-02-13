.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/dvb/dmx.h

.. _`dmx_output`:

enum dmx_output
===============

.. c:type:: enum dmx_output

    Output for the demux.

.. _`dmx_output.definition`:

Definition
----------

.. code-block:: c

    enum dmx_output {
        DMX_OUT_DECODER,
        DMX_OUT_TAP,
        DMX_OUT_TS_TAP,
        DMX_OUT_TSDEMUX_TAP
    };

.. _`dmx_output.constants`:

Constants
---------

DMX_OUT_DECODER
    Streaming directly to decoder.

DMX_OUT_TAP
    Output going to a memory buffer (to be retrieved via the read command).
    Delivers the stream output to the demux device on which the ioctl
    is called.

DMX_OUT_TS_TAP
    Output multiplexed into a new TS (to be retrieved by reading from the
    logical DVR device). Routes output to the logical DVR device
    ``/dev/dvb/adapter?/dvr?``, which delivers a TS multiplexed from all
    filters for which \ ``DMX_OUT_TS_TAP``\  was specified.

DMX_OUT_TSDEMUX_TAP
    Like \ ``DMX_OUT_TS_TAP``\  but retrieved from the DMX device.

.. _`dmx_input`:

enum dmx_input
==============

.. c:type:: enum dmx_input

    Input from the demux.

.. _`dmx_input.definition`:

Definition
----------

.. code-block:: c

    enum dmx_input {
        DMX_IN_FRONTEND,
        DMX_IN_DVR
    };

.. _`dmx_input.constants`:

Constants
---------

DMX_IN_FRONTEND
    Input from a front-end device.

DMX_IN_DVR
    Input from the logical DVR device.

.. _`dmx_ts_pes`:

enum dmx_ts_pes
===============

.. c:type:: enum dmx_ts_pes

    type of the PES filter.

.. _`dmx_ts_pes.definition`:

Definition
----------

.. code-block:: c

    enum dmx_ts_pes {
        DMX_PES_AUDIO0,
        DMX_PES_VIDEO0,
        DMX_PES_TELETEXT0,
        DMX_PES_SUBTITLE0,
        DMX_PES_PCR0,
        DMX_PES_AUDIO1,
        DMX_PES_VIDEO1,
        DMX_PES_TELETEXT1,
        DMX_PES_SUBTITLE1,
        DMX_PES_PCR1,
        DMX_PES_AUDIO2,
        DMX_PES_VIDEO2,
        DMX_PES_TELETEXT2,
        DMX_PES_SUBTITLE2,
        DMX_PES_PCR2,
        DMX_PES_AUDIO3,
        DMX_PES_VIDEO3,
        DMX_PES_TELETEXT3,
        DMX_PES_SUBTITLE3,
        DMX_PES_PCR3,
        DMX_PES_OTHER
    };

.. _`dmx_ts_pes.constants`:

Constants
---------

DMX_PES_AUDIO0
    first audio PID. Also referred as \ ``DMX_PES_AUDIO``\ .

DMX_PES_VIDEO0
    first video PID. Also referred as \ ``DMX_PES_VIDEO``\ .

DMX_PES_TELETEXT0
    first teletext PID. Also referred as \ ``DMX_PES_TELETEXT``\ .

DMX_PES_SUBTITLE0
    first subtitle PID. Also referred as \ ``DMX_PES_SUBTITLE``\ .

DMX_PES_PCR0
    first Program Clock Reference PID.
    Also referred as \ ``DMX_PES_PCR``\ .

DMX_PES_AUDIO1
    second audio PID.

DMX_PES_VIDEO1
    second video PID.

DMX_PES_TELETEXT1
    second teletext PID.

DMX_PES_SUBTITLE1
    second subtitle PID.

DMX_PES_PCR1
    second Program Clock Reference PID.

DMX_PES_AUDIO2
    third audio PID.

DMX_PES_VIDEO2
    third video PID.

DMX_PES_TELETEXT2
    third teletext PID.

DMX_PES_SUBTITLE2
    third subtitle PID.

DMX_PES_PCR2
    third Program Clock Reference PID.

DMX_PES_AUDIO3
    fourth audio PID.

DMX_PES_VIDEO3
    fourth video PID.

DMX_PES_TELETEXT3
    fourth teletext PID.

DMX_PES_SUBTITLE3
    fourth subtitle PID.

DMX_PES_PCR3
    fourth Program Clock Reference PID.

DMX_PES_OTHER
    any other PID.

.. _`dmx_filter`:

struct dmx_filter
=================

.. c:type:: struct dmx_filter

    Specifies a section header filter.

.. _`dmx_filter.definition`:

Definition
----------

.. code-block:: c

    struct dmx_filter {
        __u8 filter[DMX_FILTER_SIZE];
        __u8 mask[DMX_FILTER_SIZE];
        __u8 mode[DMX_FILTER_SIZE];
    }

.. _`dmx_filter.members`:

Members
-------

filter
    bit array with bits to be matched at the section header.

mask
    bits that are valid at the filter bit array.

mode
    mode of match: if bit is zero, it will match if equal (positive
    match); if bit is one, it will match if the bit is negated.

.. _`dmx_filter.note`:

Note
----

All arrays in this struct have a size of DMX_FILTER_SIZE (16 bytes).

.. _`dmx_sct_filter_params`:

struct dmx_sct_filter_params
============================

.. c:type:: struct dmx_sct_filter_params

    Specifies a section filter.

.. _`dmx_sct_filter_params.definition`:

Definition
----------

.. code-block:: c

    struct dmx_sct_filter_params {
        __u16 pid;
        struct dmx_filter filter;
        __u32 timeout;
        __u32 flags;
    #define DMX_CHECK_CRC 1
    #define DMX_ONESHOT 2
    #define DMX_IMMEDIATE_START 4
    }

.. _`dmx_sct_filter_params.members`:

Members
-------

pid
    PID to be filtered.

filter
    section header filter, as defined by \ :c:type:`struct dmx_filter <dmx_filter>`\ .

timeout
    maximum time to filter, in milliseconds.

flags
    extra flags for the section filter.

.. _`dmx_sct_filter_params.description`:

Description
-----------

Carries the configuration for a MPEG-TS section filter.

The \ ``flags``\  can be:

     - \ ``DMX_CHECK_CRC``\  - only deliver sections where the CRC check succeeded;
     - \ ``DMX_ONESHOT``\  - disable the section filter after one section
       has been delivered;
     - \ ``DMX_IMMEDIATE_START``\  - Start filter immediately without requiring a
       :ref:`DMX_START`.

.. _`dmx_pes_filter_params`:

struct dmx_pes_filter_params
============================

.. c:type:: struct dmx_pes_filter_params

    Specifies Packetized Elementary Stream (PES) filter parameters.

.. _`dmx_pes_filter_params.definition`:

Definition
----------

.. code-block:: c

    struct dmx_pes_filter_params {
        __u16 pid;
        enum dmx_input input;
        enum dmx_output output;
        enum dmx_ts_pes pes_type;
        __u32 flags;
    }

.. _`dmx_pes_filter_params.members`:

Members
-------

pid
    PID to be filtered.

input
    Demux input, as specified by \ :c:type:`enum dmx_input <dmx_input>`\ .

output
    Demux output, as specified by \ :c:type:`enum dmx_output <dmx_output>`\ .

pes_type
    Type of the pes filter, as specified by \ :c:type:`enum dmx_pes_type <dmx_pes_type>`\ .

flags
    Demux PES flags.

.. _`dmx_stc`:

struct dmx_stc
==============

.. c:type:: struct dmx_stc

    Stores System Time Counter (STC) information.

.. _`dmx_stc.definition`:

Definition
----------

.. code-block:: c

    struct dmx_stc {
        unsigned int num;
        unsigned int base;
        __u64 stc;
    }

.. _`dmx_stc.members`:

Members
-------

num
    input data: number of the STC, from 0 to N.

base
    output: divisor for STC to get 90 kHz clock.

stc
    output: stc in \ ``base``\  * 90 kHz units.

.. _`dmx_buffer`:

struct dmx_buffer
=================

.. c:type:: struct dmx_buffer

    dmx buffer info

.. _`dmx_buffer.definition`:

Definition
----------

.. code-block:: c

    struct dmx_buffer {
        __u32 index;
        __u32 bytesused;
        __u32 offset;
        __u32 length;
    }

.. _`dmx_buffer.members`:

Members
-------

index
    id number of the buffer

bytesused
    number of bytes occupied by data in the buffer (payload);

offset
    for buffers with memory == DMX_MEMORY_MMAP;
    offset from the start of the device memory for this plane,
    (or a "cookie" that should be passed to \ :c:func:`mmap`\  as offset)

length
    size in bytes of the buffer

.. _`dmx_buffer.description`:

Description
-----------

Contains data exchanged by application and driver using one of the streaming
I/O methods.

.. _`dmx_requestbuffers`:

struct dmx_requestbuffers
=========================

.. c:type:: struct dmx_requestbuffers

    request dmx buffer information

.. _`dmx_requestbuffers.definition`:

Definition
----------

.. code-block:: c

    struct dmx_requestbuffers {
        __u32 count;
        __u32 size;
    }

.. _`dmx_requestbuffers.members`:

Members
-------

count
    number of requested buffers,

size
    size in bytes of the requested buffer

.. _`dmx_requestbuffers.description`:

Description
-----------

Contains data used for requesting a dmx buffer.
All reserved fields must be set to zero.

.. _`dmx_exportbuffer`:

struct dmx_exportbuffer
=======================

.. c:type:: struct dmx_exportbuffer

    export of dmx buffer as DMABUF file descriptor

.. _`dmx_exportbuffer.definition`:

Definition
----------

.. code-block:: c

    struct dmx_exportbuffer {
        __u32 index;
        __u32 flags;
        __s32 fd;
    }

.. _`dmx_exportbuffer.members`:

Members
-------

index
    id number of the buffer

flags
    flags for newly created file, currently only O_CLOEXEC is
    supported, refer to manual of open syscall for more details

fd
    file descriptor associated with DMABUF (set by driver)

.. _`dmx_exportbuffer.description`:

Description
-----------

Contains data used for exporting a dmx buffer as DMABUF file descriptor.
The buffer is identified by a 'cookie' returned by DMX_QUERYBUF
(identical to the cookie used to \ :c:func:`mmap`\  the buffer to userspace). All
reserved fields must be set to zero. The field reserved0 is expected to
become a structure 'type' allowing an alternative layout of the structure
content. Therefore this field should not be used for any other extensions.

.. This file was automatic generated / don't edit.

