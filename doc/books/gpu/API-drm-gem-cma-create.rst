
.. _API-drm-gem-cma-create:

==================
drm_gem_cma_create
==================

*man drm_gem_cma_create(9)*

*4.6.0-rc1*

allocate an object with the given size


Synopsis
========

.. c:function:: struct drm_gem_cma_object ⋆ drm_gem_cma_create( struct drm_device * drm, size_t size )

Arguments
=========

``drm``
    DRM device

``size``
    size of the object to allocate


Description
===========

This function creates a CMA GEM object and allocates a contiguous chunk of memory as backing store. The backing memory has the writecombine attribute set.


Returns
=======

A struct drm_gem_cma_object ⋆ on success or an ``ERR_PTR``-encoded negative error code on failure.
