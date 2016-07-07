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

This is what a descriptor looks like, from LSB to MSB:
bits  0-11:    flags, GEN8_CTX\_\* (cached in ctx_desc_template)
bits 12-31:    LRCA, GTT address of (the HWSP of) this context
bits 32-52:    ctx ID, a globally unique tag
bits 53-54:    mbz, reserved for use by hardware
bits 55-63:    group ID, currently unused and set to 0

.. _`intel_lrc_irq_handler`:

intel_lrc_irq_handler
=====================

.. c:function:: void intel_lrc_irq_handler(unsigned long data)

    handle Context Switch interrupts

    :param unsigned long data:
        tasklet handler passed in unsigned long

.. _`intel_lrc_irq_handler.description`:

Description
-----------

Check the unread Context Status Buffers and manage the submission of new
contexts to the ELSP accordingly.

.. _`intel_execlists_submission`:

intel_execlists_submission
==========================

.. c:function:: int intel_execlists_submission(struct i915_execbuffer_params *params, struct drm_i915_gem_execbuffer2 *args, struct list_head *vmas)

    submit a batchbuffer for execution, Execlists style

    :param struct i915_execbuffer_params \*params:
        execbuffer call parameters.

    :param struct drm_i915_gem_execbuffer2 \*args:
        execbuffer call arguments.

    :param struct list_head \*vmas:
        list of vmas.

.. _`intel_execlists_submission.description`:

Description
-----------

This is the evil twin version of i915_gem_ringbuffer_submission. It abstracts
away the submission details of the execbuffer ioctl call.

.. _`intel_execlists_submission.return`:

Return
------

non-zero if the submission fails.

.. _`gen8_init_indirectctx_bb`:

gen8_init_indirectctx_bb
========================

.. c:function:: int gen8_init_indirectctx_bb(struct intel_engine_cs *engine, struct i915_wa_ctx_bb *wa_ctx, uint32_t *const batch, uint32_t *offset)

    initialize indirect ctx batch with WA

    :param struct intel_engine_cs \*engine:
        only applicable for RCS

    :param struct i915_wa_ctx_bb \*wa_ctx:
        structure representing wa_ctx

    :param uint32_t \*const batch:
        page in which WA are loaded

    :param uint32_t \*offset:
        This field specifies the start of the batch, it should be
        cache-aligned otherwise it is adjusted accordingly.
        Typically we only have one indirect_ctx and per_ctx batch buffer which are
        initialized at the beginning and shared across all contexts but this field
        helps us to have multiple batches at different offsets and select them based
        on a criteria. At the moment this batch always start at the beginning of the page
        and at this point we don't have multiple wa_ctx batch buffers.

.. _`gen8_init_indirectctx_bb.offset`:

offset
------

specifies start of the batch, should be cache-aligned. This is updated
with the offset value received as input.

.. _`gen8_init_indirectctx_bb.size`:

size
----

size of the batch in DWORDS but HW expects in terms of cachelines

.. _`gen8_init_indirectctx_bb.description`:

Description
-----------

The number of WA applied are not known at the beginning; we use this field
to return the no of DWORDS written.

It is to be noted that this batch does not contain MI_BATCH_BUFFER_END
so it adds NOOPs as padding to make it cacheline aligned.
MI_BATCH_BUFFER_END will be added to perctx batch and both of them together
makes a complete batch buffer.

.. _`gen8_init_indirectctx_bb.return`:

Return
------

non-zero if we exceed the PAGE_SIZE limit.

.. _`gen8_init_perctx_bb`:

gen8_init_perctx_bb
===================

.. c:function:: int gen8_init_perctx_bb(struct intel_engine_cs *engine, struct i915_wa_ctx_bb *wa_ctx, uint32_t *const batch, uint32_t *offset)

    initialize per ctx batch with WA

    :param struct intel_engine_cs \*engine:
        only applicable for RCS

    :param struct i915_wa_ctx_bb \*wa_ctx:
        structure representing wa_ctx

    :param uint32_t \*const batch:
        page in which WA are loaded

    :param uint32_t \*offset:
        This field specifies the start of this batch.
        This batch is started immediately after indirect_ctx batch. Since we ensure
        that indirect_ctx ends on a cacheline this batch is aligned automatically.

.. _`gen8_init_perctx_bb.offset`:

offset
------

specifies start of the batch, should be cache-aligned.

.. _`gen8_init_perctx_bb.size`:

size
----

size of the batch in DWORDS but HW expects in terms of cachelines

.. _`gen8_init_perctx_bb.description`:

Description
-----------

The number of DWORDS written are returned using this field.

This batch is terminated with MI_BATCH_BUFFER_END and so we need not add padding
to align it with cacheline as padding after MI_BATCH_BUFFER_END is redundant.

.. _`intel_logical_ring_cleanup`:

intel_logical_ring_cleanup
==========================

.. c:function:: void intel_logical_ring_cleanup(struct intel_engine_cs *engine)

    deallocate the Engine Command Streamer

    :param struct intel_engine_cs \*engine:
        Engine Command Streamer.

.. _`intel_logical_rings_init`:

intel_logical_rings_init
========================

.. c:function:: int intel_logical_rings_init(struct drm_device *dev)

    allocate, populate and init the Engine Command Streamers

    :param struct drm_device \*dev:
        DRM device.

.. _`intel_logical_rings_init.description`:

Description
-----------

This function inits the engines for an Execlists submission style (the equivalent in the
legacy ringbuffer submission world would be i915_gem_init_engines). It does it only for
those engines that are present in the hardware.

.. _`intel_logical_rings_init.return`:

Return
------

non-zero if the initialization failed.

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

.. _`execlists_context_deferred_alloc`:

execlists_context_deferred_alloc
================================

.. c:function:: int execlists_context_deferred_alloc(struct i915_gem_context *ctx, struct intel_engine_cs *engine)

    create the LRC specific bits of a context

    :param struct i915_gem_context \*ctx:
        LR context to create.

    :param struct intel_engine_cs \*engine:
        engine to be used with the context.

.. _`execlists_context_deferred_alloc.description`:

Description
-----------

This function can be called more than once, with different engines, if we plan
to use the context with them. The context backing objects and the ringbuffers
(specially the ringbuffer backing objects) suck a lot of memory up, and that's why

.. _`execlists_context_deferred_alloc.the-creation-is-a-deferred-call`:

the creation is a deferred call
-------------------------------

it's better to make sure first that we need to use
a given ring with the context.

.. _`execlists_context_deferred_alloc.return`:

Return
------

non-zero on error.

.. This file was automatic generated / don't edit.

