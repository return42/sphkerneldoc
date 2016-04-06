
.. _API-struct-drm-gem-cma-object:

=========================
struct drm_gem_cma_object
=========================

*man struct drm_gem_cma_object(9)*

*4.6.0-rc1*

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
