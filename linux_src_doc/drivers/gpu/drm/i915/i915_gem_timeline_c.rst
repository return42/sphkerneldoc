.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_timeline.c

.. _`i915_gem_timelines_mark_idle`:

i915_gem_timelines_mark_idle
============================

.. c:function:: void i915_gem_timelines_mark_idle(struct drm_i915_private *i915)

    - called when the driver idles \ ``i915``\  - the drm_i915_private device

    :param struct drm_i915_private \*i915:
        *undescribed*

.. _`i915_gem_timelines_mark_idle.description`:

Description
-----------

When the driver is completely idle, we know that all of our sync points
have been signaled and our tracking is then entirely redundant. Any request
to wait upon an older sync point will be completed instantly as we know
the fence is signaled and therefore we will not even look them up in the
sync point map.

.. This file was automatic generated / don't edit.

