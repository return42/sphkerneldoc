
.. _API-drm-property-lookup-blob:

========================
drm_property_lookup_blob
========================

*man drm_property_lookup_blob(9)*

*4.6.0-rc1*

look up a blob property and take a reference


Synopsis
========

.. c:function:: struct drm_property_blob ⋆ drm_property_lookup_blob( struct drm_device * dev, uint32_t id )

Arguments
=========

``dev``
    drm device

``id``
    id of the blob property


Description
===========

If successful, this takes an additional reference to the blob property. callers need to make sure to eventually unreference the returned property again, using
``drm_property_unreference_blob``.
