
.. _API-i915-gem-object-put-fence:

=========================
i915_gem_object_put_fence
=========================

*man i915_gem_object_put_fence(9)*

*4.6.0-rc1*

force-remove fence for an object


Synopsis
========

.. c:function:: int i915_gem_object_put_fence( struct drm_i915_gem_object * obj )

Arguments
=========

``obj``
    object to map through a fence reg


Description
===========

This function force-removes any fence from the given object, which is useful if the kernel wants to do untiled GTT access.


Returns
=======

0 on success, negative error code on failure.
