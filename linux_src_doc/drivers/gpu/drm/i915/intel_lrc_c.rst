.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_lrc.c

.. _`intel_sanitize_enable_execlists`:

intel_sanitize_enable_execlists
===============================

.. c:function:: int intel_sanitize_enable_execlists(struct drm_i915_private *dev_priv, int enable_execlists)

    sanitize i915.enable_execlists

    :param struct drm_i915_private \*dev_priv:
        i915 device private

    :param int enable_execlists:
        value of i915.enable_execlists module parameter.

.. _`intel_sanitize_enable_execlists.description`:

Description
-----------

Only certain platforms support Execlists (the prerequisites being
support for Logical Ring Contexts and Aliasing PPGTT or better).

.. _`intel_sanitize_enable_execlists.return`:

Return
------

1 if Execlists is supported and has to be enabled.

.. _`intel_lr_context_descriptor_update`:

intel_lr_context_descriptor_update
==================================

.. c:function:: void intel_lr_context_descriptor_update(struct i915_gem_context *ctx, struct intel_engine_cs *engine)

    calculate & cache the descriptor descriptor for a pinned context

    :param struct i915_gem_context \*ctx:
        Context to work on

    :param struct intel_engine_cs \*engine:
        Engine the descriptor will be used with

.. _`intel_lr_context_descriptor_update.description`:

Description
-----------

The context descriptor encodes various attributes of a context,
including its GTT address and some flags. Because it's fairly
expensive to calculate, we'll just do it once and cache the result,
which remains valid until the context is unpinned.

This is what a descriptor looks like, from LSB to MSB::

     bits  0-11:    flags, GEN8_CTX_* (cached in ctx_desc_template)
     bits 12-31:    LRCA, GTT address of (the HWSP of) this context
     bits 32-52:    ctx ID, a globally unique tag
     bits 53-54:    mbz, reserved for use by hardware
     bits 55-63:    group ID, currently unused and set to 0

.. _`intel_logical_ring_cleanup`:

intel_logical_ring_cleanup
==========================

.. c:function:: void intel_logical_ring_cleanup(struct intel_engine_cs *engine)

    deallocate the Engine Command Streamer

    :param struct intel_engine_cs \*engine:
        Engine Command Streamer.

.. _`intel_lr_context_size`:

intel_lr_context_size
=====================

.. c:function:: uint32_t intel_lr_context_size(struct intel_engine_cs *engine)

    return the size of the context for an engine

    :param struct intel_engine_cs \*engine:
        which engine to find the context size for

.. _`intel_lr_context_size.description`:

Description
-----------

Each engine may require a different amount of space for a context image,
so when allocating (or copying) an image, this function can be used to
find the right size for the specific engine.

.. _`intel_lr_context_size.return`:

Return
------

size (in bytes) of an engine-specific context image

.. _`intel_lr_context_size.note`:

Note
----

this size includes the HWSP, which is part of the context image
in LRC mode, but does not include the "shared data page" used with
GuC submission. The caller should account for this if using the GuC.

.. This file was automatic generated / don't edit.

