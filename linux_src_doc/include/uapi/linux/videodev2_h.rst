.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/videodev2.h

.. _`v4l2_capability`:

struct v4l2_capability
======================

.. c:type:: struct v4l2_capability

    Describes V4L2 device caps returned by VIDIOC_QUERYCAP

.. _`v4l2_capability.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_capability {
        __u8 driver[16];
        __u8 card[32];
        __u8 bus_info[32];
        __u32 version;
        __u32 capabilities;
        __u32 device_caps;
        __u32 reserved[3];
    }

.. _`v4l2_capability.members`:

Members
-------

driver
    name of the driver module (e.g. "bttv")

card
    name of the card (e.g. "Hauppauge WinTV")

bus_info
    name of the bus (e.g. "PCI:" + pci_name(pci_dev) )

version
    KERNEL_VERSION

capabilities
    capabilities of the physical device as a whole

device_caps
    capabilities accessed via this particular device (node)

reserved
    reserved fields for future extensions

.. _`v4l2_plane`:

struct v4l2_plane
=================

.. c:type:: struct v4l2_plane

    plane info for multi-planar buffers

.. _`v4l2_plane.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_plane {
        __u32 bytesused;
        __u32 length;
        union m;
        __u32 data_offset;
        __u32 reserved[11];
    }

.. _`v4l2_plane.members`:

Members
-------

bytesused
    number of bytes occupied by data in the plane (payload)

length
    size of this plane (NOT the payload) in bytes

m
    *undescribed*

data_offset
    offset in the plane to the start of data; usually 0,
    unless there is a header in front of the data

.. _`v4l2_plane.description`:

Description
-----------

Multi-planar buffers consist of one or more planes, e.g. an YCbCr buffer
with two planes can have one plane for Y, and another for interleaved CbCr
components. Each plane can reside in a separate memory buffer, or even in
a completely separate memory node (e.g. in embedded devices).

.. _`v4l2_buffer`:

struct v4l2_buffer
==================

.. c:type:: struct v4l2_buffer

    video buffer info

.. _`v4l2_buffer.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_buffer {
        __u32 index;
        __u32 type;
        __u32 bytesused;
        __u32 flags;
        __u32 field;
        struct timeval timestamp;
        struct v4l2_timecode timecode;
        __u32 sequence;
        __u32 memory;
        union m;
        __u32 length;
        __u32 reserved2;
        __u32 reserved;
    }

.. _`v4l2_buffer.members`:

Members
-------

index
    id number of the buffer

type
    enum v4l2_buf_type; buffer type (type == \*\_MPLANE for
    multiplanar buffers);

bytesused
    number of bytes occupied by data in the buffer (payload);
    unused (set to 0) for multiplanar buffers

flags
    buffer informational flags

field
    enum v4l2_field; field order of the image in the buffer

timestamp
    frame timestamp

timecode
    frame timecode

sequence
    sequence count of this frame

memory
    enum v4l2_memory; the method, in which the actual video data is
    passed

m
    *undescribed*

length
    size in bytes of the buffer (NOT its payload) for single-plane
    buffers (when type != \*\_MPLANE); number of elements in the
    planes array for multi-plane buffers

reserved2
    *undescribed*

reserved
    *undescribed*

.. _`v4l2_buffer.description`:

Description
-----------

Contains data exchanged by application and driver using one of the Streaming
I/O methods.

.. _`v4l2_exportbuffer`:

struct v4l2_exportbuffer
========================

.. c:type:: struct v4l2_exportbuffer

    export of video buffer as DMABUF file descriptor

.. _`v4l2_exportbuffer.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_exportbuffer {
        __u32 type;
        __u32 index;
        __u32 plane;
        __u32 flags;
        __s32 fd;
        __u32 reserved[11];
    }

.. _`v4l2_exportbuffer.members`:

Members
-------

type
    enum v4l2_buf_type; buffer type (type == \*\_MPLANE for
    multiplanar buffers);

index
    id number of the buffer

plane
    index of the plane to be exported, 0 for single plane queues

flags
    flags for newly created file, currently only O_CLOEXEC is
    supported, refer to manual of open syscall for more details

fd
    file descriptor associated with DMABUF (set by driver)

.. _`v4l2_exportbuffer.description`:

Description
-----------

Contains data used for exporting a video buffer as DMABUF file descriptor.
The buffer is identified by a 'cookie' returned by VIDIOC_QUERYBUF
(identical to the cookie used to \ :c:func:`mmap`\  the buffer to userspace). All
reserved fields must be set to zero. The field reserved0 is expected to
become a structure 'type' allowing an alternative layout of the structure
content. Therefore this field should not be used for any other extensions.

.. _`v4l2_selection`:

struct v4l2_selection
=====================

.. c:type:: struct v4l2_selection

    selection info

.. _`v4l2_selection.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_selection {
        __u32 type;
        __u32 target;
        __u32 flags;
        struct v4l2_rect r;
        __u32 reserved[9];
    }

.. _`v4l2_selection.members`:

Members
-------

type
    buffer type (do not use \*\_MPLANE types)

target
    Selection target, used to choose one of possible rectangles;
    defined in v4l2-common.h; V4L2_SEL_TGT\_\* .

flags
    constraints flags, defined in v4l2-common.h; V4L2_SEL_FLAG\_\*.

r
    coordinates of selection window

reserved
    for future use, rounds structure size to 64 bytes, set to zero

.. _`v4l2_selection.description`:

Description
-----------

Hardware may use multiple helper windows to process a video stream.
The structure is used to exchange this selection areas between
an application and a driver.

.. _`v4l2_plane_pix_format`:

struct v4l2_plane_pix_format
============================

.. c:type:: struct v4l2_plane_pix_format

    additional, per-plane format definition

.. _`v4l2_plane_pix_format.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_plane_pix_format {
        __u32 sizeimage;
        __u32 bytesperline;
        __u16 reserved[6];
    }

.. _`v4l2_plane_pix_format.members`:

Members
-------

sizeimage
    maximum size in bytes required for data, for which
    this plane will be used

bytesperline
    distance in bytes between the leftmost pixels in two
    adjacent lines

.. _`v4l2_pix_format_mplane`:

struct v4l2_pix_format_mplane
=============================

.. c:type:: struct v4l2_pix_format_mplane

    multiplanar format definition

.. _`v4l2_pix_format_mplane.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_pix_format_mplane {
        __u32 width;
        __u32 height;
        __u32 pixelformat;
        __u32 field;
        __u32 colorspace;
        struct v4l2_plane_pix_format plane_fmt[VIDEO_MAX_PLANES];
        __u8 num_planes;
        __u8 flags;
        union {unnamed_union};
        __u8 quantization;
        __u8 xfer_func;
        __u8 reserved[7];
    }

.. _`v4l2_pix_format_mplane.members`:

Members
-------

width
    image width in pixels

height
    image height in pixels

pixelformat
    little endian four character code (fourcc)

field
    enum v4l2_field; field order (for interlaced video)

colorspace
    enum v4l2_colorspace; supplemental to pixelformat

plane_fmt
    per-plane information

num_planes
    number of planes for this format

flags
    format flags (V4L2_PIX_FMT_FLAG\_\*)

{unnamed_union}
    anonymous


quantization
    enum v4l2_quantization, colorspace quantization

xfer_func
    enum v4l2_xfer_func, colorspace transfer function

.. _`v4l2_sdr_format`:

struct v4l2_sdr_format
======================

.. c:type:: struct v4l2_sdr_format

    SDR format definition

.. _`v4l2_sdr_format.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_sdr_format {
        __u32 pixelformat;
        __u32 buffersize;
        __u8 reserved[24];
    }

.. _`v4l2_sdr_format.members`:

Members
-------

pixelformat
    little endian four character code (fourcc)

buffersize
    maximum size in bytes required for data

.. _`v4l2_format`:

struct v4l2_format
==================

.. c:type:: struct v4l2_format

    stream data format

.. _`v4l2_format.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_format {
        __u32 type;
        union fmt;
    }

.. _`v4l2_format.members`:

Members
-------

type
    enum v4l2_buf_type; type of the data stream

fmt
    *undescribed*

.. _`v4l2_event_motion_det`:

struct v4l2_event_motion_det
============================

.. c:type:: struct v4l2_event_motion_det

    motion detection event

.. _`v4l2_event_motion_det.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_event_motion_det {
        __u32 flags;
        __u32 frame_sequence;
        __u32 region_mask;
    }

.. _`v4l2_event_motion_det.members`:

Members
-------

flags
    if V4L2_EVENT_MD_FL_HAVE_FRAME_SEQ is set, then the
    frame_sequence field is valid.

frame_sequence
    the frame sequence number associated with this event.

region_mask
    which regions detected motion.

.. _`v4l2_create_buffers`:

struct v4l2_create_buffers
==========================

.. c:type:: struct v4l2_create_buffers

    VIDIOC_CREATE_BUFS argument

.. _`v4l2_create_buffers.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_create_buffers {
        __u32 index;
        __u32 count;
        __u32 memory;
        struct v4l2_format format;
        __u32 reserved[8];
    }

.. _`v4l2_create_buffers.members`:

Members
-------

index
    on return, index of the first created buffer

count
    entry: number of requested buffers,
    return: number of created buffers

memory
    enum v4l2_memory; buffer memory type

format
    frame format, for which buffers are requested

reserved
    future extensions

.. This file was automatic generated / don't edit.

