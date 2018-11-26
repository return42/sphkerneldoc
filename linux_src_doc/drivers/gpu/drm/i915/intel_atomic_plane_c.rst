.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_atomic_plane.c

.. _`atomic-plane-helpers`:

atomic plane helpers
====================

The functions here are used by the atomic plane helper functions to
implement legacy plane updates (i.e., drm_plane->update_plane() and
drm_plane->disable_plane()).  This allows plane updates to use the
atomic state infrastructure and perform plane updates as separate
prepare/check/commit/cleanup steps.

.. _`intel_create_plane_state`:

intel_create_plane_state
========================

.. c:function:: struct intel_plane_state *intel_create_plane_state(struct drm_plane *plane)

    create plane state object

    :param plane:
        drm plane
    :type plane: struct drm_plane \*

.. _`intel_create_plane_state.description`:

Description
-----------

Allocates a fresh plane state for the given plane and sets some of
the state values to sensible initial values.

.. _`intel_create_plane_state.return`:

Return
------

A newly allocated plane state, or NULL on failure

.. _`intel_plane_duplicate_state`:

intel_plane_duplicate_state
===========================

.. c:function:: struct drm_plane_state *intel_plane_duplicate_state(struct drm_plane *plane)

    duplicate plane state

    :param plane:
        drm plane
    :type plane: struct drm_plane \*

.. _`intel_plane_duplicate_state.description`:

Description
-----------

Allocates and returns a copy of the plane state (both common and
Intel-specific) for the specified plane.

.. _`intel_plane_duplicate_state.return`:

Return
------

The newly allocated plane state, or NULL on failure.

.. _`intel_plane_destroy_state`:

intel_plane_destroy_state
=========================

.. c:function:: void intel_plane_destroy_state(struct drm_plane *plane, struct drm_plane_state *state)

    destroy plane state

    :param plane:
        drm plane
    :type plane: struct drm_plane \*

    :param state:
        state object to destroy
    :type state: struct drm_plane_state \*

.. _`intel_plane_destroy_state.description`:

Description
-----------

Destroys the plane state (both common and Intel-specific) for the
specified plane.

.. _`intel_plane_atomic_get_property`:

intel_plane_atomic_get_property
===============================

.. c:function:: int intel_plane_atomic_get_property(struct drm_plane *plane, const struct drm_plane_state *state, struct drm_property *property, uint64_t *val)

    fetch plane property value

    :param plane:
        plane to fetch property for
    :type plane: struct drm_plane \*

    :param state:
        state containing the property value
    :type state: const struct drm_plane_state \*

    :param property:
        property to look up
    :type property: struct drm_property \*

    :param val:
        pointer to write property value into
    :type val: uint64_t \*

.. _`intel_plane_atomic_get_property.description`:

Description
-----------

The DRM core does not store shadow copies of properties for
atomic-capable drivers.  This entrypoint is used to fetch
the current value of a driver-specific plane property.

.. _`intel_plane_atomic_set_property`:

intel_plane_atomic_set_property
===============================

.. c:function:: int intel_plane_atomic_set_property(struct drm_plane *plane, struct drm_plane_state *state, struct drm_property *property, uint64_t val)

    set plane property value

    :param plane:
        plane to set property for
    :type plane: struct drm_plane \*

    :param state:
        state to update property value in
    :type state: struct drm_plane_state \*

    :param property:
        property to set
    :type property: struct drm_property \*

    :param val:
        value to set property to
    :type val: uint64_t

.. _`intel_plane_atomic_set_property.description`:

Description
-----------

Writes the specified property value for a plane into the provided atomic
state object.

Returns 0 on success, -EINVAL on unrecognized properties

.. This file was automatic generated / don't edit.

