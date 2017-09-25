.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos-gsc/gsc-core.h

.. _`gsc_datapath`:

enum gsc_datapath
=================

.. c:type:: enum gsc_datapath

    the path of data used for G-Scaler

.. _`gsc_datapath.definition`:

Definition
----------

.. code-block:: c

    enum gsc_datapath {
        GSC_CAMERA,
        GSC_DMA,
        GSC_MIXER,
        GSC_FIMD,
        GSC_WRITEBACK
    };

.. _`gsc_datapath.constants`:

Constants
---------

GSC_CAMERA
    from camera

GSC_DMA
    from/to DMA

GSC_MIXER
    *undescribed*

GSC_FIMD
    *undescribed*

GSC_WRITEBACK
    from FIMD

.. _`gsc_fmt`:

struct gsc_fmt
==============

.. c:type:: struct gsc_fmt

    the driver's internal color format data

.. _`gsc_fmt.definition`:

Definition
----------

.. code-block:: c

    struct gsc_fmt {
        u32 mbus_code;
        char *name;
        u32 pixelformat;
        u32 color;
        u32 yorder;
        u32 corder;
        u16 num_planes;
        u16 num_comp;
        u8 depth[VIDEO_MAX_PLANES];
        u32 flags;
    }

.. _`gsc_fmt.members`:

Members
-------

mbus_code
    Media Bus pixel code, -1 if not applicable

name
    format description

pixelformat
    the fourcc code for this format, 0 if not applicable

color
    *undescribed*

yorder
    Y/C order

corder
    Chrominance order control

num_planes
    number of physically non-contiguous data planes

num_comp
    *undescribed*

depth
    per plane driver's private 'number of bits per pixel'

flags
    flags indicating which operation mode format applies to

.. _`gsc_input_buf`:

struct gsc_input_buf
====================

.. c:type:: struct gsc_input_buf

    the driver's video buffer

.. _`gsc_input_buf.definition`:

Definition
----------

.. code-block:: c

    struct gsc_input_buf {
        struct vb2_v4l2_buffer vb;
        struct list_head list;
        int idx;
    }

.. _`gsc_input_buf.members`:

Members
-------

vb
    videobuf2 buffer

list
    linked list structure for buffer queue

idx
    index of G-Scaler input buffer

.. _`gsc_addr`:

struct gsc_addr
===============

.. c:type:: struct gsc_addr

    the G-Scaler physical address set

.. _`gsc_addr.definition`:

Definition
----------

.. code-block:: c

    struct gsc_addr {
        dma_addr_t y;
        dma_addr_t cb;
        dma_addr_t cr;
    }

.. _`gsc_addr.members`:

Members
-------

y
    luminance plane address

cb
    Cb plane address

cr
    Cr plane address

.. _`gsc_scaler`:

struct gsc_scaler
=================

.. c:type:: struct gsc_scaler

    the configuration data for G-Scaler inetrnal scaler

.. _`gsc_scaler.definition`:

Definition
----------

.. code-block:: c

    struct gsc_scaler {
        u32 pre_shfactor;
        u32 pre_hratio;
        u32 pre_vratio;
        u32 main_hratio;
        u32 main_vratio;
    }

.. _`gsc_scaler.members`:

Members
-------

pre_shfactor
    pre sclaer shift factor

pre_hratio
    horizontal ratio of the prescaler

pre_vratio
    vertical ratio of the prescaler

main_hratio
    the main scaler's horizontal ratio

main_vratio
    the main scaler's vertical ratio

.. _`gsc_frame`:

struct gsc_frame
================

.. c:type:: struct gsc_frame

    source/target frame properties

.. _`gsc_frame.definition`:

Definition
----------

.. code-block:: c

    struct gsc_frame {
        u32 f_width;
        u32 f_height;
        struct v4l2_rect crop;
        unsigned long payload[VIDEO_MAX_PLANES];
        struct gsc_addr addr;
        const struct gsc_fmt *fmt;
        u32 colorspace;
        u8 alpha;
    }

.. _`gsc_frame.members`:

Members
-------

f_width
    SRC : SRCIMG_WIDTH, DST : OUTPUTDMA_WHOLE_IMG_WIDTH

f_height
    SRC : SRCIMG_HEIGHT, DST : OUTPUTDMA_WHOLE_IMG_HEIGHT

crop
    cropped(source)/scaled(destination) size

payload
    image size in bytes (w x h x bpp)

addr
    image frame buffer physical addresses

fmt
    G-Scaler color format pointer

colorspace
    value indicating v4l2_colorspace

alpha
    frame's alpha value

.. _`gsc_m2m_device`:

struct gsc_m2m_device
=====================

.. c:type:: struct gsc_m2m_device

    v4l2 memory-to-memory device data

.. _`gsc_m2m_device.definition`:

Definition
----------

.. code-block:: c

    struct gsc_m2m_device {
        struct video_device *vfd;
        struct v4l2_m2m_dev *m2m_dev;
        struct gsc_ctx *ctx;
        int refcnt;
    }

.. _`gsc_m2m_device.members`:

Members
-------

vfd
    the video device node for v4l2 m2m mode

m2m_dev
    v4l2 memory-to-memory device data

ctx
    hardware context data

refcnt
    the reference counter

.. _`gsc_pix_max`:

struct gsc_pix_max
==================

.. c:type:: struct gsc_pix_max

    image pixel size limits in various IP configurations

.. _`gsc_pix_max.definition`:

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
    }

.. _`gsc_pix_max.members`:

Members
-------

org_scaler_bypass_w
    max pixel width when the scaler is disabled

org_scaler_bypass_h
    max pixel height when the scaler is disabled

org_scaler_input_w
    max pixel width when the scaler is enabled

org_scaler_input_h
    max pixel height when the scaler is enabled

real_rot_dis_w
    max pixel src cropped height with the rotator is off

real_rot_dis_h
    max pixel src croppped width with the rotator is off

real_rot_en_w
    max pixel src cropped width with the rotator is on

real_rot_en_h
    max pixel src cropped height with the rotator is on

target_rot_dis_w
    max pixel dst scaled width with the rotator is off

target_rot_dis_h
    max pixel dst scaled height with the rotator is off

target_rot_en_w
    max pixel dst scaled width with the rotator is on

target_rot_en_h
    max pixel dst scaled height with the rotator is on

.. _`gsc_pix_min`:

struct gsc_pix_min
==================

.. c:type:: struct gsc_pix_min

    image pixel size limits in various IP configurations

.. _`gsc_pix_min.definition`:

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
    }

.. _`gsc_pix_min.members`:

Members
-------

org_w
    minimum source pixel width

org_h
    minimum source pixel height

real_w
    minimum input crop pixel width

real_h
    minimum input crop pixel height

target_rot_dis_w
    minimum output scaled pixel height when rotator is off

target_rot_dis_h
    minimum output scaled pixel height when rotator is off

target_rot_en_w
    minimum output scaled pixel height when rotator is on

target_rot_en_h
    minimum output scaled pixel height when rotator is on

.. _`gsc_variant`:

struct gsc_variant
==================

.. c:type:: struct gsc_variant

    G-Scaler variant information

.. _`gsc_variant.definition`:

Definition
----------

.. code-block:: c

    struct gsc_variant {
        struct gsc_pix_max *pix_max;
        struct gsc_pix_min *pix_min;
        struct gsc_pix_align *pix_align;
        u16 in_buf_cnt;
        u16 out_buf_cnt;
        u16 sc_up_max;
        u16 sc_down_max;
        u16 poly_sc_down_max;
        u16 pre_sc_down_max;
        u16 local_sc_down;
    }

.. _`gsc_variant.members`:

Members
-------

pix_max
    *undescribed*

pix_min
    *undescribed*

pix_align
    *undescribed*

in_buf_cnt
    *undescribed*

out_buf_cnt
    *undescribed*

sc_up_max
    *undescribed*

sc_down_max
    *undescribed*

poly_sc_down_max
    *undescribed*

pre_sc_down_max
    *undescribed*

local_sc_down
    *undescribed*

.. _`gsc_driverdata`:

struct gsc_driverdata
=====================

.. c:type:: struct gsc_driverdata

    per device type driver data for init time.

.. _`gsc_driverdata.definition`:

Definition
----------

.. code-block:: c

    struct gsc_driverdata {
        struct gsc_variant *variant[GSC_MAX_DEVS];
        const char *clk_names[GSC_MAX_CLOCKS];
        int num_clocks;
        int num_entities;
    }

.. _`gsc_driverdata.members`:

Members
-------

variant
    the variant information for this driver.

clk_names
    *undescribed*

num_clocks
    *undescribed*

num_entities
    the number of g-scalers

.. _`gsc_dev`:

struct gsc_dev
==============

.. c:type:: struct gsc_dev

    abstraction for G-Scaler entity

.. _`gsc_dev.definition`:

Definition
----------

.. code-block:: c

    struct gsc_dev {
        spinlock_t slock;
        struct mutex lock;
        struct platform_device *pdev;
        struct gsc_variant *variant;
        u16 id;
        int num_clocks;
        struct clk *clock[GSC_MAX_CLOCKS];
        void __iomem *regs;
        wait_queue_head_t irq_queue;
        struct gsc_m2m_device m2m;
        unsigned long state;
        struct video_device vdev;
        struct v4l2_device v4l2_dev;
    }

.. _`gsc_dev.members`:

Members
-------

slock
    the spinlock protecting this data structure

lock
    the mutex protecting this data structure

pdev
    pointer to the G-Scaler platform device

variant
    the IP variant information

id
    G-Scaler device index (0..GSC_MAX_DEVS)

num_clocks
    *undescribed*

clock
    clocks required for G-Scaler operation

regs
    the mapped hardware registers

irq_queue
    interrupt handler waitqueue

m2m
    memory-to-memory V4L2 device information

state
    flags used to synchronize m2m and capture mode operation

vdev
    video device for G-Scaler instance

v4l2_dev
    *undescribed*

.. This file was automatic generated / don't edit.

