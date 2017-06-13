.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/mtk-mdp/mtk_mdp_core.h

.. _`mtk_mdp_pix_align`:

struct mtk_mdp_pix_align
========================

.. c:type:: struct mtk_mdp_pix_align

    alignement of image

.. _`mtk_mdp_pix_align.definition`:

Definition
----------

.. code-block:: c

    struct mtk_mdp_pix_align {
        u16 org_w;
        u16 org_h;
        u16 target_w;
        u16 target_h;
    }

.. _`mtk_mdp_pix_align.members`:

Members
-------

org_w
    source alignment of width

org_h
    source alignment of height

target_w
    dst alignment of width

target_h
    dst alignment of height

.. _`mtk_mdp_fmt`:

struct mtk_mdp_fmt
==================

.. c:type:: struct mtk_mdp_fmt

    the driver's internal color format data

.. _`mtk_mdp_fmt.definition`:

Definition
----------

.. code-block:: c

    struct mtk_mdp_fmt {
        u32 pixelformat;
        u16 num_planes;
        u16 num_comp;
        u8 depth;
        u8 row_depth;
        u32 flags;
        struct mtk_mdp_pix_align *align;
    }

.. _`mtk_mdp_fmt.members`:

Members
-------

pixelformat
    the fourcc code for this format, 0 if not applicable

num_planes
    number of physically non-contiguous data planes

num_comp
    number of logical data planes

depth
    per plane driver's private 'number of bits per pixel'

row_depth
    per plane driver's private 'number of bits per pixel per row'

flags
    flags indicating which operation mode format applies to

align
    pointer to a pixel alignment struct, NULL if using default value

.. _`mtk_mdp_addr`:

struct mtk_mdp_addr
===================

.. c:type:: struct mtk_mdp_addr

    the image processor physical address set

.. _`mtk_mdp_addr.definition`:

Definition
----------

.. code-block:: c

    struct mtk_mdp_addr {
        dma_addr_t addr;
    }

.. _`mtk_mdp_addr.members`:

Members
-------

addr
    address of planes

.. _`mtk_mdp_frame`:

struct mtk_mdp_frame
====================

.. c:type:: struct mtk_mdp_frame

    source/target frame properties

.. _`mtk_mdp_frame.definition`:

Definition
----------

.. code-block:: c

    struct mtk_mdp_frame {
        u32 width;
        u32 height;
        struct v4l2_rect crop;
        unsigned long payload;
        unsigned int pitch;
        struct mtk_mdp_addr addr;
        const struct mtk_mdp_fmt *fmt;
        u8 alpha;
    }

.. _`mtk_mdp_frame.members`:

Members
-------

width
    SRC : SRCIMG_WIDTH, DST : OUTPUTDMA_WHOLE_IMG_WIDTH

height
    SRC : SRCIMG_HEIGHT, DST : OUTPUTDMA_WHOLE_IMG_HEIGHT

crop
    cropped(source)/scaled(destination) size

payload
    image size in bytes (w x h x bpp)

pitch
    bytes per line of image in memory

addr
    image frame buffer physical addresses

fmt
    color format pointer

alpha
    frame's alpha value

.. _`mtk_mdp_variant`:

struct mtk_mdp_variant
======================

.. c:type:: struct mtk_mdp_variant

    image processor variant information

.. _`mtk_mdp_variant.definition`:

Definition
----------

.. code-block:: c

    struct mtk_mdp_variant {
        struct mtk_mdp_pix_limit *pix_max;
        struct mtk_mdp_pix_limit *pix_min;
        struct mtk_mdp_pix_align *pix_align;
        u16 h_scale_up_max;
        u16 v_scale_up_max;
        u16 h_scale_down_max;
        u16 v_scale_down_max;
    }

.. _`mtk_mdp_variant.members`:

Members
-------

pix_max
    maximum limit of image size

pix_min
    minimun limit of image size

pix_align
    alignement of image

h_scale_up_max
    maximum scale-up in horizontal

v_scale_up_max
    maximum scale-up in vertical

h_scale_down_max
    maximum scale-down in horizontal

v_scale_down_max
    maximum scale-down in vertical

.. _`mtk_mdp_dev`:

struct mtk_mdp_dev
==================

.. c:type:: struct mtk_mdp_dev

    abstraction for image processor entity

.. _`mtk_mdp_dev.definition`:

Definition
----------

.. code-block:: c

    struct mtk_mdp_dev {
        struct mutex lock;
        struct mutex vpulock;
        struct platform_device *pdev;
        struct mtk_mdp_variant *variant;
        u16 id;
        struct mtk_mdp_comp  *comp;
        struct v4l2_m2m_dev *m2m_dev;
        struct list_head ctx_list;
        struct video_device *vdev;
        struct v4l2_device v4l2_dev;
        struct workqueue_struct *job_wq;
        struct platform_device *vpu_dev;
        int ctx_num;
        unsigned long id_counter;
        struct workqueue_struct *wdt_wq;
        struct work_struct wdt_work;
    }

.. _`mtk_mdp_dev.members`:

Members
-------

lock
    the mutex protecting this data structure

vpulock
    the mutex protecting the communication with VPU

pdev
    pointer to the image processor platform device

variant
    the IP variant information

id
    image processor device index (0..MTK_MDP_MAX_DEVS)

comp
    MDP function components

m2m_dev
    v4l2 memory-to-memory device data

ctx_list
    list of struct mtk_mdp_ctx

vdev
    video device for image processor driver

v4l2_dev
    V4L2 device to register video devices for.

job_wq
    processor work queue

vpu_dev
    VPU platform device

ctx_num
    counter of active MTK MDP context

id_counter
    An integer id given to the next opened context

wdt_wq
    work queue for VPU watchdog

wdt_work
    worker for VPU watchdog

.. This file was automatic generated / don't edit.

