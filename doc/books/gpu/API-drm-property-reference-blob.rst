
.. _API-drm-property-reference-blob:

===========================
drm_property_reference_blob
===========================

*man drm_property_reference_blob(9)*

*4.6.0-rc1*

Take a reference on an existing property


Synopsis
========

.. c:function:: struct drm_property_blob ⋆ drm_property_reference_blob( struct drm_property_blob * blob )

Arguments
=========

``blob``
    Pointer to blob property


Description
===========

Take a new reference on an existing blob property.
