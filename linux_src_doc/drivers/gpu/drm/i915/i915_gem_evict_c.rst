.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_evict.c

.. _`i915_gem_evict_something`:

i915_gem_evict_something
========================

.. c:function:: int i915_gem_evict_something(struct i915_address_space *vm, u64 min_size, u64 alignment, unsigned cache_level, u64 start, u64 end, unsigned flags)

    Evict vmas to make room for binding a new one

    :param vm:
        address space to evict from
    :type vm: struct i915_address_space \*

    :param min_size:
        size of the desired free space
    :type min_size: u64

    :param alignment:
        alignment constraint of the desired free space
    :type alignment: u64

    :param cache_level:
        cache_level for the desired space
    :type cache_level: unsigned

    :param start:
        start (inclusive) of the range from which to evict objects
    :type start: u64

    :param end:
        end (exclusive) of the range from which to evict objects
    :type end: u64

    :param flags:
        additional flags to control the eviction algorithm
    :type flags: unsigned

.. _`i915_gem_evict_something.description`:

Description
-----------

This function will try to evict vmas until a free space satisfying the
requirements is found. Callers must check first whether any such hole exists
already before calling this function.

This function is used by the object/vma binding code.

Since this function is only used to free up virtual address space it only
ignores pinned vmas, and not object where the backing storage itself is
pinned. Hence obj->pages_pin_count does not protect against eviction.

To clarify: This is for freeing up virtual address space, not for freeing
memory in e.g. the shrinker.

.. _`i915_gem_evict_for_node`:

i915_gem_evict_for_node
=======================

.. c:function:: int i915_gem_evict_for_node(struct i915_address_space *vm, struct drm_mm_node *target, unsigned int flags)

    Evict vmas to make room for binding a new one

    :param vm:
        address space to evict from
    :type vm: struct i915_address_space \*

    :param target:
        range (and color) to evict for
    :type target: struct drm_mm_node \*

    :param flags:
        additional flags to control the eviction algorithm
    :type flags: unsigned int

.. _`i915_gem_evict_for_node.description`:

Description
-----------

This function will try to evict vmas that overlap the target node.

To clarify: This is for freeing up virtual address space, not for freeing
memory in e.g. the shrinker.

.. _`i915_gem_evict_vm`:

i915_gem_evict_vm
=================

.. c:function:: int i915_gem_evict_vm(struct i915_address_space *vm)

    Evict all idle vmas from a vm

    :param vm:
        Address space to cleanse
    :type vm: struct i915_address_space \*

.. _`i915_gem_evict_vm.description`:

Description
-----------

This function evicts all vmas from a vm.

This is used by the execbuf code as a last-ditch effort to defragment the
address space.

To clarify: This is for freeing up virtual address space, not for freeing
memory in e.g. the shrinker.

.. This file was automatic generated / don't edit.

