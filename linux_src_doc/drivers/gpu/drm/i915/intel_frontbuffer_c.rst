.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_frontbuffer.c

.. _`intel_frontbuffer_flush`:

intel_frontbuffer_flush
=======================

.. c:function:: void intel_frontbuffer_flush(struct drm_i915_private *dev_priv, unsigned frontbuffer_bits, enum fb_op_origin origin)

    flush frontbuffer

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits

    :param enum fb_op_origin origin:
        which operation caused the flush

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

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits

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

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits

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

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits

.. _`intel_frontbuffer_flip.description`:

Description
-----------

This function gets called after scheduling a flip on \ ``obj``\ . This is for
synchronous plane updates which will happen on the next vblank and which will
not get delayed by pending gpu rendering.

Can be called without any locks held.

.. This file was automatic generated / don't edit.

