.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_atomic.c

.. _`atomic-modeset-support`:

atomic modeset support
======================

The functions here implement the state management and hardware programming
dispatch required by the atomic modeset infrastructure.
See intel_atomic_plane.c for the plane-specific atomic functionality.

.. _`intel_digital_connector_atomic_get_property`:

intel_digital_connector_atomic_get_property
===========================================

.. c:function:: int intel_digital_connector_atomic_get_property(struct drm_connector *connector, const struct drm_connector_state *state, struct drm_property *property, uint64_t *val)

    hook for connector->atomic_get_property.

    :param connector:
        Connector to get the property for.
    :type connector: struct drm_connector \*

    :param state:
        Connector state to retrieve the property from.
    :type state: const struct drm_connector_state \*

    :param property:
        Property to retrieve.
    :type property: struct drm_property \*

    :param val:
        Return value for the property.
    :type val: uint64_t \*

.. _`intel_digital_connector_atomic_get_property.description`:

Description
-----------

Returns the atomic property value for a digital connector.

.. _`intel_digital_connector_atomic_set_property`:

intel_digital_connector_atomic_set_property
===========================================

.. c:function:: int intel_digital_connector_atomic_set_property(struct drm_connector *connector, struct drm_connector_state *state, struct drm_property *property, uint64_t val)

    hook for connector->atomic_set_property.

    :param connector:
        Connector to set the property for.
    :type connector: struct drm_connector \*

    :param state:
        Connector state to set the property on.
    :type state: struct drm_connector_state \*

    :param property:
        Property to set.
    :type property: struct drm_property \*

    :param val:
        New value for the property.
    :type val: uint64_t

.. _`intel_digital_connector_atomic_set_property.description`:

Description
-----------

Sets the atomic property value for a digital connector.

.. _`intel_digital_connector_duplicate_state`:

intel_digital_connector_duplicate_state
=======================================

.. c:function:: struct drm_connector_state *intel_digital_connector_duplicate_state(struct drm_connector *connector)

    duplicate connector state

    :param connector:
        digital connector
    :type connector: struct drm_connector \*

.. _`intel_digital_connector_duplicate_state.description`:

Description
-----------

Allocates and returns a copy of the connector state (both common and
digital connector specific) for the specified connector.

.. _`intel_digital_connector_duplicate_state.return`:

Return
------

The newly allocated connector state, or NULL on failure.

.. _`intel_crtc_duplicate_state`:

intel_crtc_duplicate_state
==========================

.. c:function:: struct drm_crtc_state *intel_crtc_duplicate_state(struct drm_crtc *crtc)

    duplicate crtc state

    :param crtc:
        drm crtc
    :type crtc: struct drm_crtc \*

.. _`intel_crtc_duplicate_state.description`:

Description
-----------

Allocates and returns a copy of the crtc state (both common and
Intel-specific) for the specified crtc.

.. _`intel_crtc_duplicate_state.return`:

Return
------

The newly allocated crtc state, or NULL on failure.

.. _`intel_crtc_destroy_state`:

intel_crtc_destroy_state
========================

.. c:function:: void intel_crtc_destroy_state(struct drm_crtc *crtc, struct drm_crtc_state *state)

    destroy crtc state

    :param crtc:
        drm crtc
    :type crtc: struct drm_crtc \*

    :param state:
        the state to destroy
    :type state: struct drm_crtc_state \*

.. _`intel_crtc_destroy_state.description`:

Description
-----------

Destroys the crtc state (both common and Intel-specific) for the
specified crtc.

.. _`intel_atomic_setup_scalers`:

intel_atomic_setup_scalers
==========================

.. c:function:: int intel_atomic_setup_scalers(struct drm_i915_private *dev_priv, struct intel_crtc *intel_crtc, struct intel_crtc_state *crtc_state)

    setup scalers for crtc per staged requests

    :param dev_priv:
        i915 device
    :type dev_priv: struct drm_i915_private \*

    :param intel_crtc:
        intel crtc
    :type intel_crtc: struct intel_crtc \*

    :param crtc_state:
        incoming crtc_state to validate and setup scalers
    :type crtc_state: struct intel_crtc_state \*

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

