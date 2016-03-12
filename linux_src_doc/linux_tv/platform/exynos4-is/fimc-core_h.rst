.. -*- coding: utf-8; mode: rst -*-

===========
fimc-core.h
===========



.. _xref_struct_fimc_dma_offset:

struct fimc_dma_offset
======================

.. c:type:: struct fimc_dma_offset

    pixel offset information for DMA



Definition
----------

.. code-block:: c

  struct fimc_dma_offset {
    int y_h;
    int y_v;
    int cb_h;
    int cb_v;
    int cr_h;
    int cr_v;
  };



Members
-------

:``int y_h``:
    y value horizontal offset

:``int y_v``:
    y value vertical offset

:``int cb_h``:
    cb value horizontal offset

:``int cb_v``:
    cb value vertical offset

:``int cr_h``:
    cr value horizontal offset

:``int cr_v``:
    cr value vertical offset





.. _xref_struct_fimc_effect:

struct fimc_effect
==================

.. c:type:: struct fimc_effect

    color effect information



Definition
----------

.. code-block:: c

  struct fimc_effect {
    u32 type;
    u8 pat_cb;
    u8 pat_cr;
  };



Members
-------

:``u32 type``:
    effect type

:``u8 pat_cb``:
    cr value when type is "arbitrary"

:``u8 pat_cr``:
    cr value when type is "arbitrary"





.. _xref_struct_fimc_scaler:

struct fimc_scaler
==================

.. c:type:: struct fimc_scaler

    the configuration data for FIMC inetrnal scaler



Definition
----------

.. code-block:: c

  struct fimc_scaler {
    unsigned int scaleup_h:1;
    unsigned int scaleup_v:1;
    unsigned int copy_mode:1;
    unsigned int enabled:1;
    u32 hfactor;
    u32 vfactor;
    u32 pre_hratio;
    u32 pre_vratio;
    u32 pre_dst_width;
    u32 pre_dst_height;
    u32 main_hratio;
    u32 main_vratio;
    u32 real_width;
    u32 real_height;
  };



Members
-------

:``unsigned int:1 scaleup_h``:
    flag indicating scaling up horizontally

:``unsigned int:1 scaleup_v``:
    flag indicating scaling up vertically

:``unsigned int:1 copy_mode``:
    flag indicating transparent DMA transfer (no scaling
    			and color format conversion)

:``unsigned int:1 enabled``:
    flag indicating if the scaler is used

:``u32 hfactor``:
    horizontal shift factor

:``u32 vfactor``:
    vertical shift factor

:``u32 pre_hratio``:
    horizontal ratio of the prescaler

:``u32 pre_vratio``:
    vertical ratio of the prescaler

:``u32 pre_dst_width``:
    the prescaler's destination width

:``u32 pre_dst_height``:
    the prescaler's destination height

:``u32 main_hratio``:
    the main scaler's horizontal ratio

:``u32 main_vratio``:
    the main scaler's vertical ratio

:``u32 real_width``:
    source pixel (width - offset)

:``u32 real_height``:
    source pixel (height - offset)





.. _xref_struct_fimc_addr:

struct fimc_addr
================

.. c:type:: struct fimc_addr

    the FIMC physical address set for DMA



Definition
----------

.. code-block:: c

  struct fimc_addr {
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





.. _xref_struct_fimc_vid_buffer:

struct fimc_vid_buffer
======================

.. c:type:: struct fimc_vid_buffer

    the driver's video buffer



Definition
----------

.. code-block:: c

  struct fimc_vid_buffer {
    struct vb2_v4l2_buffer vb;
    struct list_head list;
    struct fimc_addr paddr;
    int index;
  };



Members
-------

:``struct vb2_v4l2_buffer vb``:
    v4l videobuf buffer

:``struct list_head list``:
    linked list structure for buffer queue

:``struct fimc_addr paddr``:
    precalculated physical address set

:``int index``:
    buffer index for the output DMA engine





.. _xref_struct_fimc_frame:

struct fimc_frame
=================

.. c:type:: struct fimc_frame

    source/target frame properties



Definition
----------

.. code-block:: c

  struct fimc_frame {
    u32 f_width;
    u32 f_height;
    u32 o_width;
    u32 o_height;
    u32 offs_h;
    u32 offs_v;
    u32 width;
    u32 height;
    unsigned int payload[VIDEO_MAX_PLANES];
    unsigned int bytesperline[VIDEO_MAX_PLANES];
    struct fimc_addr paddr;
    struct fimc_dma_offset dma_offset;
    struct fimc_fmt * fmt;
  };



Members
-------

:``u32 f_width``:
    image full width (virtual screen size)

:``u32 f_height``:
    image full height (virtual screen size)

:``u32 o_width``:
    original image width as set by S_FMT

:``u32 o_height``:
    original image height as set by S_FMT

:``u32 offs_h``:
    image horizontal pixel offset

:``u32 offs_v``:
    image vertical pixel offset

:``u32 width``:
    image pixel width

:``u32 height``:
    image pixel weight

:``unsigned int payload[VIDEO_MAX_PLANES]``:
    image size in bytes (w x h x bpp)

:``unsigned int bytesperline[VIDEO_MAX_PLANES]``:
    bytesperline value for each plane

:``struct fimc_addr paddr``:
    image frame buffer physical addresses

:``struct fimc_dma_offset dma_offset``:
    DMA offset in bytes

:``struct fimc_fmt * fmt``:
    fimc color format pointer





.. _xref_struct_fimc_m2m_device:

struct fimc_m2m_device
======================

.. c:type:: struct fimc_m2m_device

    v4l2 memory-to-memory device data



Definition
----------

.. code-block:: c

  struct fimc_m2m_device {
    struct video_device vfd;
    struct v4l2_m2m_dev * m2m_dev;
    struct fimc_ctx * ctx;
    int refcnt;
  };



Members
-------

:``struct video_device vfd``:
    the video device node for v4l2 m2m mode

:``struct v4l2_m2m_dev * m2m_dev``:
    v4l2 memory-to-memory device data

:``struct fimc_ctx * ctx``:
    hardware context data

:``int refcnt``:
    the reference counter





.. _xref_struct_fimc_vid_cap:

struct fimc_vid_cap
===================

.. c:type:: struct fimc_vid_cap

    camera capture device information



Definition
----------

.. code-block:: c

  struct fimc_vid_cap {
    struct fimc_ctx * ctx;
    struct v4l2_subdev subdev;
    struct exynos_video_entity ve;
    struct media_pad vd_pad;
    struct media_pad sd_pads[FIMC_SD_PADS_NUM];
    struct v4l2_mbus_framefmt ci_fmt;
    struct v4l2_mbus_framefmt wb_fmt;
    struct fimc_source_info source_config;
    struct list_head pending_buf_q;
    struct list_head active_buf_q;
    struct vb2_queue vbq;
    int active_buf_cnt;
    int buf_index;
    unsigned int frame_count;
    unsigned int reqbufs_count;
    int input_index;
    u32 input;
    bool user_subdev_api;
    bool inh_sensor_ctrls;
  };



Members
-------

:``struct fimc_ctx * ctx``:
    hardware context data

:``struct v4l2_subdev subdev``:
    subdev exposing the FIMC processing block

:``struct exynos_video_entity ve``:
    exynos video device entity structure

:``struct media_pad vd_pad``:
    fimc video capture node pad

:``struct media_pad sd_pads[FIMC_SD_PADS_NUM]``:
    fimc video processing block pads

:``struct v4l2_mbus_framefmt ci_fmt``:
    image format at the FIMC camera input (and the scaler output)

:``struct v4l2_mbus_framefmt wb_fmt``:
    image format at the FIMC ISP Writeback input

:``struct fimc_source_info source_config``:
    external image source related configuration structure

:``struct list_head pending_buf_q``:
    the pending buffer queue head

:``struct list_head active_buf_q``:
    the queue head of buffers scheduled in hardware

:``struct vb2_queue vbq``:
    the capture am video buffer queue

:``int active_buf_cnt``:
    number of video buffers scheduled in hardware

:``int buf_index``:
    index for managing the output DMA buffers

:``unsigned int frame_count``:
    the frame counter for statistics

:``unsigned int reqbufs_count``:
    the number of buffers requested in REQBUFS ioctl

:``int input_index``:
    input (camera sensor) index

:``u32 input``:
    capture input type, grp_id of the attached subdev

:``bool user_subdev_api``:
    true if subdevs are not configured by the host driver

:``bool inh_sensor_ctrls``:
    a flag indicating v4l2 controls are inherited from
    		      an image sensor subdev





.. _xref_struct_fimc_pix_limit:

struct fimc_pix_limit
=====================

.. c:type:: struct fimc_pix_limit

    image pixel size limits in various IP configurations



Definition
----------

.. code-block:: c

  struct fimc_pix_limit {
    u16 scaler_en_w;
    u16 scaler_dis_w;
    u16 in_rot_en_h;
    u16 in_rot_dis_w;
    u16 out_rot_en_w;
    u16 out_rot_dis_w;
  };



Members
-------

:``u16 scaler_en_w``:
    max input pixel width when the scaler is enabled

:``u16 scaler_dis_w``:
    max input pixel width when the scaler is disabled

:``u16 in_rot_en_h``:
    max input width with the input rotator is on

:``u16 in_rot_dis_w``:
    max input width with the input rotator is off

:``u16 out_rot_en_w``:
    max output width with the output rotator on

:``u16 out_rot_dis_w``:
    max output width with the output rotator off





.. _xref_struct_fimc_variant:

struct fimc_variant
===================

.. c:type:: struct fimc_variant

    FIMC device variant information



Definition
----------

.. code-block:: c

  struct fimc_variant {
    unsigned int has_inp_rot:1;
    unsigned int has_out_rot:1;
    unsigned int has_mainscaler_ext:1;
    unsigned int has_cam_if:1;
    unsigned int has_isp_wb:1;
    const struct fimc_pix_limit * pix_limit;
    u16 min_inp_pixsize;
    u16 min_out_pixsize;
    u16 hor_offs_align;
    u16 min_vsize_align;
  };



Members
-------

:``unsigned int:1 has_inp_rot``:
    set if has input rotator

:``unsigned int:1 has_out_rot``:
    set if has output rotator

:``unsigned int:1 has_mainscaler_ext``:
    1 if extended mainscaler ratios in CIEXTEN register
    			 are present in this IP revision

:``unsigned int:1 has_cam_if``:
    set if this instance has a camera input interface

:``unsigned int:1 has_isp_wb``:
    set if this instance has ISP writeback input

:``const struct fimc_pix_limit * pix_limit``:
    pixel size constraints for the scaler

:``u16 min_inp_pixsize``:
    minimum input pixel size

:``u16 min_out_pixsize``:
    minimum output pixel size

:``u16 hor_offs_align``:
    horizontal pixel offset aligment

:``u16 min_vsize_align``:
    minimum vertical pixel size alignment





.. _xref_struct_fimc_drvdata:

struct fimc_drvdata
===================

.. c:type:: struct fimc_drvdata

    per device type driver data



Definition
----------

.. code-block:: c

  struct fimc_drvdata {
    const struct fimc_variant * variant[FIMC_MAX_DEVS];
    int num_entities;
    unsigned long lclk_frequency;
    u8 cistatus2;
    u8 dma_pix_hoff;
    u8 alpha_color;
    u8 out_buf_count;
  };



Members
-------

:``const struct fimc_variant * variant[FIMC_MAX_DEVS]``:
    variant information for this device

:``int num_entities``:
    number of fimc instances available in a SoC

:``unsigned long lclk_frequency``:
    local bus clock frequency

:``u8 cistatus2``:
    1 if the FIMC IPs have CISTATUS2 register

:``u8 dma_pix_hoff``:
    the horizontal DMA offset unit: 1 - pixels, 0 - bytes

:``u8 alpha_color``:
    1 if alpha color component is supported

:``u8 out_buf_count``:
    maximum number of output DMA buffers supported





.. _xref_struct_fimc_dev:

struct fimc_dev
===============

.. c:type:: struct fimc_dev

    abstraction for FIMC entity



Definition
----------

.. code-block:: c

  struct fimc_dev {
    spinlock_t slock;
    struct mutex lock;
    struct platform_device * pdev;
    struct s5p_platform_fimc * pdata;
    struct regmap * sysreg;
    const struct fimc_variant * variant;
    int id;
    struct clk * clock[MAX_FIMC_CLOCKS];
    void __iomem * regs;
    wait_queue_head_t irq_queue;
    struct v4l2_device * v4l2_dev;
    struct fimc_m2m_device m2m;
    struct fimc_vid_cap vid_cap;
    unsigned long state;
    struct vb2_alloc_ctx * alloc_ctx;
  };



Members
-------

:``spinlock_t slock``:
    the spinlock protecting this data structure

:``struct mutex lock``:
    the mutex protecting this data structure

:``struct platform_device * pdev``:
    pointer to the FIMC platform device

:``struct s5p_platform_fimc * pdata``:
    pointer to the device platform data

:``struct regmap * sysreg``:
    pointer to the SYSREG regmap

:``const struct fimc_variant * variant``:
    the IP variant information

:``int id``:
    FIMC device index (0..FIMC_MAX_DEVS)

:``struct clk * clock[MAX_FIMC_CLOCKS]``:
    clocks required for FIMC operation

:``void __iomem * regs``:
    the mapped hardware registers

:``wait_queue_head_t irq_queue``:
    interrupt handler waitqueue

:``struct v4l2_device * v4l2_dev``:
    root v4l2_device

:``struct fimc_m2m_device m2m``:
    memory-to-memory V4L2 device information

:``struct fimc_vid_cap vid_cap``:
    camera capture device information

:``unsigned long state``:
    flags used to synchronize m2m and capture mode operation

:``struct vb2_alloc_ctx * alloc_ctx``:
    videobuf2 memory allocator context





.. _xref_struct_fimc_ctrls:

struct fimc_ctrls
=================

.. c:type:: struct fimc_ctrls

    v4l2 controls structure



Definition
----------

.. code-block:: c

  struct fimc_ctrls {
    struct v4l2_ctrl_handler handler;
    struct {unnamed_struct};
    struct v4l2_ctrl * rotate;
    struct v4l2_ctrl * hflip;
    struct v4l2_ctrl * vflip;
    struct v4l2_ctrl * alpha;
    bool ready;
  };



Members
-------

:``struct v4l2_ctrl_handler handler``:
    the control handler

:``struct {unnamed_struct}``:
    anonymous

:``struct v4l2_ctrl * rotate``:
    image rotation control

:``struct v4l2_ctrl * hflip``:
    horizontal flip control

:``struct v4l2_ctrl * vflip``:
    vertical flip control

:``struct v4l2_ctrl * alpha``:
    RGB alpha control

:``bool ready``:
    true if **handler** is initialized





.. _xref_fimc_active_queue_add:

fimc_active_queue_add
=====================

.. c:function:: void fimc_active_queue_add (struct fimc_vid_cap * vid_cap, struct fimc_vid_buffer * buf)

    add buffer to the capture active buffers queue

    :param struct fimc_vid_cap * vid_cap:

        _undescribed_

    :param struct fimc_vid_buffer * buf:
        buffer to add to the active buffers list




.. _xref_fimc_active_queue_pop:

fimc_active_queue_pop
=====================

.. c:function:: struct fimc_vid_buffer * fimc_active_queue_pop (struct fimc_vid_cap * vid_cap)

    pop buffer from the capture active buffers queue

    :param struct fimc_vid_cap * vid_cap:

        _undescribed_



Description
-----------



The caller must assure the active_buf_q list is not empty.




.. _xref_fimc_pending_queue_add:

fimc_pending_queue_add
======================

.. c:function:: void fimc_pending_queue_add (struct fimc_vid_cap * vid_cap, struct fimc_vid_buffer * buf)

    add buffer to the capture pending buffers queue

    :param struct fimc_vid_cap * vid_cap:

        _undescribed_

    :param struct fimc_vid_buffer * buf:
        buffer to add to the pending buffers list




.. _xref_fimc_pending_queue_pop:

fimc_pending_queue_pop
======================

.. c:function:: struct fimc_vid_buffer * fimc_pending_queue_pop (struct fimc_vid_cap * vid_cap)

    pop buffer from the capture pending buffers queue

    :param struct fimc_vid_cap * vid_cap:

        _undescribed_



Description
-----------



The caller must assure the pending_buf_q list is not empty.


