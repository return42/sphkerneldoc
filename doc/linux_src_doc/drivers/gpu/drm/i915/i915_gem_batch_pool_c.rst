.. -*- coding: utf-8; mode: rst -*-

=====================
i915_gem_batch_pool.c
=====================



.. _xref_i915_gem_batch_pool_init:

i915_gem_batch_pool_init
========================

.. c:function:: void i915_gem_batch_pool_init (struct drm_device * dev, struct i915_gem_batch_pool * pool)

    initialize a batch buffer pool

    :param struct drm_device * dev:
        the drm device

    :param struct i915_gem_batch_pool * pool:
        the batch buffer pool




.. _xref_i915_gem_batch_pool_fini:

i915_gem_batch_pool_fini
========================

.. c:function:: void i915_gem_batch_pool_fini (struct i915_gem_batch_pool * pool)

    clean up a batch buffer pool

    :param struct i915_gem_batch_pool * pool:
        the pool to clean up



Note
----

Callers must hold the struct_mutex.




.. _xref_i915_gem_batch_pool_get:

i915_gem_batch_pool_get
=======================

.. c:function:: struct drm_i915_gem_object * i915_gem_batch_pool_get (struct i915_gem_batch_pool * pool, size_t size)

    allocate a buffer from the pool

    :param struct i915_gem_batch_pool * pool:
        the batch buffer pool

    :param size_t size:
        the minimum desired size of the returned buffer



Description
-----------

Returns an inactive buffer from **pool** with at least **size** bytes,
with the pages pinned. The caller must :c:func:`i915_gem_object_unpin_pages`
on the returned object.



Note
----

Callers must hold the struct_mutex



Return
------

the buffer object or an error pointer


