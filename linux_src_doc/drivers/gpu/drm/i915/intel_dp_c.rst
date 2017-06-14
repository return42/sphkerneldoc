.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_dp.c

.. _`is_edp`:

is_edp
======

.. c:function:: bool is_edp(struct intel_dp *intel_dp)

    is the given port attached to an eDP panel (either CPU or PCH)

    :param struct intel_dp \*intel_dp:
        DP struct

.. _`is_edp.description`:

Description
-----------

If a CPU or PCH DP output is attached to an eDP panel, this function
will return true, and false otherwise.

.. _`intel_dp_set_drrs_state`:

intel_dp_set_drrs_state
=======================

.. c:function:: void intel_dp_set_drrs_state(struct drm_i915_private *dev_priv, struct intel_crtc_state *crtc_state, int refresh_rate)

    program registers for RR switch to take effect

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param struct intel_crtc_state \*crtc_state:
        a pointer to the active intel_crtc_state

    :param int refresh_rate:
        RR to be programmed

.. _`intel_dp_set_drrs_state.description`:

Description
-----------

This function gets called when refresh rate (RR) has to be changed from
one frequency to another. Switches can be between high and low RR
supported by the panel or to any other RR based on media playback (in
this case, RR value needs to be passed from user space).

The caller of this function needs to take a lock on dev_priv->drrs.

.. _`intel_edp_drrs_enable`:

intel_edp_drrs_enable
=====================

.. c:function:: void intel_edp_drrs_enable(struct intel_dp *intel_dp, struct intel_crtc_state *crtc_state)

    init drrs struct if supported

    :param struct intel_dp \*intel_dp:
        DP struct

    :param struct intel_crtc_state \*crtc_state:
        A pointer to the active crtc state.

.. _`intel_edp_drrs_enable.description`:

Description
-----------

Initializes frontbuffer_bits and drrs.dp

.. _`intel_edp_drrs_disable`:

intel_edp_drrs_disable
======================

.. c:function:: void intel_edp_drrs_disable(struct intel_dp *intel_dp, struct intel_crtc_state *old_crtc_state)

    Disable DRRS

    :param struct intel_dp \*intel_dp:
        DP struct

    :param struct intel_crtc_state \*old_crtc_state:
        Pointer to old crtc_state.

.. _`intel_edp_drrs_invalidate`:

intel_edp_drrs_invalidate
=========================

.. c:function:: void intel_edp_drrs_invalidate(struct drm_i915_private *dev_priv, unsigned int frontbuffer_bits)

    Disable Idleness DRRS

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param unsigned int frontbuffer_bits:
        frontbuffer plane tracking bits

.. _`intel_edp_drrs_invalidate.description`:

Description
-----------

This function gets called everytime rendering on the given planes start.
Hence DRRS needs to be Upclocked, i.e. (LOW_RR -> HIGH_RR).

Dirty frontbuffers relevant to DRRS are tracked in busy_frontbuffer_bits.

.. _`intel_edp_drrs_flush`:

intel_edp_drrs_flush
====================

.. c:function:: void intel_edp_drrs_flush(struct drm_i915_private *dev_priv, unsigned int frontbuffer_bits)

    Restart Idleness DRRS

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param unsigned int frontbuffer_bits:
        frontbuffer plane tracking bits

.. _`intel_edp_drrs_flush.description`:

Description
-----------

This function gets called every time rendering on the given planes has
completed or flip on a crtc is completed. So DRRS should be upclocked
(LOW_RR -> HIGH_RR). And also Idleness detection should be started again,
if no other planes are dirty.

Dirty frontbuffers relevant to DRRS are tracked in busy_frontbuffer_bits.

.. _`display-refresh-rate-switching--drrs-`:

Display Refresh Rate Switching (DRRS)
=====================================

Display Refresh Rate Switching (DRRS) is a power conservation feature
which enables swtching between low and high refresh rates,
dynamically, based on the usage scenario. This feature is applicable
for internal panels.

Indication that the panel supports DRRS is given by the panel EDID, which
would list multiple refresh rates for one resolution.

DRRS is of 2 types - static and seamless.
Static DRRS involves changing refresh rate (RR) by doing a full modeset
(may appear as a blink on screen) and is used in dock-undock scenario.
Seamless DRRS involves changing RR without any visual effect to the user
and can be used during normal system usage. This is done by programming
certain registers.

Support for static/seamless DRRS may be indicated in the VBT based on
inputs from the panel spec.

DRRS saves power by switching to low RR based on usage scenarios.

The implementation is based on frontbuffer tracking implementation.  When
there is a disturbance on the screen triggered by user activity or a periodic
system activity, DRRS is disabled (RR is changed to high RR).  When there is
no movement on screen, after a timeout of 1 second, a switch to low RR is
made.

For integration with frontbuffer tracking code, \ :c:func:`intel_edp_drrs_invalidate`\ 
and \ :c:func:`intel_edp_drrs_flush`\  are called.

DRRS can be further extended to support other internal panels and also
the scenario of video playback wherein RR is set based on the rate
requested by userspace.

.. _`intel_dp_drrs_init`:

intel_dp_drrs_init
==================

.. c:function:: struct drm_display_mode *intel_dp_drrs_init(struct intel_connector *intel_connector, struct drm_display_mode *fixed_mode)

    Init basic DRRS work and mutex.

    :param struct intel_connector \*intel_connector:
        eDP connector

    :param struct drm_display_mode \*fixed_mode:
        preferred mode of panel

.. _`intel_dp_drrs_init.description`:

Description
-----------

This function is  called only once at driver load to initialize basic
DRRS stuff.

.. _`intel_dp_drrs_init.return`:

Return
------

Downclock mode if panel supports it, else return NULL.
DRRS support is determined by the presence of downclock mode (apart
from VBT setting).

.. This file was automatic generated / don't edit.

