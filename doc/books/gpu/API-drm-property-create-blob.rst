
.. _API-drm-property-create-blob:

========================
drm_property_create_blob
========================

*man drm_property_create_blob(9)*

*4.6.0-rc1*

Create new blob property


Synopsis
========

.. c:function:: struct drm_property_blob ⋆ drm_property_create_blob( struct drm_device * dev, size_t length, const void * data )

Arguments
=========

``dev``
    DRM device to create property for

``length``
    Length to allocate for blob data

``data``
    If specified, copies data into blob


Description
===========

Creates a new blob property for a specified DRM device, optionally copying data.


Returns
=======

New blob property with a single reference on success, or an ERR_PTR value on failure.
