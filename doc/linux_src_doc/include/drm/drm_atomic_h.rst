.. -*- coding: utf-8; mode: rst -*-

============
drm_atomic.h
============


.. _`drm_atomic_get_existing_crtc_state`:

drm_atomic_get_existing_crtc_state
==================================

.. c:function:: struct drm_crtc_state *drm_atomic_get_existing_crtc_state (struct drm_atomic_state *state, struct drm_crtc *crtc)

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

.. c:function:: struct drm_plane_state *drm_atomic_get_existing_plane_state (struct drm_atomic_state *state, struct drm_plane *plane)

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

.. c:function:: struct drm_connector_state *drm_atomic_get_existing_connector_state (struct drm_atomic_state *state, struct drm_connector *connector)

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

