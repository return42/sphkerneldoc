.. -*- coding: utf-8; mode: rst -*-

================
i915_gem_evict.c
================


.. _`i915_gem_evict_something`:

i915_gem_evict_something
========================

.. c:function:: int i915_gem_evict_something (struct drm_device *dev, struct i915_address_space *vm, int min_size, unsigned alignment, unsigned cache_level, unsigned long start, unsigned long end, unsigned flags)

    Evict vmas to make room for binding a new one

    :param struct drm_device \*dev:
        drm_device

    :param struct i915_address_space \*vm:
        address space to evict from

    :param int min_size:
        size of the desired free space

    :param unsigned alignment:
        alignment constraint of the desired free space

    :param unsigned cache_level:
        cache_level for the desired space

    :param unsigned long start:
        start (inclusive) of the range from which to evict objects

    :param unsigned long end:
        end (exclusive) of the range from which to evict objects

    :param unsigned flags:
        additional flags to control the eviction algorithm



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



.. _`i915_gem_evict_something.to-clarify`:

To clarify
----------

This is for freeing up virtual address space, not for freeing
memory in e.g. the shrinker.



.. _`i915_gem_evict_vm`:

i915_gem_evict_vm
=================

.. c:function:: int i915_gem_evict_vm (struct i915_address_space *vm, bool do_idle)

    Evict all idle vmas from a vm

    :param struct i915_address_space \*vm:
        Address space to cleanse

    :param bool do_idle:
        Boolean directing whether to idle first.



.. _`i915_gem_evict_vm.description`:

Description
-----------

This function evicts all idles vmas from a vm. If all unpinned vmas should be
evicted the ``do_idle`` needs to be set to true.

This is used by the execbuf code as a last-ditch effort to defragment the
address space.



.. _`i915_gem_evict_vm.to-clarify`:

To clarify
----------

This is for freeing up virtual address space, not for freeing
memory in e.g. the shrinker.

