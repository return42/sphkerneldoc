.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-fb-obj-invalidate:

=======================
intel_fb_obj_invalidate
=======================

*man intel_fb_obj_invalidate(9)*

*4.6.0-rc5*

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

This function gets called every time rendering on the given object
starts and frontbuffer caching (fbc, low refresh rate for DRRS, panel
self refresh) must be invalidated. For ORIGIN_CS any subsequent
invalidation will be delayed until the rendering completes or a flip on
this frontbuffer plane is scheduled.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
