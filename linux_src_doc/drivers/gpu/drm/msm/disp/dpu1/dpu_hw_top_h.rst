.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_hw_top.h

.. _`traffic_shaper_cfg`:

struct traffic_shaper_cfg
=========================

.. c:type:: struct traffic_shaper_cfg

    traffic shaper configuration

.. _`traffic_shaper_cfg.definition`:

Definition
----------

.. code-block:: c

    struct traffic_shaper_cfg {
        bool en;
        bool rd_client;
        u32 client_id;
        u32 bpc_denom;
        u64 bpc_numer;
    }

.. _`traffic_shaper_cfg.members`:

Members
-------

en
    enable/disable traffic shaper

rd_client
    true if read client; false if write client

client_id
    client identifier

bpc_denom
    denominator of byte per clk

bpc_numer
    numerator of byte per clk

.. _`split_pipe_cfg`:

struct split_pipe_cfg
=====================

.. c:type:: struct split_pipe_cfg

    pipe configuration for dual display panels

.. _`split_pipe_cfg.definition`:

Definition
----------

.. code-block:: c

    struct split_pipe_cfg {
        bool en;
        enum dpu_intf_mode mode;
        enum dpu_intf intf;
        bool split_flush_en;
    }

.. _`split_pipe_cfg.members`:

Members
-------

en
    Enable/disable dual pipe confguration

mode
    Panel interface mode

intf
    Interface id for main control path

split_flush_en
    Allows both the paths to be flushed when master path is
    flushed

.. _`dpu_danger_safe_status`:

struct dpu_danger_safe_status
=============================

.. c:type:: struct dpu_danger_safe_status

    danger and safe status signals

.. _`dpu_danger_safe_status.definition`:

Definition
----------

.. code-block:: c

    struct dpu_danger_safe_status {
        u8 mdp;
        u8 sspp[SSPP_MAX];
    }

.. _`dpu_danger_safe_status.members`:

Members
-------

mdp
    top level status

sspp
    source pipe status

.. _`dpu_vsync_source_cfg`:

struct dpu_vsync_source_cfg
===========================

.. c:type:: struct dpu_vsync_source_cfg

    configure vsync source and configure the watchdog timers if required.

.. _`dpu_vsync_source_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpu_vsync_source_cfg {
        u32 pp_count;
        u32 frame_rate;
        u32 ppnumber[PINGPONG_MAX];
        u32 vsync_source;
    }

.. _`dpu_vsync_source_cfg.members`:

Members
-------

pp_count
    number of ping pongs active

frame_rate
    Display frame rate

ppnumber
    ping pong index array

vsync_source
    vsync source selection

.. _`dpu_hw_mdp_ops`:

struct dpu_hw_mdp_ops
=====================

.. c:type:: struct dpu_hw_mdp_ops

    interface to the MDP TOP Hw driver functions Assumption is these functions will be called after clocks are enabled.

.. _`dpu_hw_mdp_ops.definition`:

Definition
----------

.. code-block:: c

    struct dpu_hw_mdp_ops {
        void (*setup_split_pipe)(struct dpu_hw_mdp *mdp, struct split_pipe_cfg *p);
        void (*setup_traffic_shaper)(struct dpu_hw_mdp *mdp, struct traffic_shaper_cfg *cfg);
        bool (*setup_clk_force_ctrl)(struct dpu_hw_mdp *mdp, enum dpu_clk_ctrl_type clk_ctrl, bool enable);
        void (*get_danger_status)(struct dpu_hw_mdp *mdp, struct dpu_danger_safe_status *status);
        void (*setup_vsync_source)(struct dpu_hw_mdp *mdp, struct dpu_vsync_source_cfg *cfg);
        void (*get_safe_status)(struct dpu_hw_mdp *mdp, struct dpu_danger_safe_status *status);
        void (*reset_ubwc)(struct dpu_hw_mdp *mdp, struct dpu_mdss_cfg *m);
        void (*intf_audio_select)(struct dpu_hw_mdp *mdp);
    }

.. _`dpu_hw_mdp_ops.members`:

Members
-------

setup_split_pipe
    Programs the pipe control registers

setup_traffic_shaper
    programs traffic shaper control

setup_clk_force_ctrl
    *undescribed*

get_danger_status
    *undescribed*

setup_vsync_source
    *undescribed*

get_safe_status
    *undescribed*

reset_ubwc
    *undescribed*

intf_audio_select
    *undescribed*

.. _`to_dpu_hw_mdp`:

to_dpu_hw_mdp
=============

.. c:function:: struct dpu_hw_mdp *to_dpu_hw_mdp(struct dpu_hw_blk *hw)

    convert base object dpu_hw_base to container

    :param hw:
        Pointer to base hardware block
    :type hw: struct dpu_hw_blk \*

.. _`to_dpu_hw_mdp.return`:

Return
------

Pointer to hardware block container

.. _`dpu_hw_mdptop_init`:

dpu_hw_mdptop_init
==================

.. c:function:: struct dpu_hw_mdp *dpu_hw_mdptop_init(enum dpu_mdp idx, void __iomem *addr, const struct dpu_mdss_cfg *m)

    initializes the top driver for the passed idx

    :param idx:
        Interface index for which driver object is required
    :type idx: enum dpu_mdp

    :param addr:
        Mapped register io address of MDP
    :type addr: void __iomem \*

    :param m:
        Pointer to mdss catalog data
    :type m: const struct dpu_mdss_cfg \*

.. This file was automatic generated / don't edit.

