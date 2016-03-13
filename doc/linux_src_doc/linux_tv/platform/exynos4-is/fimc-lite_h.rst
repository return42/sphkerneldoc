.. -*- coding: utf-8; mode: rst -*-

===========
fimc-lite.h
===========



.. _xref_struct_flite_drvdata:

struct flite_drvdata
====================

.. c:type:: struct flite_drvdata

    FIMC-LITE IP variant data structure



Definition
----------

.. code-block:: c

  struct flite_drvdata {
    unsigned short max_width;
    unsigned short max_height;
    unsigned short out_width_align;
    unsigned short win_hor_offs_align;
    unsigned short out_hor_offs_align;
    unsigned short max_dma_bufs;
    unsigned short num_instances;
  };



Members
-------

:``unsigned short max_width``:
    maximum camera interface input width in pixels

:``unsigned short max_height``:
    maximum camera interface input height in pixels

:``unsigned short out_width_align``:
    minimum output width alignment in pixels

:``unsigned short win_hor_offs_align``:
    minimum camera interface crop window horizontal
    			offset alignment in pixels

:``unsigned short out_hor_offs_align``:
    minimum output DMA compose rectangle horizontal
    			offset alignment in pixels

:``unsigned short max_dma_bufs``:
    number of output DMA buffer start address registers

:``unsigned short num_instances``:
    total number of FIMC-LITE IP instances available





.. _xref_struct_flite_frame:

struct flite_frame
==================

.. c:type:: struct flite_frame

    source/target frame properties



Definition
----------

.. code-block:: c

  struct flite_frame {
    u16 f_width;
    u16 f_height;
    struct v4l2_rect rect;
    const struct fimc_fmt * fmt;
  };



Members
-------

:``u16 f_width``:
    full pixel width

:``u16 f_height``:
    full pixel height

:``struct v4l2_rect rect``:
    crop/composition rectangle

:``const struct fimc_fmt * fmt``:
    pointer to pixel format description data structure





.. _xref_struct_flite_buffer:

struct flite_buffer
===================

.. c:type:: struct flite_buffer

    video buffer structure



Definition
----------

.. code-block:: c

  struct flite_buffer {
    struct vb2_v4l2_buffer vb;
    struct list_head list;
    dma_addr_t paddr;
    unsigned short index;
  };



Members
-------

:``struct vb2_v4l2_buffer vb``:
    vb2 buffer

:``struct list_head list``:
    list head for the buffers queue

:``dma_addr_t paddr``:
    DMA buffer start address

:``unsigned short index``:
    DMA start address register's index





.. _xref_struct_fimc_lite:

struct fimc_lite
================

.. c:type:: struct fimc_lite

    fimc lite structure



Definition
----------

.. code-block:: c

  struct fimc_lite {
    struct platform_device * pdev;
    struct flite_drvdata * dd;
    struct exynos_video_entity ve;
    struct v4l2_device * v4l2_dev;
    struct v4l2_fh fh;
    struct vb2_alloc_ctx * alloc_ctx;
    struct v4l2_subdev subdev;
    struct media_pad vd_pad;
    struct media_pad subdev_pads[FLITE_SD_PADS_NUM];
    struct v4l2_subdev * sensor;
    struct v4l2_ctrl_handler ctrl_handler;
    struct v4l2_ctrl * test_pattern;
    int index;
    struct mutex lock;
    spinlock_t slock;
    struct clk * clock;
    void __iomem * regs;
    wait_queue_head_t irq_queue;
    unsigned long payload[FLITE_MAX_PLANES];
    struct flite_frame inp_frame;
    struct flite_frame out_frame;
    atomic_t out_path;
    unsigned int source_subdev_grp_id;
    unsigned long state;
    struct list_head pending_buf_q;
    struct list_head active_buf_q;
    struct vb2_queue vb_queue;
    unsigned short buf_index;
    unsigned int frame_count;
    unsigned int reqbufs_count;
  };



Members
-------

:``struct platform_device * pdev``:
    pointer to FIMC-LITE platform device

:``struct flite_drvdata * dd``:
    SoC specific driver data structure

:``struct exynos_video_entity ve``:
    exynos video device entity structure

:``struct v4l2_device * v4l2_dev``:
    pointer to top the level v4l2_device

:``struct v4l2_fh fh``:
    v4l2 file handle

:``struct vb2_alloc_ctx * alloc_ctx``:
    videobuf2 memory allocator context

:``struct v4l2_subdev subdev``:
    FIMC-LITE subdev

:``struct media_pad vd_pad``:
    media (sink) pad for the capture video node

:``struct media_pad subdev_pads[FLITE_SD_PADS_NUM]``:
    the subdev media pads

:``struct v4l2_subdev * sensor``:
    sensor subdev attached to FIMC-LITE directly or through MIPI-CSIS

:``struct v4l2_ctrl_handler ctrl_handler``:
    v4l2 control handler

:``struct v4l2_ctrl * test_pattern``:
    test pattern controls

:``int index``:
    FIMC-LITE platform device index

:``struct mutex lock``:
    mutex serializing video device and the subdev operations

:``spinlock_t slock``:
    spinlock protecting this data structure and the hw registers

:``struct clk * clock``:
    FIMC-LITE gate clock

:``void __iomem * regs``:
    memory mapped io registers

:``wait_queue_head_t irq_queue``:
    interrupt handler waitqueue

:``unsigned long payload[FLITE_MAX_PLANES]``:
    image size in bytes (w x h x bpp)

:``struct flite_frame inp_frame``:
    camera input frame structure

:``struct flite_frame out_frame``:
    DMA output frame structure

:``atomic_t out_path``:
    output data path (DMA or FIFO)

:``unsigned int source_subdev_grp_id``:
    source subdev group id

:``unsigned long state``:
    driver state flags

:``struct list_head pending_buf_q``:
    pending buffers queue head

:``struct list_head active_buf_q``:
    the queue head of buffers scheduled in hardware

:``struct vb2_queue vb_queue``:
    vb2 buffers queue

:``unsigned short buf_index``:
    helps to keep track of the DMA start address register index

:``unsigned int frame_count``:
    the captured frames counter

:``unsigned int reqbufs_count``:
    the number of buffers requested with REQBUFS ioctl



