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

.. c:function:: void intel_dp_set_drrs_state(struct drm_device *dev, int refresh_rate)

    program registers for RR switch to take effect

    :param struct drm_device \*dev:
        DRM device

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

.. c:function:: void intel_edp_drrs_enable(struct intel_dp *intel_dp)

    init drrs struct if supported

    :param struct intel_dp \*intel_dp:
        DP struct

.. _`intel_edp_drrs_enable.description`:

Description
-----------

Initializes frontbuffer_bits and drrs.dp

.. _`intel_edp_drrs_disable`:

intel_edp_drrs_disable
======================

.. c:function:: void intel_edp_drrs_disable(struct intel_dp *intel_dp)

    Disable DRRS

    :param struct intel_dp \*intel_dp:
        DP struct

.. _`intel_edp_drrs_invalidate`:

intel_edp_drrs_invalidate
=========================

.. c:function:: void intel_edp_drrs_invalidate(struct drm_device *dev, unsigned frontbuffer_bits)

    Disable Idleness DRRS

    :param struct drm_device \*dev:
        DRM device

    :param unsigned frontbuffer_bits:
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

.. c:function:: void intel_edp_drrs_flush(struct drm_device *dev, unsigned frontbuffer_bits)

    Restart Idleness DRRS

    :param struct drm_device \*dev:
        DRM device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits

.. _`intel_edp_drrs_flush.description`:

Description
-----------

This function gets called every time rendering on the given planes has
completed or flip on a crtc is completed. So DRRS should be upclocked
(LOW_RR -> HIGH_RR). And also Idleness detection should be started again,
if no other planes are dirty.

Dirty frontbuffers relevant to DRRS are tracked in busy_frontbuffer_bits.

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
