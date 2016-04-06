
.. _API-drm-object-property-get-value:

=============================
drm_object_property_get_value
=============================

*man drm_object_property_get_value(9)*

*4.6.0-rc1*

retrieve the value of a property


Synopsis
========

.. c:function:: int drm_object_property_get_value( struct drm_mode_object * obj, struct drm_property * property, uint64_t * val )

Arguments
=========

``obj``
    drm mode object to get property value from

``property``
    property to retrieve

``val``
    storage for the property value


Description
===========

This function retrieves the softare state of the given property for the given property. Since there is no driver callback to retrieve the current property value this might be out
of sync with the hardware, depending upon the driver and property.


Returns
=======

Zero on success, error code on failure.
