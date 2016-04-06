
.. _API-drm-mode-create-from-cmdline-mode:

=================================
drm_mode_create_from_cmdline_mode
=================================

*man drm_mode_create_from_cmdline_mode(9)*

*4.6.0-rc1*

convert a command line modeline into a DRM display mode


Synopsis
========

.. c:function:: struct drm_display_mode ⋆ drm_mode_create_from_cmdline_mode( struct drm_device * dev, struct drm_cmdline_mode * cmd )

Arguments
=========

``dev``
    DRM device to create the new mode for

``cmd``
    input command line modeline


Returns
=======

Pointer to converted mode on success, NULL on error.
