.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_shrinker.c

.. _`i915_gem_shrink`:

i915_gem_shrink
===============

.. c:function:: unsigned long i915_gem_shrink(struct drm_i915_private *i915, unsigned long target, unsigned long *nr_scanned, unsigned flags)

    Shrink buffer object caches

    :param i915:
        i915 device
    :type i915: struct drm_i915_private \*

    :param target:
        amount of memory to make available, in pages
    :type target: unsigned long

    :param nr_scanned:
        optional output for number of pages scanned (incremental)
    :type nr_scanned: unsigned long \*

    :param flags:
        control flags for selecting cache types
    :type flags: unsigned

.. _`i915_gem_shrink.description`:

Description
-----------

This function is the main interface to the shrinker. It will try to release
up to \ ``target``\  pages of main memory backing storage from buffer objects.
Selection of the specific caches can be done with \ ``flags``\ . This is e.g. useful
when purgeable objects should be removed from caches preferentially.

Note that it's not guaranteed that released amount is actually available as
free system memory - the pages might still be in-used to due to other reasons
(like cpu mmaps) or the mm core has reused them before we could grab them.
Therefore code that needs to explicitly shrink buffer objects caches (e.g. to
avoid deadlocks in memory reclaim) must fall back to \ :c:func:`i915_gem_shrink_all`\ .

Also note that any kind of pinning (both per-vma address space pins and
backing storage pins at the buffer object level) result in the shrinker code
having to skip the object.

.. _`i915_gem_shrink.return`:

Return
------

The number of pages of backing storage actually released.

.. _`i915_gem_shrink_all`:

i915_gem_shrink_all
===================

.. c:function:: unsigned long i915_gem_shrink_all(struct drm_i915_private *i915)

    Shrink buffer object caches completely

    :param i915:
        i915 device
    :type i915: struct drm_i915_private \*

.. _`i915_gem_shrink_all.description`:

Description
-----------

This is a simple wraper around \ :c:func:`i915_gem_shrink`\  to aggressively shrink all
caches completely. It also first waits for and retires all outstanding
requests to also be able to release backing storage for active objects.

This should only be used in code to intentionally quiescent the gpu or as a
last-ditch effort when memory seems to have run out.

.. _`i915_gem_shrink_all.return`:

Return
------

The number of pages of backing storage actually released.

.. _`i915_gem_shrinker_register`:

i915_gem_shrinker_register
==========================

.. c:function:: void i915_gem_shrinker_register(struct drm_i915_private *i915)

    Register the i915 shrinker

    :param i915:
        i915 device
    :type i915: struct drm_i915_private \*

.. _`i915_gem_shrinker_register.description`:

Description
-----------

This function registers and sets up the i915 shrinker and OOM handler.

.. _`i915_gem_shrinker_unregister`:

i915_gem_shrinker_unregister
============================

.. c:function:: void i915_gem_shrinker_unregister(struct drm_i915_private *i915)

    Unregisters the i915 shrinker

    :param i915:
        i915 device
    :type i915: struct drm_i915_private \*

.. _`i915_gem_shrinker_unregister.description`:

Description
-----------

This function unregisters the i915 shrinker and OOM handler.

.. This file was automatic generated / don't edit.

