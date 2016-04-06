
.. _API-drm-plane-cleanup:

=================
drm_plane_cleanup
=================

*man drm_plane_cleanup(9)*

*4.6.0-rc1*

Clean up the core plane usage


Synopsis
========

.. c:function:: void drm_plane_cleanup( struct drm_plane * plane )

Arguments
=========

``plane``
    plane to cleanup


Description
===========

This function cleans up ``plane`` and removes it from the DRM mode setting core. Note that the function does ⋆not⋆ free the plane structure itself, this is the responsibility of
the caller.
