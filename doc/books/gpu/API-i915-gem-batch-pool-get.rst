
.. _API-i915-gem-batch-pool-get:

=======================
i915_gem_batch_pool_get
=======================

*man i915_gem_batch_pool_get(9)*

*4.6.0-rc1*

allocate a buffer from the pool


Synopsis
========

.. c:function:: struct drm_i915_gem_object ⋆ i915_gem_batch_pool_get( struct i915_gem_batch_pool * pool, size_t size )

Arguments
=========

``pool``
    the batch buffer pool

``size``
    the minimum desired size of the returned buffer


Description
===========

Returns an inactive buffer from ``pool`` with at least ``size`` bytes, with the pages pinned. The caller must ``i915_gem_object_unpin_pages`` on the returned object.


Note
====

Callers must hold the struct_mutex


Return
======

the buffer object or an error pointer
