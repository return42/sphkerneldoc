
.. _API-drm-crtc-check-viewport:

=======================
drm_crtc_check_viewport
=======================

*man drm_crtc_check_viewport(9)*

*4.6.0-rc1*

Checks that a framebuffer is big enough for the CRTC viewport


Synopsis
========

.. c:function:: int drm_crtc_check_viewport( const struct drm_crtc * crtc, int x, int y, const struct drm_display_mode * mode, const struct drm_framebuffer * fb )

Arguments
=========

``crtc``
    CRTC that framebuffer will be displayed on

``x``
    x panning

``y``
    y panning

``mode``
    mode that framebuffer will be displayed under

``fb``
    framebuffer to check size of
