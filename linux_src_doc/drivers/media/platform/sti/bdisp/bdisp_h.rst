.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/sti/bdisp/bdisp.h

.. _`bdisp_fmt`:

struct bdisp_fmt
================

.. c:type:: struct bdisp_fmt

    driver's internal color format data

.. _`bdisp_fmt.definition`:

Definition
----------

.. code-block:: c

    struct bdisp_fmt {
        u32 pixelformat;
        u8 nb_planes;
        u8 bpp;
        u8 bpp_plane0;
        u8 w_align;
        u8 h_align;
    }

.. _`bdisp_fmt.members`:

Members
-------

pixelformat
    fourcc code for this format

nb_planes
    number of planes  (ex: [0]=RGB/Y - [1]=Cb/Cr, ...)

bpp
    bits per pixel (general)

bpp_plane0
    byte per pixel for the 1st plane

w_align
    width alignment in pixel (multiple of)

h_align
    height alignment in pixel (multiple of)

.. _`bdisp_frame`:

struct bdisp_frame
==================

.. c:type:: struct bdisp_frame

    frame properties

.. _`bdisp_frame.definition`:

Definition
----------

.. code-block:: c

    struct bdisp_frame {
        u32 width;
        u32 height;
        const struct bdisp_fmt *fmt;
        enum v4l2_field field;
        u32 bytesperline;
        u32 sizeimage;
        enum v4l2_colorspace colorspace;
        struct v4l2_rect crop;
        dma_addr_t paddr[4];
    }

.. _`bdisp_frame.members`:

Members
-------

width
    frame width (including padding)

height
    frame height (including padding)

fmt
    pointer to frame format descriptor

field
    frame / field type

bytesperline
    stride of the 1st plane

sizeimage
    image size in bytes

colorspace
    colorspace

crop
    crop area

paddr
    image physical addresses per plane ([0]=RGB/Y - [1]=Cb/Cr, ...)

.. _`bdisp_request`:

struct bdisp_request
====================

.. c:type:: struct bdisp_request

    bdisp request

.. _`bdisp_request.definition`:

Definition
----------

.. code-block:: c

    struct bdisp_request {
        struct bdisp_frame src;
        struct bdisp_frame dst;
        unsigned int hflip:1;
        unsigned int vflip:1;
        int nb_req;
    }

.. _`bdisp_request.members`:

Members
-------

src
    source frame properties

dst
    destination frame properties

hflip
    horizontal flip

vflip
    vertical flip

nb_req
    number of run request

.. _`bdisp_ctx`:

struct bdisp_ctx
================

.. c:type:: struct bdisp_ctx

    device context data

.. _`bdisp_ctx.definition`:

Definition
----------

.. code-block:: c

    struct bdisp_ctx {
        struct bdisp_frame src;
        struct bdisp_frame dst;
        u32 state;
        unsigned int hflip:1;
        unsigned int vflip:1;
        struct bdisp_dev *bdisp_dev;
        struct bdisp_node *node[MAX_NB_NODE];
        dma_addr_t node_paddr[MAX_NB_NODE];
        struct v4l2_fh fh;
        struct v4l2_ctrl_handler ctrl_handler;
        struct bdisp_ctrls bdisp_ctrls;
        bool ctrls_rdy;
    }

.. _`bdisp_ctx.members`:

Members
-------

src
    source frame properties

dst
    destination frame properties

state
    flags to keep track of user configuration

hflip
    horizontal flip

vflip
    vertical flip

bdisp_dev
    the device this context applies to

node
    node array

node_paddr
    node physical address array

fh
    v4l2 file handle

ctrl_handler
    v4l2 controls handler

bdisp_ctrls
    bdisp control set

ctrls_rdy
    true if the control handler is initialized

.. _`bdisp_m2m_device`:

struct bdisp_m2m_device
=======================

.. c:type:: struct bdisp_m2m_device

    v4l2 memory-to-memory device data

.. _`bdisp_m2m_device.definition`:

Definition
----------

.. code-block:: c

    struct bdisp_m2m_device {
        struct video_device *vdev;
        struct v4l2_m2m_dev *m2m_dev;
        struct bdisp_ctx *ctx;
        int refcnt;
    }

.. _`bdisp_m2m_device.members`:

Members
-------

vdev
    video device node for v4l2 m2m mode

m2m_dev
    v4l2 m2m device data

ctx
    hardware context data

refcnt
    reference counter

.. _`bdisp_dbg`:

struct bdisp_dbg
================

.. c:type:: struct bdisp_dbg

    debug info

.. _`bdisp_dbg.definition`:

Definition
----------

.. code-block:: c

    struct bdisp_dbg {
        struct dentry *debugfs_entry;
        struct bdisp_node *copy_node[MAX_NB_NODE];
        struct bdisp_request copy_request;
        ktime_t hw_start;
        s64 last_duration;
        s64 min_duration;
        s64 max_duration;
        s64 tot_duration;
    }

.. _`bdisp_dbg.members`:

Members
-------

debugfs_entry
    debugfs

copy_node
    array of last used nodes

copy_request
    last bdisp request

hw_start
    start time of last HW request

last_duration
    last HW processing duration in microsecs

min_duration
    min HW processing duration in microsecs

max_duration
    max HW processing duration in microsecs

tot_duration
    total HW processing duration in microsecs

.. _`bdisp_dev`:

struct bdisp_dev
================

.. c:type:: struct bdisp_dev

    abstraction for bdisp entity

.. _`bdisp_dev.definition`:

Definition
----------

.. code-block:: c

    struct bdisp_dev {
        struct v4l2_device v4l2_dev;
        struct video_device vdev;
        struct platform_device *pdev;
        struct device *dev;
        spinlock_t slock;
        struct mutex lock;
        u16 id;
        struct bdisp_m2m_device m2m;
        unsigned long state;
        struct clk *clock;
        void __iomem *regs;
        wait_queue_head_t irq_queue;
        struct workqueue_struct *work_queue;
        struct delayed_work timeout_work;
        struct bdisp_dbg dbg;
    }

.. _`bdisp_dev.members`:

Members
-------

v4l2_dev
    v4l2 device

vdev
    video device

pdev
    platform device

dev
    device

slock
    spinlock protecting this data structure

lock
    mutex protecting this data structure

id
    device index

m2m
    memory-to-memory V4L2 device information

state
    flags used to synchronize m2m and capture mode operation

clock
    IP clock

regs
    registers

irq_queue
    interrupt handler waitqueue

work_queue
    workqueue to handle timeouts

timeout_work
    IRQ timeout structure

dbg
    debug info

.. This file was automatic generated / don't edit.

