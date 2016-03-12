.. -*- coding: utf-8; mode: rst -*-

=======
bdisp.h
=======



.. _xref_struct_bdisp_fmt:

struct bdisp_fmt
================

.. c:type:: struct bdisp_fmt

    driver's internal color format data



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
  };



Members
-------

:``u32 pixelformat``:
    fourcc code for this format

:``u8 nb_planes``:
    number of planes  (ex: [0]=RGB/Y - [1]=Cb/Cr, ...)

:``u8 bpp``:
    bits per pixel (general)

:``u8 bpp_plane0``:
    byte per pixel for the 1st plane

:``u8 w_align``:
    width alignment in pixel (multiple of)

:``u8 h_align``:
    height alignment in pixel (multiple of)





.. _xref_struct_bdisp_frame:

struct bdisp_frame
==================

.. c:type:: struct bdisp_frame

    frame properties



Definition
----------

.. code-block:: c

  struct bdisp_frame {
    u32 width;
    u32 height;
    const struct bdisp_fmt * fmt;
    enum v4l2_field field;
    u32 bytesperline;
    u32 sizeimage;
    enum v4l2_colorspace colorspace;
    struct v4l2_rect crop;
    dma_addr_t paddr[4];
  };



Members
-------

:``u32 width``:
    frame width (including padding)

:``u32 height``:
    frame height (including padding)

:``const struct bdisp_fmt * fmt``:
    pointer to frame format descriptor

:``enum v4l2_field field``:
    frame / field type

:``u32 bytesperline``:
    stride of the 1st plane

:``u32 sizeimage``:
    image size in bytes

:``enum v4l2_colorspace colorspace``:
    colorspace

:``struct v4l2_rect crop``:
    crop area

:``dma_addr_t paddr[4]``:
    image physical addresses per plane ([0]=RGB/Y - [1]=Cb/Cr, ...)





.. _xref_struct_bdisp_request:

struct bdisp_request
====================

.. c:type:: struct bdisp_request

    bdisp request



Definition
----------

.. code-block:: c

  struct bdisp_request {
    struct bdisp_frame src;
    struct bdisp_frame dst;
    unsigned int hflip:1;
    unsigned int vflip:1;
    int nb_req;
  };



Members
-------

:``struct bdisp_frame src``:
    source frame properties

:``struct bdisp_frame dst``:
    destination frame properties

:``unsigned int:1 hflip``:
    horizontal flip

:``unsigned int:1 vflip``:
    vertical flip

:``int nb_req``:
    number of run request





.. _xref_struct_bdisp_ctx:

struct bdisp_ctx
================

.. c:type:: struct bdisp_ctx

    device context data



Definition
----------

.. code-block:: c

  struct bdisp_ctx {
    struct bdisp_frame src;
    struct bdisp_frame dst;
    u32 state;
    unsigned int hflip:1;
    unsigned int vflip:1;
    struct bdisp_dev * bdisp_dev;
    struct bdisp_node * node[MAX_NB_NODE];
    dma_addr_t node_paddr[MAX_NB_NODE];
    struct v4l2_fh fh;
    struct v4l2_ctrl_handler ctrl_handler;
    struct bdisp_ctrls bdisp_ctrls;
    bool ctrls_rdy;
  };



Members
-------

:``struct bdisp_frame src``:
    source frame properties

:``struct bdisp_frame dst``:
    destination frame properties

:``u32 state``:
    flags to keep track of user configuration

:``unsigned int:1 hflip``:
    horizontal flip

:``unsigned int:1 vflip``:
    vertical flip

:``struct bdisp_dev * bdisp_dev``:
    the device this context applies to

:``struct bdisp_node * node[MAX_NB_NODE]``:
    node array

:``dma_addr_t node_paddr[MAX_NB_NODE]``:
    node physical address array

:``struct v4l2_fh fh``:
    v4l2 file handle

:``struct v4l2_ctrl_handler ctrl_handler``:
    v4l2 controls handler

:``struct bdisp_ctrls bdisp_ctrls``:
    bdisp control set

:``bool ctrls_rdy``:
    true if the control handler is initialized





.. _xref_struct_bdisp_m2m_device:

struct bdisp_m2m_device
=======================

.. c:type:: struct bdisp_m2m_device

    v4l2 memory-to-memory device data



Definition
----------

.. code-block:: c

  struct bdisp_m2m_device {
    struct video_device * vdev;
    struct v4l2_m2m_dev * m2m_dev;
    struct bdisp_ctx * ctx;
    int refcnt;
  };



Members
-------

:``struct video_device * vdev``:
    video device node for v4l2 m2m mode

:``struct v4l2_m2m_dev * m2m_dev``:
    v4l2 m2m device data

:``struct bdisp_ctx * ctx``:
    hardware context data

:``int refcnt``:
    reference counter





.. _xref_struct_bdisp_dbg:

struct bdisp_dbg
================

.. c:type:: struct bdisp_dbg

    debug info



Definition
----------

.. code-block:: c

  struct bdisp_dbg {
    struct dentry * debugfs_entry;
    struct bdisp_node * copy_node[MAX_NB_NODE];
    struct bdisp_request copy_request;
    ktime_t hw_start;
    s64 last_duration;
    s64 min_duration;
    s64 max_duration;
    s64 tot_duration;
  };



Members
-------

:``struct dentry * debugfs_entry``:
    debugfs

:``struct bdisp_node * copy_node[MAX_NB_NODE]``:
    array of last used nodes

:``struct bdisp_request copy_request``:
    last bdisp request

:``ktime_t hw_start``:
    start time of last HW request

:``s64 last_duration``:
    last HW processing duration in microsecs

:``s64 min_duration``:
    min HW processing duration in microsecs

:``s64 max_duration``:
    max HW processing duration in microsecs

:``s64 tot_duration``:
    total HW processing duration in microsecs





.. _xref_struct_bdisp_dev:

struct bdisp_dev
================

.. c:type:: struct bdisp_dev

    abstraction for bdisp entity



Definition
----------

.. code-block:: c

  struct bdisp_dev {
    struct v4l2_device v4l2_dev;
    struct video_device vdev;
    struct platform_device * pdev;
    struct device * dev;
    spinlock_t slock;
    struct mutex lock;
    u16 id;
    struct bdisp_m2m_device m2m;
    unsigned long state;
    struct vb2_alloc_ctx * alloc_ctx;
    struct clk * clock;
    void __iomem * regs;
    wait_queue_head_t irq_queue;
    struct workqueue_struct * work_queue;
    struct delayed_work timeout_work;
    struct bdisp_dbg dbg;
  };



Members
-------

:``struct v4l2_device v4l2_dev``:
    v4l2 device

:``struct video_device vdev``:
    video device

:``struct platform_device * pdev``:
    platform device

:``struct device * dev``:
    device

:``spinlock_t slock``:
    spinlock protecting this data structure

:``struct mutex lock``:
    mutex protecting this data structure

:``u16 id``:
    device index

:``struct bdisp_m2m_device m2m``:
    memory-to-memory V4L2 device information

:``unsigned long state``:
    flags used to synchronize m2m and capture mode operation

:``struct vb2_alloc_ctx * alloc_ctx``:
    videobuf2 memory allocator context

:``struct clk * clock``:
    IP clock

:``void __iomem * regs``:
    registers

:``wait_queue_head_t irq_queue``:
    interrupt handler waitqueue

:``struct workqueue_struct * work_queue``:
    workqueue to handle timeouts

:``struct delayed_work timeout_work``:
    IRQ timeout structure

:``struct bdisp_dbg dbg``:
    debug info



