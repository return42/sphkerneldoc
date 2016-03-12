.. -*- coding: utf-8; mode: rst -*-

==========
rcar_jpu.c
==========



.. _xref_struct_jpu:

struct jpu
==========

.. c:type:: struct jpu

    JPEG IP abstraction



Definition
----------

.. code-block:: c

  struct jpu {
    struct mutex mutex;
    spinlock_t lock;
    struct v4l2_device v4l2_dev;
    struct video_device vfd_encoder;
    struct video_device vfd_decoder;
    struct v4l2_m2m_dev * m2m_dev;
    struct jpu_ctx * curr;
    wait_queue_head_t irq_queue;
    void __iomem * regs;
    unsigned int irq;
    struct clk * clk;
    struct device * dev;
    void * alloc_ctx;
    int ref_count;
  };



Members
-------

:``struct mutex mutex``:
    the mutex protecting this structure

:``spinlock_t lock``:
    spinlock protecting the device contexts

:``struct v4l2_device v4l2_dev``:
    v4l2 device for mem2mem mode

:``struct video_device vfd_encoder``:
    video device node for encoder mem2mem mode

:``struct video_device vfd_decoder``:
    video device node for decoder mem2mem mode

:``struct v4l2_m2m_dev * m2m_dev``:
    v4l2 mem2mem device data

:``struct jpu_ctx * curr``:
    pointer to current context

:``wait_queue_head_t irq_queue``:
    interrupt handler waitqueue

:``void __iomem * regs``:
    JPEG IP registers mapping

:``unsigned int irq``:
    JPEG IP irq

:``struct clk * clk``:
    JPEG IP clock

:``struct device * dev``:
    JPEG IP struct device

:``void * alloc_ctx``:
    videobuf2 memory allocator's context

:``int ref_count``:
    reference counter





.. _xref_struct_jpu_buffer:

struct jpu_buffer
=================

.. c:type:: struct jpu_buffer

    driver's specific video buffer



Definition
----------

.. code-block:: c

  struct jpu_buffer {
    struct v4l2_m2m_buffer buf;
    unsigned short compr_quality;
    unsigned char subsampling;
  };



Members
-------

:``struct v4l2_m2m_buffer buf``:
    m2m buffer

:``unsigned short compr_quality``:
    destination image quality in compression mode

:``unsigned char subsampling``:
    source image subsampling in decompression mode





.. _xref_struct_jpu_fmt:

struct jpu_fmt
==============

.. c:type:: struct jpu_fmt

    driver's internal format data



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
  };



Members
-------

:``u32 fourcc``:
    the fourcc code, 0 if not applicable

:``u32 colorspace``:
    the colorspace specifier

:``u8 bpp[2]``:
    number of bits per pixel per plane

:``u8 h_align``:
    horizontal alignment order (align to 2^h_align)

:``u8 v_align``:
    vertical alignment order (align to 2^v_align)

:``u8 subsampling``:
    (horizontal:4 | vertical:4) subsampling factor

:``u8 num_planes``:
    number of planes

:``u16 types``:
    types of queue this format is applicable to



