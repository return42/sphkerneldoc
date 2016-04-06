
.. _API-intel-plane-atomic-set-property:

===============================
intel_plane_atomic_set_property
===============================

*man intel_plane_atomic_set_property(9)*

*4.6.0-rc1*

set plane property value


Synopsis
========

.. c:function:: int intel_plane_atomic_set_property( struct drm_plane * plane, struct drm_plane_state * state, struct drm_property * property, uint64_t val )

Arguments
=========

``plane``
    plane to set property for

``state``
    state to update property value in

``property``
    property to set

``val``
    value to set property to


Description
===========

Writes the specified property value for a plane into the provided atomic state object.

Returns 0 on success, -EINVAL on unrecognized properties
