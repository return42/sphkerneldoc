
.. _API-drm-gem-prime-import:

====================
drm_gem_prime_import
====================

*man drm_gem_prime_import(9)*

*4.6.0-rc1*

helper library implementation of the import callback


Synopsis
========

.. c:function:: struct drm_gem_object ⋆ drm_gem_prime_import( struct drm_device * dev, struct dma_buf * dma_buf )

Arguments
=========

``dev``
    drm_device to import into

``dma_buf``
    dma-buf object to import


Description
===========

This is the implementation of the gem_prime_import functions for GEM drivers using the PRIME helpers.
