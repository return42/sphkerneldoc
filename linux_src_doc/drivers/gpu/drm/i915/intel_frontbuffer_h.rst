.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_frontbuffer.h

.. _`intel_fb_obj_invalidate`:

intel_fb_obj_invalidate
=======================

.. c:function:: void intel_fb_obj_invalidate(struct drm_i915_gem_object *obj, enum fb_op_origin origin)

    invalidate frontbuffer object

    :param struct drm_i915_gem_object \*obj:
        GEM object to invalidate

    :param enum fb_op_origin origin:
        which operation caused the invalidation

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

.. c:function:: void intel_fb_obj_flush(struct drm_i915_gem_object *obj, bool retire, enum fb_op_origin origin)

    flush frontbuffer object

    :param struct drm_i915_gem_object \*obj:
        GEM object to flush

    :param bool retire:
        set when retiring asynchronous rendering

    :param enum fb_op_origin origin:
        which operation caused the flush

.. _`intel_fb_obj_flush.description`:

Description
-----------

This function gets called every time rendering on the given object has
completed and frontbuffer caching can be started again. If \ ``retire``\  is true
then any delayed flushes will be unblocked.

.. This file was automatic generated / don't edit.
