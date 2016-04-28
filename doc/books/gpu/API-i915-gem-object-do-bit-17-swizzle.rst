.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-object-do-bit-17-swizzle:

=================================
i915_gem_object_do_bit_17_swizzle
=================================

*man i915_gem_object_do_bit_17_swizzle(9)*

*4.6.0-rc5*

fixup bit 17 swizzling


Synopsis
========

.. c:function:: void i915_gem_object_do_bit_17_swizzle( struct drm_i915_gem_object * obj )

Arguments
=========

``obj``
    i915 GEM buffer object


Description
===========

This function fixes up the swizzling in case any page frame number for
this object has changed in bit 17 since that state has been saved with
``i915_gem_object_save_bit_17_swizzle``.

This is called when pinning backing storage again, since the kernel is
free to move unpinned backing storage around (either by directly moving
pages or by swapping them out and back in again).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
