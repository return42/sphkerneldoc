.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-batch-pool-get:

=======================
i915_gem_batch_pool_get
=======================

*man i915_gem_batch_pool_get(9)*

*4.6.0-rc5*

allocate a buffer from the pool


Synopsis
========

.. c:function:: struct drm_i915_gem_object * i915_gem_batch_pool_get( struct i915_gem_batch_pool * pool, size_t size )

Arguments
=========

``pool``
    the batch buffer pool

``size``
    the minimum desired size of the returned buffer


Description
===========

Returns an inactive buffer from ``pool`` with at least ``size`` bytes,
with the pages pinned. The caller must ``i915_gem_object_unpin_pages``
on the returned object.


Note
====

Callers must hold the struct_mutex


Return
======

the buffer object or an error pointer


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
