.. -*- coding: utf-8; mode: rst -*-

==========
gsc-core.h
==========



.. _xref_enum gsc_datapath:

enum gsc_datapath
=================

.. c:type:: enum gsc_datapath

    the path of data used for G-Scaler



Constants
---------

:``GSC_CAMERA``:
    from camera

:``GSC_DMA``:
    from/to DMA

:``GSC_MIXER``:
    -- undescribed --

:``GSC_FIMD``:
    -- undescribed --

:``GSC_WRITEBACK``:
    from FIMD




.. _xref_struct_gsc_fmt:

struct gsc_fmt
==============

.. c:type:: struct gsc_fmt

    the driver's internal color format data



Definition
----------

.. code-block:: c

  struct gsc_fmt {
    u32 mbus_code;
    char * name;
    u32 pixelformat;
    u32 yorder;
    u32 corder;
    u16 num_planes;
    u8 depth[VIDEO_MAX_PLANES];
    u32 flags;
  };



Members
-------

:``u32 mbus_code``:
    Media Bus pixel code, -1 if not applicable

:``char * name``:
    format description

:``u32 pixelformat``:
    the fourcc code for this format, 0 if not applicable

:``u32 yorder``:
    Y/C order

:``u32 corder``:
    Chrominance order control

:``u16 num_planes``:
    number of physically non-contiguous data planes

:``u8 depth[VIDEO_MAX_PLANES]``:
    per plane driver's private 'number of bits per pixel'

:``u32 flags``:
    flags indicating which operation mode format applies to





.. _xref_struct_gsc_input_buf:

struct gsc_input_buf
====================

.. c:type:: struct gsc_input_buf

    the driver's video buffer



Definition
----------

.. code-block:: c

  struct gsc_input_buf {
    struct vb2_v4l2_buffer vb;
    struct list_head list;
    int idx;
  };



Members
-------

:``struct vb2_v4l2_buffer vb``:
    videobuf2 buffer

:``struct list_head list``:
    linked list structure for buffer queue

:``int idx``:
    index of G-Scaler input buffer





.. _xref_struct_gsc_addr:

struct gsc_addr
===============

.. c:type:: struct gsc_addr

    the G-Scaler physical address set



Definition
----------

.. code-block:: c

  struct gsc_addr {
    dma_addr_t y;
    dma_addr_t cb;
    dma_addr_t cr;
  };



Members
-------

:``dma_addr_t y``:
    luminance plane address

:``dma_addr_t cb``:
    Cb plane address

:``dma_addr_t cr``:
    Cr plane address





.. _xref_struct_gsc_scaler:

struct gsc_scaler
=================

.. c:type:: struct gsc_scaler

    the configuration data for G-Scaler inetrnal scaler



Definition
----------

.. code-block:: c

  struct gsc_scaler {
    u32 pre_shfactor;
    u32 pre_hratio;
    u32 pre_vratio;
    u32 main_hratio;
    u32 main_vratio;
  };



Members
-------

:``u32 pre_shfactor``:
    pre sclaer shift factor

:``u32 pre_hratio``:
    horizontal ratio of the prescaler

:``u32 pre_vratio``:
    vertical ratio of the prescaler

:``u32 main_hratio``:
    the main scaler's horizontal ratio

:``u32 main_vratio``:
    the main scaler's vertical ratio





.. _xref_struct_gsc_frame:

struct gsc_frame
================

.. c:type:: struct gsc_frame

    source/target frame properties



Definition
----------

.. code-block:: c

  struct gsc_frame {
    u32 f_width;
    u32 f_height;
    struct v4l2_rect crop;
    unsigned long payload[VIDEO_MAX_PLANES];
    struct gsc_addr addr;
    const struct gsc_fmt * fmt;
    u32 colorspace;
    u8 alpha;
  };



Members
-------

:``u32 f_width``:
    SRC : SRCIMG_WIDTH, DST : OUTPUTDMA_WHOLE_IMG_WIDTH

:``u32 f_height``:
    SRC : SRCIMG_HEIGHT, DST : OUTPUTDMA_WHOLE_IMG_HEIGHT

:``struct v4l2_rect crop``:
    cropped(source)/scaled(destination) size

:``unsigned long payload[VIDEO_MAX_PLANES]``:
    image size in bytes (w x h x bpp)

:``struct gsc_addr addr``:
    image frame buffer physical addresses

:``const struct gsc_fmt * fmt``:
    G-Scaler color format pointer

:``u32 colorspace``:
    value indicating v4l2_colorspace

:``u8 alpha``:
    frame's alpha value





.. _xref_struct_gsc_m2m_device:

struct gsc_m2m_device
=====================

.. c:type:: struct gsc_m2m_device

    v4l2 memory-to-memory device data



Definition
----------

.. code-block:: c

  struct gsc_m2m_device {
    struct video_device * vfd;
    struct v4l2_m2m_dev * m2m_dev;
    struct gsc_ctx * ctx;
    int refcnt;
  };



Members
-------

:``struct video_device * vfd``:
    the video device node for v4l2 m2m mode

:``struct v4l2_m2m_dev * m2m_dev``:
    v4l2 memory-to-memory device data

:``struct gsc_ctx * ctx``:
    hardware context data

:``int refcnt``:
    the reference counter





.. _xref_struct_gsc_pix_max:

struct gsc_pix_max
==================

.. c:type:: struct gsc_pix_max

    image pixel size limits in various IP configurations



Definition
----------

.. code-block:: c

  struct gsc_pix_max {
    u16 org_scaler_bypass_w;
    u16 org_scaler_bypass_h;
    u16 org_scaler_input_w;
    u16 org_scaler_input_h;
    u16 real_rot_dis_w;
    u16 real_rot_dis_h;
    u16 real_rot_en_w;
    u16 real_rot_en_h;
    u16 target_rot_dis_w;
    u16 target_rot_dis_h;
    u16 target_rot_en_w;
    u16 target_rot_en_h;
  };



Members
-------

:``u16 org_scaler_bypass_w``:
    max pixel width when the scaler is disabled

:``u16 org_scaler_bypass_h``:
    max pixel height when the scaler is disabled

:``u16 org_scaler_input_w``:
    max pixel width when the scaler is enabled

:``u16 org_scaler_input_h``:
    max pixel height when the scaler is enabled

:``u16 real_rot_dis_w``:
    max pixel src cropped height with the rotator is off

:``u16 real_rot_dis_h``:
    max pixel src croppped width with the rotator is off

:``u16 real_rot_en_w``:
    max pixel src cropped width with the rotator is on

:``u16 real_rot_en_h``:
    max pixel src cropped height with the rotator is on

:``u16 target_rot_dis_w``:
    max pixel dst scaled width with the rotator is off

:``u16 target_rot_dis_h``:
    max pixel dst scaled height with the rotator is off

:``u16 target_rot_en_w``:
    max pixel dst scaled width with the rotator is on

:``u16 target_rot_en_h``:
    max pixel dst scaled height with the rotator is on





.. _xref_struct_gsc_pix_min:

struct gsc_pix_min
==================

.. c:type:: struct gsc_pix_min

    image pixel size limits in various IP configurations



Definition
----------

.. code-block:: c

  struct gsc_pix_min {
    u16 org_w;
    u16 org_h;
    u16 real_w;
    u16 real_h;
    u16 target_rot_dis_w;
    u16 target_rot_dis_h;
    u16 target_rot_en_w;
    u16 target_rot_en_h;
  };



Members
-------

:``u16 org_w``:
    minimum source pixel width

:``u16 org_h``:
    minimum source pixel height

:``u16 real_w``:
    minimum input crop pixel width

:``u16 real_h``:
    minimum input crop pixel height

:``u16 target_rot_dis_w``:
    minimum output scaled pixel height when rotator is off

:``u16 target_rot_dis_h``:
    minimum output scaled pixel height when rotator is off

:``u16 target_rot_en_w``:
    minimum output scaled pixel height when rotator is on

:``u16 target_rot_en_h``:
    minimum output scaled pixel height when rotator is on





.. _xref_struct_gsc_variant:

struct gsc_variant
==================

.. c:type:: struct gsc_variant

    G-Scaler variant information



Definition
----------

.. code-block:: c

  struct gsc_variant {
  };



Members
-------





.. _xref_struct_gsc_driverdata:

struct gsc_driverdata
=====================

.. c:type:: struct gsc_driverdata

    per device type driver data for init time.



Definition
----------

.. code-block:: c

  struct gsc_driverdata {
    struct gsc_variant * variant[GSC_MAX_DEVS];
    unsigned long lclk_frequency;
    int num_entities;
  };



Members
-------

:``struct gsc_variant * variant[GSC_MAX_DEVS]``:
    the variant information for this driver.

:``unsigned long lclk_frequency``:
    G-Scaler clock frequency

:``int num_entities``:
    the number of g-scalers





.. _xref_struct_gsc_dev:

struct gsc_dev
==============

.. c:type:: struct gsc_dev

    abstraction for G-Scaler entity



Definition
----------

.. code-block:: c

  struct gsc_dev {
    spinlock_t slock;
    struct mutex lock;
    struct platform_device * pdev;
    struct gsc_variant * variant;
    u16 id;
    struct clk * clock;
    void __iomem * regs;
    wait_queue_head_t irq_queue;
    struct gsc_m2m_device m2m;
    unsigned long state;
    struct vb2_alloc_ctx * alloc_ctx;
    struct video_device vdev;
  };



Members
-------

:``spinlock_t slock``:
    the spinlock protecting this data structure

:``struct mutex lock``:
    the mutex protecting this data structure

:``struct platform_device * pdev``:
    pointer to the G-Scaler platform device

:``struct gsc_variant * variant``:
    the IP variant information

:``u16 id``:
    G-Scaler device index (0..GSC_MAX_DEVS)

:``struct clk * clock``:
    clocks required for G-Scaler operation

:``void __iomem * regs``:
    the mapped hardware registers

:``wait_queue_head_t irq_queue``:
    interrupt handler waitqueue

:``struct gsc_m2m_device m2m``:
    memory-to-memory V4L2 device information

:``unsigned long state``:
    flags used to synchronize m2m and capture mode operation

:``struct vb2_alloc_ctx * alloc_ctx``:
    videobuf2 memory allocator context

:``struct video_device vdev``:
    video device for G-Scaler instance



