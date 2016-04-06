
.. _API-drm-plane-helper-add:

====================
drm_plane_helper_add
====================

*man drm_plane_helper_add(9)*

*4.6.0-rc1*

sets the helper vtable for a plane


Synopsis
========

.. c:function:: void drm_plane_helper_add( struct drm_plane * plane, const struct drm_plane_helper_funcs * funcs )

Arguments
=========

``plane``
    DRM plane

``funcs``
    helper vtable to set for ``plane``
