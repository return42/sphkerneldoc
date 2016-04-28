.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-crtc-get-property:

============================
drm_atomic_crtc_get_property
============================

*man drm_atomic_crtc_get_property(9)*

*4.6.0-rc5*

get property value from CRTC state


Synopsis
========

.. c:function:: int drm_atomic_crtc_get_property( struct drm_crtc * crtc, const struct drm_crtc_state * state, struct drm_property * property, uint64_t * val )

Arguments
=========

``crtc``
    the drm CRTC to set a property on

``state``
    the state object to get the property value from

``property``
    the property to set

``val``
    return location for the property value


Description
===========

This function handles generic/core properties and calls out to driver's
->``atomic_get_property`` for driver properties. To ensure consistent
behavior you must call this function rather than the driver hook
directly.


RETURNS
=======

Zero on success, error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
