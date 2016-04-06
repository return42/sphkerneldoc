
.. _API-struct-drm-mode-config:

======================
struct drm_mode_config
======================

*man struct drm_mode_config(9)*

*4.6.0-rc1*

Mode configuration control structure


Synopsis
========

.. code-block:: c

    struct drm_mode_config {
      struct mutex mutex;
      struct drm_modeset_lock connection_mutex;
      struct drm_modeset_acquire_ctx * acquire_ctx;
      struct mutex idr_mutex;
      struct idr crtc_idr;
      struct mutex fb_lock;
      int num_fb;
      struct list_head fb_list;
      int num_connector;
      struct list_head connector_list;
      int num_encoder;
      struct list_head encoder_list;
      int num_overlay_plane;
      int num_total_plane;
      struct list_head plane_list;
      int num_crtc;
      struct list_head crtc_list;
      struct list_head property_list;
      int min_width;
      int min_height;
      int max_width;
      int max_height;
      const struct drm_mode_config_funcs * funcs;
      resource_size_t fb_base;
      bool poll_enabled;
      bool poll_running;
      struct delayed_work output_poll_work;
      struct mutex blob_lock;
      struct list_head property_blob_list;
      struct drm_property * degamma_lut_property;
      struct drm_property * degamma_lut_size_property;
      struct drm_property * ctm_property;
      struct drm_property * gamma_lut_property;
      struct drm_property * gamma_lut_size_property;
      uint32_t preferred_depth;
      uint32_t prefer_shadow;
      bool async_page_flip;
      uint32_t cursor_width;
      uint32_t cursor_height;
    };


Members
=======

mutex
    mutex protecting KMS related lists and structures

connection_mutex
    ww mutex protecting connector state and routing

acquire_ctx
    global implicit acquire context used by atomic drivers for legacy IOCTLs

idr_mutex
    mutex for KMS ID allocation and management

crtc_idr
    main KMS ID tracking object

fb_lock
    mutex to protect fb state and lists

num_fb
    number of fbs available

fb_list
    list of framebuffers available

num_connector
    number of connectors on this device

connector_list
    list of connector objects

num_encoder
    number of encoders on this device

encoder_list
    list of encoder objects

num_overlay_plane
    number of overlay planes on this device

num_total_plane
    number of universal (i.e. with primary/curso) planes on this device

plane_list
    list of plane objects

num_crtc
    number of CRTCs on this device

crtc_list
    list of CRTC objects

property_list
    list of property objects

min_width
    minimum pixel width on this device

min_height
    minimum pixel height on this device

max_width
    maximum pixel width on this device

max_height
    maximum pixel height on this device

funcs
    core driver provided mode setting functions

fb_base
    base address of the framebuffer

poll_enabled
    track polling support for this device

poll_running
    track polling status for this device

output_poll_work
    delayed work for polling in process context

blob_lock
    mutex for blob property allocation and management

property_blob_list
    list of all the blob property objects

degamma_lut_property
    LUT used to convert the framebuffer's colors to linear gamma

degamma_lut_size_property
    size of the degamma LUT as supported by the driver (read-only)

ctm_property
    Matrix used to convert colors after the lookup in the degamma LUT

gamma_lut_property
    LUT used to convert the colors, after the CSC matrix, to the gamma space of the connected screen (read-only)

gamma_lut_size_property
    size of the gamma LUT as supported by the driver

preferred_depth
    preferred RBG pixel depth, used by fb helpers

prefer_shadow
    hint to userspace to prefer shadow-fb rendering

async_page_flip
    does this device support async flips on the primary plane?

cursor_width
    hint to userspace for max cursor width

cursor_height
    hint to userspace for max cursor height


_property
=========

core property tracking


Description
===========

Core mode resource tracking structure. All CRTC, encoders, and connectors enumerated by the driver are added here, as are global properties. Some global restrictions are also here,
e.g. dimension restrictions.
