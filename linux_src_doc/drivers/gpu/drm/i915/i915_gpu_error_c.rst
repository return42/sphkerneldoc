.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gpu_error.c

.. _`i915_capture_error_state`:

i915_capture_error_state
========================

.. c:function:: void i915_capture_error_state(struct drm_i915_private *i915, u32 engine_mask, const char *error_msg)

    capture an error record for later analysis

    :param i915:
        i915 device
    :type i915: struct drm_i915_private \*

    :param engine_mask:
        the mask of engines triggering the hang
    :type engine_mask: u32

    :param error_msg:
        a message to insert into the error capture header
    :type error_msg: const char \*

.. _`i915_capture_error_state.description`:

Description
-----------

Should be called when an error is detected (either a hang or an error
interrupt) to capture error state from the time of the error.  Fills
out a structure which becomes available in debugfs for user level tools
to pick up.

.. This file was automatic generated / don't edit.

