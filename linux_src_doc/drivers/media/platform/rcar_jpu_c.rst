.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/rcar_jpu.c

.. _`jpu`:

struct jpu
==========

.. c:type:: struct jpu

    JPEG IP abstraction

.. _`jpu.definition`:

Definition
----------

.. code-block:: c

    struct jpu {
        struct mutex mutex;
        spinlock_t lock;
        struct v4l2_device v4l2_dev;
        struct video_device vfd_encoder;
        struct video_device vfd_decoder;
        struct v4l2_m2m_dev *m2m_dev;
        struct jpu_ctx *curr;
        void __iomem *regs;
        unsigned int irq;
        struct clk *clk;
        struct device *dev;
        int ref_count;
    }

.. _`jpu.members`:

Members
-------

mutex
    the mutex protecting this structure

lock
    spinlock protecting the device contexts

v4l2_dev
    v4l2 device for mem2mem mode

vfd_encoder
    video device node for encoder mem2mem mode

vfd_decoder
    video device node for decoder mem2mem mode

m2m_dev
    v4l2 mem2mem device data

curr
    pointer to current context

regs
    JPEG IP registers mapping

irq
    JPEG IP irq

clk
    JPEG IP clock

dev
    JPEG IP struct device

ref_count
    reference counter

.. _`jpu_buffer`:

struct jpu_buffer
=================

.. c:type:: struct jpu_buffer

    driver's specific video buffer

.. _`jpu_buffer.definition`:

Definition
----------

.. code-block:: c

    struct jpu_buffer {
        struct v4l2_m2m_buffer buf;
        unsigned short compr_quality;
        unsigned char subsampling;
    }

.. _`jpu_buffer.members`:

Members
-------

buf
    m2m buffer

compr_quality
    destination image quality in compression mode

subsampling
    source image subsampling in decompression mode

.. _`jpu_fmt`:

struct jpu_fmt
==============

.. c:type:: struct jpu_fmt

    driver's internal format data

.. _`jpu_fmt.definition`:

Definition
----------

.. code-block:: c

    struct jpu_fmt {
        u32 fourcc;
        u32 colorspace;
        u8 bpp[2];
        u8 h_align;
        u8 v_align;
        u8 subsampling;
        u8 num_planes;
        u16 types;
    }

.. _`jpu_fmt.members`:

Members
-------

fourcc
    the fourcc code, 0 if not applicable

colorspace
    the colorspace specifier

bpp
    number of bits per pixel per plane

h_align
    horizontal alignment order (align to 2^h_align)

v_align
    vertical alignment order (align to 2^v_align)

subsampling
    (horizontal:4 \| vertical:4) subsampling factor

num_planes
    number of planes

types
    types of queue this format is applicable to

.. _`jpu_q_data`:

struct jpu_q_data
=================

.. c:type:: struct jpu_q_data

    parameters of one queue

.. _`jpu_q_data.definition`:

Definition
----------

.. code-block:: c

    struct jpu_q_data {
        struct jpu_fmt *fmtinfo;
        struct v4l2_pix_format_mplane format;
        unsigned int sequence;
    }

.. _`jpu_q_data.members`:

Members
-------

fmtinfo
    driver-specific format of this queue

format
    multiplanar format of this queue

sequence
    sequence number

.. _`jpu_ctx`:

struct jpu_ctx
==============

.. c:type:: struct jpu_ctx

    the device context data

.. _`jpu_ctx.definition`:

Definition
----------

.. code-block:: c

    struct jpu_ctx {
        struct jpu *jpu;
        bool encoder;
        unsigned short compr_quality;
        struct jpu_q_data out_q;
        struct jpu_q_data cap_q;
        struct v4l2_fh fh;
        struct v4l2_ctrl_handler ctrl_handler;
    }

.. _`jpu_ctx.members`:

Members
-------

jpu
    JPEG IP device for this context

encoder
    compression (encode) operation or decompression (decode)

compr_quality
    destination image quality in compression (encode) mode

out_q
    source (output) queue information

cap_q
    destination (capture) queue information

fh
    file handler

ctrl_handler
    controls handler

.. This file was automatic generated / don't edit.

