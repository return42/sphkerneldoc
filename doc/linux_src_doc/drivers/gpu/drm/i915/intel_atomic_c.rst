.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_atomic.c

.. _`intel_connector_atomic_get_property`:

intel_connector_atomic_get_property
===================================

.. c:function:: int intel_connector_atomic_get_property(struct drm_connector *connector, const struct drm_connector_state *state, struct drm_property *property, uint64_t *val)

    fetch connector property value

    :param struct drm_connector \*connector:
        connector to fetch property for

    :param const struct drm_connector_state \*state:
        state containing the property value

    :param struct drm_property \*property:
        property to look up

    :param uint64_t \*val:
        pointer to write property value into

.. _`intel_connector_atomic_get_property.description`:

Description
-----------

The DRM core does not store shadow copies of properties for
atomic-capable drivers.  This entrypoint is used to fetch
the current value of a driver-specific connector property.

.. _`intel_crtc_destroy_state`:

intel_crtc_destroy_state
========================

.. c:function:: void intel_crtc_destroy_state(struct drm_crtc *crtc, struct drm_crtc_state *state)

    destroy crtc state

    :param struct drm_crtc \*crtc:
        drm crtc

    :param struct drm_crtc_state \*state:
        *undescribed*

.. _`intel_crtc_destroy_state.description`:

Description
-----------

Destroys the crtc state (both common and Intel-specific) for the
specified crtc.

.. _`intel_atomic_setup_scalers`:

intel_atomic_setup_scalers
==========================

.. c:function:: int intel_atomic_setup_scalers(struct drm_device *dev, struct intel_crtc *intel_crtc, struct intel_crtc_state *crtc_state)

    setup scalers for crtc per staged requests

    :param struct drm_device \*dev:
        DRM device

    :param struct intel_crtc \*intel_crtc:
        *undescribed*

    :param struct intel_crtc_state \*crtc_state:
        incoming crtc_state to validate and setup scalers

.. _`intel_atomic_setup_scalers.description`:

Description
-----------

This function sets up scalers based on staged scaling requests for
a \ ``crtc``\  and its planes. It is called from crtc level check path. If request
is a supportable request, it attaches scalers to requested planes and crtc.

This function takes into account the current scaler(s) in use by any planes
not being part of this atomic state

.. _`intel_atomic_setup_scalers.return`:

Return
------

0 - scalers were setup succesfully
error code - otherwise

.. This file was automatic generated / don't edit.

