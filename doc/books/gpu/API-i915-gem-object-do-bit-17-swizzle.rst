
.. _API-i915-gem-object-do-bit-17-swizzle:

=================================
i915_gem_object_do_bit_17_swizzle
=================================

*man i915_gem_object_do_bit_17_swizzle(9)*

*4.6.0-rc1*

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

This function fixes up the swizzling in case any page frame number for this object has changed in bit 17 since that state has been saved with
``i915_gem_object_save_bit_17_swizzle``.

This is called when pinning backing storage again, since the kernel is free to move unpinned backing storage around (either by directly moving pages or by swapping them out and
back in again).
