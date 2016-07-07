.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_atomic.h

.. _`drm_atomic_get_existing_crtc_state`:

drm_atomic_get_existing_crtc_state
==================================

.. c:function:: struct drm_crtc_state *drm_atomic_get_existing_crtc_state(struct drm_atomic_state *state, struct drm_crtc *crtc)

    get crtc state, if it exists

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_crtc \*crtc:
        crtc to grab

.. _`drm_atomic_get_existing_crtc_state.description`:

Description
-----------

This function returns the crtc state for the given crtc, or NULL
if the crtc is not part of the global atomic state.

.. _`drm_atomic_get_existing_plane_state`:

drm_atomic_get_existing_plane_state
===================================

.. c:function:: struct drm_plane_state *drm_atomic_get_existing_plane_state(struct drm_atomic_state *state, struct drm_plane *plane)

    get plane state, if it exists

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_plane \*plane:
        plane to grab

.. _`drm_atomic_get_existing_plane_state.description`:

Description
-----------

This function returns the plane state for the given plane, or NULL
if the plane is not part of the global atomic state.

.. _`drm_atomic_get_existing_connector_state`:

drm_atomic_get_existing_connector_state
=======================================

.. c:function:: struct drm_connector_state *drm_atomic_get_existing_connector_state(struct drm_atomic_state *state, struct drm_connector *connector)

    get connector state, if it exists

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_connector \*connector:
        connector to grab

.. _`drm_atomic_get_existing_connector_state.description`:

Description
-----------

This function returns the connector state for the given connector,
or NULL if the connector is not part of the global atomic state.

.. _`__drm_atomic_get_current_plane_state`:

__drm_atomic_get_current_plane_state
====================================

.. c:function:: const struct drm_plane_state *__drm_atomic_get_current_plane_state(struct drm_atomic_state *state, struct drm_plane *plane)

    get current plane state

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_plane \*plane:
        plane to grab

.. _`__drm_atomic_get_current_plane_state.description`:

Description
-----------

This function returns the plane state for the given plane, either from
\ ``state``\ , or if the plane isn't part of the atomic state update, from \ ``plane``\ .
This is useful in atomic check callbacks, when drivers need to peek at, but
not change, state of other planes, since it avoids threading an error code
back up the call chain.

.. _`__drm_atomic_get_current_plane_state.warning`:

WARNING
-------


Note that this function is in general unsafe since it doesn't check for the
required locking for access state structures. Drivers must ensure that it is
safe to access the returned state structure through other means. One common
example is when planes are fixed to a single CRTC, and the driver knows that
the CRTC lock is held already. In that case holding the CRTC lock gives a
read-lock on all planes connected to that CRTC. But if planes can be
reassigned things get more tricky. In that case it's better to use
drm_atomic_get_plane_state and wire up full error handling.

.. _`__drm_atomic_get_current_plane_state.return`:

Return
------


Read-only pointer to the current plane state.

.. _`drm_atomic_crtc_needs_modeset`:

drm_atomic_crtc_needs_modeset
=============================

.. c:function:: bool drm_atomic_crtc_needs_modeset(struct drm_crtc_state *state)

    compute combined modeset need

    :param struct drm_crtc_state \*state:
        \ :c:type:`struct drm_crtc_state <drm_crtc_state>` for the CRTC

.. _`drm_atomic_crtc_needs_modeset.description`:

Description
-----------

To give drivers flexibility struct \ :c:type:`struct drm_crtc_state <drm_crtc_state>` has 3 booleans to track

.. _`drm_atomic_crtc_needs_modeset.whether-the-state-crtc-changed-enough-to-need-a-full-modeset-cycle`:

whether the state CRTC changed enough to need a full modeset cycle
------------------------------------------------------------------

connectors_changed, mode_changed and active_change. This helper simply
combines these three to compute the overall need for a modeset for \ ``state``\ .

.. This file was automatic generated / don't edit.

