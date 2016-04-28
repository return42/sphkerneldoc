.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-cma-prime-vmap:

======================
drm_gem_cma_prime_vmap
======================

*man drm_gem_cma_prime_vmap(9)*

*4.6.0-rc5*

map a CMA GEM object into the kernel's virtual address space


Synopsis
========

.. c:function:: void * drm_gem_cma_prime_vmap( struct drm_gem_object * obj )

Arguments
=========

``obj``
    GEM object


Description
===========

This function maps a buffer exported via DRM PRIME into the kernel's
virtual address space. Since the CMA buffers are already mapped into the
kernel virtual address space this simply returns the cached virtual
address. Drivers using the CMA helpers should set this as their DRM
driver's ->``gem_prime_vmap`` callback.


Returns
=======

The kernel virtual address of the CMA GEM object's backing store.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
