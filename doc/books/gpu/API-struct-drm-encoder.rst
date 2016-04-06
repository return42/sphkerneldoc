
.. _API-struct-drm-encoder:

==================
struct drm_encoder
==================

*man struct drm_encoder(9)*

*4.6.0-rc1*

central DRM encoder structure


Synopsis
========

.. code-block:: c

    struct drm_encoder {
      struct drm_device * dev;
      struct list_head head;
      struct drm_mode_object base;
      char * name;
      int encoder_type;
      uint32_t possible_crtcs;
      uint32_t possible_clones;
      struct drm_crtc * crtc;
      struct drm_bridge * bridge;
      const struct drm_encoder_funcs * funcs;
      const struct drm_encoder_helper_funcs * helper_private;
    };


Members
=======

dev
    parent DRM device

head
    list management

base
    base KMS object

name
    encoder name

encoder_type
    one of the ``DRM_MODE_ENCODER_`` <foo> types in drm_mode.h

possible_crtcs
    bitmask of potential CRTC bindings

possible_clones
    bitmask of potential sibling encoders for cloning

crtc
    currently bound CRTC

bridge
    bridge associated to the encoder

funcs
    control functions

helper_private
    mid-layer private data


Description
===========

CRTCs drive pixels to encoders, which convert them into signals appropriate for a given connector or set of connectors.
