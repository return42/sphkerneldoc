.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_sspp.h

.. _`dpu_sspp_flip_lr`:

DPU_SSPP_FLIP_LR
================

.. c:function::  DPU_SSPP_FLIP_LR()

.. _`dpu_sspp_scaler`:

DPU_SSPP_SCALER
===============

.. c:function::  DPU_SSPP_SCALER()

.. _`dpu_hw_pipe_cfg`:

struct dpu_hw_pipe_cfg
======================

.. c:type:: struct dpu_hw_pipe_cfg

    Pipe description

.. _`dpu_hw_pipe_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_pipe_cfg {
        struct dpu_hw_fmt_layout layout;
        struct drm_rect src_rect;
        struct drm_rect dst_rect;
        enum dpu_sspp_multirect_index index;
        enum dpu_sspp_multirect_mode mode;
    }

.. _`dpu_hw_pipe_cfg.members`:

Members
-------

layout
    format layout information for programming buffer to hardware

src_rect
    src ROI, caller takes into account the different operations
    such as decimation, flip etc to program this field

dst_rect
    *undescribed*

index
    index of the rectangle of SSPP

mode
    parallel or time multiplex multirect mode

.. _`dpu_hw_pipe_qos_cfg`:

struct dpu_hw_pipe_qos_cfg
==========================

.. c:type:: struct dpu_hw_pipe_qos_cfg

    Source pipe QoS configuration

.. _`dpu_hw_pipe_qos_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_pipe_qos_cfg {
        u32 danger_lut;
        u32 safe_lut;
        u64 creq_lut;
        u32 creq_vblank;
        u32 danger_vblank;
        bool vblank_en;
        bool danger_safe_en;
    }

.. _`dpu_hw_pipe_qos_cfg.members`:

Members
-------

danger_lut
    LUT for generate danger level based on fill level

safe_lut
    LUT for generate safe level based on fill level

creq_lut
    LUT for generate creq level based on fill level

creq_vblank
    creq value generated to vbif during vertical blanking

danger_vblank
    danger value generated during vertical blanking

vblank_en
    enable creq_vblank and danger_vblank during vblank

danger_safe_en
    enable danger safe generation

.. _`dpu_hw_pipe_cdp_cfg`:

struct dpu_hw_pipe_cdp_cfg
==========================

.. c:type:: struct dpu_hw_pipe_cdp_cfg

    CDP configuration

.. _`dpu_hw_pipe_cdp_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_pipe_cdp_cfg {
        bool enable;
        bool ubwc_meta_enable;
        bool tile_amortize_enable;
        u32 preload_ahead;
    }

.. _`dpu_hw_pipe_cdp_cfg.members`:

Members
-------

enable
    true to enable CDP

ubwc_meta_enable
    true to enable ubwc metadata preload

tile_amortize_enable
    true to enable amortization control for tile format

preload_ahead
    number of request to preload ahead
    DPU_SSPP_CDP_PRELOAD_AHEAD_32,
    DPU_SSPP_CDP_PRELOAD_AHEAD_64

.. _`dpu_hw_pipe_ts_cfg`:

struct dpu_hw_pipe_ts_cfg
=========================

.. c:type:: struct dpu_hw_pipe_ts_cfg

    traffic shaper configuration

.. _`dpu_hw_pipe_ts_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_pipe_ts_cfg {
        u64 size;
        u64 time;
    }

.. _`dpu_hw_pipe_ts_cfg.members`:

Members
-------

size
    size to prefill in bytes, or zero to disable

time
    time to prefill in usec, or zero to disable

.. _`dpu_hw_sspp_ops`:

struct dpu_hw_sspp_ops
======================

.. c:type:: struct dpu_hw_sspp_ops

    interface to the SSPP Hw driver functions Caller must call the init function to get the pipe context for each pipe Assumption is these functions will be called after clocks are enabled

.. _`dpu_hw_sspp_ops.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_sspp_ops {
        void (*setup_format)(struct dpu_hw_pipe *ctx,const struct dpu_format *fmt, u32 flags, enum dpu_sspp_multirect_index index);
        void (*setup_rects)(struct dpu_hw_pipe *ctx,struct dpu_hw_pipe_cfg *cfg, enum dpu_sspp_multirect_index index);
        void (*setup_pe)(struct dpu_hw_pipe *ctx, struct dpu_hw_pixel_ext *pe_ext);
        void (*setup_sourceaddress)(struct dpu_hw_pipe *ctx,struct dpu_hw_pipe_cfg *cfg, enum dpu_sspp_multirect_index index);
        void (*setup_csc)(struct dpu_hw_pipe *ctx, struct dpu_csc_cfg *data);
        void (*setup_solidfill)(struct dpu_hw_pipe *ctx, u32 color, enum dpu_sspp_multirect_index index);
        void (*setup_multirect)(struct dpu_hw_pipe *ctx,enum dpu_sspp_multirect_index index, enum dpu_sspp_multirect_mode mode);
        void (*setup_sharpening)(struct dpu_hw_pipe *ctx, struct dpu_hw_sharp_cfg *cfg);
        void (*setup_danger_safe_lut)(struct dpu_hw_pipe *ctx, struct dpu_hw_pipe_qos_cfg *cfg);
        void (*setup_creq_lut)(struct dpu_hw_pipe *ctx, struct dpu_hw_pipe_qos_cfg *cfg);
        void (*setup_qos_ctrl)(struct dpu_hw_pipe *ctx, struct dpu_hw_pipe_qos_cfg *cfg);
        void (*setup_histogram)(struct dpu_hw_pipe *ctx, void *cfg);
        void (*setup_scaler)(struct dpu_hw_pipe *ctx,struct dpu_hw_pipe_cfg *pipe_cfg,struct dpu_hw_pixel_ext *pe_cfg, void *scaler_cfg);
        u32 (*get_scaler_ver)(struct dpu_hw_pipe *ctx);
        void (*setup_cdp)(struct dpu_hw_pipe *ctx, struct dpu_hw_pipe_cdp_cfg *cfg);
    }

.. _`dpu_hw_sspp_ops.members`:

Members
-------

setup_format
    *undescribed*

setup_rects
    *undescribed*

setup_pe
    *undescribed*

setup_sourceaddress
    *undescribed*

setup_csc
    *undescribed*

setup_solidfill
    *undescribed*

setup_multirect
    *undescribed*

setup_sharpening
    *undescribed*

setup_danger_safe_lut
    *undescribed*

setup_creq_lut
    *undescribed*

setup_qos_ctrl
    *undescribed*

setup_histogram
    *undescribed*

setup_scaler
    *undescribed*

get_scaler_ver
    *undescribed*

setup_cdp
    *undescribed*

.. _`dpu_hw_pipe`:

struct dpu_hw_pipe
==================

.. c:type:: struct dpu_hw_pipe

    pipe description

.. _`dpu_hw_pipe.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_pipe {
        struct dpu_hw_blk base;
        struct dpu_hw_blk_reg_map hw;
        struct dpu_mdss_cfg *catalog;
        struct dpu_mdp_cfg *mdp;
        enum dpu_sspp idx;
        const struct dpu_sspp_cfg *cap;
        struct dpu_hw_sspp_ops ops;
    }

.. _`dpu_hw_pipe.members`:

Members
-------

base
    hardware block base structure

hw
    block hardware details

catalog
    back pointer to catalog

mdp
    pointer to associated mdp portion of the catalog

idx
    pipe index

cap
    pointer to layer_cfg

ops
    pointer to operations possible for this pipe

.. _`to_dpu_hw_pipe`:

to_dpu_hw_pipe
==============

.. c:function:: struct dpu_hw_pipe *to_dpu_hw_pipe(struct dpu_hw_blk *hw)

    convert base object dpu_hw_base to container

    :param hw:
        Pointer to base hardware block
    :type hw: struct dpu_hw_blk \*

.. _`to_dpu_hw_pipe.return`:

Return
------

Pointer to hardware block container

.. _`dpu_hw_sspp_init`:

dpu_hw_sspp_init
================

.. c:function:: struct dpu_hw_pipe *dpu_hw_sspp_init(enum dpu_sspp idx, void __iomem *addr, struct dpu_mdss_cfg *catalog, bool is_virtual_pipe)

    initializes the sspp hw driver object. Should be called once before accessing every pipe.

    :param idx:
        Pipe index for which driver object is required
    :type idx: enum dpu_sspp

    :param addr:
        Mapped register io address of MDP
    :type addr: void __iomem \*

    :param catalog:
        Pointer to mdss catalog data
    :type catalog: struct dpu_mdss_cfg \*

    :param is_virtual_pipe:
        is this pipe virtual pipe
    :type is_virtual_pipe: bool

.. _`dpu_hw_sspp_destroy`:

dpu_hw_sspp_destroy
===================

.. c:function:: void dpu_hw_sspp_destroy(struct dpu_hw_pipe *ctx)

    Destroys SSPP driver context should be called during Hw pipe cleanup.

    :param ctx:
        Pointer to SSPP driver context returned by dpu_hw_sspp_init
    :type ctx: struct dpu_hw_pipe \*

.. This file was automatic generated / don't edit.

