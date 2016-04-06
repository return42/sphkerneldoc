.. -*- coding: utf-8; mode: rst -*-

===================
intel_frontbuffer.c
===================



.. _xref_intel_fb_obj_invalidate:

intel_fb_obj_invalidate
=======================

.. c:function:: void intel_fb_obj_invalidate (struct drm_i915_gem_object * obj, enum fb_op_origin origin)

    invalidate frontbuffer object

    :param struct drm_i915_gem_object * obj:
        GEM object to invalidate

    :param enum fb_op_origin origin:
        which operation caused the invalidation



Description
-----------

This function gets called every time rendering on the given object starts and
frontbuffer caching (fbc, low refresh rate for DRRS, panel self refresh) must
be invalidated. For ORIGIN_CS any subsequent invalidation will be delayed
until the rendering completes or a flip on this frontbuffer plane is
scheduled.




.. _xref_intel_frontbuffer_flush:

intel_frontbuffer_flush
=======================

.. c:function:: void intel_frontbuffer_flush (struct drm_device * dev, unsigned frontbuffer_bits, enum fb_op_origin origin)

    flush frontbuffer

    :param struct drm_device * dev:
        DRM device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits

    :param enum fb_op_origin origin:
        which operation caused the flush



Description
-----------

This function gets called every time rendering on the given planes has
completed and frontbuffer caching can be started again. Flushes will get
delayed if they're blocked by some outstanding asynchronous rendering.


Can be called without any locks held.




.. _xref_intel_fb_obj_flush:

intel_fb_obj_flush
==================

.. c:function:: void intel_fb_obj_flush (struct drm_i915_gem_object * obj, bool retire, enum fb_op_origin origin)

    flush frontbuffer object

    :param struct drm_i915_gem_object * obj:
        GEM object to flush

    :param bool retire:
        set when retiring asynchronous rendering

    :param enum fb_op_origin origin:
        which operation caused the flush



Description
-----------

This function gets called every time rendering on the given object has
completed and frontbuffer caching can be started again. If **retire** is true
then any delayed flushes will be unblocked.




.. _xref_intel_frontbuffer_flip_prepare:

intel_frontbuffer_flip_prepare
==============================

.. c:function:: void intel_frontbuffer_flip_prepare (struct drm_device * dev, unsigned frontbuffer_bits)

    prepare asynchronous frontbuffer flip

    :param struct drm_device * dev:
        DRM device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits



Description
-----------

This function gets called after scheduling a flip on **obj**. The actual
frontbuffer flushing will be delayed until completion is signalled with
intel_frontbuffer_flip_complete. If an invalidate happens in between this
flush will be cancelled.


Can be called without any locks held.




.. _xref_intel_frontbuffer_flip_complete:

intel_frontbuffer_flip_complete
===============================

.. c:function:: void intel_frontbuffer_flip_complete (struct drm_device * dev, unsigned frontbuffer_bits)

    complete asynchronous frontbuffer flip

    :param struct drm_device * dev:
        DRM device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits



Description
-----------

This function gets called after the flip has been latched and will complete
on the next vblank. It will execute the flush if it hasn't been cancelled yet.


Can be called without any locks held.




.. _xref_intel_frontbuffer_flip:

intel_frontbuffer_flip
======================

.. c:function:: void intel_frontbuffer_flip (struct drm_device * dev, unsigned frontbuffer_bits)

    synchronous frontbuffer flip

    :param struct drm_device * dev:
        DRM device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits



Description
-----------

This function gets called after scheduling a flip on **obj**. This is for
synchronous plane updates which will happen on the next vblank and which will
not get delayed by pending gpu rendering.


Can be called without any locks held.


