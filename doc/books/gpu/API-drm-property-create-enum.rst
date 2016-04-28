.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-property-create-enum:

========================
drm_property_create_enum
========================

*man drm_property_create_enum(9)*

*4.6.0-rc5*

create a new enumeration property type


Synopsis
========

.. c:function:: struct drm_property * drm_property_create_enum( struct drm_device * dev, int flags, const char * name, const struct drm_prop_enum_list * props, int num_values )

Arguments
=========

``dev``
    drm device

``flags``
    flags specifying the property type

``name``
    name of the property

``props``
    enumeration lists with property values

``num_values``
    number of pre-defined values


Description
===========

This creates a new generic drm property which can then be attached to a
drm object with drm_object_attach_property. The returned property
object must be freed with drm_property_destroy.

Userspace is only allowed to set one of the predefined values for
enumeration properties.


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
