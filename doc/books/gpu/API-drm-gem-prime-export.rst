
.. _API-drm-gem-prime-export:

====================
drm_gem_prime_export
====================

*man drm_gem_prime_export(9)*

*4.6.0-rc1*

helper library implementation of the export callback


Synopsis
========

.. c:function:: struct dma_buf ⋆ drm_gem_prime_export( struct drm_device * dev, struct drm_gem_object * obj, int flags )

Arguments
=========

``dev``
    drm_device to export from

``obj``
    GEM object to export

``flags``
    flags like DRM_CLOEXEC and DRM_RDWR


Description
===========

This is the implementation of the gem_prime_export functions for GEM drivers using the PRIME helpers.
