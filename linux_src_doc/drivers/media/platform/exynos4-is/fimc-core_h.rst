.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/fimc-core.h

.. _`fimc_dma_offset`:

struct fimc_dma_offset
======================

.. c:type:: struct fimc_dma_offset

    pixel offset information for DMA

.. _`fimc_dma_offset.definition`:

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
    }

.. _`fimc_dma_offset.members`:

Members
-------

y_h
    y value horizontal offset

y_v
    y value vertical offset

cb_h
    cb value horizontal offset

cb_v
    cb value vertical offset

cr_h
    cr value horizontal offset

cr_v
    cr value vertical offset

.. _`fimc_effect`:

struct fimc_effect
==================

.. c:type:: struct fimc_effect

    color effect information

.. _`fimc_effect.definition`:

Definition
----------

.. code-block:: c

    struct fimc_effect {
        u32 type;
        u8 pat_cb;
        u8 pat_cr;
    }

.. _`fimc_effect.members`:

Members
-------

type
    effect type

pat_cb
    cr value when type is "arbitrary"

pat_cr
    cr value when type is "arbitrary"

.. _`fimc_scaler`:

struct fimc_scaler
==================

.. c:type:: struct fimc_scaler

    the configuration data for FIMC inetrnal scaler

.. _`fimc_scaler.definition`:

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
    }

.. _`fimc_scaler.members`:

Members
-------

scaleup_h
    flag indicating scaling up horizontally

scaleup_v
    flag indicating scaling up vertically

copy_mode
    flag indicating transparent DMA transfer (no scaling
    and color format conversion)

enabled
    flag indicating if the scaler is used

hfactor
    horizontal shift factor

vfactor
    vertical shift factor

pre_hratio
    horizontal ratio of the prescaler

pre_vratio
    vertical ratio of the prescaler

pre_dst_width
    the prescaler's destination width

pre_dst_height
    the prescaler's destination height

main_hratio
    the main scaler's horizontal ratio

main_vratio
    the main scaler's vertical ratio

real_width
    source pixel (width - offset)

real_height
    source pixel (height - offset)

.. _`fimc_addr`:

struct fimc_addr
================

.. c:type:: struct fimc_addr

    the FIMC physical address set for DMA

.. _`fimc_addr.definition`:

Definition
----------

.. code-block:: c

    struct fimc_addr {
        u32 y;
        u32 cb;
        u32 cr;
    }

.. _`fimc_addr.members`:

Members
-------

y
    luminance plane physical address

cb
    Cb plane physical address

cr
    Cr plane physical address

.. _`fimc_vid_buffer`:

struct fimc_vid_buffer
======================

.. c:type:: struct fimc_vid_buffer

    the driver's video buffer

.. _`fimc_vid_buffer.definition`:

Definition
----------

.. code-block:: c

    struct fimc_vid_buffer {
        struct vb2_v4l2_buffer vb;
        struct list_head list;
        struct fimc_addr paddr;
        int index;
    }

.. _`fimc_vid_buffer.members`:

Members
-------

vb
    v4l videobuf buffer

list
    linked list structure for buffer queue

paddr
    precalculated physical address set

index
    buffer index for the output DMA engine

.. _`fimc_frame`:

struct fimc_frame
=================

.. c:type:: struct fimc_frame

    source/target frame properties

.. _`fimc_frame.definition`:

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
        struct fimc_fmt *fmt;
        u8 alpha;
    }

.. _`fimc_frame.members`:

Members
-------

f_width
    image full width (virtual screen size)

f_height
    image full height (virtual screen size)

o_width
    original image width as set by S_FMT

o_height
    original image height as set by S_FMT

offs_h
    image horizontal pixel offset

offs_v
    image vertical pixel offset

width
    image pixel width

height
    image pixel weight

payload
    image size in bytes (w x h x bpp)

bytesperline
    bytesperline value for each plane

paddr
    image frame buffer physical addresses

dma_offset
    DMA offset in bytes

fmt
    fimc color format pointer

alpha
    *undescribed*

.. _`fimc_m2m_device`:

struct fimc_m2m_device
======================

.. c:type:: struct fimc_m2m_device

    v4l2 memory-to-memory device data

.. _`fimc_m2m_device.definition`:

Definition
----------

.. code-block:: c

    struct fimc_m2m_device {
        struct video_device vfd;
        struct v4l2_m2m_dev *m2m_dev;
        struct fimc_ctx *ctx;
        int refcnt;
    }

.. _`fimc_m2m_device.members`:

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

.. _`fimc_vid_cap`:

struct fimc_vid_cap
===================

.. c:type:: struct fimc_vid_cap

    camera capture device information

.. _`fimc_vid_cap.definition`:

Definition
----------

.. code-block:: c

    struct fimc_vid_cap {
        struct fimc_ctx *ctx;
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
        bool streaming;
        int input_index;
        u32 input;
        bool user_subdev_api;
        bool inh_sensor_ctrls;
    }

.. _`fimc_vid_cap.members`:

Members
-------

ctx
    hardware context data

subdev
    subdev exposing the FIMC processing block

ve
    exynos video device entity structure

vd_pad
    fimc video capture node pad

sd_pads
    fimc video processing block pads

ci_fmt
    image format at the FIMC camera input (and the scaler output)

wb_fmt
    image format at the FIMC ISP Writeback input

source_config
    external image source related configuration structure

pending_buf_q
    the pending buffer queue head

active_buf_q
    the queue head of buffers scheduled in hardware

vbq
    the capture am video buffer queue

active_buf_cnt
    number of video buffers scheduled in hardware

buf_index
    index for managing the output DMA buffers

frame_count
    the frame counter for statistics

reqbufs_count
    the number of buffers requested in REQBUFS ioctl

streaming
    *undescribed*

input_index
    input (camera sensor) index

input
    capture input type, grp_id of the attached subdev

user_subdev_api
    true if subdevs are not configured by the host driver

inh_sensor_ctrls
    a flag indicating v4l2 controls are inherited from
    an image sensor subdev

.. _`fimc_pix_limit`:

struct fimc_pix_limit
=====================

.. c:type:: struct fimc_pix_limit

    image pixel size limits in various IP configurations

.. _`fimc_pix_limit.definition`:

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
    }

.. _`fimc_pix_limit.members`:

Members
-------

scaler_en_w
    max input pixel width when the scaler is enabled

scaler_dis_w
    max input pixel width when the scaler is disabled

in_rot_en_h
    max input width with the input rotator is on

in_rot_dis_w
    max input width with the input rotator is off

out_rot_en_w
    max output width with the output rotator on

out_rot_dis_w
    max output width with the output rotator off

.. _`fimc_variant`:

struct fimc_variant
===================

.. c:type:: struct fimc_variant

    FIMC device variant information

.. _`fimc_variant.definition`:

Definition
----------

.. code-block:: c

    struct fimc_variant {
        unsigned int has_inp_rot:1;
        unsigned int has_out_rot:1;
        unsigned int has_mainscaler_ext:1;
        unsigned int has_cam_if:1;
        unsigned int has_isp_wb:1;
        const struct fimc_pix_limit *pix_limit;
        u16 min_inp_pixsize;
        u16 min_out_pixsize;
        u16 hor_offs_align;
        u16 min_vsize_align;
    }

.. _`fimc_variant.members`:

Members
-------

has_inp_rot
    set if has input rotator

has_out_rot
    set if has output rotator

has_mainscaler_ext
    1 if extended mainscaler ratios in CIEXTEN register
    are present in this IP revision

has_cam_if
    set if this instance has a camera input interface

has_isp_wb
    set if this instance has ISP writeback input

pix_limit
    pixel size constraints for the scaler

min_inp_pixsize
    minimum input pixel size

min_out_pixsize
    minimum output pixel size

hor_offs_align
    horizontal pixel offset alignment

min_vsize_align
    minimum vertical pixel size alignment

.. _`fimc_drvdata`:

struct fimc_drvdata
===================

.. c:type:: struct fimc_drvdata

    per device type driver data

.. _`fimc_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct fimc_drvdata {
        const struct fimc_variant  *variant[FIMC_MAX_DEVS];
        int num_entities;
        unsigned long lclk_frequency;
        u8 cistatus2;
        u8 dma_pix_hoff;
        u8 alpha_color;
        u8 out_buf_count;
    }

.. _`fimc_drvdata.members`:

Members
-------

variant
    variant information for this device

num_entities
    number of fimc instances available in a SoC

lclk_frequency
    local bus clock frequency

cistatus2
    1 if the FIMC IPs have CISTATUS2 register

dma_pix_hoff
    the horizontal DMA offset unit: 1 - pixels, 0 - bytes

alpha_color
    1 if alpha color component is supported

out_buf_count
    maximum number of output DMA buffers supported

.. _`fimc_dev`:

struct fimc_dev
===============

.. c:type:: struct fimc_dev

    abstraction for FIMC entity

.. _`fimc_dev.definition`:

Definition
----------

.. code-block:: c

    struct fimc_dev {
        spinlock_t slock;
        struct mutex lock;
        struct platform_device *pdev;
        struct s5p_platform_fimc *pdata;
        struct regmap *sysreg;
        const struct fimc_variant *variant;
        const struct fimc_drvdata *drv_data;
        int id;
        struct clk  *clock[MAX_FIMC_CLOCKS];
        void __iomem *regs;
        wait_queue_head_t irq_queue;
        struct v4l2_device *v4l2_dev;
        struct fimc_m2m_device m2m;
        struct fimc_vid_cap vid_cap;
        unsigned long state;
    }

.. _`fimc_dev.members`:

Members
-------

slock
    the spinlock protecting this data structure

lock
    the mutex protecting this data structure

pdev
    pointer to the FIMC platform device

pdata
    pointer to the device platform data

sysreg
    pointer to the SYSREG regmap

variant
    the IP variant information

drv_data
    *undescribed*

id
    FIMC device index (0..FIMC_MAX_DEVS)

clock
    clocks required for FIMC operation

regs
    the mapped hardware registers

irq_queue
    interrupt handler waitqueue

v4l2_dev
    root v4l2_device

m2m
    memory-to-memory V4L2 device information

vid_cap
    camera capture device information

state
    flags used to synchronize m2m and capture mode operation

.. _`fimc_ctrls`:

struct fimc_ctrls
=================

.. c:type:: struct fimc_ctrls

    v4l2 controls structure

.. _`fimc_ctrls.definition`:

Definition
----------

.. code-block:: c

    struct fimc_ctrls {
        struct v4l2_ctrl_handler handler;
        struct {unnamed_struct};
        struct v4l2_ctrl *rotate;
        struct v4l2_ctrl *hflip;
        struct v4l2_ctrl *vflip;
        struct v4l2_ctrl *alpha;
        bool ready;
    }

.. _`fimc_ctrls.members`:

Members
-------

handler
    the control handler

{unnamed_struct}
    anonymous


rotate
    image rotation control

hflip
    horizontal flip control

vflip
    vertical flip control

alpha
    RGB alpha control

ready
    true if \ ``handler``\  is initialized

.. _`fimc_active_queue_add`:

fimc_active_queue_add
=====================

.. c:function:: void fimc_active_queue_add(struct fimc_vid_cap *vid_cap, struct fimc_vid_buffer *buf)

    add buffer to the capture active buffers queue

    :param struct fimc_vid_cap \*vid_cap:
        *undescribed*

    :param struct fimc_vid_buffer \*buf:
        buffer to add to the active buffers list

.. _`fimc_active_queue_pop`:

fimc_active_queue_pop
=====================

.. c:function:: struct fimc_vid_buffer *fimc_active_queue_pop(struct fimc_vid_cap *vid_cap)

    pop buffer from the capture active buffers queue

    :param struct fimc_vid_cap \*vid_cap:
        *undescribed*

.. _`fimc_active_queue_pop.description`:

Description
-----------

The caller must assure the active_buf_q list is not empty.

.. _`fimc_pending_queue_add`:

fimc_pending_queue_add
======================

.. c:function:: void fimc_pending_queue_add(struct fimc_vid_cap *vid_cap, struct fimc_vid_buffer *buf)

    add buffer to the capture pending buffers queue

    :param struct fimc_vid_cap \*vid_cap:
        *undescribed*

    :param struct fimc_vid_buffer \*buf:
        buffer to add to the pending buffers list

.. _`fimc_pending_queue_pop`:

fimc_pending_queue_pop
======================

.. c:function:: struct fimc_vid_buffer *fimc_pending_queue_pop(struct fimc_vid_cap *vid_cap)

    pop buffer from the capture pending buffers queue

    :param struct fimc_vid_cap \*vid_cap:
        *undescribed*

.. _`fimc_pending_queue_pop.description`:

Description
-----------

The caller must assure the pending_buf_q list is not empty.

.. This file was automatic generated / don't edit.

