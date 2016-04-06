
.. _API-drm-helper-crtc-mode-set-base:

=============================
drm_helper_crtc_mode_set_base
=============================

*man drm_helper_crtc_mode_set_base(9)*

*4.6.0-rc1*

mode_set_base implementation for atomic plane helpers


Synopsis
========

.. c:function:: int drm_helper_crtc_mode_set_base( struct drm_crtc * crtc, int x, int y, struct drm_framebuffer * old_fb )

Arguments
=========

``crtc``
    DRM CRTC

``x``
    x offset of the CRTC scanout area on the underlying framebuffer

``y``
    y offset of the CRTC scanout area on the underlying framebuffer

``old_fb``
    previous framebuffer


Description
===========

This function implements a callback useable as the ->mode_set_base used required by the CRTC helpers. The driver must provide the atomic plane helper functions for the primary
plane.

This is a transitional helper useful for converting drivers to the atomic interfaces.
