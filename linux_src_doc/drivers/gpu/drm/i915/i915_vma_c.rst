.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_vma.c

.. _`i915_vma_instance`:

i915_vma_instance
=================

.. c:function:: struct i915_vma *i915_vma_instance(struct drm_i915_gem_object *obj, struct i915_address_space *vm, const struct i915_ggtt_view *view)

    return the singleton instance of the VMA

    :param struct drm_i915_gem_object \*obj:
        parent \ :c:type:`struct drm_i915_gem_object <drm_i915_gem_object>`\  to be mapped

    :param struct i915_address_space \*vm:
        address space in which the mapping is located

    :param const struct i915_ggtt_view \*view:
        additional mapping requirements

.. _`i915_vma_instance.description`:

Description
-----------

\ :c:func:`i915_vma_instance`\  looks up an existing VMA of the \ ``obj``\  in the \ ``vm``\  with
the same \ ``view``\  characteristics. If a match is not found, one is created.
Once created, the VMA is kept until either the object is freed, or the
address space is closed.

Must be called with struct_mutex held.

Returns the vma, or an error pointer.

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

.. _`i915_vma_insert`:

i915_vma_insert
===============

.. c:function:: int i915_vma_insert(struct i915_vma *vma, u64 size, u64 alignment, u64 flags)

    finds a slot for the vma in its address space

    :param struct i915_vma \*vma:
        the vma

    :param u64 size:
        requested size in bytes (can be larger than the VMA)

    :param u64 alignment:
        required alignment

    :param u64 flags:
        mask of PIN\_\* flags to use

.. _`i915_vma_insert.description`:

Description
-----------

First we try to allocate some free space that meets the requirements for
the VMA. Failiing that, if the flags permit, it will evict an old VMA,
preferrably the oldest idle entry to make room for the new VMA.

.. _`i915_vma_insert.return`:

Return
------

0 on success, negative error code otherwise.

.. This file was automatic generated / don't edit.

