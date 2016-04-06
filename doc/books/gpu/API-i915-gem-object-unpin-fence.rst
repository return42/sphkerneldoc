
.. _API-i915-gem-object-unpin-fence:

===========================
i915_gem_object_unpin_fence
===========================

*man i915_gem_object_unpin_fence(9)*

*4.6.0-rc1*

unpin fencing state


Synopsis
========

.. c:function:: void i915_gem_object_unpin_fence( struct drm_i915_gem_object * obj )

Arguments
=========

``obj``
    object to unpin fencing for


Description
===========

This releases the fence pin reference acquired through i915_gem_object_pin_fence. It will handle both objects with and without an attached fence correctly, callers do not need
to distinguish this.
