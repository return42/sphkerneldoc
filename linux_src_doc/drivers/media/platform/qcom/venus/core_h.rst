.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/qcom/venus/core.h

.. _`venus_core`:

struct venus_core
=================

.. c:type:: struct venus_core

    holds core parameters valid for all instances

.. _`venus_core.definition`:

Definition
----------

.. code-block:: c

    struct venus_core {
        void __iomem *base;
        int irq;
        struct clk *clks[VIDC_CLKS_NUM_MAX];
        struct clk *core0_clk;
        struct clk *core1_clk;
        struct clk *core0_bus_clk;
        struct clk *core1_bus_clk;
        struct video_device *vdev_dec;
        struct video_device *vdev_enc;
        struct v4l2_device v4l2_dev;
        const struct venus_resources *res;
        struct device *dev;
        struct device *dev_dec;
        struct device *dev_enc;
        struct mutex lock;
        struct list_head instances;
        atomic_t insts_count;
        unsigned int state;
        struct completion done;
        unsigned int error;
        bool sys_error;
        const struct hfi_core_ops *core_ops;
        unsigned long enc_codecs;
        unsigned long dec_codecs;
        unsigned int max_sessions_supported;
    #define ENC_ROTATION_CAPABILITY 0x1
    #define ENC_SCALING_CAPABILITY 0x2
    #define ENC_DEINTERLACE_CAPABILITY 0x4
    #define DEC_MULTI_STREAM_CAPABILITY 0x8
        unsigned int core_caps;
        void *priv;
        const struct hfi_ops *ops;
        struct delayed_work work;
        struct venus_caps caps[MAX_CODEC_NUM];
        unsigned int codecs_count;
    }

.. _`venus_core.members`:

Members
-------

base
    IO memory base address

irq
    Venus irq

clks
    an array of struct clk pointers

core0_clk
    a struct clk pointer for core0

core1_clk
    a struct clk pointer for core1

core0_bus_clk
    a struct clk pointer for core0 bus clock

core1_bus_clk
    a struct clk pointer for core1 bus clock

vdev_dec
    a reference to video device structure for decoder instances

vdev_enc
    a reference to video device structure for encoder instances

v4l2_dev
    a holder for v4l2 device structure

res
    a reference to venus resources structure

dev
    convenience struct device pointer

dev_dec
    convenience struct device pointer for decoder device

dev_enc
    convenience struct device pointer for encoder device

lock
    a lock for this strucure

instances
    a list_head of all instances

insts_count
    num of instances

state
    the state of the venus core

done
    a completion for sync HFI operations

error
    an error returned during last HFI sync operations

sys_error
    an error flag that signal system error event

core_ops
    the core operations

enc_codecs
    encoders supported by this core

dec_codecs
    decoders supported by this core

max_sessions_supported
    holds the maximum number of sessions

core_caps
    core capabilities

priv
    a private filed for HFI operations

ops
    the core HFI operations

work
    a delayed work for handling system fatal error

caps
    *undescribed*

codecs_count
    *undescribed*

.. _`venus_inst`:

struct venus_inst
=================

.. c:type:: struct venus_inst

    holds per instance paramerters

.. _`venus_inst.definition`:

Definition
----------

.. code-block:: c

    struct venus_inst {
        struct list_head list;
        struct mutex lock;
        struct venus_core *core;
        struct list_head dpbbufs;
        struct list_head internalbufs;
        struct list_head registeredbufs;
        struct list_head delayed_process;
        struct work_struct delayed_process_work;
        struct v4l2_ctrl_handler ctrl_handler;
        union {
            struct vdec_controls dec;
            struct venc_controls enc;
        } controls;
        struct v4l2_fh fh;
        unsigned int streamon_cap, streamon_out;
        u32 width;
        u32 height;
        u32 out_width;
        u32 out_height;
        u32 colorspace;
        u8 ycbcr_enc;
        u8 quantization;
        u8 xfer_func;
        u64 fps;
        struct v4l2_fract timeperframe;
        const struct venus_format *fmt_out;
        const struct venus_format *fmt_cap;
        unsigned int num_input_bufs;
        unsigned int num_output_bufs;
        unsigned int input_buf_size;
        unsigned int output_buf_size;
        unsigned int output2_buf_size;
        u32 dpb_buftype;
        u32 dpb_fmt;
        u32 opb_buftype;
        u32 opb_fmt;
        bool reconfig;
        u32 reconfig_width;
        u32 reconfig_height;
        u32 hfi_codec;
        u32 sequence_cap;
        u32 sequence_out;
        struct v4l2_m2m_dev *m2m_dev;
        struct v4l2_m2m_ctx *m2m_ctx;
        unsigned int state;
        struct completion done;
        unsigned int error;
        bool session_error;
        const struct hfi_inst_ops *ops;
        u32 session_type;
        union hfi_get_property hprop;
    }

.. _`venus_inst.members`:

Members
-------

list
    used for attach an instance to the core

lock
    instance lock

core
    a reference to the core struct

dpbbufs
    a list of decoded picture buffers

internalbufs
    a list of internal bufferes

registeredbufs
    a list of registered capture bufferes
    \ ``delayed_process``\      a list of delayed buffers

delayed_process
    *undescribed*

delayed_process_work
    a work_struct for process delayed buffers

ctrl_handler
    v4l control handler

controls
    a union of decoder and encoder control parameters

fh
    a holder of v4l file handle structure

streamon_cap
    stream on flag for capture queue

streamon_out
    stream on flag for output queue

width
    current capture width

height
    current capture height

out_width
    current output width

out_height
    current output height

colorspace
    current color space

ycbcr_enc
    *undescribed*

quantization
    current quantization

xfer_func
    current xfer function

fps
    holds current FPS

timeperframe
    holds current time per frame structure

fmt_out
    a reference to output format structure

fmt_cap
    a reference to capture format structure

num_input_bufs
    holds number of input buffers

num_output_bufs
    holds number of output buffers
    \ ``input_buf_size``\       holds input buffer size

input_buf_size
    *undescribed*

output_buf_size
    holds output buffer size

output2_buf_size
    holds secondary decoder output buffer size

dpb_buftype
    decoded picture buffer type

dpb_fmt
    decoded picture buffer raw format

opb_buftype
    output picture buffer type

opb_fmt
    output picture buffer raw format

reconfig
    a flag raised by decoder when the stream resolution changed

reconfig_width
    holds the new width

reconfig_height
    holds the new height

hfi_codec
    current codec for this instance in HFI space

sequence_cap
    a sequence counter for capture queue

sequence_out
    a sequence counter for output queue

m2m_dev
    a reference to m2m device structure

m2m_ctx
    a reference to m2m context structure

state
    current state of the instance

done
    a completion for sync HFI operation

error
    an error returned during last HFI sync operation

session_error
    a flag rised by HFI interface in case of session error

ops
    HFI operations

session_type
    the type of the session (decoder or encoder)

hprop
    a union used as a holder by get property

.. This file was automatic generated / don't edit.

