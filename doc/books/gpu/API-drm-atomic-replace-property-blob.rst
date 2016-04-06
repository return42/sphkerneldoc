
.. _API-drm-atomic-replace-property-blob:

================================
drm_atomic_replace_property_blob
================================

*man drm_atomic_replace_property_blob(9)*

*4.6.0-rc1*

replace a blob property


Synopsis
========

.. c:function:: void drm_atomic_replace_property_blob( struct drm_property_blob ** blob, struct drm_property_blob * new_blob, bool * replaced )

Arguments
=========

``blob``
    a pointer to the member blob to be replaced

``new_blob``
    the new blob to replace with

``replaced``
    whether the blob has been replaced


RETURNS
=======

Zero on success, error code on failure
