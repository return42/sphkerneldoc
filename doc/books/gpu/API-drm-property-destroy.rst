
.. _API-drm-property-destroy:

====================
drm_property_destroy
====================

*man drm_property_destroy(9)*

*4.6.0-rc1*

destroy a drm property


Synopsis
========

.. c:function:: void drm_property_destroy( struct drm_device * dev, struct drm_property * property )

Arguments
=========

``dev``
    drm device

``property``
    property to destry


Description
===========

This function frees a property including any attached resources like enumeration values.
