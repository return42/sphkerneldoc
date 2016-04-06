
.. _API-drm-gem-cma-prime-get-sg-table:

==============================
drm_gem_cma_prime_get_sg_table
==============================

*man drm_gem_cma_prime_get_sg_table(9)*

*4.6.0-rc1*

provide a scatter/gather table of pinned pages for a CMA GEM object


Synopsis
========

.. c:function:: struct sg_table ⋆ drm_gem_cma_prime_get_sg_table( struct drm_gem_object * obj )

Arguments
=========

``obj``
    GEM object


Description
===========

This function exports a scatter/gather table suitable for PRIME usage by calling the standard DMA mapping API. Drivers using the CMA helpers should set this as their DRM driver's
->``gem_prime_get_sg_table`` callback.


Returns
=======

A pointer to the scatter/gather table of pinned pages or NULL on failure.
