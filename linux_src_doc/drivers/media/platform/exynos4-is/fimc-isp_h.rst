.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/fimc-isp.h

.. _`fimc_isp_frame`:

struct fimc_isp_frame
=====================

.. c:type:: struct fimc_isp_frame

    source/target frame properties

.. _`fimc_isp_frame.definition`:

Definition
----------

.. code-block:: c

    struct fimc_isp_frame {
        u16 width;
        u16 height;
        struct v4l2_rect rect;
    }

.. _`fimc_isp_frame.members`:

Members
-------

width
    full image width

height
    full image height

rect
    crop/composition rectangle

.. _`fimc_is_video`:

struct fimc_is_video
====================

.. c:type:: struct fimc_is_video

    fimc-is video device structure

.. _`fimc_is_video.definition`:

Definition
----------

.. code-block:: c

    struct fimc_is_video {
        struct exynos_video_entity ve;
        enum v4l2_buf_type type;
        struct media_pad pad;
        struct list_head pending_buf_q;
        struct list_head active_buf_q;
        struct vb2_queue vb_queue;
        unsigned int reqbufs_count;
        unsigned int buf_count;
        unsigned int buf_mask;
        unsigned int frame_count;
        int streaming;
        struct isp_video_buf *buffers[FIMC_ISP_MAX_BUFS];
        const struct fimc_fmt *format;
        struct v4l2_pix_format_mplane pixfmt;
    }

.. _`fimc_is_video.members`:

Members
-------

ve
    *undescribed*

type
    video device type (CAPTURE/OUTPUT)

pad
    video device media (sink) pad

pending_buf_q
    pending buffers queue head

active_buf_q
    a queue head of buffers scheduled in hardware

vb_queue
    vb2 buffer queue

reqbufs_count
    number of buffers requested with REQBUFS ioctl

buf_count
    *undescribed*

buf_mask
    *undescribed*

frame_count
    counter of frames dequeued to user space

streaming
    *undescribed*

buffers
    *undescribed*

format
    current pixel format

pixfmt
    *undescribed*

.. _`fimc_isp`:

struct fimc_isp
===============

.. c:type:: struct fimc_isp

    FIMC-IS ISP data structure

.. _`fimc_isp.definition`:

Definition
----------

.. code-block:: c

    struct fimc_isp {
        struct platform_device *pdev;
        struct v4l2_subdev subdev;
        struct media_pad subdev_pads[FIMC_ISP_SD_PADS_NUM];
        struct v4l2_mbus_framefmt src_fmt;
        struct v4l2_mbus_framefmt sink_fmt;
        struct v4l2_ctrl *test_pattern;
        struct fimc_isp_ctrls ctrls;
        struct mutex video_lock;
        struct mutex subdev_lock;
        unsigned int cac_margin_x;
        unsigned int cac_margin_y;
        unsigned long state;
        struct fimc_is_video video_capture;
    }

.. _`fimc_isp.members`:

Members
-------

pdev
    pointer to FIMC-IS platform device

subdev
    ISP v4l2_subdev

subdev_pads
    the ISP subdev media pads

src_fmt
    *undescribed*

sink_fmt
    *undescribed*

test_pattern
    test pattern controls

ctrls
    v4l2 controls structure

video_lock
    mutex serializing video device and the subdev operations

subdev_lock
    *undescribed*

cac_margin_x
    horizontal CAC margin in pixels

cac_margin_y
    vertical CAC margin in pixels

state
    driver state flags

video_capture
    the ISP block video capture device

.. This file was automatic generated / don't edit.

