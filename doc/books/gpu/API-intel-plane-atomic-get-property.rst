.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-plane-atomic-get-property:

===============================
intel_plane_atomic_get_property
===============================

*man intel_plane_atomic_get_property(9)*

*4.6.0-rc5*

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

The DRM core does not store shadow copies of properties for
atomic-capable drivers. This entrypoint is used to fetch the current
value of a driver-specific plane property.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
