
.. _API-drm-primary-helper-destroy:

==========================
drm_primary_helper_destroy
==========================

*man drm_primary_helper_destroy(9)*

*4.6.0-rc1*

Helper for primary plane destruction


Synopsis
========

.. c:function:: void drm_primary_helper_destroy( struct drm_plane * plane )

Arguments
=========

``plane``
    plane to destroy


Description
===========

Provides a default plane destroy handler for primary planes. This handler is called during CRTC destruction. We disable the primary plane, remove it from the DRM plane list, and
deallocate the plane structure.
