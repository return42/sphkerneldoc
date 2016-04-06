
.. _API-drm-property-create-bitmask:

===========================
drm_property_create_bitmask
===========================

*man drm_property_create_bitmask(9)*

*4.6.0-rc1*

create a new bitmask property type


Synopsis
========

.. c:function:: struct drm_property ⋆ drm_property_create_bitmask( struct drm_device * dev, int flags, const char * name, const struct drm_prop_enum_list * props, int num_props, uint64_t supported_bits )

Arguments
=========

``dev``
    drm device

``flags``
    flags specifying the property type

``name``
    name of the property

``props``
    enumeration lists with property bitflags

``num_props``
    size of the ``props`` array

``supported_bits``
    bitmask of all supported enumeration values


Description
===========

This creates a new bitmask drm property which can then be attached to a drm object with drm_object_attach_property. The returned property object must be freed with
drm_property_destroy.

Compared to plain enumeration properties userspace is allowed to set any or'ed together combination of the predefined property bitflag values


Returns
=======

A pointer to the newly created property on success, NULL on failure.
