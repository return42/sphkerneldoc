.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-evict-something:

========================
i915_gem_evict_something
========================

*man i915_gem_evict_something(9)*

*4.6.0-rc5*

Evict vmas to make room for binding a new one


Synopsis
========

.. c:function:: int i915_gem_evict_something( struct drm_device * dev, struct i915_address_space * vm, int min_size, unsigned alignment, unsigned cache_level, unsigned long start, unsigned long end, unsigned flags )

Arguments
=========

``dev``
    drm_device

``vm``
    address space to evict from

``min_size``
    size of the desired free space

``alignment``
    alignment constraint of the desired free space

``cache_level``
    cache_level for the desired space

``start``
    start (inclusive) of the range from which to evict objects

``end``
    end (exclusive) of the range from which to evict objects

``flags``
    additional flags to control the eviction algorithm


Description
===========

This function will try to evict vmas until a free space satisfying the
requirements is found. Callers must check first whether any such hole
exists already before calling this function.

This function is used by the object/vma binding code.

Since this function is only used to free up virtual address space it
only ignores pinned vmas, and not object where the backing storage
itself is pinned. Hence obj->pages_pin_count does not protect against
eviction.


To clarify
==========

This is for freeing up virtual address space, not for freeing memory in
e.g. the shrinker.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
