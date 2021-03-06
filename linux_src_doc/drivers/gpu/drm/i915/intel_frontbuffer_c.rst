.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_frontbuffer.c

.. _`frontbuffer-tracking`:

frontbuffer tracking
====================

Many features require us to track changes to the currently active
frontbuffer, especially rendering targeted at the frontbuffer.

To be able to do so GEM tracks frontbuffers using a bitmask for all possible
frontbuffer slots through \ :c:func:`i915_gem_track_fb`\ . The function in this file are
then called when the contents of the frontbuffer are invalidated, when
frontbuffer rendering has stopped again to flush out all the changes and when
the frontbuffer is exchanged with a flip. Subsystems interested in
frontbuffer changes (e.g. PSR, FBC, DRRS) should directly put their callbacks
into the relevant places and filter for the frontbuffer slots that they are
interested int.

On a high level there are two types of powersaving features. The first one
work like a special cache (FBC and PSR) and are interested when they should
stop caching and when to restart caching. This is done by placing callbacks
into the invalidate and the flush functions: At invalidate the caching must
be stopped and at flush time it can be restarted. And maybe they need to know
when the frontbuffer changes (e.g. when the hw doesn't initiate an invalidate
and flush on its own) which can be achieved with placing callbacks into the
flip functions.

The other type of display power saving feature only cares about busyness
(e.g. DRRS). In that case all three (invalidate, flush and flip) indicate
busyness. There is no direct way to detect idleness. Instead an idle timer
work delayed work should be started from the flush and flip functions and
cancelled as soon as busyness is detected.

Note that there's also an older frontbuffer activity tracking scheme which
just tracks general activity. This is done by the various mark_busy and
mark_idle functions. For display power management features using these
functions is deprecated and should be avoided.

.. _`intel_frontbuffer_flush`:

intel_frontbuffer_flush
=======================

.. c:function:: void intel_frontbuffer_flush(struct drm_i915_private *dev_priv, unsigned frontbuffer_bits, enum fb_op_origin origin)

    flush frontbuffer

    :param dev_priv:
        i915 device
    :type dev_priv: struct drm_i915_private \*

    :param frontbuffer_bits:
        frontbuffer plane tracking bits
    :type frontbuffer_bits: unsigned

    :param origin:
        which operation caused the flush
    :type origin: enum fb_op_origin

.. _`intel_frontbuffer_flush.description`:

Description
-----------

This function gets called every time rendering on the given planes has
completed and frontbuffer caching can be started again. Flushes will get
delayed if they're blocked by some outstanding asynchronous rendering.

Can be called without any locks held.

.. _`intel_frontbuffer_flip_prepare`:

intel_frontbuffer_flip_prepare
==============================

.. c:function:: void intel_frontbuffer_flip_prepare(struct drm_i915_private *dev_priv, unsigned frontbuffer_bits)

    prepare asynchronous frontbuffer flip

    :param dev_priv:
        i915 device
    :type dev_priv: struct drm_i915_private \*

    :param frontbuffer_bits:
        frontbuffer plane tracking bits
    :type frontbuffer_bits: unsigned

.. _`intel_frontbuffer_flip_prepare.description`:

Description
-----------

This function gets called after scheduling a flip on \ ``obj``\ . The actual
frontbuffer flushing will be delayed until completion is signalled with
intel_frontbuffer_flip_complete. If an invalidate happens in between this
flush will be cancelled.

Can be called without any locks held.

.. _`intel_frontbuffer_flip_complete`:

intel_frontbuffer_flip_complete
===============================

.. c:function:: void intel_frontbuffer_flip_complete(struct drm_i915_private *dev_priv, unsigned frontbuffer_bits)

    complete asynchronous frontbuffer flip

    :param dev_priv:
        i915 device
    :type dev_priv: struct drm_i915_private \*

    :param frontbuffer_bits:
        frontbuffer plane tracking bits
    :type frontbuffer_bits: unsigned

.. _`intel_frontbuffer_flip_complete.description`:

Description
-----------

This function gets called after the flip has been latched and will complete
on the next vblank. It will execute the flush if it hasn't been cancelled yet.

Can be called without any locks held.

.. _`intel_frontbuffer_flip`:

intel_frontbuffer_flip
======================

.. c:function:: void intel_frontbuffer_flip(struct drm_i915_private *dev_priv, unsigned frontbuffer_bits)

    synchronous frontbuffer flip

    :param dev_priv:
        i915 device
    :type dev_priv: struct drm_i915_private \*

    :param frontbuffer_bits:
        frontbuffer plane tracking bits
    :type frontbuffer_bits: unsigned

.. _`intel_frontbuffer_flip.description`:

Description
-----------

This function gets called after scheduling a flip on \ ``obj``\ . This is for
synchronous plane updates which will happen on the next vblank and which will
not get delayed by pending gpu rendering.

Can be called without any locks held.

.. This file was automatic generated / don't edit.

