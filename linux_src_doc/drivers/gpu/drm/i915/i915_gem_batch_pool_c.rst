.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_batch_pool.c

.. _`i915_gem_batch_pool_init`:

i915_gem_batch_pool_init
========================

.. c:function:: void i915_gem_batch_pool_init(struct drm_device *dev, struct i915_gem_batch_pool *pool)

    initialize a batch buffer pool

    :param struct drm_device \*dev:
        the drm device

    :param struct i915_gem_batch_pool \*pool:
        the batch buffer pool

.. _`i915_gem_batch_pool_fini`:

i915_gem_batch_pool_fini
========================

.. c:function:: void i915_gem_batch_pool_fini(struct i915_gem_batch_pool *pool)

    clean up a batch buffer pool

    :param struct i915_gem_batch_pool \*pool:
        the pool to clean up

.. _`i915_gem_batch_pool_fini.note`:

Note
----

Callers must hold the struct_mutex.

.. _`i915_gem_batch_pool_get`:

i915_gem_batch_pool_get
=======================

.. c:function:: struct drm_i915_gem_object *i915_gem_batch_pool_get(struct i915_gem_batch_pool *pool, size_t size)

    allocate a buffer from the pool

    :param struct i915_gem_batch_pool \*pool:
        the batch buffer pool

    :param size_t size:
        the minimum desired size of the returned buffer

.. _`i915_gem_batch_pool_get.description`:

Description
-----------

Returns an inactive buffer from \ ``pool``\  with at least \ ``size``\  bytes,
with the pages pinned. The caller must \ :c:func:`i915_gem_object_unpin_pages`\ 
on the returned object.

.. _`i915_gem_batch_pool_get.note`:

Note
----

Callers must hold the struct_mutex

.. _`i915_gem_batch_pool_get.return`:

Return
------

the buffer object or an error pointer

.. This file was automatic generated / don't edit.
