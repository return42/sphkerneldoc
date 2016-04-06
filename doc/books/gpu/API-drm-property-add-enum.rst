
.. _API-drm-property-add-enum:

=====================
drm_property_add_enum
=====================

*man drm_property_add_enum(9)*

*4.6.0-rc1*

add a possible value to an enumeration property


Synopsis
========

.. c:function:: int drm_property_add_enum( struct drm_property * property, int index, uint64_t value, const char * name )

Arguments
=========

``property``
    enumeration property to change

``index``
    index of the new enumeration

``value``
    value of the new enumeration

``name``
    symbolic name of the new enumeration


Description
===========

This functions adds enumerations to a property.

It's use is deprecated, drivers should use one of the more specific helpers to directly create the property with all enumerations already attached.


Returns
=======

Zero on success, error code on failure.
