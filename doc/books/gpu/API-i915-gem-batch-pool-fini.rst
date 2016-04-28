.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-batch-pool-fini:

========================
i915_gem_batch_pool_fini
========================

*man i915_gem_batch_pool_fini(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
