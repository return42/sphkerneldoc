.. -*- coding: utf-8; mode: rst -*-

============
camif-core.h
============



.. _xref_struct_camif_fmt:

struct camif_fmt
================

.. c:type:: struct camif_fmt

    pixel format description



Definition
----------

.. code-block:: c

  struct camif_fmt {
    u32 fourcc;
    u32 color;
    u16 colplanes;
    u16 flags;
    u8 depth;
    u8 ybpp;
  };



Members
-------

:``u32 fourcc``:
    fourcc code for this format, 0 if not applicable

:``u32 color``:
    a corresponding enum img_fmt

:``u16 colplanes``:
    number of physically contiguous data planes

:``u16 flags``:
    indicate for which SoCs revisions this format is valid

:``u8 depth``:
    bits per pixel (total)

:``u8 ybpp``:
    number of luminance bytes per pixel





.. _xref_struct_camif_dma_offset:

struct camif_dma_offset
=======================

.. c:type:: struct camif_dma_offset

    pixel offset information for DMA



Definition
----------

.. code-block:: c

  struct camif_dma_offset {
    int initial;
    int line;
  };



Members
-------

:``int initial``:
    offset (in pixels) to first pixel

:``int line``:
    offset (in pixels) from end of line to start of next line





.. _xref_struct_camif_frame:

struct camif_frame
==================

.. c:type:: struct camif_frame

    source/target frame properties



Definition
----------

.. code-block:: c

  struct camif_frame {
    u16 f_width;
    u16 f_height;
    struct v4l2_rect rect;
    struct camif_dma_offset dma_offset;
  };



Members
-------

:``u16 f_width``:
    full pixel width

:``u16 f_height``:
    full pixel height

:``struct v4l2_rect rect``:
    crop/composition rectangle

:``struct camif_dma_offset dma_offset``:
    DMA offset configuration





.. _xref_struct_s3c_camif_variant:

struct s3c_camif_variant
========================

.. c:type:: struct s3c_camif_variant

    CAMIF variant structure



Definition
----------

.. code-block:: c

  struct s3c_camif_variant {
    struct vp_pix_limits vp_pix_limits[2];
    u8 ip_revision;
  };



Members
-------

:``struct vp_pix_limits vp_pix_limits[2]``:
    pixel limits for the codec and preview paths

:``u8 ip_revision``:
    the CAMIF IP revision: 0x20 for s3c244x, 0x32 for s3c6410





.. _xref_struct_camif_vp:

struct camif_vp
===============

.. c:type:: struct camif_vp

    CAMIF data processing path structure (codec/preview)



Definition
----------

.. code-block:: c

  struct camif_vp {
    wait_queue_head_t irq_queue;
    int irq;
    struct camif_dev * camif;
    struct media_pad pad;
    struct v4l2_ctrl_handler ctrl_handler;
    struct v4l2_fh * owner;
    struct list_head pending_buf_q;
    struct list_head active_buf_q;
    unsigned int active_buffers;
    unsigned int buf_index;
    unsigned int frame_sequence;
    unsigned int reqbufs_count;
    struct camif_scaler scaler;
    const struct camif_fmt * out_fmt;
    unsigned int payload;
    struct camif_frame out_frame;
    unsigned int state;
    u16 fmt_flags;
    u8 id;
    u16 rotation;
    u8 hflip;
    u8 vflip;
  };



Members
-------

:``wait_queue_head_t irq_queue``:
    interrupt handling waitqueue

:``int irq``:
    interrupt number for this data path

:``struct camif_dev * camif``:
    pointer to the camif structure

:``struct media_pad pad``:
    media pad for the video node
    **vdev**            video device

:``struct v4l2_ctrl_handler ctrl_handler``:
    video node controls handler

:``struct v4l2_fh * owner``:
    file handle that own the streaming

:``struct list_head pending_buf_q``:
    pending (empty) buffers queue head

:``struct list_head active_buf_q``:
    active (being written) buffers queue head

:``unsigned int active_buffers``:
    counter of buffer set up at the DMA engine

:``unsigned int buf_index``:
    identifier of a last empty buffer set up in H/W

:``unsigned int frame_sequence``:
    image frame sequence counter

:``unsigned int reqbufs_count``:
    the number of buffers requested

:``struct camif_scaler scaler``:
    the scaler structure

:``const struct camif_fmt * out_fmt``:
    pixel format at this video path output

:``unsigned int payload``:
    the output data frame payload size

:``struct camif_frame out_frame``:
    the output pixel resolution

:``unsigned int state``:
    the video path's state

:``u16 fmt_flags``:
    flags determining supported pixel formats

:``u8 id``:
    CAMIF id, 0 - codec, 1 - preview

:``u16 rotation``:
    current image rotation value

:``u8 hflip``:
    apply horizontal flip if set

:``u8 vflip``:
    apply vertical flip if set





.. _xref_struct_camif_dev:

struct camif_dev
================

.. c:type:: struct camif_dev

    the CAMIF driver private data structure



Definition
----------

.. code-block:: c

  struct camif_dev {
    struct media_device media_dev;
    struct v4l2_device v4l2_dev;
    struct v4l2_subdev subdev;
    struct v4l2_mbus_framefmt mbus_fmt;
    struct v4l2_rect camif_crop;
    struct media_pad pads[CAMIF_SD_PADS_NUM];
    int stream_count;
    u8 test_pattern;
    struct camif_vp vp[CAMIF_VP_NUM];
    struct vb2_alloc_ctx * alloc_ctx;
    const struct s3c_camif_variant * variant;
    struct device * dev;
    struct s3c_camif_plat_data pdata;
    struct clk * clock[CLK_MAX_NUM];
    struct mutex lock;
    spinlock_t slock;
    void __iomem * io_base;
  };



Members
-------

:``struct media_device media_dev``:
    top-level media device structure

:``struct v4l2_device v4l2_dev``:
    root v4l2_device

:``struct v4l2_subdev subdev``:
    camera interface ("catchcam") subdev

:``struct v4l2_mbus_framefmt mbus_fmt``:
    camera input media bus format

:``struct v4l2_rect camif_crop``:
    camera input interface crop rectangle

:``struct media_pad pads[CAMIF_SD_PADS_NUM]``:
    the camif subdev's media pads

:``int stream_count``:
    the camera interface streaming reference counter

:``u8 test_pattern``:
    test pattern controls

:``struct camif_vp vp[CAMIF_VP_NUM]``:
    video path (DMA) description (codec/preview)

:``struct vb2_alloc_ctx * alloc_ctx``:
    memory buffer allocator context

:``const struct s3c_camif_variant * variant``:
    variant information for this device

:``struct device * dev``:
    pointer to the CAMIF device struct

:``struct s3c_camif_plat_data pdata``:
    a copy of the driver's platform data

:``struct clk * clock[CLK_MAX_NUM]``:
    clocks required for the CAMIF operation

:``struct mutex lock``:
    mutex protecting this data structure

:``spinlock_t slock``:
    spinlock protecting CAMIF registers

:``void __iomem * io_base``:
    start address of the mmaped CAMIF registers





.. _xref_struct_camif_addr:

struct camif_addr
=================

.. c:type:: struct camif_addr

    Y/Cb/Cr DMA start address structure



Definition
----------

.. code-block:: c

  struct camif_addr {
    dma_addr_t y;
    dma_addr_t cb;
    dma_addr_t cr;
  };



Members
-------

:``dma_addr_t y``:
    luminance plane dma address

:``dma_addr_t cb``:
    Cb plane dma address

:``dma_addr_t cr``:
    Cr plane dma address





.. _xref_struct_camif_buffer:

struct camif_buffer
===================

.. c:type:: struct camif_buffer

    the camif video buffer structure



Definition
----------

.. code-block:: c

  struct camif_buffer {
    struct vb2_v4l2_buffer vb;
    struct list_head list;
    struct camif_addr paddr;
    unsigned int index;
  };



Members
-------

:``struct vb2_v4l2_buffer vb``:
    vb2 buffer

:``struct list_head list``:
    list head for the buffers queue

:``struct camif_addr paddr``:
    DMA start addresses

:``unsigned int index``:
    an identifier of this buffer at the DMA engine



