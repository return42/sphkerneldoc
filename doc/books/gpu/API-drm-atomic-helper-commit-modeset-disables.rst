
.. _API-drm-atomic-helper-commit-modeset-disables:

=========================================
drm_atomic_helper_commit_modeset_disables
=========================================

*man drm_atomic_helper_commit_modeset_disables(9)*

*4.6.0-rc1*

modeset commit to disable outputs


Synopsis
========

.. c:function:: void drm_atomic_helper_commit_modeset_disables( struct drm_device * dev, struct drm_atomic_state * old_state )

Arguments
=========

``dev``
    DRM device

``old_state``
    atomic state object with old state structures


Description
===========

This function shuts down all the outputs that need to be shut down and prepares them (if required) with the new mode.

For compatibility with legacy crtc helpers this should be called before ``drm_atomic_helper_commit_planes``, which is what the default commit function does. But drivers with
different needs can group the modeset commits together and do the plane commits at the end. This is useful for drivers doing runtime PM since planes updates then only happen when
the CRTC is actually enabled.
