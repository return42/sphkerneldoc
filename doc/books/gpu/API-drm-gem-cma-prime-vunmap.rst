
.. _API-drm-gem-cma-prime-vunmap:

========================
drm_gem_cma_prime_vunmap
========================

*man drm_gem_cma_prime_vunmap(9)*

*4.6.0-rc1*

unmap a CMA GEM object from the kernel's virtual address space


Synopsis
========

.. c:function:: void drm_gem_cma_prime_vunmap( struct drm_gem_object * obj, void * vaddr )

Arguments
=========

``obj``
    GEM object

``vaddr``
    kernel virtual address where the CMA GEM object was mapped


Description
===========

This function removes a buffer exported via DRM PRIME from the kernel's virtual address space. This is a no-op because CMA buffers cannot be unmapped from kernel space. Drivers
using the CMA helpers should set this as their DRM driver's ->``gem_prime_vunmap`` callback.
