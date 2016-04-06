
.. _API-drm-mode-debug-printmodeline:

============================
drm_mode_debug_printmodeline
============================

*man drm_mode_debug_printmodeline(9)*

*4.6.0-rc1*

print a mode to dmesg


Synopsis
========

.. c:function:: void drm_mode_debug_printmodeline( const struct drm_display_mode * mode )

Arguments
=========

``mode``
    mode to print


Description
===========

Describe ``mode`` using DRM_DEBUG.
