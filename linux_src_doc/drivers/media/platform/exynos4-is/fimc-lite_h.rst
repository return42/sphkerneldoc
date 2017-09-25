.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/fimc-lite.h

.. _`flite_drvdata`:

struct flite_drvdata
====================

.. c:type:: struct flite_drvdata

    FIMC-LITE IP variant data structure

.. _`flite_drvdata.definition`:

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
    }

.. _`flite_drvdata.members`:

Members
-------

max_width
    maximum camera interface input width in pixels

max_height
    maximum camera interface input height in pixels

out_width_align
    minimum output width alignment in pixels

win_hor_offs_align
    minimum camera interface crop window horizontal
    offset alignment in pixels

out_hor_offs_align
    minimum output DMA compose rectangle horizontal
    offset alignment in pixels

max_dma_bufs
    number of output DMA buffer start address registers

num_instances
    total number of FIMC-LITE IP instances available

.. _`flite_frame`:

struct flite_frame
==================

.. c:type:: struct flite_frame

    source/target frame properties

.. _`flite_frame.definition`:

Definition
----------

.. code-block:: c

    struct flite_frame {
        u16 f_width;
        u16 f_height;
        struct v4l2_rect rect;
        const struct fimc_fmt *fmt;
    }

.. _`flite_frame.members`:

Members
-------

f_width
    full pixel width

f_height
    full pixel height

rect
    crop/composition rectangle

fmt
    pointer to pixel format description data structure

.. _`flite_buffer`:

struct flite_buffer
===================

.. c:type:: struct flite_buffer

    video buffer structure

.. _`flite_buffer.definition`:

Definition
----------

.. code-block:: c

    struct flite_buffer {
        struct vb2_v4l2_buffer vb;
        struct list_head list;
        dma_addr_t paddr;
        unsigned short index;
    }

.. _`flite_buffer.members`:

Members
-------

vb
    vb2 buffer

list
    list head for the buffers queue

paddr
    DMA buffer start address

index
    DMA start address register's index

.. _`fimc_lite`:

struct fimc_lite
================

.. c:type:: struct fimc_lite

    fimc lite structure

.. _`fimc_lite.definition`:

Definition
----------

.. code-block:: c

    struct fimc_lite {
        struct platform_device *pdev;
        struct flite_drvdata *dd;
        struct exynos_video_entity ve;
        struct v4l2_device *v4l2_dev;
        struct v4l2_fh fh;
        struct v4l2_subdev subdev;
        struct media_pad vd_pad;
        struct media_pad subdev_pads[FLITE_SD_PADS_NUM];
        struct v4l2_subdev *sensor;
        struct v4l2_ctrl_handler ctrl_handler;
        struct v4l2_ctrl *test_pattern;
        int index;
        struct mutex lock;
        spinlock_t slock;
        struct clk *clock;
        void __iomem *regs;
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
        struct fimc_lite_events events;
        bool streaming;
    }

.. _`fimc_lite.members`:

Members
-------

pdev
    pointer to FIMC-LITE platform device

dd
    SoC specific driver data structure

ve
    exynos video device entity structure

v4l2_dev
    pointer to top the level v4l2_device

fh
    v4l2 file handle

subdev
    FIMC-LITE subdev

vd_pad
    media (sink) pad for the capture video node

subdev_pads
    the subdev media pads

sensor
    sensor subdev attached to FIMC-LITE directly or through MIPI-CSIS

ctrl_handler
    v4l2 control handler

test_pattern
    test pattern controls

index
    FIMC-LITE platform device index

lock
    mutex serializing video device and the subdev operations

slock
    spinlock protecting this data structure and the hw registers

clock
    FIMC-LITE gate clock

regs
    memory mapped io registers

irq_queue
    interrupt handler waitqueue

payload
    image size in bytes (w x h x bpp)

inp_frame
    camera input frame structure

out_frame
    DMA output frame structure

out_path
    output data path (DMA or FIFO)

source_subdev_grp_id
    source subdev group id

state
    driver state flags

pending_buf_q
    pending buffers queue head

active_buf_q
    the queue head of buffers scheduled in hardware

vb_queue
    vb2 buffers queue

buf_index
    helps to keep track of the DMA start address register index

frame_count
    the captured frames counter

reqbufs_count
    the number of buffers requested with REQBUFS ioctl

events
    *undescribed*

streaming
    *undescribed*

.. This file was automatic generated / don't edit.

