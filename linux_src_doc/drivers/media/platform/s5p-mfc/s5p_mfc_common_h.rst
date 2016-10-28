.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/s5p-mfc/s5p_mfc_common.h

.. _`s5p_mfc_fmt_type`:

enum s5p_mfc_fmt_type
=====================

.. c:type:: enum s5p_mfc_fmt_type

    type of the pixelformat

.. _`s5p_mfc_fmt_type.definition`:

Definition
----------

.. code-block:: c

    enum s5p_mfc_fmt_type {
        MFC_FMT_DEC,
        MFC_FMT_ENC,
        MFC_FMT_RAW
    };

.. _`s5p_mfc_fmt_type.constants`:

Constants
---------

MFC_FMT_DEC
    *undescribed*

MFC_FMT_ENC
    *undescribed*

MFC_FMT_RAW
    *undescribed*

.. _`s5p_mfc_inst_type`:

enum s5p_mfc_inst_type
======================

.. c:type:: enum s5p_mfc_inst_type

    The type of an MFC instance.

.. _`s5p_mfc_inst_type.definition`:

Definition
----------

.. code-block:: c

    enum s5p_mfc_inst_type {
        MFCINST_INVALID,
        MFCINST_DECODER,
        MFCINST_ENCODER
    };

.. _`s5p_mfc_inst_type.constants`:

Constants
---------

MFCINST_INVALID
    *undescribed*

MFCINST_DECODER
    *undescribed*

MFCINST_ENCODER
    *undescribed*

.. _`s5p_mfc_inst_state`:

enum s5p_mfc_inst_state
=======================

.. c:type:: enum s5p_mfc_inst_state

    The state of an MFC instance.

.. _`s5p_mfc_inst_state.definition`:

Definition
----------

.. code-block:: c

    enum s5p_mfc_inst_state {
        MFCINST_FREE,
        MFCINST_INIT,
        MFCINST_GOT_INST,
        MFCINST_HEAD_PARSED,
        MFCINST_HEAD_PRODUCED,
        MFCINST_BUFS_SET,
        MFCINST_RUNNING,
        MFCINST_FINISHING,
        MFCINST_FINISHED,
        MFCINST_RETURN_INST,
        MFCINST_ERROR,
        MFCINST_ABORT,
        MFCINST_FLUSH,
        MFCINST_RES_CHANGE_INIT,
        MFCINST_RES_CHANGE_FLUSH,
        MFCINST_RES_CHANGE_END
    };

.. _`s5p_mfc_inst_state.constants`:

Constants
---------

MFCINST_FREE
    *undescribed*

MFCINST_INIT
    *undescribed*

MFCINST_GOT_INST
    *undescribed*

MFCINST_HEAD_PARSED
    *undescribed*

MFCINST_HEAD_PRODUCED
    *undescribed*

MFCINST_BUFS_SET
    *undescribed*

MFCINST_RUNNING
    *undescribed*

MFCINST_FINISHING
    *undescribed*

MFCINST_FINISHED
    *undescribed*

MFCINST_RETURN_INST
    *undescribed*

MFCINST_ERROR
    *undescribed*

MFCINST_ABORT
    *undescribed*

MFCINST_FLUSH
    *undescribed*

MFCINST_RES_CHANGE_INIT
    *undescribed*

MFCINST_RES_CHANGE_FLUSH
    *undescribed*

MFCINST_RES_CHANGE_END
    *undescribed*

.. _`s5p_mfc_queue_state`:

enum s5p_mfc_queue_state
========================

.. c:type:: enum s5p_mfc_queue_state

    The state of buffer queue.

.. _`s5p_mfc_queue_state.definition`:

Definition
----------

.. code-block:: c

    enum s5p_mfc_queue_state {
        QUEUE_FREE,
        QUEUE_BUFS_REQUESTED,
        QUEUE_BUFS_QUERIED,
        QUEUE_BUFS_MMAPED
    };

.. _`s5p_mfc_queue_state.constants`:

Constants
---------

QUEUE_FREE
    *undescribed*

QUEUE_BUFS_REQUESTED
    *undescribed*

QUEUE_BUFS_QUERIED
    *undescribed*

QUEUE_BUFS_MMAPED
    *undescribed*

.. _`s5p_mfc_decode_arg`:

enum s5p_mfc_decode_arg
=======================

.. c:type:: enum s5p_mfc_decode_arg

    type of frame decoding

.. _`s5p_mfc_decode_arg.definition`:

Definition
----------

.. code-block:: c

    enum s5p_mfc_decode_arg {
        MFC_DEC_FRAME,
        MFC_DEC_LAST_FRAME,
        MFC_DEC_RES_CHANGE
    };

.. _`s5p_mfc_decode_arg.constants`:

Constants
---------

MFC_DEC_FRAME
    *undescribed*

MFC_DEC_LAST_FRAME
    *undescribed*

MFC_DEC_RES_CHANGE
    *undescribed*

.. _`s5p_mfc_buf`:

struct s5p_mfc_buf
==================

.. c:type:: struct s5p_mfc_buf

    MFC buffer

.. _`s5p_mfc_buf.definition`:

Definition
----------

.. code-block:: c

    struct s5p_mfc_buf {
        struct vb2_v4l2_buffer *b;
        struct list_head list;
        union cookie;
        int flags;
    }

.. _`s5p_mfc_buf.members`:

Members
-------

b
    *undescribed*

list
    *undescribed*

cookie
    *undescribed*

flags
    *undescribed*

.. _`s5p_mfc_pm`:

struct s5p_mfc_pm
=================

.. c:type:: struct s5p_mfc_pm

    power management data structure

.. _`s5p_mfc_pm.definition`:

Definition
----------

.. code-block:: c

    struct s5p_mfc_pm {
        struct clk *clock;
        struct clk *clock_gate;
        atomic_t power;
        struct device *device;
    }

.. _`s5p_mfc_pm.members`:

Members
-------

clock
    *undescribed*

clock_gate
    *undescribed*

power
    *undescribed*

device
    *undescribed*

.. _`s5p_mfc_priv_buf`:

struct s5p_mfc_priv_buf
=======================

.. c:type:: struct s5p_mfc_priv_buf

    represents internal used buffer

.. _`s5p_mfc_priv_buf.definition`:

Definition
----------

.. code-block:: c

    struct s5p_mfc_priv_buf {
        unsigned long ofs;
        void *virt;
        dma_addr_t dma;
        size_t size;
    }

.. _`s5p_mfc_priv_buf.members`:

Members
-------

ofs
    offset of each buffer, will be used for MFC

virt
    kernel virtual address, only valid when the
    buffer accessed by driver

dma
    DMA address, only valid when kernel DMA API used

size
    size of the buffer

.. _`s5p_mfc_dev`:

struct s5p_mfc_dev
==================

.. c:type:: struct s5p_mfc_dev

    The struct containing driver internal parameters.

.. _`s5p_mfc_dev.definition`:

Definition
----------

.. code-block:: c

    struct s5p_mfc_dev {
        struct v4l2_device v4l2_dev;
        struct video_device *vfd_dec;
        struct video_device *vfd_enc;
        struct platform_device *plat_dev;
        struct device *mem_dev_l;
        struct device *mem_dev_r;
        void __iomem *regs_base;
        int irq;
        struct v4l2_ctrl_handler dec_ctrl_handler;
        struct v4l2_ctrl_handler enc_ctrl_handler;
        struct s5p_mfc_pm pm;
        struct s5p_mfc_variant *variant;
        int num_inst;
        spinlock_t irqlock;
        spinlock_t condlock;
        struct mutex mfc_mutex;
        int int_cond;
        int int_type;
        unsigned int int_err;
        wait_queue_head_t queue;
        size_t fw_size;
        void *fw_virt_addr;
        dma_addr_t bank1;
        dma_addr_t bank2;
        unsigned long hw_lock;
        struct s5p_mfc_ctx  *ctx[MFC_NUM_CONTEXTS];
        int curr_ctx;
        unsigned long ctx_work_bits;
        atomic_t watchdog_cnt;
        struct timer_list watchdog_timer;
        struct workqueue_struct *watchdog_workqueue;
        struct work_struct watchdog_work;
        void  *alloc_ctx[2];
        unsigned long enter_suspend;
        struct s5p_mfc_priv_buf ctx_buf;
        int warn_start;
        struct s5p_mfc_hw_ops *mfc_ops;
        struct s5p_mfc_hw_cmds *mfc_cmds;
        const struct s5p_mfc_regs *mfc_regs;
        enum s5p_mfc_fw_ver fw_ver;
        bool risc_on;
    }

.. _`s5p_mfc_dev.members`:

Members
-------

v4l2_dev
    v4l2_device

vfd_dec
    video device for decoding

vfd_enc
    video device for encoding

plat_dev
    platform device

mem_dev_l
    child device of the left memory bank (0)

mem_dev_r
    child device of the right memory bank (1)

regs_base
    base address of the MFC hw registers

irq
    irq resource

dec_ctrl_handler
    control framework handler for decoding

enc_ctrl_handler
    control framework handler for encoding

pm
    power management control

variant
    MFC hardware variant information

num_inst
    couter of active MFC instances

irqlock
    lock for operations on videobuf2 queues

condlock
    lock for changing/checking if a context is ready to be
    processed

mfc_mutex
    lock for video_device

int_cond
    variable used by the waitqueue

int_type
    type of last interrupt

int_err
    error number for last interrupt

queue
    waitqueue for waiting for completion of device commands

fw_size
    size of firmware

fw_virt_addr
    virtual firmware address

bank1
    address of the beginning of bank 1 memory

bank2
    address of the beginning of bank 2 memory

hw_lock
    used for hardware locking

ctx
    array of driver contexts

curr_ctx
    number of the currently running context

ctx_work_bits
    used to mark which contexts are waiting for hardware

watchdog_cnt
    counter for the watchdog

watchdog_timer
    *undescribed*

watchdog_workqueue
    workqueue for the watchdog

watchdog_work
    worker for the watchdog

alloc_ctx
    videobuf2 allocator contexts for two memory banks

enter_suspend
    flag set when entering suspend

ctx_buf
    common context memory (MFCv6)

warn_start
    hardware error code from which warnings start

mfc_ops
    ops structure holding HW operation function pointers

mfc_cmds
    cmd structure holding HW commands function pointers

mfc_regs
    *undescribed*

fw_ver
    loaded firmware sub-version

risc_on
    *undescribed*

.. _`s5p_mfc_h264_enc_params`:

struct s5p_mfc_h264_enc_params
==============================

.. c:type:: struct s5p_mfc_h264_enc_params

    encoding parameters for h264

.. _`s5p_mfc_h264_enc_params.definition`:

Definition
----------

.. code-block:: c

    struct s5p_mfc_h264_enc_params {
        enum v4l2_mpeg_video_h264_profile profile;
        enum v4l2_mpeg_video_h264_loop_filter_mode loop_filter_mode;
        s8 loop_filter_alpha;
        s8 loop_filter_beta;
        enum v4l2_mpeg_video_h264_entropy_mode entropy_mode;
        u8 max_ref_pic;
        u8 num_ref_pic_4p;
        int _8x8_transform;
        int rc_mb_dark;
        int rc_mb_smooth;
        int rc_mb_static;
        int rc_mb_activity;
        int vui_sar;
        u8 vui_sar_idc;
        u16 vui_ext_sar_width;
        u16 vui_ext_sar_height;
        int open_gop;
        u16 open_gop_size;
        u8 rc_frame_qp;
        u8 rc_min_qp;
        u8 rc_max_qp;
        u8 rc_p_frame_qp;
        u8 rc_b_frame_qp;
        enum v4l2_mpeg_video_h264_level level_v4l2;
        int level;
        u16 cpb_size;
        int interlace;
        u8 hier_qp;
        u8 hier_qp_type;
        u8 hier_qp_layer;
        u8 hier_qp_layer_qp[7];
        u8 sei_frame_packing;
        u8 sei_fp_curr_frame_0;
        u8 sei_fp_arrangement_type;
        u8 fmo;
        u8 fmo_map_type;
        u8 fmo_slice_grp;
        u8 fmo_chg_dir;
        u32 fmo_chg_rate;
        u32 fmo_run_len[4];
        u8 aso;
        u32 aso_slice_order[8];
    }

.. _`s5p_mfc_h264_enc_params.members`:

Members
-------

profile
    *undescribed*

loop_filter_mode
    *undescribed*

loop_filter_alpha
    *undescribed*

loop_filter_beta
    *undescribed*

entropy_mode
    *undescribed*

max_ref_pic
    *undescribed*

num_ref_pic_4p
    *undescribed*

_8x8_transform
    *undescribed*

rc_mb_dark
    *undescribed*

rc_mb_smooth
    *undescribed*

rc_mb_static
    *undescribed*

rc_mb_activity
    *undescribed*

vui_sar
    *undescribed*

vui_sar_idc
    *undescribed*

vui_ext_sar_width
    *undescribed*

vui_ext_sar_height
    *undescribed*

open_gop
    *undescribed*

open_gop_size
    *undescribed*

rc_frame_qp
    *undescribed*

rc_min_qp
    *undescribed*

rc_max_qp
    *undescribed*

rc_p_frame_qp
    *undescribed*

rc_b_frame_qp
    *undescribed*

level_v4l2
    *undescribed*

level
    *undescribed*

cpb_size
    *undescribed*

interlace
    *undescribed*

hier_qp
    *undescribed*

hier_qp_type
    *undescribed*

hier_qp_layer
    *undescribed*

sei_frame_packing
    *undescribed*

sei_fp_curr_frame_0
    *undescribed*

sei_fp_arrangement_type
    *undescribed*

fmo
    *undescribed*

fmo_map_type
    *undescribed*

fmo_slice_grp
    *undescribed*

fmo_chg_dir
    *undescribed*

fmo_chg_rate
    *undescribed*

aso
    *undescribed*

.. _`s5p_mfc_mpeg4_enc_params`:

struct s5p_mfc_mpeg4_enc_params
===============================

.. c:type:: struct s5p_mfc_mpeg4_enc_params

    encoding parameters for h263 and mpeg4

.. _`s5p_mfc_mpeg4_enc_params.definition`:

Definition
----------

.. code-block:: c

    struct s5p_mfc_mpeg4_enc_params {
        enum v4l2_mpeg_video_mpeg4_profile profile;
        int quarter_pixel;
        u16 vop_time_res;
        u16 vop_frm_delta;
        u8 rc_frame_qp;
        u8 rc_min_qp;
        u8 rc_max_qp;
        u8 rc_p_frame_qp;
        u8 rc_b_frame_qp;
        enum v4l2_mpeg_video_mpeg4_level level_v4l2;
        int level;
    }

.. _`s5p_mfc_mpeg4_enc_params.members`:

Members
-------

profile
    *undescribed*

quarter_pixel
    *undescribed*

vop_time_res
    *undescribed*

vop_frm_delta
    *undescribed*

rc_frame_qp
    *undescribed*

rc_min_qp
    *undescribed*

rc_max_qp
    *undescribed*

rc_p_frame_qp
    *undescribed*

rc_b_frame_qp
    *undescribed*

level_v4l2
    *undescribed*

level
    *undescribed*

.. _`s5p_mfc_vp8_enc_params`:

struct s5p_mfc_vp8_enc_params
=============================

.. c:type:: struct s5p_mfc_vp8_enc_params

    encoding parameters for vp8

.. _`s5p_mfc_vp8_enc_params.definition`:

Definition
----------

.. code-block:: c

    struct s5p_mfc_vp8_enc_params {
        u8 imd_4x4;
        enum v4l2_vp8_num_partitions num_partitions;
        enum v4l2_vp8_num_ref_frames num_ref;
        u8 filter_level;
        u8 filter_sharpness;
        u32 golden_frame_ref_period;
        enum v4l2_vp8_golden_frame_sel golden_frame_sel;
        u8 hier_layer;
        u8 hier_layer_qp[3];
        u8 rc_min_qp;
        u8 rc_max_qp;
        u8 rc_frame_qp;
        u8 rc_p_frame_qp;
        u8 profile;
    }

.. _`s5p_mfc_vp8_enc_params.members`:

Members
-------

imd_4x4
    *undescribed*

num_partitions
    *undescribed*

num_ref
    *undescribed*

filter_level
    *undescribed*

filter_sharpness
    *undescribed*

golden_frame_ref_period
    *undescribed*

golden_frame_sel
    *undescribed*

hier_layer
    *undescribed*

rc_min_qp
    *undescribed*

rc_max_qp
    *undescribed*

rc_frame_qp
    *undescribed*

rc_p_frame_qp
    *undescribed*

profile
    *undescribed*

.. _`s5p_mfc_enc_params`:

struct s5p_mfc_enc_params
=========================

.. c:type:: struct s5p_mfc_enc_params

    general encoding parameters

.. _`s5p_mfc_enc_params.definition`:

Definition
----------

.. code-block:: c

    struct s5p_mfc_enc_params {
        u16 width;
        u16 height;
        u32 mv_h_range;
        u32 mv_v_range;
        u16 gop_size;
        enum v4l2_mpeg_video_multi_slice_mode slice_mode;
        u16 slice_mb;
        u32 slice_bit;
        u16 intra_refresh_mb;
        int pad;
        u8 pad_luma;
        u8 pad_cb;
        u8 pad_cr;
        int rc_frame;
        int rc_mb;
        u32 rc_bitrate;
        u16 rc_reaction_coeff;
        u16 vbv_size;
        u32 vbv_delay;
        enum v4l2_mpeg_video_header_mode seq_hdr_mode;
        enum v4l2_mpeg_mfc51_video_frame_skip_mode frame_skip_mode;
        int fixed_target_bit;
        u8 num_b_frame;
        u32 rc_framerate_num;
        u32 rc_framerate_denom;
        struct codec;
    }

.. _`s5p_mfc_enc_params.members`:

Members
-------

width
    *undescribed*

height
    *undescribed*

mv_h_range
    *undescribed*

mv_v_range
    *undescribed*

gop_size
    *undescribed*

slice_mode
    *undescribed*

slice_mb
    *undescribed*

slice_bit
    *undescribed*

intra_refresh_mb
    *undescribed*

pad
    *undescribed*

pad_luma
    *undescribed*

pad_cb
    *undescribed*

pad_cr
    *undescribed*

rc_frame
    *undescribed*

rc_mb
    *undescribed*

rc_bitrate
    *undescribed*

rc_reaction_coeff
    *undescribed*

vbv_size
    *undescribed*

vbv_delay
    *undescribed*

seq_hdr_mode
    *undescribed*

frame_skip_mode
    *undescribed*

fixed_target_bit
    *undescribed*

num_b_frame
    *undescribed*

rc_framerate_num
    *undescribed*

rc_framerate_denom
    *undescribed*

codec
    *undescribed*

.. _`s5p_mfc_codec_ops`:

struct s5p_mfc_codec_ops
========================

.. c:type:: struct s5p_mfc_codec_ops

    codec ops, used by encoding

.. _`s5p_mfc_codec_ops.definition`:

Definition
----------

.. code-block:: c

    struct s5p_mfc_codec_ops {
        int (*pre_seq_start)(struct s5p_mfc_ctx *ctx);
        int (*post_seq_start)(struct s5p_mfc_ctx *ctx);
        int (*pre_frame_start)(struct s5p_mfc_ctx *ctx);
        int (*post_frame_start)(struct s5p_mfc_ctx *ctx);
    }

.. _`s5p_mfc_codec_ops.members`:

Members
-------

pre_seq_start
    *undescribed*

post_seq_start
    *undescribed*

pre_frame_start
    *undescribed*

post_frame_start
    *undescribed*

.. _`s5p_mfc_ctx`:

struct s5p_mfc_ctx
==================

.. c:type:: struct s5p_mfc_ctx

    This struct contains the instance context

.. _`s5p_mfc_ctx.definition`:

Definition
----------

.. code-block:: c

    struct s5p_mfc_ctx {
        struct s5p_mfc_dev *dev;
        struct v4l2_fh fh;
        int num;
        int int_cond;
        int int_type;
        unsigned int int_err;
        wait_queue_head_t queue;
        struct s5p_mfc_fmt *src_fmt;
        struct s5p_mfc_fmt *dst_fmt;
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
        int src_bufs_cnt;
        struct s5p_mfc_buf dst_bufs[MFC_MAX_BUFFERS];
        int dst_bufs_cnt;
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
        int pb_count;
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
        enum v4l2_mpeg_mfc51_video_force_frame_type force_frame_type;
        struct list_head ref_queue;
        unsigned int ref_queue_cnt;
        enum v4l2_mpeg_video_multi_slice_mode slice_mode;
        union slice_size;
        const struct s5p_mfc_codec_ops *c_ops;
        struct v4l2_ctrl  *ctrls[MFC_MAX_CTRLS];
        struct v4l2_ctrl_handler ctrl_handler;
        unsigned int frame_tag;
        size_t scratch_buf_size;
    }

.. _`s5p_mfc_ctx.members`:

Members
-------

dev
    pointer to the s5p_mfc_dev of the device

fh
    struct v4l2_fh

num
    number of the context that this structure describes

int_cond
    variable used by the waitqueue

int_type
    type of the last interrupt

int_err
    error number received from MFC hw in the interrupt

queue
    waitqueue that can be used to wait for this context to
    finish

src_fmt
    source pixelformat information

dst_fmt
    destination pixelformat information

vq_src
    vb2 queue for source buffers

vq_dst
    vb2 queue for destination buffers

src_queue
    driver internal queue for source buffers

dst_queue
    driver internal queue for destination buffers

src_queue_cnt
    number of buffers queued on the source internal queue

dst_queue_cnt
    number of buffers queued on the dest internal queue

type
    type of the instance - decoder or encoder

state
    state of the context

inst_no
    number of hw instance associated with the context

img_width
    width of the image that is decoded or encoded

img_height
    height of the image that is decoded or encoded

buf_width
    width of the buffer for processed image

buf_height
    height of the buffer for processed image

luma_size
    size of a luma plane

chroma_size
    size of a chroma plane

mv_size
    size of a motion vectors buffer

consumed_stream
    number of bytes that have been used so far from the
    decoding buffer

dpb_flush_flag
    flag used to indicate that a DPB buffers are being
    flushed

head_processed
    flag mentioning whether the header data is processed
    completely or not

bank1
    handle to memory allocated for temporary buffers from
    memory bank 1

bank2
    handle to memory allocated for temporary buffers from
    memory bank 2

capture_state
    state of the capture buffers queue

output_state
    state of the output buffers queue

src_bufs
    information on allocated source buffers

src_bufs_cnt
    *undescribed*

dst_bufs
    information on allocated destination buffers

dst_bufs_cnt
    *undescribed*

sequence
    counter for the sequence number for v4l2

dec_dst_flag
    flags for buffers queued in the hardware

dec_src_buf_size
    size of the buffer for source buffers in decoding

codec_mode
    number of codec mode used by MFC hw

slice_interface
    slice interface flag

loop_filter_mpeg4
    loop filter for MPEG4 flag

display_delay
    value of the display delay for H264

display_delay_enable
    display delay for H264 enable flag

after_packed_pb
    flag used to track buffer when stream is in
    Packed PB format

sei_fp_parse
    enable/disable parsing of frame packing SEI information

pb_count
    *undescribed*

total_dpb_count
    count of DPB buffers with additional buffers
    requested by the application

mv_count
    number of MV buffers allocated for decoding

ctx
    context buffer information

dsc
    descriptor buffer information

shm
    shared memory buffer information

enc_params
    encoding parameters for MFC

enc_dst_buf_size
    size of the buffers for encoder output

luma_dpb_size
    dpb buffer size for luma

chroma_dpb_size
    dpb buffer size for chroma

me_buffer_size
    size of the motion estimation buffer

tmv_buffer_size
    size of temporal predictor motion vector buffer

force_frame_type
    *undescribed*

ref_queue
    list of the reference buffers for encoding

ref_queue_cnt
    number of the buffers in the reference list

slice_mode
    *undescribed*

slice_size
    *undescribed*

c_ops
    ops for encoding

ctrls
    array of controls, used when adding controls to the
    v4l2 control framework

ctrl_handler
    handler for v4l2 framework

frame_tag
    *undescribed*

scratch_buf_size
    *undescribed*

.. _`mfc_control`:

struct mfc_control
==================

.. c:type:: struct mfc_control

    structure used to store information about MFC controls it is used to initialize the control framework.

.. _`mfc_control.definition`:

Definition
----------

.. code-block:: c

    struct mfc_control {
        __u32 id;
        enum v4l2_ctrl_type type;
        __u8 name[32];
        __s32 minimum;
        __s32 maximum;
        __s32 step;
        __u32 menu_skip_mask;
        __s32 default_value;
        __u32 flags;
        __u32 reserved[2];
        __u8 is_volatile;
    }

.. _`mfc_control.members`:

Members
-------

id
    *undescribed*

type
    *undescribed*

minimum
    *undescribed*

maximum
    *undescribed*

step
    *undescribed*

menu_skip_mask
    *undescribed*

default_value
    *undescribed*

flags
    *undescribed*

is_volatile
    *undescribed*

.. This file was automatic generated / don't edit.

