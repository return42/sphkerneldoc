.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_gtt.c

.. _`gen8_ppgtt_alloc_pagetabs`:

gen8_ppgtt_alloc_pagetabs
=========================

.. c:function:: int gen8_ppgtt_alloc_pagetabs(struct i915_address_space *vm, struct i915_page_directory *pd, uint64_t start, uint64_t length, unsigned long *new_pts)

    Allocate page tables for VA range.

    :param struct i915_address_space \*vm:
        Master vm structure.

    :param struct i915_page_directory \*pd:
        Page directory for this address range.

    :param uint64_t start:
        Starting virtual address to begin allocations.

    :param uint64_t length:
        Size of the allocations.

    :param unsigned long \*new_pts:
        Bitmap set by function with new allocations. Likely used by the
        caller to free on error.

.. _`gen8_ppgtt_alloc_pagetabs.description`:

Description
-----------

Allocate the required number of page tables. Extremely similar to
\ :c:func:`gen8_ppgtt_alloc_page_directories`\ . The main difference is here we are limited by
the page directory boundary (instead of the page directory pointer). That
boundary is 1GB virtual. Therefore, unlike \ :c:func:`gen8_ppgtt_alloc_page_directories`\ , it is
possible, and likely that the caller will need to use multiple calls of this
function to achieve the appropriate allocation.

.. _`gen8_ppgtt_alloc_pagetabs.return`:

Return
------

0 if success; negative error code otherwise.

.. _`gen8_ppgtt_alloc_page_directories`:

gen8_ppgtt_alloc_page_directories
=================================

.. c:function:: int gen8_ppgtt_alloc_page_directories(struct i915_address_space *vm, struct i915_page_directory_pointer *pdp, uint64_t start, uint64_t length, unsigned long *new_pds)

    Allocate page directories for VA range.

    :param struct i915_address_space \*vm:
        Master vm structure.

    :param struct i915_page_directory_pointer \*pdp:
        Page directory pointer for this address range.

    :param uint64_t start:
        Starting virtual address to begin allocations.

    :param uint64_t length:
        Size of the allocations.

    :param unsigned long \*new_pds:
        Bitmap set by function with new allocations. Likely used by the
        caller to free on error.

.. _`gen8_ppgtt_alloc_page_directories.description`:

Description
-----------

Allocate the required number of page directories starting at the pde index of
\ ``start``\ , and ending at the pde index \ ``start``\  + \ ``length``\ . This function will skip
over already allocated page directories within the range, and only allocate
new ones, setting the appropriate pointer within the pdp as well as the
correct position in the bitmap \ ``new_pds``\ .

The function will only allocate the pages within the range for a give page
directory pointer. In other words, if \ ``start``\  + \ ``length``\  straddles a virtually
addressed PDP boundary (512GB for 4k pages), there will be more allocations
required by the caller, This is not currently possible, and the BUG in the
code will prevent it.

.. _`gen8_ppgtt_alloc_page_directories.return`:

Return
------

0 if success; negative error code otherwise.

.. _`gen8_ppgtt_alloc_page_dirpointers`:

gen8_ppgtt_alloc_page_dirpointers
=================================

.. c:function:: int gen8_ppgtt_alloc_page_dirpointers(struct i915_address_space *vm, struct i915_pml4 *pml4, uint64_t start, uint64_t length, unsigned long *new_pdps)

    Allocate pdps for VA range.

    :param struct i915_address_space \*vm:
        Master vm structure.

    :param struct i915_pml4 \*pml4:
        Page map level 4 for this address range.

    :param uint64_t start:
        Starting virtual address to begin allocations.

    :param uint64_t length:
        Size of the allocations.

    :param unsigned long \*new_pdps:
        Bitmap set by function with new allocations. Likely used by the
        caller to free on error.

.. _`gen8_ppgtt_alloc_page_dirpointers.description`:

Description
-----------

Allocate the required number of page directory pointers. Extremely similar to
\ :c:func:`gen8_ppgtt_alloc_page_directories`\  and \ :c:func:`gen8_ppgtt_alloc_pagetabs`\ .
The main difference is here we are limited by the pml4 boundary (instead of
the page directory pointer).

.. _`gen8_ppgtt_alloc_page_dirpointers.return`:

Return
------

0 if success; negative error code otherwise.

.. _`i915_gem_init_ggtt`:

i915_gem_init_ggtt
==================

.. c:function:: void i915_gem_init_ggtt(struct drm_device *dev)

    Initialize GEM for Global GTT

    :param struct drm_device \*dev:
        DRM device

.. _`i915_ggtt_cleanup_hw`:

i915_ggtt_cleanup_hw
====================

.. c:function:: void i915_ggtt_cleanup_hw(struct drm_device *dev)

    Clean up GGTT hardware initialization

    :param struct drm_device \*dev:
        DRM device

.. _`i915_ggtt_init_hw`:

i915_ggtt_init_hw
=================

.. c:function:: int i915_ggtt_init_hw(struct drm_device *dev)

    Initialize GGTT hardware

    :param struct drm_device \*dev:
        DRM device

.. _`i915_vma_bind`:

i915_vma_bind
=============

.. c:function:: int i915_vma_bind(struct i915_vma *vma, enum i915_cache_level cache_level, u32 flags)

    Sets up PTEs for an VMA in it's corresponding address space.

    :param struct i915_vma \*vma:
        VMA to map

    :param enum i915_cache_level cache_level:
        mapping cache level

    :param u32 flags:
        flags like global or local mapping

.. _`i915_vma_bind.description`:

Description
-----------

DMA addresses are taken from the scatter-gather table of this object (or of
this VMA in case of non-default GGTT views) and PTE entries set up.
Note that DMA addresses are also the only part of the SG table we care about.

.. _`i915_ggtt_view_size`:

i915_ggtt_view_size
===================

.. c:function:: size_t i915_ggtt_view_size(struct drm_i915_gem_object *obj, const struct i915_ggtt_view *view)

    Get the size of a GGTT view.

    :param struct drm_i915_gem_object \*obj:
        Object the view is of.

    :param const struct i915_ggtt_view \*view:
        The view in question.

.. _`i915_ggtt_view_size.description`:

Description
-----------

\ ``return``\  The size of the GGTT view in bytes.

.. This file was automatic generated / don't edit.

