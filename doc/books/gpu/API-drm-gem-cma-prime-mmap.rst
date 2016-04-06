
.. _API-drm-gem-cma-prime-mmap:

======================
drm_gem_cma_prime_mmap
======================

*man drm_gem_cma_prime_mmap(9)*

*4.6.0-rc1*

memory-map an exported CMA GEM object


Synopsis
========

.. c:function:: int drm_gem_cma_prime_mmap( struct drm_gem_object * obj, struct vm_area_struct * vma )

Arguments
=========

``obj``
    GEM object

``vma``
    VMA for the area to be mapped


Description
===========

This function maps a buffer imported via DRM PRIME into a userspace process's address space. Drivers that use the CMA helpers should set this as their DRM driver's
->``gem_prime_mmap`` callback.


Returns
=======

0 on success or a negative error code on failure.
