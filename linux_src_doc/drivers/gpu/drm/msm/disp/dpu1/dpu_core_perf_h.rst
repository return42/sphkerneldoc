.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_core_perf.h

.. _`dpu_core_perf_params`:

struct dpu_core_perf_params
===========================

.. c:type:: struct dpu_core_perf_params

    definition of performance parameters

.. _`dpu_core_perf_params.definition`:

Definition
----------

.. code-block:: c

    struct dpu_core_perf_params {
        u64 max_per_pipe_ib[DPU_POWER_HANDLE_DBUS_ID_MAX];
        u64 bw_ctl[DPU_POWER_HANDLE_DBUS_ID_MAX];
        u64 core_clk_rate;
    }

.. _`dpu_core_perf_params.members`:

Members
-------

max_per_pipe_ib
    maximum instantaneous bandwidth request

bw_ctl
    arbitrated bandwidth request

core_clk_rate
    core clock rate request

.. _`dpu_core_perf_tune`:

struct dpu_core_perf_tune
=========================

.. c:type:: struct dpu_core_perf_tune

    definition of performance tuning control

.. _`dpu_core_perf_tune.definition`:

Definition
----------

.. code-block:: c

    struct dpu_core_perf_tune {
        u32 mode;
        u64 min_core_clk;
        u64 min_bus_vote;
    }

.. _`dpu_core_perf_tune.members`:

Members
-------

mode
    performance mode

min_core_clk
    minimum core clock

min_bus_vote
    minimum bus vote

.. _`dpu_core_perf`:

struct dpu_core_perf
====================

.. c:type:: struct dpu_core_perf

    definition of core performance context

.. _`dpu_core_perf.definition`:

Definition
----------

.. code-block:: c

    struct dpu_core_perf {
        struct drm_device *dev;
        struct dentry *debugfs_root;
        struct dpu_mdss_cfg *catalog;
        struct dpu_power_handle *phandle;
        struct dss_clk *core_clk;
        u64 core_clk_rate;
        u64 max_core_clk_rate;
        struct dpu_core_perf_tune perf_tune;
        u32 enable_bw_release;
        u64 fix_core_clk_rate;
        u64 fix_core_ib_vote;
        u64 fix_core_ab_vote;
    }

.. _`dpu_core_perf.members`:

Members
-------

dev
    Pointer to drm device

debugfs_root
    top level debug folder

catalog
    Pointer to catalog configuration

phandle
    Pointer to power handler

core_clk
    Pointer to core clock structure

core_clk_rate
    current core clock rate

max_core_clk_rate
    maximum allowable core clock rate

perf_tune
    debug control for performance tuning

enable_bw_release
    debug control for bandwidth release

fix_core_clk_rate
    fixed core clock request in Hz used in mode 2

fix_core_ib_vote
    fixed core ib vote in bps used in mode 2

fix_core_ab_vote
    fixed core ab vote in bps used in mode 2

.. _`dpu_core_perf_crtc_check`:

dpu_core_perf_crtc_check
========================

.. c:function:: int dpu_core_perf_crtc_check(struct drm_crtc *crtc, struct drm_crtc_state *state)

    validate performance of the given crtc state

    :param crtc:
        Pointer to crtc
    :type crtc: struct drm_crtc \*

    :param state:
        Pointer to new crtc state
    :type state: struct drm_crtc_state \*

.. _`dpu_core_perf_crtc_check.return`:

Return
------

zero if success, or error code otherwise

.. _`dpu_core_perf_crtc_update`:

dpu_core_perf_crtc_update
=========================

.. c:function:: int dpu_core_perf_crtc_update(struct drm_crtc *crtc, int params_changed, bool stop_req)

    update performance of the given crtc

    :param crtc:
        Pointer to crtc
    :type crtc: struct drm_crtc \*

    :param params_changed:
        true if crtc parameters are modified
    :type params_changed: int

    :param stop_req:
        true if this is a stop request
    :type stop_req: bool

.. _`dpu_core_perf_crtc_update.return`:

Return
------

zero if success, or error code otherwise

.. _`dpu_core_perf_crtc_release_bw`:

dpu_core_perf_crtc_release_bw
=============================

.. c:function:: void dpu_core_perf_crtc_release_bw(struct drm_crtc *crtc)

    release bandwidth of the given crtc

    :param crtc:
        Pointer to crtc
    :type crtc: struct drm_crtc \*

.. _`dpu_core_perf_destroy`:

dpu_core_perf_destroy
=====================

.. c:function:: void dpu_core_perf_destroy(struct dpu_core_perf *perf)

    destroy the given core performance context

    :param perf:
        Pointer to core performance context
    :type perf: struct dpu_core_perf \*

.. _`dpu_core_perf_init`:

dpu_core_perf_init
==================

.. c:function:: int dpu_core_perf_init(struct dpu_core_perf *perf, struct drm_device *dev, struct dpu_mdss_cfg *catalog, struct dpu_power_handle *phandle, struct dss_clk *core_clk)

    initialize the given core performance context

    :param perf:
        Pointer to core performance context
    :type perf: struct dpu_core_perf \*

    :param dev:
        Pointer to drm device
    :type dev: struct drm_device \*

    :param catalog:
        Pointer to catalog
    :type catalog: struct dpu_mdss_cfg \*

    :param phandle:
        Pointer to power handle
    :type phandle: struct dpu_power_handle \*

    :param core_clk:
        pointer to core clock
    :type core_clk: struct dss_clk \*

.. _`dpu_core_perf_debugfs_init`:

dpu_core_perf_debugfs_init
==========================

.. c:function:: int dpu_core_perf_debugfs_init(struct dpu_core_perf *perf, struct dentry *parent)

    initialize debugfs for core performance context

    :param perf:
        Pointer to core performance context
    :type perf: struct dpu_core_perf \*

    :param parent:
        *undescribed*
    :type parent: struct dentry \*

.. This file was automatic generated / don't edit.

