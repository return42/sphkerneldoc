
.. _API-i915-gem-batch-pool-fini:

========================
i915_gem_batch_pool_fini
========================

*man i915_gem_batch_pool_fini(9)*

*4.6.0-rc1*

clean up a batch buffer pool


Synopsis
========

.. c:function:: void i915_gem_batch_pool_fini( struct i915_gem_batch_pool * pool )

Arguments
=========

``pool``
    the pool to clean up


Note
====

Callers must hold the struct_mutex.
