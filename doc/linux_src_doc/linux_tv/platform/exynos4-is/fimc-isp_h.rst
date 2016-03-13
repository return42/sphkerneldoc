.. -*- coding: utf-8; mode: rst -*-

==========
fimc-isp.h
==========



.. _xref_struct_fimc_isp_frame:

struct fimc_isp_frame
=====================

.. c:type:: struct fimc_isp_frame

    source/target frame properties



Definition
----------

.. code-block:: c

  struct fimc_isp_frame {
    u16 width;
    u16 height;
    struct v4l2_rect rect;
  };



Members
-------

:``u16 width``:
    full image width

:``u16 height``:
    full image height

:``struct v4l2_rect rect``:
    crop/composition rectangle





.. _xref_struct_fimc_is_video:

struct fimc_is_video
====================

.. c:type:: struct fimc_is_video

    fimc-is video device structure



Definition
----------

.. code-block:: c

  struct fimc_is_video {
    enum v4l2_buf_type type;
    struct media_pad pad;
    struct list_head pending_buf_q;
    struct list_head active_buf_q;
    struct vb2_queue vb_queue;
    unsigned int reqbufs_count;
    unsigned int frame_count;
    const struct fimc_fmt * format;
  };



Members
-------

:``enum v4l2_buf_type type``:
    video device type (CAPTURE/OUTPUT)

:``struct media_pad pad``:
    video device media (sink) pad

:``struct list_head pending_buf_q``:
    pending buffers queue head

:``struct list_head active_buf_q``:
    a queue head of buffers scheduled in hardware

:``struct vb2_queue vb_queue``:
    vb2 buffer queue

:``unsigned int reqbufs_count``:
    number of buffers requested with REQBUFS ioctl

:``unsigned int frame_count``:
    counter of frames dequeued to user space

:``const struct fimc_fmt * format``:
    current pixel format





.. _xref_struct_fimc_isp:

struct fimc_isp
===============

.. c:type:: struct fimc_isp

    FIMC-IS ISP data structure



Definition
----------

.. code-block:: c

  struct fimc_isp {
    struct platform_device * pdev;
    struct vb2_alloc_ctx * alloc_ctx;
    struct v4l2_subdev subdev;
    struct media_pad subdev_pads[FIMC_ISP_SD_PADS_NUM];
    struct v4l2_ctrl * test_pattern;
    struct fimc_isp_ctrls ctrls;
    struct mutex video_lock;
    unsigned int cac_margin_x;
    unsigned int cac_margin_y;
    unsigned long state;
    struct fimc_is_video video_capture;
  };



Members
-------

:``struct platform_device * pdev``:
    pointer to FIMC-IS platform device

:``struct vb2_alloc_ctx * alloc_ctx``:
    videobuf2 memory allocator context

:``struct v4l2_subdev subdev``:
    ISP v4l2_subdev

:``struct media_pad subdev_pads[FIMC_ISP_SD_PADS_NUM]``:
    the ISP subdev media pads

:``struct v4l2_ctrl * test_pattern``:
    test pattern controls

:``struct fimc_isp_ctrls ctrls``:
    v4l2 controls structure

:``struct mutex video_lock``:
    mutex serializing video device and the subdev operations

:``unsigned int cac_margin_x``:
    horizontal CAC margin in pixels

:``unsigned int cac_margin_y``:
    vertical CAC margin in pixels

:``unsigned long state``:
    driver state flags

:``struct fimc_is_video video_capture``:
    the ISP block video capture device



