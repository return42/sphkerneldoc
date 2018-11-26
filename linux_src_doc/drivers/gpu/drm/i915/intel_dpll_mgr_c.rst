.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_dpll_mgr.c

.. _`display-plls`:

Display PLLs
============

Display PLLs used for driving outputs vary by platform. While some have
per-pipe or per-encoder dedicated PLLs, others allow the use of any PLL
from a pool. In the latter scenario, it is possible that multiple pipes
share a PLL if their configurations match.

This file provides an abstraction over display PLLs. The function
\ :c:func:`intel_shared_dpll_init`\  initializes the PLLs for the given platform.  The
users of a PLL are tracked and that tracking is integrated with the atomic
modest interface. During an atomic operation, a PLL can be requested for a
given CRTC and encoder configuration by calling \ :c:func:`intel_get_shared_dpll`\  and
a previously used PLL can be released with \ :c:func:`intel_release_shared_dpll`\ .
Changes to the users are first staged in the atomic state, and then made
effective by calling \ :c:func:`intel_shared_dpll_swap_state`\  during the atomic
commit phase.

.. _`intel_get_shared_dpll_by_id`:

intel_get_shared_dpll_by_id
===========================

.. c:function:: struct intel_shared_dpll *intel_get_shared_dpll_by_id(struct drm_i915_private *dev_priv, enum intel_dpll_id id)

    get a DPLL given its id

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param id:
        pll id
    :type id: enum intel_dpll_id

.. _`intel_get_shared_dpll_by_id.return`:

Return
------

A pointer to the DPLL with \ ``id``\ 

.. _`intel_get_shared_dpll_id`:

intel_get_shared_dpll_id
========================

.. c:function:: enum intel_dpll_id intel_get_shared_dpll_id(struct drm_i915_private *dev_priv, struct intel_shared_dpll *pll)

    get the id of a DPLL

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param pll:
        the DPLL
    :type pll: struct intel_shared_dpll \*

.. _`intel_get_shared_dpll_id.return`:

Return
------

The id of \ ``pll``\ 

.. _`intel_prepare_shared_dpll`:

intel_prepare_shared_dpll
=========================

.. c:function:: void intel_prepare_shared_dpll(struct intel_crtc *crtc)

    call a dpll's prepare hook

    :param crtc:
        CRTC which has a shared dpll
    :type crtc: struct intel_crtc \*

.. _`intel_prepare_shared_dpll.description`:

Description
-----------

This calls the PLL's prepare hook if it has one and if the PLL is not
already enabled. The prepare hook is platform specific.

.. _`intel_enable_shared_dpll`:

intel_enable_shared_dpll
========================

.. c:function:: void intel_enable_shared_dpll(struct intel_crtc *crtc)

    enable a CRTC's shared DPLL

    :param crtc:
        CRTC which has a shared DPLL
    :type crtc: struct intel_crtc \*

.. _`intel_enable_shared_dpll.description`:

Description
-----------

Enable the shared DPLL used by \ ``crtc``\ .

.. _`intel_disable_shared_dpll`:

intel_disable_shared_dpll
=========================

.. c:function:: void intel_disable_shared_dpll(struct intel_crtc *crtc)

    disable a CRTC's shared DPLL

    :param crtc:
        CRTC which has a shared DPLL
    :type crtc: struct intel_crtc \*

.. _`intel_disable_shared_dpll.description`:

Description
-----------

Disable the shared DPLL used by \ ``crtc``\ .

.. _`intel_shared_dpll_swap_state`:

intel_shared_dpll_swap_state
============================

.. c:function:: void intel_shared_dpll_swap_state(struct drm_atomic_state *state)

    make atomic DPLL configuration effective

    :param state:
        atomic state
    :type state: struct drm_atomic_state \*

.. _`intel_shared_dpll_swap_state.description`:

Description
-----------

This is the dpll version of \ :c:func:`drm_atomic_helper_swap_state`\  since the
helper does not handle driver-specific global state.

For consistency with atomic helpers this function does a complete swap,
i.e. it also puts the current state into \ ``state``\ , even though there is no
need for that at this moment.

.. _`intel_shared_dpll_init`:

intel_shared_dpll_init
======================

.. c:function:: void intel_shared_dpll_init(struct drm_device *dev)

    Initialize shared DPLLs

    :param dev:
        drm device
    :type dev: struct drm_device \*

.. _`intel_shared_dpll_init.description`:

Description
-----------

Initialize shared DPLLs for \ ``dev``\ .

.. _`intel_get_shared_dpll`:

intel_get_shared_dpll
=====================

.. c:function:: struct intel_shared_dpll *intel_get_shared_dpll(struct intel_crtc *crtc, struct intel_crtc_state *crtc_state, struct intel_encoder *encoder)

    get a shared DPLL for CRTC and encoder combination

    :param crtc:
        CRTC
    :type crtc: struct intel_crtc \*

    :param crtc_state:
        atomic state for \ ``crtc``\ 
    :type crtc_state: struct intel_crtc_state \*

    :param encoder:
        encoder
    :type encoder: struct intel_encoder \*

.. _`intel_get_shared_dpll.description`:

Description
-----------

Find an appropriate DPLL for the given CRTC and encoder combination. A
reference from the \ ``crtc``\  to the returned pll is registered in the atomic
state. That configuration is made effective by calling
\ :c:func:`intel_shared_dpll_swap_state`\ . The reference should be released by calling
\ :c:func:`intel_release_shared_dpll`\ .

.. _`intel_get_shared_dpll.return`:

Return
------

A shared DPLL to be used by \ ``crtc``\  and \ ``encoder``\  with the given \ ``crtc_state``\ .

.. _`intel_release_shared_dpll`:

intel_release_shared_dpll
=========================

.. c:function:: void intel_release_shared_dpll(struct intel_shared_dpll *dpll, struct intel_crtc *crtc, struct drm_atomic_state *state)

    end use of DPLL by CRTC in atomic state

    :param dpll:
        dpll in use by \ ``crtc``\ 
    :type dpll: struct intel_shared_dpll \*

    :param crtc:
        crtc
    :type crtc: struct intel_crtc \*

    :param state:
        atomic state
    :type state: struct drm_atomic_state \*

.. _`intel_release_shared_dpll.description`:

Description
-----------

This function releases the reference from \ ``crtc``\  to \ ``dpll``\  from the
atomic \ ``state``\ . The new configuration is made effective by calling
\ :c:func:`intel_shared_dpll_swap_state`\ .

.. _`intel_dpll_dump_hw_state`:

intel_dpll_dump_hw_state
========================

.. c:function:: void intel_dpll_dump_hw_state(struct drm_i915_private *dev_priv, struct intel_dpll_hw_state *hw_state)

    write hw_state to dmesg

    :param dev_priv:
        i915 drm device
    :type dev_priv: struct drm_i915_private \*

    :param hw_state:
        hw state to be written to the log
    :type hw_state: struct intel_dpll_hw_state \*

.. _`intel_dpll_dump_hw_state.description`:

Description
-----------

Write the relevant values in \ ``hw_state``\  to dmesg using DRM_DEBUG_KMS.

.. This file was automatic generated / don't edit.

