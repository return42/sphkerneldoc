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
    scatter/gather table for imported PRIME buffers. The table can have
    more than one entry but they are guaranteed to have contiguous
    DMA addresses.

vaddr
    kernel virtual address of the backing memory

.. _`define_drm_gem_cma_fops`:

DEFINE_DRM_GEM_CMA_FOPS
=======================

.. c:function::  DEFINE_DRM_GEM_CMA_FOPS( name)

    macro to generate file operations for CMA drivers

    :param name:
        name for the generated structure
    :type name: 

.. _`define_drm_gem_cma_fops.description`:

Description
-----------

This macro autogenerates a suitable \ :c:type:`struct file_operations <file_operations>`\  for CMA based
drivers, which can be assigned to \ :c:type:`drm_driver.fops <drm_driver>`\ . Note that this structure
cannot be shared between drivers, because it contains a reference to the
current module using THIS_MODULE.

Note that the declaration is already marked as static - if you need a
non-static version of this you're probably doing it wrong and will break the
THIS_MODULE reference by accident.

.. This file was automatic generated / don't edit.

