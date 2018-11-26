.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_timeline.c

.. _`i915_timelines_park`:

i915_timelines_park
===================

.. c:function:: void i915_timelines_park(struct drm_i915_private *i915)

    called when the driver idles

    :param i915:
        the drm_i915_private device
    :type i915: struct drm_i915_private \*

.. _`i915_timelines_park.description`:

Description
-----------

When the driver is completely idle, we know that all of our sync points
have been signaled and our tracking is then entirely redundant. Any request
to wait upon an older sync point will be completed instantly as we know
the fence is signaled and therefore we will not even look them up in the
sync point map.

.. This file was automatic generated / don't edit.

