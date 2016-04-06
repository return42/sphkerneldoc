
.. _API-drm-gem-cma-prime-import-sg-table:

=================================
drm_gem_cma_prime_import_sg_table
=================================

*man drm_gem_cma_prime_import_sg_table(9)*

*4.6.0-rc1*

produce a CMA GEM object from another driver's scatter/gather table of pinned pages


Synopsis
========

.. c:function:: struct drm_gem_object ⋆ drm_gem_cma_prime_import_sg_table( struct drm_device * dev, struct dma_buf_attachment * attach, struct sg_table * sgt )

Arguments
=========

``dev``
    device to import into

``attach``
    DMA-BUF attachment

``sgt``
    scatter/gather table of pinned pages


Description
===========

This function imports a scatter/gather table exported via DMA-BUF by another driver. Imported buffers must be physically contiguous in memory (i.e. the scatter/gather table must
contain a single entry). Drivers that use the CMA helpers should set this as their DRM driver's ->``gem_prime_import_sg_table`` callback.


Returns
=======

A pointer to a newly created GEM object or an ERR_PTR-encoded negative error code on failure.
