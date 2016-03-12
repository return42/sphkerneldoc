.. -*- coding: utf-8; mode: rst -*-

================
s5p_mfc_common.h
================



.. _xref_enum s5p_mfc_fmt_type:

enum s5p_mfc_fmt_type
=====================

.. c:type:: enum s5p_mfc_fmt_type

    type of the pixelformat



Constants
---------

:``MFC_FMT_DEC``:
    -- undescribed --

:``MFC_FMT_ENC``:
    -- undescribed --

:``MFC_FMT_RAW``:
    -- undescribed --




.. _xref_enum s5p_mfc_inst_type:

enum s5p_mfc_inst_type
======================

.. c:type:: enum s5p_mfc_inst_type

    The type of an MFC instance.



Constants
---------

:``MFCINST_INVALID``:
    -- undescribed --

:``MFCINST_DECODER``:
    -- undescribed --

:``MFCINST_ENCODER``:
    -- undescribed --




.. _xref_enum s5p_mfc_inst_state:

enum s5p_mfc_inst_state
=======================

.. c:type:: enum s5p_mfc_inst_state

    The state of an MFC instance.



Constants
---------

:``MFCINST_FREE``:
    -- undescribed --

:``MFCINST_INIT``:
    -- undescribed --

:``MFCINST_GOT_INST``:
    -- undescribed --

:``MFCINST_HEAD_PARSED``:
    -- undescribed --

:``MFCINST_HEAD_PRODUCED``:
    -- undescribed --

:``MFCINST_BUFS_SET``:
    -- undescribed --

:``MFCINST_RUNNING``:
    -- undescribed --

:``MFCINST_FINISHING``:
    -- undescribed --

:``MFCINST_FINISHED``:
    -- undescribed --

:``MFCINST_RETURN_INST``:
    -- undescribed --

:``MFCINST_ERROR``:
    -- undescribed --

:``MFCINST_ABORT``:
    -- undescribed --

:``MFCINST_FLUSH``:
    -- undescribed --

:``MFCINST_RES_CHANGE_INIT``:
    -- undescribed --

:``MFCINST_RES_CHANGE_FLUSH``:
    -- undescribed --

:``MFCINST_RES_CHANGE_END``:
    -- undescribed --




.. _xref_enum s5p_mfc_queue_state:

enum s5p_mfc_queue_state
========================

.. c:type:: enum s5p_mfc_queue_state

    The state of buffer queue.



Constants
---------

:``QUEUE_FREE``:
    -- undescribed --

:``QUEUE_BUFS_REQUESTED``:
    -- undescribed --

:``QUEUE_BUFS_QUERIED``:
    -- undescribed --

:``QUEUE_BUFS_MMAPED``:
    -- undescribed --




.. _xref_enum s5p_mfc_decode_arg:

enum s5p_mfc_decode_arg
=======================

.. c:type:: enum s5p_mfc_decode_arg

    type of frame decoding



Constants
---------

:``MFC_DEC_FRAME``:
    -- undescribed --

:``MFC_DEC_LAST_FRAME``:
    -- undescribed --

:``MFC_DEC_RES_CHANGE``:
    -- undescribed --




.. _xref_struct_s5p_mfc_buf:

struct s5p_mfc_buf
==================

.. c:type:: struct s5p_mfc_buf

    MFC buffer



Definition
----------

.. code-block:: c

  struct s5p_mfc_buf {
  };



Members
-------





.. _xref_struct_s5p_mfc_pm:

struct s5p_mfc_pm
=================

.. c:type:: struct s5p_mfc_pm

    power management data structure



Definition
----------

.. code-block:: c

  struct s5p_mfc_pm {
  };



Members
-------





.. _xref_struct_s5p_mfc_priv_buf:

struct s5p_mfc_priv_buf
=======================

.. c:type:: struct s5p_mfc_priv_buf

    represents internal used buffer



Definition
----------

.. code-block:: c

  struct s5p_mfc_priv_buf {
    unsigned long ofs;
    void * virt;
    dma_addr_t dma;
    size_t size;
  };



Members
-------

:``unsigned long ofs``:
    offset of each buffer, will be used for MFC

:``void * virt``:
    kernel virtual address, only valid when the
    			buffer accessed by driver

:``dma_addr_t dma``:
    DMA address, only valid when kernel DMA API used

:``size_t size``:
    size of the buffer





.. _xref_struct_s5p_mfc_dev:

struct s5p_mfc_dev
==================

.. c:type:: struct s5p_mfc_dev

    The struct containing driver internal parameters.



Definition
----------

.. code-block:: c

  struct s5p_mfc_dev {
    struct v4l2_device v4l2_dev;
    struct video_device * vfd_dec;
    struct video_device * vfd_enc;
    struct platform_device * plat_dev;
    struct device * mem_dev_l;
    struct device * mem_dev_r;
    void __iomem * regs_base;
    int irq;
    struct v4l2_ctrl_handler dec_ctrl_handler;
    struct v4l2_ctrl_handler enc_ctrl_handler;
    struct s5p_mfc_pm pm;
    struct s5p_mfc_variant * variant;
    int num_inst;
    spinlock_t irqlock;
    spinlock_t condlock;
    struct mutex mfc_mutex;
    int int_cond;
    int int_type;
    unsigned int int_err;
    wait_queue_head_t queue;
    size_t fw_size;
    void * fw_virt_addr;
    dma_addr_t bank1;
    dma_addr_t bank2;
    unsigned long hw_lock;
    struct s5p_mfc_ctx * ctx[MFC_NUM_CONTEXTS];
    int curr_ctx;
    unsigned long ctx_work_bits;
    atomic_t watchdog_cnt;
    struct workqueue_struct * watchdog_workqueue;
    struct work_struct watchdog_work;
    void * alloc_ctx[2];
    unsigned long enter_suspend;
    struct s5p_mfc_priv_buf ctx_buf;
    int warn_start;
    struct s5p_mfc_hw_ops * mfc_ops;
    struct s5p_mfc_hw_cmds * mfc_cmds;
    enum s5p_mfc_fw_ver fw_ver;
  };



Members
-------

:``struct v4l2_device v4l2_dev``:
    v4l2_device

:``struct video_device * vfd_dec``:
    video device for decoding

:``struct video_device * vfd_enc``:
    video device for encoding

:``struct platform_device * plat_dev``:
    platform device

:``struct device * mem_dev_l``:
    child device of the left memory bank (0)

:``struct device * mem_dev_r``:
    child device of the right memory bank (1)

:``void __iomem * regs_base``:
    base address of the MFC hw registers

:``int irq``:
    irq resource

:``struct v4l2_ctrl_handler dec_ctrl_handler``:
    control framework handler for decoding

:``struct v4l2_ctrl_handler enc_ctrl_handler``:
    control framework handler for encoding

:``struct s5p_mfc_pm pm``:
    power management control

:``struct s5p_mfc_variant * variant``:
    MFC hardware variant information

:``int num_inst``:
    couter of active MFC instances

:``spinlock_t irqlock``:
    lock for operations on videobuf2 queues

:``spinlock_t condlock``:
    lock for changing/checking if a context is ready to be
    			processed

:``struct mutex mfc_mutex``:
    lock for video_device

:``int int_cond``:
    variable used by the waitqueue

:``int int_type``:
    type of last interrupt

:``unsigned int int_err``:
    error number for last interrupt

:``wait_queue_head_t queue``:
    waitqueue for waiting for completion of device commands

:``size_t fw_size``:
    size of firmware

:``void * fw_virt_addr``:
    virtual firmware address

:``dma_addr_t bank1``:
    address of the beginning of bank 1 memory

:``dma_addr_t bank2``:
    address of the beginning of bank 2 memory

:``unsigned long hw_lock``:
    used for hardware locking

:``struct s5p_mfc_ctx * ctx[MFC_NUM_CONTEXTS]``:
    array of driver contexts

:``int curr_ctx``:
    number of the currently running context

:``unsigned long ctx_work_bits``:
    used to mark which contexts are waiting for hardware

:``atomic_t watchdog_cnt``:
    counter for the watchdog

:``struct workqueue_struct * watchdog_workqueue``:
    workqueue for the watchdog

:``struct work_struct watchdog_work``:
    worker for the watchdog

:``void * alloc_ctx[2]``:
    videobuf2 allocator contexts for two memory banks

:``unsigned long enter_suspend``:
    flag set when entering suspend

:``struct s5p_mfc_priv_buf ctx_buf``:
    common context memory (MFCv6)

:``int warn_start``:
    hardware error code from which warnings start

:``struct s5p_mfc_hw_ops * mfc_ops``:
    ops structure holding HW operation function pointers

:``struct s5p_mfc_hw_cmds * mfc_cmds``:
    cmd structure holding HW commands function pointers

:``enum s5p_mfc_fw_ver fw_ver``:
    loaded firmware sub-version





.. _xref_struct_s5p_mfc_h264_enc_params:

struct s5p_mfc_h264_enc_params
==============================

.. c:type:: struct s5p_mfc_h264_enc_params

    encoding parameters for h264



Definition
----------

.. code-block:: c

  struct s5p_mfc_h264_enc_params {
  };



Members
-------





.. _xref_struct_s5p_mfc_mpeg4_enc_params:

struct s5p_mfc_mpeg4_enc_params
===============================

.. c:type:: struct s5p_mfc_mpeg4_enc_params

    encoding parameters for h263 and mpeg4



Definition
----------

.. code-block:: c

  struct s5p_mfc_mpeg4_enc_params {
  };



Members
-------





.. _xref_struct_s5p_mfc_vp8_enc_params:

struct s5p_mfc_vp8_enc_params
=============================

.. c:type:: struct s5p_mfc_vp8_enc_params

    encoding parameters for vp8



Definition
----------

.. code-block:: c

  struct s5p_mfc_vp8_enc_params {
  };



Members
-------





.. _xref_struct_s5p_mfc_enc_params:

struct s5p_mfc_enc_params
=========================

.. c:type:: struct s5p_mfc_enc_params

    general encoding parameters



Definition
----------

.. code-block:: c

  struct s5p_mfc_enc_params {
  };



Members
-------





.. _xref_struct_s5p_mfc_codec_ops:

struct s5p_mfc_codec_ops
========================

.. c:type:: struct s5p_mfc_codec_ops

    codec ops, used by encoding



Definition
----------

.. code-block:: c

  struct s5p_mfc_codec_ops {
  };



Members
-------





.. _xref_struct_s5p_mfc_ctx:

struct s5p_mfc_ctx
==================

.. c:type:: struct s5p_mfc_ctx

    This struct contains the instance context



Definition
----------

.. code-block:: c

  struct s5p_mfc_ctx {
    struct s5p_mfc_dev * dev;
    struct v4l2_fh fh;
    int num;
    int int_cond;
    int int_type;
    unsigned int int_err;
    wait_queue_head_t queue;
    struct s5p_mfc_fmt * src_fmt;
    struct s5p_mfc_fmt * dst_fmt;
    struct vb2_queue vq_src;
    struct vb2_queue vq_dst;
    struct list_head src_queue;
    struct list_head dst_queue;
    unsigned int src_queue_cnt;
    unsigned int dst_queue_cnt;
    enum s5p_mfc_inst_type type;
    enum s5p_mfc_inst_state state;
    int inst_no;
    int img_width;
    int img_height;
    int buf_width;
    int buf_height;
    int luma_size;
    int chroma_size;
    int mv_size;
    unsigned long consumed_stream;
    unsigned int dpb_flush_flag;
    unsigned int head_processed;
    struct s5p_mfc_priv_buf bank1;
    struct s5p_mfc_priv_buf bank2;
    enum s5p_mfc_queue_state capture_state;
    enum s5p_mfc_queue_state output_state;
    struct s5p_mfc_buf src_bufs[MFC_MAX_BUFFERS];
    struct s5p_mfc_buf dst_bufs[MFC_MAX_BUFFERS];
    unsigned int sequence;
    unsigned long dec_dst_flag;
    size_t dec_src_buf_size;
    int codec_mode;
    int slice_interface;
    int loop_filter_mpeg4;
    int display_delay;
    int display_delay_enable;
    int after_packed_pb;
    int sei_fp_parse;
    int total_dpb_count;
    int mv_count;
    struct s5p_mfc_priv_buf ctx;
    struct s5p_mfc_priv_buf dsc;
    struct s5p_mfc_priv_buf shm;
    struct s5p_mfc_enc_params enc_params;
    size_t enc_dst_buf_size;
    size_t luma_dpb_size;
    size_t chroma_dpb_size;
    size_t me_buffer_size;
    size_t tmv_buffer_size;
    struct list_head ref_queue;
    unsigned int ref_queue_cnt;
    const struct s5p_mfc_codec_ops * c_ops;
    struct v4l2_ctrl * ctrls[MFC_MAX_CTRLS];
    struct v4l2_ctrl_handler ctrl_handler;
  };



Members
-------

:``struct s5p_mfc_dev * dev``:
    pointer to the s5p_mfc_dev of the device

:``struct v4l2_fh fh``:
    struct v4l2_fh

:``int num``:
    number of the context that this structure describes

:``int int_cond``:
    variable used by the waitqueue

:``int int_type``:
    type of the last interrupt

:``unsigned int int_err``:
    error number received from MFC hw in the interrupt

:``wait_queue_head_t queue``:
    waitqueue that can be used to wait for this context to
    			finish

:``struct s5p_mfc_fmt * src_fmt``:
    source pixelformat information

:``struct s5p_mfc_fmt * dst_fmt``:
    destination pixelformat information

:``struct vb2_queue vq_src``:
    vb2 queue for source buffers

:``struct vb2_queue vq_dst``:
    vb2 queue for destination buffers

:``struct list_head src_queue``:
    driver internal queue for source buffers

:``struct list_head dst_queue``:
    driver internal queue for destination buffers

:``unsigned int src_queue_cnt``:
    number of buffers queued on the source internal queue

:``unsigned int dst_queue_cnt``:
    number of buffers queued on the dest internal queue

:``enum s5p_mfc_inst_type type``:
    type of the instance - decoder or encoder

:``enum s5p_mfc_inst_state state``:
    state of the context

:``int inst_no``:
    number of hw instance associated with the context

:``int img_width``:
    width of the image that is decoded or encoded

:``int img_height``:
    height of the image that is decoded or encoded

:``int buf_width``:
    width of the buffer for processed image

:``int buf_height``:
    height of the buffer for processed image

:``int luma_size``:
    size of a luma plane

:``int chroma_size``:
    size of a chroma plane

:``int mv_size``:
    size of a motion vectors buffer

:``unsigned long consumed_stream``:
    number of bytes that have been used so far from the
    			decoding buffer

:``unsigned int dpb_flush_flag``:
    flag used to indicate that a DPB buffers are being
    			flushed

:``unsigned int head_processed``:
    flag mentioning whether the header data is processed
    			completely or not

:``struct s5p_mfc_priv_buf bank1``:
    handle to memory allocated for temporary buffers from
    			memory bank 1

:``struct s5p_mfc_priv_buf bank2``:
    handle to memory allocated for temporary buffers from
    			memory bank 2

:``enum s5p_mfc_queue_state capture_state``:
    state of the capture buffers queue

:``enum s5p_mfc_queue_state output_state``:
    state of the output buffers queue

:``struct s5p_mfc_buf src_bufs[MFC_MAX_BUFFERS]``:
    information on allocated source buffers

:``struct s5p_mfc_buf dst_bufs[MFC_MAX_BUFFERS]``:
    information on allocated destination buffers

:``unsigned int sequence``:
    counter for the sequence number for v4l2

:``unsigned long dec_dst_flag``:
    flags for buffers queued in the hardware

:``size_t dec_src_buf_size``:
    size of the buffer for source buffers in decoding

:``int codec_mode``:
    number of codec mode used by MFC hw

:``int slice_interface``:
    slice interface flag

:``int loop_filter_mpeg4``:
    loop filter for MPEG4 flag

:``int display_delay``:
    value of the display delay for H264

:``int display_delay_enable``:
    display delay for H264 enable flag

:``int after_packed_pb``:
    flag used to track buffer when stream is in
    			Packed PB format

:``int sei_fp_parse``:
    enable/disable parsing of frame packing SEI information

:``int total_dpb_count``:
    count of DPB buffers with additional buffers
    			requested by the application

:``int mv_count``:
    number of MV buffers allocated for decoding

:``struct s5p_mfc_priv_buf ctx``:
    context buffer information

:``struct s5p_mfc_priv_buf dsc``:
    descriptor buffer information

:``struct s5p_mfc_priv_buf shm``:
    shared memory buffer information

:``struct s5p_mfc_enc_params enc_params``:
    encoding parameters for MFC

:``size_t enc_dst_buf_size``:
    size of the buffers for encoder output

:``size_t luma_dpb_size``:
    dpb buffer size for luma

:``size_t chroma_dpb_size``:
    dpb buffer size for chroma

:``size_t me_buffer_size``:
    size of the motion estimation buffer

:``size_t tmv_buffer_size``:
    size of temporal predictor motion vector buffer

:``struct list_head ref_queue``:
    list of the reference buffers for encoding

:``unsigned int ref_queue_cnt``:
    number of the buffers in the reference list

:``const struct s5p_mfc_codec_ops * c_ops``:
    ops for encoding

:``struct v4l2_ctrl * ctrls[MFC_MAX_CTRLS]``:
    array of controls, used when adding controls to the
    			v4l2 control framework

:``struct v4l2_ctrl_handler ctrl_handler``:
    handler for v4l2 framework





.. _xref_struct_mfc_control:

struct mfc_control
==================

.. c:type:: struct mfc_control

    structure used to store information about MFC controls it is used to initialize the control framework.



Definition
----------

.. code-block:: c

  struct mfc_control {
  };



Members
-------



