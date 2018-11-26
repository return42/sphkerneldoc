.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_catalog.h

.. _`max_blocks`:

MAX_BLOCKS
==========

.. c:function::  MAX_BLOCKS()

    For ex: max 12 SSPP pipes or 5 ctl paths. In all cases, it can have max 12 hardware blocks based on current design

.. _`dpu_hw_blk_info`:

DPU_HW_BLK_INFO
===============

.. c:function::  DPU_HW_BLK_INFO()

    information of HW blocks inside DPU

.. _`dpu_hw_subblk_info`:

DPU_HW_SUBBLK_INFO
==================

.. c:function::  DPU_HW_SUBBLK_INFO()

    information of HW sub-block inside DPU

.. _`dpu_src_blk`:

struct dpu_src_blk
==================

.. c:type:: struct dpu_src_blk

    SSPP part of the source pipes

.. _`dpu_src_blk.definition`:

Definition
----------

.. code-block:: c

    struct dpu_src_blk {
        DPU_HW_SUBBLK_INFO;
    }

.. _`dpu_src_blk.members`:

Members
-------

DPU_HW_SUBBLK_INFO
    *undescribed*

.. _`dpu_scaler_blk`:

struct dpu_scaler_blk
=====================

.. c:type:: struct dpu_scaler_blk

    Scaler information

.. _`dpu_scaler_blk.definition`:

Definition
----------

.. code-block:: c

    struct dpu_scaler_blk {
        DPU_HW_SUBBLK_INFO;
        u32 version;
    }

.. _`dpu_scaler_blk.members`:

Members
-------

DPU_HW_SUBBLK_INFO
    *undescribed*

version
    qseed block revision

.. _`dpu_pp_blk`:

struct dpu_pp_blk
=================

.. c:type:: struct dpu_pp_blk

    Pixel processing sub-blk information

.. _`dpu_pp_blk.definition`:

Definition
----------

.. code-block:: c

    struct dpu_pp_blk {
        DPU_HW_SUBBLK_INFO;
        u32 version;
    }

.. _`dpu_pp_blk.members`:

Members
-------

DPU_HW_SUBBLK_INFO
    *undescribed*

version
    HW Algorithm version

.. _`dpu_format_extended`:

struct dpu_format_extended
==========================

.. c:type:: struct dpu_format_extended

    define dpu specific pixel format+modifier

.. _`dpu_format_extended.definition`:

Definition
----------

.. code-block:: c

    struct dpu_format_extended {
        uint32_t fourcc_format;
        uint64_t modifier;
    }

.. _`dpu_format_extended.members`:

Members
-------

fourcc_format
    Base FOURCC pixel format code

modifier
    64-bit drm format modifier, same modifier must be applied to all
    framebuffer planes

.. _`dpu_qos_lut_usage`:

enum dpu_qos_lut_usage
======================

.. c:type:: enum dpu_qos_lut_usage

    define QoS LUT use cases

.. _`dpu_qos_lut_usage.definition`:

Definition
----------

.. code-block:: c

    enum dpu_qos_lut_usage {
        DPU_QOS_LUT_USAGE_LINEAR,
        DPU_QOS_LUT_USAGE_MACROTILE,
        DPU_QOS_LUT_USAGE_NRT,
        DPU_QOS_LUT_USAGE_MAX
    };

.. _`dpu_qos_lut_usage.constants`:

Constants
---------

DPU_QOS_LUT_USAGE_LINEAR
    *undescribed*

DPU_QOS_LUT_USAGE_MACROTILE
    *undescribed*

DPU_QOS_LUT_USAGE_NRT
    *undescribed*

DPU_QOS_LUT_USAGE_MAX
    *undescribed*

.. _`dpu_qos_lut_entry`:

struct dpu_qos_lut_entry
========================

.. c:type:: struct dpu_qos_lut_entry

    define QoS LUT table entry

.. _`dpu_qos_lut_entry.definition`:

Definition
----------

.. code-block:: c

    struct dpu_qos_lut_entry {
        u32 fl;
        u64 lut;
    }

.. _`dpu_qos_lut_entry.members`:

Members
-------

fl
    fill level, or zero on last entry to indicate default lut

lut
    lut to use if equal to or less than fill level

.. _`dpu_qos_lut_tbl`:

struct dpu_qos_lut_tbl
======================

.. c:type:: struct dpu_qos_lut_tbl

    define QoS LUT table

.. _`dpu_qos_lut_tbl.definition`:

Definition
----------

.. code-block:: c

    struct dpu_qos_lut_tbl {
        u32 nentry;
        struct dpu_qos_lut_entry *entries;
    }

.. _`dpu_qos_lut_tbl.members`:

Members
-------

nentry
    number of entry in this table

entries
    Pointer to table entries

.. _`dpu_caps`:

struct dpu_caps
===============

.. c:type:: struct dpu_caps

    define DPU capabilities \ ``max_mixer_width``\     max layer mixer line width support. \ ``max_mixer_blendstages``\  max layer mixer blend stages or supported z order \ ``qseed_type``\          qseed2 or qseed3 support. \ ``smart_dma_rev``\       Supported version of SmartDMA feature. \ ``ubwc_version``\        UBWC feature version (0x0 for not supported) \ ``has_src_split``\       source split feature status \ ``has_dim_layer``\       dim layer feature status \ ``has_idle_pc``\         indicate if idle power collapse feature is supported

.. _`dpu_caps.definition`:

Definition
----------

.. code-block:: c

    struct dpu_caps {
        u32 max_mixer_width;
        u32 max_mixer_blendstages;
        u32 qseed_type;
        u32 smart_dma_rev;
        u32 ubwc_version;
        bool has_src_split;
        bool has_dim_layer;
        bool has_idle_pc;
    }

.. _`dpu_caps.members`:

Members
-------

max_mixer_width
    *undescribed*

max_mixer_blendstages
    *undescribed*

qseed_type
    *undescribed*

smart_dma_rev
    *undescribed*

ubwc_version
    *undescribed*

has_src_split
    *undescribed*

has_dim_layer
    *undescribed*

has_idle_pc
    *undescribed*

.. _`dpu_sspp_blks_common`:

struct dpu_sspp_blks_common
===========================

.. c:type:: struct dpu_sspp_blks_common

    SSPP sub-blocks common configuration

.. _`dpu_sspp_blks_common.definition`:

Definition
----------

.. code-block:: c

    struct dpu_sspp_blks_common {
        u32 maxlinewidth;
        u32 pixel_ram_size;
        u32 maxhdeciexp;
        u32 maxvdeciexp;
    }

.. _`dpu_sspp_blks_common.members`:

Members
-------

maxlinewidth
    *undescribed*

pixel_ram_size
    size of latency hiding and de-tiling buffer in bytes

maxhdeciexp
    max horizontal decimation supported by this pipe
    (max is 2^value)

maxvdeciexp
    max vertical decimation supported by this pipe
    (max is 2^value)

.. _`dpu_sspp_sub_blks`:

struct dpu_sspp_sub_blks
========================

.. c:type:: struct dpu_sspp_sub_blks

    SSPP sub-blocks

.. _`dpu_sspp_sub_blks.definition`:

Definition
----------

.. code-block:: c

    struct dpu_sspp_sub_blks {
        const struct dpu_sspp_blks_common *common;
        u32 creq_vblank;
        u32 danger_vblank;
        u32 maxdwnscale;
        u32 maxupscale;
        u32 smart_dma_priority;
        u32 max_per_pipe_bw;
        struct dpu_src_blk src_blk;
        struct dpu_scaler_blk scaler_blk;
        struct dpu_pp_blk csc_blk;
        struct dpu_pp_blk hsic_blk;
        struct dpu_pp_blk memcolor_blk;
        struct dpu_pp_blk pcc_blk;
        struct dpu_pp_blk igc_blk;
        const struct dpu_format_extended *format_list;
        const struct dpu_format_extended *virt_format_list;
    }

.. _`dpu_sspp_sub_blks.members`:

Members
-------

common
    *undescribed*

creq_vblank
    creq priority during vertical blanking

danger_vblank
    danger priority during vertical blanking

maxdwnscale
    max downscale ratio supported(without DECIMATION)

maxupscale
    maxupscale ratio supported

smart_dma_priority
    hw priority of rect1 of multirect pipe

max_per_pipe_bw
    maximum allowable bandwidth of this pipe in kBps

src_blk
    *undescribed*

scaler_blk
    *undescribed*

csc_blk
    *undescribed*

hsic_blk
    *undescribed*

memcolor_blk
    *undescribed*

pcc_blk
    *undescribed*

igc_blk
    *undescribed*

format_list
    Pointer to list of supported formats

virt_format_list
    Pointer to list of supported formats for virtual planes

.. _`dpu_sspp_sub_blks.common`:

common
------

Pointer to common configurations shared by sub blocks

.. _`dpu_lm_sub_blks`:

struct dpu_lm_sub_blks
======================

.. c:type:: struct dpu_lm_sub_blks

    information of mixer block

.. _`dpu_lm_sub_blks.definition`:

Definition
----------

.. code-block:: c

    struct dpu_lm_sub_blks {
        u32 maxwidth;
        u32 maxblendstages;
        u32 blendstage_base[MAX_BLOCKS];
        struct dpu_pp_blk gc;
    }

.. _`dpu_lm_sub_blks.members`:

Members
-------

maxwidth
    Max pixel width supported by this mixer

maxblendstages
    Max number of blend-stages supported

blendstage_base
    Blend-stage register base offset

gc
    gamma correction block

.. _`dpu_sspp_cfg`:

struct dpu_sspp_cfg
===================

.. c:type:: struct dpu_sspp_cfg

    information of source pipes

.. _`dpu_sspp_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_sspp_cfg {
        DPU_HW_BLK_INFO;
        const struct dpu_sspp_sub_blks *sblk;
        u32 xin_id;
        enum dpu_clk_ctrl_type clk_ctrl;
        u32 type;
    }

.. _`dpu_sspp_cfg.members`:

Members
-------

DPU_HW_BLK_INFO
    *undescribed*

sblk
    SSPP sub-blocks information

xin_id
    bus client identifier
    \ ``clk_ctrl``\            clock control identifier
    \ ``type``\                sspp type identifier

clk_ctrl
    *undescribed*

type
    *undescribed*

.. _`dpu_lm_cfg`:

struct dpu_lm_cfg
=================

.. c:type:: struct dpu_lm_cfg

    information of layer mixer blocks

.. _`dpu_lm_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_lm_cfg {
        DPU_HW_BLK_INFO;
        const struct dpu_lm_sub_blks *sblk;
        u32 pingpong;
        unsigned long lm_pair_mask;
    }

.. _`dpu_lm_cfg.members`:

Members
-------

DPU_HW_BLK_INFO
    *undescribed*

sblk
    LM Sub-blocks information

pingpong
    ID of connected PingPong, PINGPONG_MAX if unsupported

lm_pair_mask
    Bitmask of LMs that can be controlled by same CTL

.. _`dpu_pingpong_cfg`:

struct dpu_pingpong_cfg
=======================

.. c:type:: struct dpu_pingpong_cfg

    information of PING-PONG blocks \ ``id``\                  enum identifying this block \ ``base``\                register offset of this block \ ``features``\            bit mask identifying sub-blocks/features \ ``sblk``\                sub-blocks information

.. _`dpu_pingpong_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_pingpong_cfg {
        DPU_HW_BLK_INFO;
        const struct dpu_pingpong_sub_blks *sblk;
    }

.. _`dpu_pingpong_cfg.members`:

Members
-------

DPU_HW_BLK_INFO
    *undescribed*

sblk
    *undescribed*

.. _`dpu_intf_cfg`:

struct dpu_intf_cfg
===================

.. c:type:: struct dpu_intf_cfg

    information of timing engine blocks \ ``id``\                  enum identifying this block \ ``base``\                register offset of this block \ ``features``\            bit mask identifying sub-blocks/features

.. _`dpu_intf_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_intf_cfg {
        DPU_HW_BLK_INFO;
        u32 type;
        u32 controller_id;
        u32 prog_fetch_lines_worst_case;
    }

.. _`dpu_intf_cfg.members`:

Members
-------

DPU_HW_BLK_INFO
    *undescribed*

type
    Interface type(DSI, DP, HDMI)

controller_id
    Controller Instance ID in case of multiple of intf type
    \ ``prog_fetch_lines_worst_case``\  Worst case latency num lines needed to prefetch

prog_fetch_lines_worst_case
    *undescribed*

.. _`dpu_vbif_dynamic_ot_cfg`:

struct dpu_vbif_dynamic_ot_cfg
==============================

.. c:type:: struct dpu_vbif_dynamic_ot_cfg

    dynamic OT setting \ ``pps``\                 pixel per seconds \ ``ot_limit``\            OT limit to use up to specified pixel per second

.. _`dpu_vbif_dynamic_ot_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_vbif_dynamic_ot_cfg {
        u64 pps;
        u32 ot_limit;
    }

.. _`dpu_vbif_dynamic_ot_cfg.members`:

Members
-------

pps
    *undescribed*

ot_limit
    *undescribed*

.. _`dpu_vbif_dynamic_ot_tbl`:

struct dpu_vbif_dynamic_ot_tbl
==============================

.. c:type:: struct dpu_vbif_dynamic_ot_tbl

    dynamic OT setting table \ ``count``\               length of cfg \ ``cfg``\                 pointer to array of configuration settings with ascending requirements

.. _`dpu_vbif_dynamic_ot_tbl.definition`:

Definition
----------

.. code-block:: c

    struct dpu_vbif_dynamic_ot_tbl {
        u32 count;
        struct dpu_vbif_dynamic_ot_cfg *cfg;
    }

.. _`dpu_vbif_dynamic_ot_tbl.members`:

Members
-------

count
    *undescribed*

cfg
    *undescribed*

.. _`dpu_vbif_qos_tbl`:

struct dpu_vbif_qos_tbl
=======================

.. c:type:: struct dpu_vbif_qos_tbl

    QoS priority table \ ``npriority_lvl``\       num of priority level \ ``priority_lvl``\        pointer to array of priority level in ascending order

.. _`dpu_vbif_qos_tbl.definition`:

Definition
----------

.. code-block:: c

    struct dpu_vbif_qos_tbl {
        u32 npriority_lvl;
        u32 *priority_lvl;
    }

.. _`dpu_vbif_qos_tbl.members`:

Members
-------

npriority_lvl
    *undescribed*

priority_lvl
    *undescribed*

.. _`dpu_vbif_cfg`:

struct dpu_vbif_cfg
===================

.. c:type:: struct dpu_vbif_cfg

    information of VBIF blocks \ ``id``\                  enum identifying this block \ ``base``\                register offset of this block \ ``features``\            bit mask identifying sub-blocks/features \ ``ot_rd_limit``\         default OT read limit \ ``ot_wr_limit``\         default OT write limit \ ``xin_halt_timeout``\    maximum time (in usec) for xin to halt \ ``dynamic_ot_rd_tbl``\   dynamic OT read configuration table \ ``dynamic_ot_wr_tbl``\   dynamic OT write configuration table \ ``qos_rt_tbl``\          real-time QoS priority table \ ``qos_nrt_tbl``\         non-real-time QoS priority table \ ``memtype_count``\       number of defined memtypes \ ``memtype``\             array of xin memtype definitions

.. _`dpu_vbif_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_vbif_cfg {
        DPU_HW_BLK_INFO;
        u32 default_ot_rd_limit;
        u32 default_ot_wr_limit;
        u32 xin_halt_timeout;
        struct dpu_vbif_dynamic_ot_tbl dynamic_ot_rd_tbl;
        struct dpu_vbif_dynamic_ot_tbl dynamic_ot_wr_tbl;
        struct dpu_vbif_qos_tbl qos_rt_tbl;
        struct dpu_vbif_qos_tbl qos_nrt_tbl;
        u32 memtype_count;
        u32 memtype[MAX_XIN_COUNT];
    }

.. _`dpu_vbif_cfg.members`:

Members
-------

DPU_HW_BLK_INFO
    *undescribed*

default_ot_rd_limit
    *undescribed*

default_ot_wr_limit
    *undescribed*

xin_halt_timeout
    *undescribed*

dynamic_ot_rd_tbl
    *undescribed*

dynamic_ot_wr_tbl
    *undescribed*

qos_rt_tbl
    *undescribed*

qos_nrt_tbl
    *undescribed*

memtype_count
    *undescribed*

memtype
    *undescribed*

.. _`dpu_reg_dma_cfg`:

struct dpu_reg_dma_cfg
======================

.. c:type:: struct dpu_reg_dma_cfg

    information of lut dma blocks \ ``id``\                  enum identifying this block \ ``base``\                register offset of this block \ ``features``\            bit mask identifying sub-blocks/features \ ``version``\             version of lutdma hw block \ ``trigger_sel_off``\     offset to trigger select registers of lutdma

.. _`dpu_reg_dma_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_reg_dma_cfg {
        DPU_HW_BLK_INFO;
        u32 version;
        u32 trigger_sel_off;
    }

.. _`dpu_reg_dma_cfg.members`:

Members
-------

DPU_HW_BLK_INFO
    *undescribed*

version
    *undescribed*

trigger_sel_off
    *undescribed*

.. _`dpu_perf_cdp_cfg`:

struct dpu_perf_cdp_cfg
=======================

.. c:type:: struct dpu_perf_cdp_cfg

    define CDP use case configuration

.. _`dpu_perf_cdp_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_perf_cdp_cfg {
        bool rd_enable;
        bool wr_enable;
    }

.. _`dpu_perf_cdp_cfg.members`:

Members
-------

rd_enable
    true if read pipe CDP is enabled

wr_enable
    true if write pipe CDP is enabled

.. _`dpu_perf_cfg`:

struct dpu_perf_cfg
===================

.. c:type:: struct dpu_perf_cfg

    performance control settings \ ``max_bw_low``\          low threshold of maximum bandwidth (kbps) \ ``max_bw_high``\         high threshold of maximum bandwidth (kbps) \ ``min_core_ib``\         minimum bandwidth for core (kbps) \ ``min_core_ib``\         minimum mnoc ib vote in kbps \ ``min_llcc_ib``\         minimum llcc ib vote in kbps \ ``min_dram_ib``\         minimum dram ib vote in kbps \ ``core_ib_ff``\          core instantaneous bandwidth fudge factor \ ``core_clk_ff``\         core clock fudge factor \ ``comp_ratio_rt``\       string of 0 or more of <fourcc>/<ven>/<mod>/<comp ratio> \ ``comp_ratio_nrt``\      string of 0 or more of <fourcc>/<ven>/<mod>/<comp ratio> \ ``undersized_prefill_lines``\    undersized prefill in lines \ ``xtra_prefill_lines``\          extra prefill latency in lines \ ``dest_scale_prefill_lines``\    destination scaler latency in lines \ ``macrotile_perfill_lines``\     macrotile latency in lines \ ``yuv_nv12_prefill_lines``\      yuv_nv12 latency in lines \ ``linear_prefill_lines``\        linear latency in lines \ ``downscaling_prefill_lines``\   downscaling latency in lines \ ``amortizable_theshold``\  minimum y position for traffic shaping prefill \ ``min_prefill_lines``\   minimum pipeline latency in lines

.. _`dpu_perf_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_perf_cfg {
        u32 max_bw_low;
        u32 max_bw_high;
        u32 min_core_ib;
        u32 min_llcc_ib;
        u32 min_dram_ib;
        const char *core_ib_ff;
        const char *core_clk_ff;
        const char *comp_ratio_rt;
        const char *comp_ratio_nrt;
        u32 undersized_prefill_lines;
        u32 xtra_prefill_lines;
        u32 dest_scale_prefill_lines;
        u32 macrotile_prefill_lines;
        u32 yuv_nv12_prefill_lines;
        u32 linear_prefill_lines;
        u32 downscaling_prefill_lines;
        u32 amortizable_threshold;
        u32 min_prefill_lines;
        u32 safe_lut_tbl[DPU_QOS_LUT_USAGE_MAX];
        u32 danger_lut_tbl[DPU_QOS_LUT_USAGE_MAX];
        struct dpu_qos_lut_tbl qos_lut_tbl[DPU_QOS_LUT_USAGE_MAX];
        struct dpu_perf_cdp_cfg cdp_cfg[DPU_PERF_CDP_USAGE_MAX];
    }

.. _`dpu_perf_cfg.members`:

Members
-------

max_bw_low
    *undescribed*

max_bw_high
    *undescribed*

min_core_ib
    *undescribed*

min_llcc_ib
    *undescribed*

min_dram_ib
    *undescribed*

core_ib_ff
    *undescribed*

core_clk_ff
    *undescribed*

comp_ratio_rt
    *undescribed*

comp_ratio_nrt
    *undescribed*

undersized_prefill_lines
    *undescribed*

xtra_prefill_lines
    *undescribed*

dest_scale_prefill_lines
    *undescribed*

macrotile_prefill_lines
    *undescribed*

yuv_nv12_prefill_lines
    *undescribed*

linear_prefill_lines
    *undescribed*

downscaling_prefill_lines
    *undescribed*

amortizable_threshold
    *undescribed*

min_prefill_lines
    *undescribed*

safe_lut_tbl
    LUT tables for safe signals

danger_lut_tbl
    LUT tables for danger signals

qos_lut_tbl
    LUT tables for QoS signals
    \ ``cdp_cfg``\             cdp use case configurations

cdp_cfg
    *undescribed*

.. _`dpu_mdss_cfg`:

struct dpu_mdss_cfg
===================

.. c:type:: struct dpu_mdss_cfg

    information of MDSS HW This is the main catalog data structure representing this HW version. Contains number of instances, register offsets, capabilities of the all MDSS HW sub-blocks.

.. _`dpu_mdss_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_mdss_cfg {
        u32 hwversion;
        const struct dpu_caps *caps;
        u32 mdp_count;
        struct dpu_mdp_cfg *mdp;
        u32 ctl_count;
        struct dpu_ctl_cfg *ctl;
        u32 sspp_count;
        struct dpu_sspp_cfg *sspp;
        u32 mixer_count;
        struct dpu_lm_cfg *mixer;
        u32 pingpong_count;
        struct dpu_pingpong_cfg *pingpong;
        u32 intf_count;
        struct dpu_intf_cfg *intf;
        u32 vbif_count;
        struct dpu_vbif_cfg *vbif;
        u32 reg_dma_count;
        struct dpu_reg_dma_cfg dma_cfg;
        u32 ad_count;
        struct dpu_perf_cfg perf;
        struct dpu_format_extended *dma_formats;
        struct dpu_format_extended *cursor_formats;
        struct dpu_format_extended *vig_formats;
    }

.. _`dpu_mdss_cfg.members`:

Members
-------

hwversion
    *undescribed*

caps
    *undescribed*

mdp_count
    *undescribed*

mdp
    *undescribed*

ctl_count
    *undescribed*

ctl
    *undescribed*

sspp_count
    *undescribed*

sspp
    *undescribed*

mixer_count
    *undescribed*

mixer
    *undescribed*

pingpong_count
    *undescribed*

pingpong
    *undescribed*

intf_count
    *undescribed*

intf
    *undescribed*

vbif_count
    *undescribed*

vbif
    *undescribed*

reg_dma_count
    *undescribed*

dma_cfg
    *undescribed*

ad_count
    *undescribed*

perf
    *undescribed*

dma_formats
    *undescribed*

cursor_formats
    *undescribed*

vig_formats
    *undescribed*

.. _`dpu_mdss_cfg.description`:

Description
-----------

\ ``dma_formats``\         Supported formats for dma pipe
\ ``cursor_formats``\      Supported formats for cursor pipe
\ ``vig_formats``\         Supported formats for vig pipe

.. _`dpu_hw_catalog_init`:

dpu_hw_catalog_init
===================

.. c:function:: struct dpu_mdss_cfg *dpu_hw_catalog_init(u32 hw_rev)

    dpu hardware catalog init API retrieves hardcoded target specific catalog information in config structure

    :param hw_rev:
        caller needs provide the hardware revision.
    :type hw_rev: u32

.. _`dpu_hw_catalog_init.return`:

Return
------

dpu config structure

.. _`dpu_hw_catalog_deinit`:

dpu_hw_catalog_deinit
=====================

.. c:function:: void dpu_hw_catalog_deinit(struct dpu_mdss_cfg *dpu_cfg)

    dpu hardware catalog cleanup

    :param dpu_cfg:
        pointer returned from init function
    :type dpu_cfg: struct dpu_mdss_cfg \*

.. _`dpu_hw_sspp_multirect_enabled`:

dpu_hw_sspp_multirect_enabled
=============================

.. c:function:: bool dpu_hw_sspp_multirect_enabled(const struct dpu_sspp_cfg *cfg)

    check multirect enabled for the sspp

    :param cfg:
        pointer to sspp cfg
    :type cfg: const struct dpu_sspp_cfg \*

.. This file was automatic generated / don't edit.

