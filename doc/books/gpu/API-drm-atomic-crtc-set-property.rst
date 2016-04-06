
.. _API-drm-atomic-crtc-set-property:

============================
drm_atomic_crtc_set_property
============================

*man drm_atomic_crtc_set_property(9)*

*4.6.0-rc1*

set property on CRTC


Synopsis
========

.. c:function:: int drm_atomic_crtc_set_property( struct drm_crtc * crtc, struct drm_crtc_state * state, struct drm_property * property, uint64_t val )

Arguments
=========

``crtc``
    the drm CRTC to set a property on

``state``
    the state object to update with the new property value

``property``
    the property to set

``val``
    the new property value


Description
===========

Use this instead of calling crtc->atomic_set_property directly. This function handles generic/core properties and calls out to driver's ->``atomic_set_property`` for driver
properties. To ensure consistent behavior you must call this function rather than the driver hook directly.


RETURNS
=======

Zero on success, error code on failure
