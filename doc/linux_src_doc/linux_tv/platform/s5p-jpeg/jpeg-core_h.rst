.. -*- coding: utf-8; mode: rst -*-

===========
jpeg-core.h
===========



.. _xref_struct_s5p_jpeg:

struct s5p_jpeg
===============

.. c:type:: struct s5p_jpeg

    JPEG IP abstraction



Definition
----------

.. code-block:: c

  struct s5p_jpeg {
    struct mutex lock;
    spinlock_t slock;
    struct v4l2_device v4l2_dev;
    struct video_device * vfd_encoder;
    struct video_device * vfd_decoder;
    struct v4l2_m2m_dev * m2m_dev;
    void __iomem * regs;
    unsigned int irq;
    struct clk * clocks[JPEG_MAX_CLOCKS];
    struct device * dev;
    void * alloc_ctx;
    struct s5p_jpeg_variant * variant;
  };



Members
-------

:``struct mutex lock``:
    the mutex protecting this structure

:``spinlock_t slock``:
    spinlock protecting the device contexts

:``struct v4l2_device v4l2_dev``:
    v4l2 device for mem2mem mode

:``struct video_device * vfd_encoder``:
    video device node for encoder mem2mem mode

:``struct video_device * vfd_decoder``:
    video device node for decoder mem2mem mode

:``struct v4l2_m2m_dev * m2m_dev``:
    v4l2 mem2mem device data

:``void __iomem * regs``:
    JPEG IP registers mapping

:``unsigned int irq``:
    JPEG IP irq

:``struct clk * clocks[JPEG_MAX_CLOCKS]``:
    JPEG IP clock(s)

:``struct device * dev``:
    JPEG IP struct device

:``void * alloc_ctx``:
    videobuf2 memory allocator's context

:``struct s5p_jpeg_variant * variant``:
    driver variant to be used
    **irq_status**		interrupt flags set during single encode/decode





.. _xref_struct_s5p_jpeg_fmt:

struct s5p_jpeg_fmt
===================

.. c:type:: struct s5p_jpeg_fmt

    driver's internal color format data



Definition
----------

.. code-block:: c

  struct s5p_jpeg_fmt {
    char * name;
    u32 fourcc;
    int depth;
    int colplanes;
    int h_align;
    int v_align;
    u32 flags;
  };



Members
-------

:``char * name``:
    format descritpion

:``u32 fourcc``:
    the fourcc code, 0 if not applicable

:``int depth``:
    number of bits per pixel

:``int colplanes``:
    number of color planes (1 for packed formats)

:``int h_align``:
    horizontal alignment order (align to 2^h_align)

:``int v_align``:
    vertical alignment order (align to 2^v_align)

:``u32 flags``:
    flags describing format applicability





.. _xref_struct_s5p_jpeg_addr:

struct s5p_jpeg_addr
====================

.. c:type:: struct s5p_jpeg_addr

    JPEG converter physical address set for DMA



Definition
----------

.. code-block:: c

  struct s5p_jpeg_addr {
    u32 y;
    u32 cb;
    u32 cr;
  };



Members
-------

:``u32 y``:
    luminance plane physical address

:``u32 cb``:
    Cb plane physical address

:``u32 cr``:
    Cr plane physical address



