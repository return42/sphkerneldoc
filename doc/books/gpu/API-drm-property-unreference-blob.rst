
.. _API-drm-property-unreference-blob:

=============================
drm_property_unreference_blob
=============================

*man drm_property_unreference_blob(9)*

*4.6.0-rc1*

Unreference a blob property


Synopsis
========

.. c:function:: void drm_property_unreference_blob( struct drm_property_blob * blob )

Arguments
=========

``blob``
    Pointer to blob property


Description
===========

Drop a reference on a blob property. May free the object.
