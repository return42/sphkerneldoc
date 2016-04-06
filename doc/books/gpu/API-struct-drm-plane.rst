
.. _API-struct-drm-plane:

================
struct drm_plane
================

*man struct drm_plane(9)*

*4.6.0-rc1*

central DRM plane control structure


Synopsis
========

.. code-block:: c

    struct drm_plane {
      struct drm_device * dev;
      struct list_head head;
      struct drm_mode_object base;
      uint32_t possible_crtcs;
      uint32_t * format_types;
      unsigned int format_count;
      bool format_default;
      struct drm_crtc * crtc;
      struct drm_framebuffer * fb;
      struct drm_framebuffer * old_fb;
      const struct drm_plane_funcs * funcs;
      struct drm_object_properties properties;
      enum drm_plane_type type;
      struct drm_plane_state * state;
    };


Members
=======

dev
    DRM device this plane belongs to

head
    for list management

base
    base mode object

possible_crtcs
    pipes this plane can be bound to

format_types
    array of formats supported by this plane

format_count
    number of formats supported

format_default
    driver hasn't supplied supported formats for the plane

crtc
    currently bound CRTC

fb
    currently bound fb

old_fb
    Temporary tracking of the old fb while a modeset is ongoing. Used by ``drm_mode_set_config_internal`` to implement correct refcounting.

funcs
    helper functions

properties
    property tracking for this plane

type
    type of plane (overlay, primary, cursor)

state
    current atomic state for this plane
