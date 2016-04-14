.. -*- coding: utf-8; mode: rst -*-

==============
i915_gem_gtt.c
==============

.. _`global-gtt-views`:

Global GTT views
================

Background and previous state

Historically objects could exists (be bound) in global GTT space only as
singular instances with a view representing all of the object's backing pages
in a linear fashion. This view will be called a normal view.

To support multiple views of the same object, where the number of mapped
pages is not equal to the backing store, or where the layout of the pages
is not linear, concept of a GGTT view was added.

One example of an alternative view is a stereo display driven by a single
image. In this case we would have a framebuffer looking like this
(2x2 pages)::

   12
   34

Above would represent a normal GGTT view as normally mapped for GPU or CPU
rendering. In contrast, fed to the display engine would be an alternative
view which could look something like this::

  1212
  3434

In this example both the size and layout of pages in the alternative view is
different from the normal view.

Implementation and usage

GGTT views are implemented using VMAs and are distinguished via enum
i915_ggtt_view_type and struct i915_ggtt_view.

A new flavour of core GEM functions which work with GGTT bound objects were
added with the _ggtt_ infix, and sometimes with _view postfix to avoid
renaming  in large amounts of code. They take the struct i915_ggtt_view
parameter encapsulating all metadata required to implement a view.

As a helper for callers which are only interested in the normal view,
globally const i915_ggtt_view_normal singleton instance exists. All old core
GEM API functions, the ones not taking the view parameter, are operating on,
or with the normal GGTT view.

Code wanting to add or use a new GGTT view needs to:

1. Add a new enum with a suitable name.
2. Extend the metadata in the i915_ggtt_view structure if required.
3. Add support to :c:func:`i915_get_vma_pages`.

New views are required to build a scatter-gather table from within the
i915_get_vma_pages function. This table is stored in the vma.ggtt_view and
exists for the lifetime of an VMA.

Core API is designed to have copy semantics which means that passed in
struct i915_ggtt_view does not need to be persistent (left around after
calling the core API functions).


.. _`gen8_ppgtt_alloc_pagetabs`:

gen8_ppgtt_alloc_pagetabs
=========================

.. c:function:: int gen8_ppgtt_alloc_pagetabs (struct i915_address_space *vm, struct i915_page_directory *pd, uint64_t start, uint64_t length, unsigned long *new_pts)

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
:c:func:`gen8_ppgtt_alloc_page_directories`. The main difference is here we are limited by
the page directory boundary (instead of the page directory pointer). That
boundary is 1GB virtual. Therefore, unlike :c:func:`gen8_ppgtt_alloc_page_directories`, it is
possible, and likely that the caller will need to use multiple calls of this
function to achieve the appropriate allocation.

Return: 0 if success; negative error code otherwise.


.. _`gen8_ppgtt_alloc_page_directories`:

gen8_ppgtt_alloc_page_directories
=================================

.. c:function:: int gen8_ppgtt_alloc_page_directories (struct i915_address_space *vm, struct i915_page_directory_pointer *pdp, uint64_t start, uint64_t length, unsigned long *new_pds)

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
``start``\ , and ending at the pde index ``start`` + ``length``\ . This function will skip
over already allocated page directories within the range, and only allocate
new ones, setting the appropriate pointer within the pdp as well as the
correct position in the bitmap ``new_pds``\ .

The function will only allocate the pages within the range for a give page
directory pointer. In other words, if ``start`` + ``length`` straddles a virtually
addressed PDP boundary (512GB for 4k pages), there will be more allocations
required by the caller, This is not currently possible, and the BUG in the
code will prevent it.

Return: 0 if success; negative error code otherwise.


.. _`gen8_ppgtt_alloc_page_dirpointers`:

gen8_ppgtt_alloc_page_dirpointers
=================================

.. c:function:: int gen8_ppgtt_alloc_page_dirpointers (struct i915_address_space *vm, struct i915_pml4 *pml4, uint64_t start, uint64_t length, unsigned long *new_pdps)

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
:c:func:`gen8_ppgtt_alloc_page_directories` and :c:func:`gen8_ppgtt_alloc_pagetabs`.
The main difference is here we are limited by the pml4 boundary (instead of
the page directory pointer).

Return: 0 if success; negative error code otherwise.


.. _`i915_vma_bind`:

i915_vma_bind
=============

.. c:function:: int i915_vma_bind (struct i915_vma *vma, enum i915_cache_level cache_level, u32 flags)

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

.. c:function:: size_t i915_ggtt_view_size (struct drm_i915_gem_object *obj, const struct i915_ggtt_view *view)

    Get the size of a GGTT view.

    :param struct drm_i915_gem_object \*obj:
        Object the view is of.

    :param const struct i915_ggtt_view \*view:
        The view in question.


.. _`i915_ggtt_view_size.description`:

Description
-----------

``return`` The size of the GGTT view in bytes.

