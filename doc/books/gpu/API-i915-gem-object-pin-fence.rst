
.. _API-i915-gem-object-pin-fence:

=========================
i915_gem_object_pin_fence
=========================

*man i915_gem_object_pin_fence(9)*

*4.6.0-rc1*

pin fencing state


Synopsis
========

.. c:function:: bool i915_gem_object_pin_fence( struct drm_i915_gem_object * obj )

Arguments
=========

``obj``
    object to pin fencing for


Description
===========

This pins the fencing state (whether tiled or untiled) to make sure the object is ready to be used as a scanout target. Fencing status must be synchronize first by calling
``i915_gem_object_get_fence``:

The resulting fence pin reference must be released again with ``i915_gem_object_unpin_fence``.


Returns
=======

True if the object has a fence, false otherwise.
