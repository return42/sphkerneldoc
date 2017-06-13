.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-jpeg/mtk_jpeg_core.h

.. _`mtk_jpeg_dev`:

struct mtk_jpeg_dev
===================

.. c:type:: struct mtk_jpeg_dev

    JPEG IP abstraction

.. _`mtk_jpeg_dev.definition`:

Definition
----------

.. code-block:: c

    struct mtk_jpeg_dev {
        struct mutex lock;
        spinlock_t hw_lock;
        struct workqueue_struct *workqueue;
        struct device *dev;
        struct v4l2_device v4l2_dev;
        struct v4l2_m2m_dev *m2m_dev;
        void *alloc_ctx;
        struct video_device *dec_vdev;
        void __iomem *dec_reg_base;
        struct clk *clk_jdec;
        struct clk *clk_jdec_smi;
        struct device *larb;
    }

.. _`mtk_jpeg_dev.members`:

Members
-------

lock
    the mutex protecting this structure

hw_lock
    spinlock protecting the hw device resource

workqueue
    decode work queue

dev
    JPEG device

v4l2_dev
    v4l2 device for mem2mem mode

m2m_dev
    v4l2 mem2mem device data

alloc_ctx
    videobuf2 memory allocator's context

dec_vdev
    video device node for decoder mem2mem mode

dec_reg_base
    JPEG registers mapping

clk_jdec
    JPEG hw working clock

clk_jdec_smi
    JPEG SMI bus clock

larb
    SMI device

.. _`mtk_jpeg_fmt`:

struct mtk_jpeg_fmt
===================

.. c:type:: struct mtk_jpeg_fmt

    driver's internal color format data

.. _`mtk_jpeg_fmt.definition`:

Definition
----------

.. code-block:: c

    struct mtk_jpeg_fmt {
        u32 fourcc;
        int h_sample[VIDEO_MAX_PLANES];
        int v_sample[VIDEO_MAX_PLANES];
        int colplanes;
        int h_align;
        int v_align;
        u32 flags;
    }

.. _`mtk_jpeg_fmt.members`:

Members
-------

fourcc
    the fourcc code, 0 if not applicable

h_sample
    horizontal sample count of plane in 4 \* 4 pixel image

v_sample
    vertical sample count of plane in 4 \* 4 pixel image

colplanes
    number of color planes (1 for packed formats)

h_align
    horizontal alignment order (align to 2^h_align)

v_align
    vertical alignment order (align to 2^v_align)

flags
    flags describing format applicability

.. This file was automatic generated / don't edit.

