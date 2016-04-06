
.. _API-intel-fb-obj-flush:

==================
intel_fb_obj_flush
==================

*man intel_fb_obj_flush(9)*

*4.6.0-rc1*

flush frontbuffer object


Synopsis
========

.. c:function:: void intel_fb_obj_flush( struct drm_i915_gem_object * obj, bool retire, enum fb_op_origin origin )

Arguments
=========

``obj``
    GEM object to flush

``retire``
    set when retiring asynchronous rendering

``origin``
    which operation caused the flush


Description
===========

This function gets called every time rendering on the given object has completed and frontbuffer caching can be started again. If ``retire`` is true then any delayed flushes will
be unblocked.
