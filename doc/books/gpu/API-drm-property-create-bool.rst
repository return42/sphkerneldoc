
.. _API-drm-property-create-bool:

========================
drm_property_create_bool
========================

*man drm_property_create_bool(9)*

*4.6.0-rc1*

create a new boolean property type


Synopsis
========

.. c:function:: struct drm_property ⋆ drm_property_create_bool( struct drm_device * dev, int flags, const char * name )

Arguments
=========

``dev``
    drm device

``flags``
    flags specifying the property type

``name``
    name of the property


Description
===========

This creates a new generic drm property which can then be attached to a drm object with drm_object_attach_property. The returned property object must be freed with
drm_property_destroy.

This is implemented as a ranged property with only {0, 1} as valid values.


Returns
=======

A pointer to the newly created property on success, NULL on failure.
