
.. _API-drm-object-property-set-value:

=============================
drm_object_property_set_value
=============================

*man drm_object_property_set_value(9)*

*4.6.0-rc1*

set the value of a property


Synopsis
========

.. c:function:: int drm_object_property_set_value( struct drm_mode_object * obj, struct drm_property * property, uint64_t val )

Arguments
=========

``obj``
    drm mode object to set property value for

``property``
    property to set

``val``
    value the property should be set to


Description
===========

This functions sets a given property on a given object. This function only changes the software state of the property, it does not call into the driver's ->set_property callback.


Returns
=======

Zero on success, error code on failure.
