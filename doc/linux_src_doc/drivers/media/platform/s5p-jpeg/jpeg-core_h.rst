.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/s5p-jpeg/jpeg-core.h

.. _`s5p_jpeg`:

struct s5p_jpeg
===============

.. c:type:: struct s5p_jpeg

    JPEG IP abstraction

.. _`s5p_jpeg.definition`:

Definition
----------

.. code-block:: c

    struct s5p_jpeg {
        struct mutex lock;
        spinlock_t slock;
        struct v4l2_device v4l2_dev;
        struct video_device *vfd_encoder;
        struct video_device *vfd_decoder;
        struct v4l2_m2m_dev *m2m_dev;
        void __iomem *regs;
        unsigned int irq;
        enum exynos4_jpeg_result irq_ret;
        struct clk  *clocks[JPEG_MAX_CLOCKS];
        struct device *dev;
        void *alloc_ctx;
        struct s5p_jpeg_variant *variant;
        u32 irq_status;
    }

.. _`s5p_jpeg.members`:

Members
-------

lock
    the mutex protecting this structure

slock
    spinlock protecting the device contexts

v4l2_dev
    v4l2 device for mem2mem mode

vfd_encoder
    video device node for encoder mem2mem mode

vfd_decoder
    video device node for decoder mem2mem mode

m2m_dev
    v4l2 mem2mem device data

regs
    JPEG IP registers mapping

irq
    JPEG IP irq

irq_ret
    *undescribed*

clocks
    JPEG IP clock(s)

dev
    JPEG IP struct device

alloc_ctx
    videobuf2 memory allocator's context

variant
    driver variant to be used
    \ ``irq_status``\           interrupt flags set during single encode/decode

irq_status
    *undescribed*

.. _`s5p_jpeg_fmt`:

struct s5p_jpeg_fmt
===================

.. c:type:: struct s5p_jpeg_fmt

    driver's internal color format data

.. _`s5p_jpeg_fmt.definition`:

Definition
----------

.. code-block:: c

    struct s5p_jpeg_fmt {
        char *name;
        u32 fourcc;
        int depth;
        int colplanes;
        int memplanes;
        int h_align;
        int v_align;
        int subsampling;
        u32 flags;
    }

.. _`s5p_jpeg_fmt.members`:

Members
-------

name
    format descritpion

fourcc
    the fourcc code, 0 if not applicable

depth
    number of bits per pixel

colplanes
    number of color planes (1 for packed formats)

memplanes
    *undescribed*

h_align
    horizontal alignment order (align to 2^h_align)

v_align
    vertical alignment order (align to 2^v_align)

subsampling
    *undescribed*

flags
    flags describing format applicability

.. _`s5p_jpeg_addr`:

struct s5p_jpeg_addr
====================

.. c:type:: struct s5p_jpeg_addr

    JPEG converter physical address set for DMA

.. _`s5p_jpeg_addr.definition`:

Definition
----------

.. code-block:: c

    struct s5p_jpeg_addr {
        u32 y;
        u32 cb;
        u32 cr;
    }

.. _`s5p_jpeg_addr.members`:

Members
-------

y
    luminance plane physical address

cb
    Cb plane physical address

cr
    Cr plane physical address

.. This file was automatic generated / don't edit.

