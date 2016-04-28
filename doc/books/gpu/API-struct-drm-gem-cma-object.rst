.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-gem-cma-object:

=========================
struct drm_gem_cma_object
=========================

*man struct drm_gem_cma_object(9)*

*4.6.0-rc5*

GEM object backed by CMA memory allocations


Synopsis
========

.. code-block:: c

    struct drm_gem_cma_object {
      struct drm_gem_object base;
      dma_addr_t paddr;
      struct sg_table * sgt;
      void * vaddr;
    };


Members
=======

base
    base GEM object

paddr
    physical address of the backing memory

sgt
    scatter/gather table for imported PRIME buffers

vaddr
    kernel virtual address of the backing memory


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
