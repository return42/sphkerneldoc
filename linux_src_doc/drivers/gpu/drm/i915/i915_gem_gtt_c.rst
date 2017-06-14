.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_gtt.c

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
(2x2 pages):

   12
   34

Above would represent a normal GGTT view as normally mapped for GPU or CPU
rendering. In contrast, fed to the display engine would be an alternative
view which could look something like this:

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
3. Add support to \ :c:func:`i915_get_vma_pages`\ .

New views are required to build a scatter-gather table from within the
i915_get_vma_pages function. This table is stored in the vma.ggtt_view and
exists for the lifetime of an VMA.

Core API is designed to have copy semantics which means that passed in
struct i915_ggtt_view does not need to be persistent (left around after
calling the core API functions).

.. _`i915_ggtt_cleanup_hw`:

i915_ggtt_cleanup_hw
====================

.. c:function:: void i915_ggtt_cleanup_hw(struct drm_i915_private *dev_priv)

    Clean up GGTT hardware initialization

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`i915_ggtt_probe_hw`:

i915_ggtt_probe_hw
==================

.. c:function:: int i915_ggtt_probe_hw(struct drm_i915_private *dev_priv)

    Probe GGTT hardware location

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`i915_ggtt_init_hw`:

i915_ggtt_init_hw
=================

.. c:function:: int i915_ggtt_init_hw(struct drm_i915_private *dev_priv)

    Initialize GGTT hardware

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`i915_gem_gtt_reserve`:

i915_gem_gtt_reserve
====================

.. c:function:: int i915_gem_gtt_reserve(struct i915_address_space *vm, struct drm_mm_node *node, u64 size, u64 offset, unsigned long color, unsigned int flags)

    reserve a node in an address_space (GTT)

    :param struct i915_address_space \*vm:
        the \ :c:type:`struct i915_address_space <i915_address_space>`\ 

    :param struct drm_mm_node \*node:
        the \ :c:type:`struct drm_mm_node <drm_mm_node>`\  (typically i915_vma.mode)

    :param u64 size:
        how much space to allocate inside the GTT,
        must be #I915_GTT_PAGE_SIZE aligned

    :param u64 offset:
        where to insert inside the GTT,
        must be #I915_GTT_MIN_ALIGNMENT aligned, and the node
        (@offset + \ ``size``\ ) must fit within the address space

    :param unsigned long color:
        color to apply to node, if this node is not from a VMA,
        color must be #I915_COLOR_UNEVICTABLE

    :param unsigned int flags:
        control search and eviction behaviour

.. _`i915_gem_gtt_reserve.description`:

Description
-----------

i915_gem_gtt_reserve() tries to insert the \ ``node``\  at the exact \ ``offset``\  inside
the address space (using \ ``size``\  and \ ``color``\ ). If the \ ``node``\  does not fit, it
tries to evict any overlapping nodes from the GTT, including any
neighbouring nodes if the colors do not match (to ensure guard pages between
differing domains). See \ :c:func:`i915_gem_evict_for_node`\  for the gory details
on the eviction algorithm. #PIN_NONBLOCK may used to prevent waiting on
evicting active overlapping objects, and any overlapping node that is pinned
or marked as unevictable will also result in failure.

.. _`i915_gem_gtt_reserve.return`:

Return
------

0 on success, -ENOSPC if no suitable hole is found, -EINTR if
asked to wait for eviction and interrupted.

.. _`i915_gem_gtt_insert`:

i915_gem_gtt_insert
===================

.. c:function:: int i915_gem_gtt_insert(struct i915_address_space *vm, struct drm_mm_node *node, u64 size, u64 alignment, unsigned long color, u64 start, u64 end, unsigned int flags)

    insert a node into an address_space (GTT)

    :param struct i915_address_space \*vm:
        the \ :c:type:`struct i915_address_space <i915_address_space>`\ 

    :param struct drm_mm_node \*node:
        the \ :c:type:`struct drm_mm_node <drm_mm_node>`\  (typically i915_vma.node)

    :param u64 size:
        how much space to allocate inside the GTT,
        must be #I915_GTT_PAGE_SIZE aligned

    :param u64 alignment:
        required alignment of starting offset, may be 0 but
        if specified, this must be a power-of-two and at least
        #I915_GTT_MIN_ALIGNMENT

    :param unsigned long color:
        color to apply to node

    :param u64 start:
        start of any range restriction inside GTT (0 for all),
        must be #I915_GTT_PAGE_SIZE aligned

    :param u64 end:
        end of any range restriction inside GTT (U64_MAX for all),
        must be #I915_GTT_PAGE_SIZE aligned if not U64_MAX

    :param unsigned int flags:
        control search and eviction behaviour

.. _`i915_gem_gtt_insert.description`:

Description
-----------

i915_gem_gtt_insert() first searches for an available hole into which
is can insert the node. The hole address is aligned to \ ``alignment``\  and
its \ ``size``\  must then fit entirely within the [@start, \ ``end``\ ] bounds. The
nodes on either side of the hole must match \ ``color``\ , or else a guard page
will be inserted between the two nodes (or the node evicted). If no
suitable hole is found, first a victim is randomly selected and tested
for eviction, otherwise then the LRU list of objects within the GTT
is scanned to find the first set of replacement nodes to create the hole.
Those old overlapping nodes are evicted from the GTT (and so must be
rebound before any future use). Any node that is currently pinned cannot
be evicted (see \ :c:func:`i915_vma_pin`\ ). Similar if the node's VMA is currently
active and #PIN_NONBLOCK is specified, that node is also skipped when
searching for an eviction candidate. See \ :c:func:`i915_gem_evict_something`\  for
the gory details on the eviction algorithm.

.. _`i915_gem_gtt_insert.return`:

Return
------

0 on success, -ENOSPC if no suitable hole is found, -EINTR if
asked to wait for eviction and interrupted.

.. This file was automatic generated / don't edit.

