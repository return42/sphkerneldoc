.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-cma-prime-vunmap:

========================
drm_gem_cma_prime_vunmap
========================

*man drm_gem_cma_prime_vunmap(9)*

*4.6.0-rc5*

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

This function removes a buffer exported via DRM PRIME from the kernel's
virtual address space. This is a no-op because CMA buffers cannot be
unmapped from kernel space. Drivers using the CMA helpers should set
this as their DRM driver's ->``gem_prime_vunmap`` callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
