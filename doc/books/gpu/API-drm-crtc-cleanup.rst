
.. _API-drm-crtc-cleanup:

================
drm_crtc_cleanup
================

*man drm_crtc_cleanup(9)*

*4.6.0-rc1*

Clean up the core crtc usage


Synopsis
========

.. c:function:: void drm_crtc_cleanup( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    CRTC to cleanup


Description
===========

This function cleans up ``crtc`` and removes it from the DRM mode setting core. Note that the function does ⋆not⋆ free the crtc structure itself, this is the responsibility of the
caller.
