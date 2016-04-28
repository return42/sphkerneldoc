.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-property-create-signed-range:

================================
drm_property_create_signed_range
================================

*man drm_property_create_signed_range(9)*

*4.6.0-rc5*

create a new signed ranged property type


Synopsis
========

.. c:function:: struct drm_property * drm_property_create_signed_range( struct drm_device * dev, int flags, const char * name, int64_t min, int64_t max )

Arguments
=========

``dev``
    drm device

``flags``
    flags specifying the property type

``name``
    name of the property

``min``
    minimum value of the property

``max``
    maximum value of the property


Description
===========

This creates a new generic drm property which can then be attached to a
drm object with drm_object_attach_property. The returned property
object must be freed with drm_property_destroy.

Userspace is allowed to set any signed integer value in the (min, max)
range inclusive.


Returns
=======

A pointer to the newly created property on success, NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
