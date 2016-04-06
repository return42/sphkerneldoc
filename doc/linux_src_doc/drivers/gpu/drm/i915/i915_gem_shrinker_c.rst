.. -*- coding: utf-8; mode: rst -*-

===================
i915_gem_shrinker.c
===================



.. _xref_i915_gem_shrink:

i915_gem_shrink
===============

.. c:function:: unsigned long i915_gem_shrink (struct drm_i915_private * dev_priv, unsigned long target, unsigned flags)

    Shrink buffer object caches

    :param struct drm_i915_private * dev_priv:
        i915 device

    :param unsigned long target:
        amount of memory to make available, in pages

    :param unsigned flags:
        control flags for selecting cache types



Description
-----------

This function is the main interface to the shrinker. It will try to release
up to **target** pages of main memory backing storage from buffer objects.
Selection of the specific caches can be done with **flags**. This is e.g. useful
when purgeable objects should be removed from caches preferentially.


Note that it's not guaranteed that released amount is actually available as
free system memory - the pages might still be in-used to due to other reasons
(like cpu mmaps) or the mm core has reused them before we could grab them.
Therefore code that needs to explicitly shrink buffer objects caches (e.g. to
avoid deadlocks in memory reclaim) must fall back to :c:func:`i915_gem_shrink_all`.


Also note that any kind of pinning (both per-vma address space pins and
backing storage pins at the buffer object level) result in the shrinker code
having to skip the object.



Returns
-------

The number of pages of backing storage actually released.




.. _xref_i915_gem_shrink_all:

i915_gem_shrink_all
===================

.. c:function:: unsigned long i915_gem_shrink_all (struct drm_i915_private * dev_priv)

    Shrink buffer object caches completely

    :param struct drm_i915_private * dev_priv:
        i915 device



Description
-----------

This is a simple wraper around :c:func:`i915_gem_shrink` to aggressively shrink all
caches completely. It also first waits for and retires all outstanding
requests to also be able to release backing storage for active objects.


This should only be used in code to intentionally quiescent the gpu or as a
last-ditch effort when memory seems to have run out.



Returns
-------

The number of pages of backing storage actually released.




.. _xref_i915_gem_shrinker_init:

i915_gem_shrinker_init
======================

.. c:function:: void i915_gem_shrinker_init (struct drm_i915_private * dev_priv)

    Initialize i915 shrinker

    :param struct drm_i915_private * dev_priv:
        i915 device



Description
-----------

This function registers and sets up the i915 shrinker and OOM handler.




.. _xref_i915_gem_shrinker_cleanup:

i915_gem_shrinker_cleanup
=========================

.. c:function:: void i915_gem_shrinker_cleanup (struct drm_i915_private * dev_priv)

    Clean up i915 shrinker

    :param struct drm_i915_private * dev_priv:
        i915 device



Description
-----------

This function unregisters the i915 shrinker and OOM handler.


