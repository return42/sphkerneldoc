
.. _API-intel-fb-obj-invalidate:

=======================
intel_fb_obj_invalidate
=======================

*man intel_fb_obj_invalidate(9)*

*4.6.0-rc1*

invalidate frontbuffer object


Synopsis
========

.. c:function:: void intel_fb_obj_invalidate( struct drm_i915_gem_object * obj, enum fb_op_origin origin )

Arguments
=========

``obj``
    GEM object to invalidate

``origin``
    which operation caused the invalidation


Description
===========

This function gets called every time rendering on the given object starts and frontbuffer caching (fbc, low refresh rate for DRRS, panel self refresh) must be invalidated. For
ORIGIN_CS any subsequent invalidation will be delayed until the rendering completes or a flip on this frontbuffer plane is scheduled.
