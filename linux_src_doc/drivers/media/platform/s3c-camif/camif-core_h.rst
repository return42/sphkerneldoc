.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/s3c-camif/camif-core.h

.. _`camif_fmt`:

struct camif_fmt
================

.. c:type:: struct camif_fmt

    pixel format description

.. _`camif_fmt.definition`:

Definition
----------

.. code-block:: c

    struct camif_fmt {
        char *name;
        u32 fourcc;
        u32 color;
        u16 colplanes;
        u16 flags;
        u8 depth;
        u8 ybpp;
    }

.. _`camif_fmt.members`:

Members
-------

name
    *undescribed*

fourcc
    fourcc code for this format, 0 if not applicable

color
    a corresponding enum img_fmt

colplanes
    number of physically contiguous data planes

flags
    indicate for which SoCs revisions this format is valid

depth
    bits per pixel (total)

ybpp
    number of luminance bytes per pixel

.. _`camif_dma_offset`:

struct camif_dma_offset
=======================

.. c:type:: struct camif_dma_offset

    pixel offset information for DMA

.. _`camif_dma_offset.definition`:

Definition
----------

.. code-block:: c

    struct camif_dma_offset {
        int initial;
        int line;
    }

.. _`camif_dma_offset.members`:

Members
-------

initial
    offset (in pixels) to first pixel

line
    offset (in pixels) from end of line to start of next line

.. _`camif_frame`:

struct camif_frame
==================

.. c:type:: struct camif_frame

    source/target frame properties

.. _`camif_frame.definition`:

Definition
----------

.. code-block:: c

    struct camif_frame {
        u16 f_width;
        u16 f_height;
        struct v4l2_rect rect;
        struct camif_dma_offset dma_offset;
    }

.. _`camif_frame.members`:

Members
-------

f_width
    full pixel width

f_height
    full pixel height

rect
    crop/composition rectangle

dma_offset
    DMA offset configuration

.. _`s3c_camif_variant`:

struct s3c_camif_variant
========================

.. c:type:: struct s3c_camif_variant

    CAMIF variant structure

.. _`s3c_camif_variant.definition`:

Definition
----------

.. code-block:: c

    struct s3c_camif_variant {
        struct vp_pix_limits vp_pix_limits;
        struct camif_pix_limits pix_limits;
        u8 ip_revision;
        u8 has_img_effect;
        unsigned int vp_offset;
    }

.. _`s3c_camif_variant.members`:

Members
-------

vp_pix_limits
    pixel limits for the codec and preview paths

pix_limits
    *undescribed*

ip_revision
    the CAMIF IP revision: 0x20 for s3c244x, 0x32 for s3c6410

has_img_effect
    *undescribed*

vp_offset
    *undescribed*

.. _`camif_vp`:

struct camif_vp
===============

.. c:type:: struct camif_vp

    CAMIF data processing path structure (codec/preview)

.. _`camif_vp.definition`:

Definition
----------

.. code-block:: c

    struct camif_vp {
        wait_queue_head_t irq_queue;
        int irq;
        struct camif_dev *camif;
        struct media_pad pad;
        struct video_device vdev;
        struct v4l2_ctrl_handler ctrl_handler;
        struct v4l2_fh *owner;
        struct vb2_queue vb_queue;
        struct list_head pending_buf_q;
        struct list_head active_buf_q;
        unsigned int active_buffers;
        unsigned int buf_index;
        unsigned int frame_sequence;
        unsigned int reqbufs_count;
        struct camif_scaler scaler;
        const struct camif_fmt *out_fmt;
        unsigned int payload;
        struct camif_frame out_frame;
        unsigned int state;
        u16 fmt_flags;
        u8 id;
        u16 rotation;
        u8 hflip;
        u8 vflip;
        unsigned int offset;
    }

.. _`camif_vp.members`:

Members
-------

irq_queue
    interrupt handling waitqueue

irq
    interrupt number for this data path

camif
    pointer to the camif structure

pad
    media pad for the video node
    \ ``vdev``\             video device

vdev
    *undescribed*

ctrl_handler
    video node controls handler

owner
    file handle that own the streaming

vb_queue
    *undescribed*

pending_buf_q
    pending (empty) buffers queue head

active_buf_q
    active (being written) buffers queue head

active_buffers
    counter of buffer set up at the DMA engine

buf_index
    identifier of a last empty buffer set up in H/W

frame_sequence
    image frame sequence counter

reqbufs_count
    the number of buffers requested

scaler
    the scaler structure

out_fmt
    pixel format at this video path output

payload
    the output data frame payload size

out_frame
    the output pixel resolution

state
    the video path's state

fmt_flags
    flags determining supported pixel formats

id
    CAMIF id, 0 - codec, 1 - preview

rotation
    current image rotation value

hflip
    apply horizontal flip if set

vflip
    apply vertical flip if set

offset
    *undescribed*

.. _`camif_dev`:

struct camif_dev
================

.. c:type:: struct camif_dev

    the CAMIF driver private data structure

.. _`camif_dev.definition`:

Definition
----------

.. code-block:: c

    struct camif_dev {
        struct media_device media_dev;
        struct v4l2_device v4l2_dev;
        struct v4l2_subdev subdev;
        struct v4l2_mbus_framefmt mbus_fmt;
        struct v4l2_rect camif_crop;
        struct media_pad pads;
        int stream_count;
        struct cam_sensor;
        u8 test_pattern;
        u8 colorfx;
        u8 colorfx_cb;
        u8 colorfx_cr;
        struct camif_vp vp;
        const struct s3c_camif_variant *variant;
        struct device *dev;
        struct s3c_camif_plat_data pdata;
        struct clk  *clock;
        struct mutex lock;
        spinlock_t slock;
        void __iomem *io_base;
    }

.. _`camif_dev.members`:

Members
-------

media_dev
    top-level media device structure

v4l2_dev
    root v4l2_device

subdev
    camera interface ("catchcam") subdev

mbus_fmt
    camera input media bus format

camif_crop
    camera input interface crop rectangle

pads
    the camif subdev's media pads

stream_count
    the camera interface streaming reference counter

cam_sensor
    *undescribed*

test_pattern
    test pattern controls

colorfx
    *undescribed*

colorfx_cb
    *undescribed*

colorfx_cr
    *undescribed*

vp
    video path (DMA) description (codec/preview)

variant
    variant information for this device

dev
    pointer to the CAMIF device struct

pdata
    a copy of the driver's platform data

clock
    clocks required for the CAMIF operation

lock
    mutex protecting this data structure

slock
    spinlock protecting CAMIF registers

io_base
    start address of the mmaped CAMIF registers

.. _`camif_addr`:

struct camif_addr
=================

.. c:type:: struct camif_addr

    Y/Cb/Cr DMA start address structure

.. _`camif_addr.definition`:

Definition
----------

.. code-block:: c

    struct camif_addr {
        dma_addr_t y;
        dma_addr_t cb;
        dma_addr_t cr;
    }

.. _`camif_addr.members`:

Members
-------

y
    luminance plane dma address

cb
    Cb plane dma address

cr
    Cr plane dma address

.. _`camif_buffer`:

struct camif_buffer
===================

.. c:type:: struct camif_buffer

    the camif video buffer structure

.. _`camif_buffer.definition`:

Definition
----------

.. code-block:: c

    struct camif_buffer {
        struct vb2_v4l2_buffer vb;
        struct list_head list;
        struct camif_addr paddr;
        unsigned int index;
    }

.. _`camif_buffer.members`:

Members
-------

vb
    vb2 buffer

list
    list head for the buffers queue

paddr
    DMA start addresses

index
    an identifier of this buffer at the DMA engine

.. This file was automatic generated / don't edit.

