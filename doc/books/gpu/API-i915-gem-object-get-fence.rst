
.. _API-i915-gem-object-get-fence:

=========================
i915_gem_object_get_fence
=========================

*man i915_gem_object_get_fence(9)*

*4.6.0-rc1*

set up fencing for an object


Synopsis
========

.. c:function:: int i915_gem_object_get_fence( struct drm_i915_gem_object * obj )

Arguments
=========

``obj``
    object to map through a fence reg


Description
===========

When mapping objects through the GTT, userspace wants to be able to write to them without having to worry about swizzling if the object is tiled. This function walks the fence regs
looking for a free one for ``obj``, stealing one if it can't find any.

It then sets up the reg based on the object's properties: address, pitch and tiling format.

For an untiled surface, this removes any existing fence.


Returns
=======

0 on success, negative error code on failure.
