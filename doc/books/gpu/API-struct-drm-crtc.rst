
.. _API-struct-drm-crtc:

===============
struct drm_crtc
===============

*man struct drm_crtc(9)*

*4.6.0-rc1*

central CRTC control structure


Synopsis
========

.. code-block:: c

    struct drm_crtc {
      struct drm_device * dev;
      struct device_node * port;
      struct list_head head;
      struct drm_modeset_lock mutex;
      struct drm_mode_object base;
      struct drm_plane * primary;
      struct drm_plane * cursor;
      int cursor_x;
      int cursor_y;
      bool enabled;
      struct drm_display_mode mode;
      struct drm_display_mode hwmode;
      int x;
      int y;
      const struct drm_crtc_funcs * funcs;
      uint32_t gamma_size;
      uint16_t * gamma_store;
      const struct drm_crtc_helper_funcs * helper_private;
      struct drm_object_properties properties;
      struct drm_crtc_state * state;
      struct drm_modeset_acquire_ctx * acquire_ctx;
    };


Members
=======

dev
    parent DRM device

port
    OF node used by ``drm_of_find_possible_crtcs``

head
    list management

mutex
    per-CRTC locking

base
    base KMS object for ID tracking etc.

primary
    primary plane for this CRTC

cursor
    cursor plane for this CRTC

cursor_x
    current x position of the cursor, used for universal cursor planes

cursor_y
    current y position of the cursor, used for universal cursor planes

enabled
    is this CRTC enabled?

mode
    current mode timings

hwmode
    mode timings as programmed to hw regs

x
    x position on screen

y
    y position on screen

funcs
    CRTC control functions

gamma_size
    size of gamma ramp

gamma_store
    gamma ramp values

helper_private
    mid-layer private data

properties
    property tracking for this CRTC

state
    current atomic state for this CRTC

acquire_ctx
    per-CRTC implicit acquire context used by atomic drivers for legacy IOCTLs


Description
===========

Each CRTC may have one or more connectors associated with it. This structure allows the CRTC to be controlled.
