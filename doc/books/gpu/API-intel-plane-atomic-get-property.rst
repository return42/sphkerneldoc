
.. _API-intel-plane-atomic-get-property:

===============================
intel_plane_atomic_get_property
===============================

*man intel_plane_atomic_get_property(9)*

*4.6.0-rc1*

fetch plane property value


Synopsis
========

.. c:function:: int intel_plane_atomic_get_property( struct drm_plane * plane, const struct drm_plane_state * state, struct drm_property * property, uint64_t * val )

Arguments
=========

``plane``
    plane to fetch property for

``state``
    state containing the property value

``property``
    property to look up

``val``
    pointer to write property value into


Description
===========

The DRM core does not store shadow copies of properties for atomic-capable drivers. This entrypoint is used to fetch the current value of a driver-specific plane property.
