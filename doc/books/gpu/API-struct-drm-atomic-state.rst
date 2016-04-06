
.. _API-struct-drm-atomic-state:

=======================
struct drm_atomic_state
=======================

*man struct drm_atomic_state(9)*

*4.6.0-rc1*

the global state object for atomic updates


Synopsis
========

.. code-block:: c

    struct drm_atomic_state {
      struct drm_device * dev;
      bool allow_modeset:1;
      bool legacy_cursor_update:1;
      bool legacy_set_config:1;
      struct drm_plane ** planes;
      struct drm_plane_state ** plane_states;
      struct drm_crtc ** crtcs;
      struct drm_crtc_state ** crtc_states;
      int num_connector;
      struct drm_connector ** connectors;
      struct drm_connector_state ** connector_states;
      struct drm_modeset_acquire_ctx * acquire_ctx;
    };


Members
=======

dev
    parent DRM device

allow_modeset
    allow full modeset

legacy_cursor_update
    hint to enforce legacy cursor IOCTL semantics

legacy_set_config
    Disable conflicting encoders instead of failing with -EINVAL.

planes
    pointer to array of plane pointers

plane_states
    pointer to array of plane states pointers

crtcs
    pointer to array of CRTC pointers

crtc_states
    pointer to array of CRTC states pointers

num_connector
    size of the ``connectors`` and ``connector_states`` arrays

connectors
    pointer to array of connector pointers

connector_states
    pointer to array of connector states pointers

acquire_ctx
    acquire context for this atomic modeset state update
