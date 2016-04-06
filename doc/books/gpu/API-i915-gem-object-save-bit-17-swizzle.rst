
.. _API-i915-gem-object-save-bit-17-swizzle:

===================================
i915_gem_object_save_bit_17_swizzle
===================================

*man i915_gem_object_save_bit_17_swizzle(9)*

*4.6.0-rc1*

save bit 17 swizzling


Synopsis
========

.. c:function:: void i915_gem_object_save_bit_17_swizzle( struct drm_i915_gem_object * obj )

Arguments
=========

``obj``
    i915 GEM buffer object


Description
===========

This function saves the bit 17 of each page frame number so that swizzling can be fixed up later on with ``i915_gem_object_do_bit_17_swizzle``. This must be called before the
backing storage can be unpinned.
