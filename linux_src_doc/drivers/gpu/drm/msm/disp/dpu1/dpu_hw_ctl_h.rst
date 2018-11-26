.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_ctl.h

.. _`dpu_hw_stage_cfg`:

struct dpu_hw_stage_cfg
=======================

.. c:type:: struct dpu_hw_stage_cfg

    blending stage cfg

.. _`dpu_hw_stage_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_stage_cfg {
        enum dpu_sspp stage[DPU_STAGE_MAX][PIPES_PER_STAGE];
        enum dpu_sspp_multirect_index multirect_index [DPU_STAGE_MAX][PIPES_PER_STAGE];
    }

.. _`dpu_hw_stage_cfg.members`:

Members
-------

stage
    SSPP_ID at each stage

multirect_index
    index of the rectangle of SSPP.

.. _`dpu_hw_intf_cfg`:

struct dpu_hw_intf_cfg
======================

.. c:type:: struct dpu_hw_intf_cfg

    Describes how the DPU writes data to output interface

.. _`dpu_hw_intf_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_intf_cfg {
        enum dpu_intf intf;
        enum dpu_3d_blend_mode mode_3d;
        enum dpu_ctl_mode_sel intf_mode_sel;
        int stream_sel;
    }

.. _`dpu_hw_intf_cfg.members`:

Members
-------

intf
    Interface id

mode_3d
    3d mux configuration

intf_mode_sel
    Interface mode, cmd / vid

stream_sel
    Stream selection for multi-stream interfaces

.. _`dpu_hw_ctl_ops`:

struct dpu_hw_ctl_ops
=====================

.. c:type:: struct dpu_hw_ctl_ops

    Interface to the wb Hw driver functions Assumption is these functions will be called after clocks are enabled

.. _`dpu_hw_ctl_ops.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_ctl_ops {
        void (*trigger_start)(struct dpu_hw_ctl *ctx);
        void (*trigger_pending)(struct dpu_hw_ctl *ctx);
        void (*clear_pending_flush)(struct dpu_hw_ctl *ctx);
        u32 (*get_pending_flush)(struct dpu_hw_ctl *ctx);
        void (*update_pending_flush)(struct dpu_hw_ctl *ctx, u32 flushbits);
        void (*trigger_flush)(struct dpu_hw_ctl *ctx);
        u32 (*get_flush_register)(struct dpu_hw_ctl *ctx);
        void (*setup_intf_cfg)(struct dpu_hw_ctl *ctx, struct dpu_hw_intf_cfg *cfg);
        int (*reset)(struct dpu_hw_ctl *c);
        int (*wait_reset_status)(struct dpu_hw_ctl *ctx);
        uint32_t (*get_bitmask_sspp)(struct dpu_hw_ctl *ctx, enum dpu_sspp blk);
        uint32_t (*get_bitmask_mixer)(struct dpu_hw_ctl *ctx, enum dpu_lm blk);
        int (*get_bitmask_intf)(struct dpu_hw_ctl *ctx,u32 *flushbits, enum dpu_intf blk);
        void (*clear_all_blendstages)(struct dpu_hw_ctl *ctx);
        void (*setup_blendstage)(struct dpu_hw_ctl *ctx, enum dpu_lm lm, struct dpu_hw_stage_cfg *cfg);
    }

.. _`dpu_hw_ctl_ops.members`:

Members
-------

trigger_start
    *undescribed*

trigger_pending
    *undescribed*

clear_pending_flush
    *undescribed*

get_pending_flush
    *undescribed*

update_pending_flush
    *undescribed*

trigger_flush
    *undescribed*

get_flush_register
    *undescribed*

setup_intf_cfg
    *undescribed*

reset
    *undescribed*

wait_reset_status
    *undescribed*

get_bitmask_sspp
    *undescribed*

get_bitmask_mixer
    *undescribed*

get_bitmask_intf
    *undescribed*

clear_all_blendstages
    *undescribed*

setup_blendstage
    *undescribed*

.. _`dpu_hw_ctl`:

struct dpu_hw_ctl
=================

.. c:type:: struct dpu_hw_ctl

    CTL PATH driver object

.. _`dpu_hw_ctl.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_ctl {
        struct dpu_hw_blk base;
        struct dpu_hw_blk_reg_map hw;
        int idx;
        const struct dpu_ctl_cfg *caps;
        int mixer_count;
        const struct dpu_lm_cfg *mixer_hw_caps;
        u32 pending_flush_mask;
        struct dpu_hw_ctl_ops ops;
    }

.. _`dpu_hw_ctl.members`:

Members
-------

base
    hardware block base structure

hw
    block register map object

idx
    control path index

caps
    control path capabilities

mixer_count
    number of mixers

mixer_hw_caps
    mixer hardware capabilities

pending_flush_mask
    storage for pending ctl_flush managed via ops

ops
    operation list

.. _`to_dpu_hw_ctl`:

to_dpu_hw_ctl
=============

.. c:function:: struct dpu_hw_ctl *to_dpu_hw_ctl(struct dpu_hw_blk *hw)

    convert base object dpu_hw_base to container

    :param hw:
        Pointer to base hardware block
    :type hw: struct dpu_hw_blk \*

.. _`to_dpu_hw_ctl.return`:

Return
------

Pointer to hardware block container

.. _`dpu_hw_ctl_init`:

dpu_hw_ctl_init
===============

.. c:function:: struct dpu_hw_ctl *dpu_hw_ctl_init(enum dpu_ctl idx, void __iomem *addr, struct dpu_mdss_cfg *m)

    Initializes the ctl_path hw driver object. should be called before accessing every ctl path registers.

    :param idx:
        ctl_path index for which driver object is required
    :type idx: enum dpu_ctl

    :param addr:
        mapped register io address of MDP
    :type addr: void __iomem \*

    :param m:
        pointer to mdss catalog data
    :type m: struct dpu_mdss_cfg \*

.. _`dpu_hw_ctl_destroy`:

dpu_hw_ctl_destroy
==================

.. c:function:: void dpu_hw_ctl_destroy(struct dpu_hw_ctl *ctx)

    Destroys ctl driver context should be called to free the context

    :param ctx:
        *undescribed*
    :type ctx: struct dpu_hw_ctl \*

.. This file was automatic generated / don't edit.

