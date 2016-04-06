
.. _API-i915-gem-batch-pool-init:

========================
i915_gem_batch_pool_init
========================

*man i915_gem_batch_pool_init(9)*

*4.6.0-rc1*

initialize a batch buffer pool


Synopsis
========

.. c:function:: void i915_gem_batch_pool_init( struct drm_device * dev, struct i915_gem_batch_pool * pool )

Arguments
=========

``dev``
    the drm device

``pool``
    the batch buffer pool
