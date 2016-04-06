
.. _API-i915-gem-detect-bit-6-swizzle:

=============================
i915_gem_detect_bit_6_swizzle
=============================

*man i915_gem_detect_bit_6_swizzle(9)*

*4.6.0-rc1*

detect bit 6 swizzling pattern


Synopsis
========

.. c:function:: void i915_gem_detect_bit_6_swizzle( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Detects bit 6 swizzling of address lookup between IGD access and CPU access through main memory.
