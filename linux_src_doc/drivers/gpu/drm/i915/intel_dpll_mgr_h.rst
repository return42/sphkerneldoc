.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_dpll_mgr.h

.. _`intel_dpll_id`:

enum intel_dpll_id
==================

.. c:type:: enum intel_dpll_id

    possible DPLL ids

.. _`intel_dpll_id.definition`:

Definition
----------

.. code-block:: c

    enum intel_dpll_id {
        DPLL_ID_PRIVATE,
        DPLL_ID_PCH_PLL_A,
        DPLL_ID_PCH_PLL_B,
        DPLL_ID_WRPLL1,
        DPLL_ID_WRPLL2,
        DPLL_ID_SPLL,
        DPLL_ID_LCPLL_810,
        DPLL_ID_LCPLL_1350,
        DPLL_ID_LCPLL_2700,
        DPLL_ID_SKL_DPLL0,
        DPLL_ID_SKL_DPLL1,
        DPLL_ID_SKL_DPLL2,
        DPLL_ID_SKL_DPLL3,
        DPLL_ID_ICL_DPLL0,
        DPLL_ID_ICL_DPLL1,
        DPLL_ID_ICL_MGPLL1,
        DPLL_ID_ICL_MGPLL2,
        DPLL_ID_ICL_MGPLL3,
        DPLL_ID_ICL_MGPLL4
    };

.. _`intel_dpll_id.constants`:

Constants
---------

DPLL_ID_PRIVATE
    non-shared dpll in use

DPLL_ID_PCH_PLL_A
    DPLL A in ILK, SNB and IVB

DPLL_ID_PCH_PLL_B
    DPLL B in ILK, SNB and IVB

DPLL_ID_WRPLL1
    HSW and BDW WRPLL1

DPLL_ID_WRPLL2
    HSW and BDW WRPLL2

DPLL_ID_SPLL
    HSW and BDW SPLL

DPLL_ID_LCPLL_810
    HSW and BDW 0.81 GHz LCPLL

DPLL_ID_LCPLL_1350
    HSW and BDW 1.35 GHz LCPLL

DPLL_ID_LCPLL_2700
    HSW and BDW 2.7 GHz LCPLL

DPLL_ID_SKL_DPLL0
    SKL and later DPLL0

DPLL_ID_SKL_DPLL1
    SKL and later DPLL1

DPLL_ID_SKL_DPLL2
    SKL and later DPLL2

DPLL_ID_SKL_DPLL3
    SKL and later DPLL3

DPLL_ID_ICL_DPLL0
    ICL combo PHY DPLL0

DPLL_ID_ICL_DPLL1
    ICL combo PHY DPLL1

DPLL_ID_ICL_MGPLL1
    ICL MG PLL 1 port 1 (C)

DPLL_ID_ICL_MGPLL2
    ICL MG PLL 1 port 2 (D)

DPLL_ID_ICL_MGPLL3
    ICL MG PLL 1 port 3 (E)

DPLL_ID_ICL_MGPLL4
    ICL MG PLL 1 port 4 (F)

.. _`intel_dpll_id.description`:

Description
-----------

Enumeration of possible IDs for a DPLL. Real shared dpll ids must be >= 0.

.. _`intel_shared_dpll_state`:

struct intel_shared_dpll_state
==============================

.. c:type:: struct intel_shared_dpll_state

    hold the DPLL atomic state

.. _`intel_shared_dpll_state.definition`:

Definition
----------

.. code-block:: c

    struct intel_shared_dpll_state {
        unsigned crtc_mask;
        struct intel_dpll_hw_state hw_state;
    }

.. _`intel_shared_dpll_state.members`:

Members
-------

crtc_mask
    mask of CRTC using this DPLL, active or not

hw_state
    hardware configuration for the DPLL stored instruct \ :c:type:`struct intel_dpll_hw_state <intel_dpll_hw_state>`\ .

.. _`intel_shared_dpll_state.description`:

Description
-----------

This structure holds an atomic state for the DPLL, that can represent
either its current state (in struct \ :c:type:`struct intel_shared_dpll <intel_shared_dpll>`\ ) or a desired
future state which would be applied by an atomic mode set (stored in
a struct \ :c:type:`struct intel_atomic_state <intel_atomic_state>`\ ).

See also \ :c:func:`intel_get_shared_dpll`\  and \ :c:func:`intel_release_shared_dpll`\ .

.. _`intel_shared_dpll_funcs`:

struct intel_shared_dpll_funcs
==============================

.. c:type:: struct intel_shared_dpll_funcs

    platform specific hooks for managing DPLLs

.. _`intel_shared_dpll_funcs.definition`:

Definition
----------

.. code-block:: c

    struct intel_shared_dpll_funcs {
        void (*prepare)(struct drm_i915_private *dev_priv, struct intel_shared_dpll *pll);
        void (*enable)(struct drm_i915_private *dev_priv, struct intel_shared_dpll *pll);
        void (*disable)(struct drm_i915_private *dev_priv, struct intel_shared_dpll *pll);
        bool (*get_hw_state)(struct drm_i915_private *dev_priv,struct intel_shared_dpll *pll, struct intel_dpll_hw_state *hw_state);
    }

.. _`intel_shared_dpll_funcs.members`:

Members
-------

prepare

    Optional hook to perform operations prior to enabling the PLL.
    Called from \ :c:func:`intel_prepare_shared_dpll`\  function unless the PLL
    is already enabled.

enable

    Hook for enabling the pll, called from \ :c:func:`intel_enable_shared_dpll`\ 
    if the pll is not already enabled.

disable

    Hook for disabling the pll, called from \ :c:func:`intel_disable_shared_dpll`\ 
    only when it is safe to disable the pll, i.e., there are no more
    tracked users for it.

get_hw_state

    Hook for reading the values currently programmed to the DPLL
    registers. This is used for initial hw state readout and state
    verification after a mode set.

.. _`dpll_info`:

struct dpll_info
================

.. c:type:: struct dpll_info

    display PLL platform specific info

.. _`dpll_info.definition`:

Definition
----------

.. code-block:: c

    struct dpll_info {
        const char *name;
        const struct intel_shared_dpll_funcs *funcs;
        enum intel_dpll_id id;
    #define INTEL_DPLL_ALWAYS_ON (1 << 0)
        uint32_t flags;
    }

.. _`dpll_info.members`:

Members
-------

name
    DPLL name; used for logging

funcs
    platform specific hooks

id
    unique indentifier for this DPLL; should match the index in thedev_priv->shared_dplls array

flags

    INTEL_DPLL_ALWAYS_ON
        Inform the state checker that the DPLL is kept enabled even if
        not in use by any CRTC.

.. _`intel_shared_dpll`:

struct intel_shared_dpll
========================

.. c:type:: struct intel_shared_dpll

    display PLL with tracked state and users

.. _`intel_shared_dpll.definition`:

Definition
----------

.. code-block:: c

    struct intel_shared_dpll {
        struct intel_shared_dpll_state state;
        unsigned active_mask;
        bool on;
        const struct dpll_info *info;
    }

.. _`intel_shared_dpll.members`:

Members
-------

state

    Store the state for the pll, including the its hw state
    and CRTCs using it.

active_mask
    mask of active CRTCs (i.e. DPMS on) using this DPLL

on
    is the PLL actually active? Disabled during modeset

info
    platform specific info

.. This file was automatic generated / don't edit.

