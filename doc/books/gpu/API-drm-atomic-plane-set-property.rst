
.. _API-drm-atomic-plane-set-property:

=============================
drm_atomic_plane_set_property
=============================

*man drm_atomic_plane_set_property(9)*

*4.6.0-rc1*

set property on plane


Synopsis
========

.. c:function:: int drm_atomic_plane_set_property( struct drm_plane * plane, struct drm_plane_state * state, struct drm_property * property, uint64_t val )

Arguments
=========

``plane``
    the drm plane to set a property on

``state``
    the state object to update with the new property value

``property``
    the property to set

``val``
    the new property value


Description
===========

Use this instead of calling plane->atomic_set_property directly. This function handles generic/core properties and calls out to driver's ->``atomic_set_property`` for driver
properties. To ensure consistent behavior you must call this function rather than the driver hook directly.


RETURNS
=======

Zero on success, error code on failure
