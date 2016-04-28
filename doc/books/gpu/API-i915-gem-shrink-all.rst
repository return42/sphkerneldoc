.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-shrink-all:

===================
i915_gem_shrink_all
===================

*man i915_gem_shrink_all(9)*

*4.6.0-rc5*

Shrink buffer object caches completely


Synopsis
========

.. c:function:: unsigned long i915_gem_shrink_all( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device


Description
===========

This is a simple wraper around ``i915_gem_shrink`` to aggressively
shrink all caches completely. It also first waits for and retires all
outstanding requests to also be able to release backing storage for
active objects.

This should only be used in code to intentionally quiescent the gpu or
as a last-ditch effort when memory seems to have run out.


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
