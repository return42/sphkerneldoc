
.. _API-drm-dev-ref:

===========
drm_dev_ref
===========

*man drm_dev_ref(9)*

*4.6.0-rc1*

Take reference of a DRM device


Synopsis
========

.. c:function:: void drm_dev_ref( struct drm_device * dev )

Arguments
=========

``dev``
    device to take reference of or NULL


Description
===========

This increases the ref-count of ``dev`` by one. You ⋆must⋆ already own a reference when calling this. Use ``drm_dev_unref`` to drop this reference again.

This function never fails. However, this function does not provide ⋆any⋆ guarantee whether the device is alive or running. It only provides a reference to the object and the memory
associated with it.
