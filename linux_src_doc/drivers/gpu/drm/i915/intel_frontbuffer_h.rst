.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_frontbuffer.h

.. _`intel_fb_obj_invalidate`:

intel_fb_obj_invalidate
=======================

.. c:function:: bool intel_fb_obj_invalidate(struct drm_i915_gem_object *obj, enum fb_op_origin origin)

    invalidate frontbuffer object

    :param obj:
        GEM object to invalidate
    :type obj: struct drm_i915_gem_object \*

    :param origin:
        which operation caused the invalidation
    :type origin: enum fb_op_origin

.. _`intel_fb_obj_invalidate.description`:

Description
-----------

This function gets called every time rendering on the given object starts and
frontbuffer caching (fbc, low refresh rate for DRRS, panel self refresh) must
be invalidated. For ORIGIN_CS any subsequent invalidation will be delayed
until the rendering completes or a flip on this frontbuffer plane is
scheduled.

.. _`intel_fb_obj_flush`:

intel_fb_obj_flush
==================

.. c:function:: void intel_fb_obj_flush(struct drm_i915_gem_object *obj, enum fb_op_origin origin)

    flush frontbuffer object

    :param obj:
        GEM object to flush
    :type obj: struct drm_i915_gem_object \*

    :param origin:
        which operation caused the flush
    :type origin: enum fb_op_origin

.. _`intel_fb_obj_flush.description`:

Description
-----------

This function gets called every time rendering on the given object has
completed and frontbuffer caching can be started again.

.. This file was automatic generated / don't edit.

