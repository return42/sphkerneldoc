.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_psr.c

.. _`panel-self-refresh--psr-srd-`:

Panel Self Refresh (PSR/SRD)
============================

Since Haswell Display controller supports Panel Self-Refresh on display
panels witch have a remote frame buffer (RFB) implemented according to PSR
spec in eDP1.3. PSR feature allows the display to go to lower standby states
when system is idle but display is on as it eliminates display refresh
request to DDR memory completely as long as the frame buffer for that
display is unchanged.

Panel Self Refresh must be supported by both Hardware (source) and
Panel (sink).

PSR saves power by caching the framebuffer in the panel RFB, which allows us
to power down the link and memory controller. For DSI panels the same idea
is called "manual mode".

The implementation uses the hardware-based PSR support which automatically
enters/exits self-refresh mode. The hardware takes care of sending the
required DP aux message and could even retrain the link (that part isn't
enabled yet though). The hardware also keeps track of any frontbuffer
changes to know when to exit self-refresh mode again. Unfortunately that
part doesn't work too well, hence why the i915 PSR support uses the
software frontbuffer tracking to make sure it doesn't miss a screen
update. For this integration \ :c:func:`intel_psr_invalidate`\  and \ :c:func:`intel_psr_flush`\ 
get called by the frontbuffer tracking code. Note that because of locking
issues the self-refresh re-enable code is done from a work queue, which
must be correctly synchronized/cancelled when shutting down the pipe."

.. _`intel_psr_enable`:

intel_psr_enable
================

.. c:function:: void intel_psr_enable(struct intel_dp *intel_dp, const struct intel_crtc_state *crtc_state)

    Enable PSR

    :param struct intel_dp \*intel_dp:
        Intel DP

    :param const struct intel_crtc_state \*crtc_state:
        new CRTC state

.. _`intel_psr_enable.description`:

Description
-----------

This function can only be called after the pipe is fully trained and enabled.

.. _`intel_psr_disable`:

intel_psr_disable
=================

.. c:function:: void intel_psr_disable(struct intel_dp *intel_dp, const struct intel_crtc_state *old_crtc_state)

    Disable PSR

    :param struct intel_dp \*intel_dp:
        Intel DP

    :param const struct intel_crtc_state \*old_crtc_state:
        old CRTC state

.. _`intel_psr_disable.description`:

Description
-----------

This function needs to be called before disabling pipe.

.. _`intel_psr_single_frame_update`:

intel_psr_single_frame_update
=============================

.. c:function:: void intel_psr_single_frame_update(struct drm_i915_private *dev_priv, unsigned frontbuffer_bits)

    Single Frame Update

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits

.. _`intel_psr_single_frame_update.description`:

Description
-----------

Some platforms support a single frame update feature that is used to
send and update only one frame on Remote Frame Buffer.
So far it is only implemented for Valleyview and Cherryview because
hardware requires this to be done before a page flip.

.. _`intel_psr_invalidate`:

intel_psr_invalidate
====================

.. c:function:: void intel_psr_invalidate(struct drm_i915_private *dev_priv, unsigned frontbuffer_bits)

    Invalidade PSR

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits

.. _`intel_psr_invalidate.description`:

Description
-----------

Since the hardware frontbuffer tracking has gaps we need to integrate
with the software frontbuffer tracking. This function gets called every
time frontbuffer rendering starts and a buffer gets dirtied. PSR must be
disabled if the frontbuffer mask contains a buffer relevant to PSR.

Dirty frontbuffers relevant to PSR are tracked in busy_frontbuffer_bits."

.. _`intel_psr_flush`:

intel_psr_flush
===============

.. c:function:: void intel_psr_flush(struct drm_i915_private *dev_priv, unsigned frontbuffer_bits, enum fb_op_origin origin)

    Flush PSR

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits

    :param enum fb_op_origin origin:
        which operation caused the flush

.. _`intel_psr_flush.description`:

Description
-----------

Since the hardware frontbuffer tracking has gaps we need to integrate
with the software frontbuffer tracking. This function gets called every
time frontbuffer rendering has completed and flushed out to memory. PSR
can be enabled again if no other frontbuffer relevant to PSR is dirty.

Dirty frontbuffers relevant to PSR are tracked in busy_frontbuffer_bits.

.. _`intel_psr_init`:

intel_psr_init
==============

.. c:function:: void intel_psr_init(struct drm_i915_private *dev_priv)

    Init basic PSR work and mutex.

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`intel_psr_init.description`:

Description
-----------

This function is  called only once at driver load to initialize basic
PSR stuff.

.. This file was automatic generated / don't edit.

