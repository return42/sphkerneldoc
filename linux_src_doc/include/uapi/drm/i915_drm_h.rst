.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/drm/i915_drm.h

.. _`i915_caching_none`:

I915_CACHING_NONE
=================

.. c:function::  I915_CACHING_NONE()

.. _`i915_caching_none.description`:

Description
-----------

GPU access is not coherent with cpu caches. Default for machines without an
LLC.

.. _`i915_caching_cached`:

I915_CACHING_CACHED
===================

.. c:function::  I915_CACHING_CACHED()

.. _`i915_caching_cached.description`:

Description
-----------

GPU access is coherent with cpu caches and furthermore the data is cached in
last-level caches shared between cpu cores and the gpu GT. Default on
machines with HAS_LLC.

.. _`i915_caching_display`:

I915_CACHING_DISPLAY
====================

.. c:function::  I915_CACHING_DISPLAY()

.. _`i915_caching_display.description`:

Description
-----------

Special GPU caching mode which is coherent with the scanout engines.
Transparently falls back to I915_CACHING_NONE on platforms where no special
cache mode (like write-through or gfdt flushing) is available. The kernel
automatically sets this mode when using a buffer as a scanout target.
Userspace can manually set this mode to avoid a costly stall and clflush in
the hotpath of drawing the first frame.

.. _`i915_perf_ioctl_enable`:

I915_PERF_IOCTL_ENABLE
======================

.. c:function::  I915_PERF_IOCTL_ENABLE()

    via I915_PERF_FLAG_DISABLED or was later disabled via I915_PERF_IOCTL_DISABLE.

.. _`i915_perf_ioctl_enable.description`:

Description
-----------

It is intended to be cheaper to disable and enable a stream than it may be
to close and re-open a stream with the same configuration.

It's undefined whether any pending data for the stream will be lost.

.. _`i915_perf_ioctl_disable`:

I915_PERF_IOCTL_DISABLE
=======================

.. c:function::  I915_PERF_IOCTL_DISABLE()

.. _`i915_perf_ioctl_disable.description`:

Description
-----------

It is an error to try and read a stream that is disabled.

.. This file was automatic generated / don't edit.

