.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_gem_cma_helper.h

.. _`drm_gem_cma_object`:

struct drm_gem_cma_object
=========================

.. c:type:: struct drm_gem_cma_object

    GEM object backed by CMA memory allocations

.. _`drm_gem_cma_object.definition`:

Definition
----------

.. code-block:: c

    struct drm_gem_cma_object {
        struct drm_gem_object base;
        dma_addr_t paddr;
        struct sg_table *sgt;
        void *vaddr;
    }

.. _`drm_gem_cma_object.members`:

Members
-------

base
    base GEM object

paddr
    physical address of the backing memory

sgt
    scatter/gather table for imported PRIME buffers

vaddr
    kernel virtual address of the backing memory

.. This file was automatic generated / don't edit.

