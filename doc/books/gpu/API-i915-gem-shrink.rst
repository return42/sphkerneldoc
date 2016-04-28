.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-shrink:

===============
i915_gem_shrink
===============

*man i915_gem_shrink(9)*

*4.6.0-rc5*

Shrink buffer object caches


Synopsis
========

.. c:function:: unsigned long i915_gem_shrink( struct drm_i915_private * dev_priv, unsigned long target, unsigned flags )

Arguments
=========

``dev_priv``
    i915 device

``target``
    amount of memory to make available, in pages

``flags``
    control flags for selecting cache types


Description
===========

This function is the main interface to the shrinker. It will try to
release up to ``target`` pages of main memory backing storage from
buffer objects. Selection of the specific caches can be done with
``flags``. This is e.g. useful when purgeable objects should be removed
from caches preferentially.

Note that it's not guaranteed that released amount is actually available
as free system memory - the pages might still be in-used to due to other
reasons (like cpu mmaps) or the mm core has reused them before we could
grab them. Therefore code that needs to explicitly shrink buffer objects
caches (e.g. to avoid deadlocks in memory reclaim) must fall back to
``i915_gem_shrink_all``.

Also note that any kind of pinning (both per-vma address space pins and
backing storage pins at the buffer object level) result in the shrinker
code having to skip the object.


Returns
=======

The number of pages of backing storage actually released.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
