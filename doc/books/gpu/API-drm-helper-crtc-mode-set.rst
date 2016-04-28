.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-helper-crtc-mode-set:

========================
drm_helper_crtc_mode_set
========================

*man drm_helper_crtc_mode_set(9)*

*4.6.0-rc5*

mode_set implementation for atomic plane helpers


Synopsis
========

.. c:function:: int drm_helper_crtc_mode_set( struct drm_crtc * crtc, struct drm_display_mode * mode, struct drm_display_mode * adjusted_mode, int x, int y, struct drm_framebuffer * old_fb )

Arguments
=========

``crtc``
    DRM CRTC

``mode``
    DRM display mode which userspace requested

``adjusted_mode``
    DRM display mode adjusted by ->mode_fixup callbacks

``x``
    x offset of the CRTC scanout area on the underlying framebuffer

``y``
    y offset of the CRTC scanout area on the underlying framebuffer

``old_fb``
    previous framebuffer


Description
===========

This function implements a callback useable as the ->mode_set callback
required by the CRTC helpers. Besides the atomic plane helper functions
for the primary plane the driver must also provide the ->mode_set_nofb
callback to set up the CRTC.

This is a transitional helper useful for converting drivers to the
atomic interfaces.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
