
.. _API-drm-atomic-helper-crtc-set-property:

===================================
drm_atomic_helper_crtc_set_property
===================================

*man drm_atomic_helper_crtc_set_property(9)*

*4.6.0-rc1*

helper for crtc properties


Synopsis
========

.. c:function:: int drm_atomic_helper_crtc_set_property( struct drm_crtc * crtc, struct drm_property * property, uint64_t val )

Arguments
=========

``crtc``
    DRM crtc

``property``
    DRM property

``val``
    value of property


Description
===========

Provides a default crtc set_property handler using the atomic driver interface.


RETURNS
=======

Zero on success, error code on failure
