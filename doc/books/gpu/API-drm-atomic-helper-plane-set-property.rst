
.. _API-drm-atomic-helper-plane-set-property:

====================================
drm_atomic_helper_plane_set_property
====================================

*man drm_atomic_helper_plane_set_property(9)*

*4.6.0-rc1*

helper for plane properties


Synopsis
========

.. c:function:: int drm_atomic_helper_plane_set_property( struct drm_plane * plane, struct drm_property * property, uint64_t val )

Arguments
=========

``plane``
    DRM plane

``property``
    DRM property

``val``
    value of property


Description
===========

Provides a default plane set_property handler using the atomic driver interface.


RETURNS
=======

Zero on success, error code on failure
