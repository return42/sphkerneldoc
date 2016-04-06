.. -*- coding: utf-8; mode: rst -*-

===========
intel_lrc.c
===========



.. _xref_intel_sanitize_enable_execlists:

intel_sanitize_enable_execlists
===============================

.. c:function:: int intel_sanitize_enable_execlists (struct drm_device * dev, int enable_execlists)

    sanitize i915.enable_execlists

    :param struct drm_device * dev:
        DRM device.

    :param int enable_execlists:
        value of i915.enable_execlists module parameter.



Description
-----------

Only certain platforms support Execlists (the prerequisites being
support for Logical Ring Contexts and Aliasing PPGTT or better).



Return
------

1 if Execlists is supported and has to be enabled.




.. _xref_intel_lr_context_descriptor_update:

intel_lr_context_descriptor_update
==================================

.. c:function:: void intel_lr_context_descriptor_update (struct intel_context * ctx, struct intel_engine_cs * ring)

    calculate \\\amp; cache the descriptor descriptor for a pinned context

    :param struct intel_context * ctx:
        Context to work on

    :param struct intel_engine_cs * ring:
        Engine the descriptor will be used with



Description
-----------

The context descriptor encodes various attributes of a context,
including its GTT address and some flags. Because it's fairly
expensive to calculate, we'll just do it once and cache the result,
which remains valid until the context is unpinned.


This is what a descriptor looks like, from LSB to MSB:
   bits 0-11:    flags, GEN8_CTX_* (cached in ctx_desc_template)
   bits 12-31:    LRCA, GTT address of (the HWSP of) this context
   bits 32-51:    ctx ID, a globally unique tag (the LRCA again!)
   bits 52-63:    reserved, may encode the engine ID (for GuC)




.. _xref_intel_execlists_ctx_id:

intel_execlists_ctx_id
======================

.. c:function:: u32 intel_execlists_ctx_id (struct intel_context * ctx, struct intel_engine_cs * ring)

    get the Execlists Context ID

    :param struct intel_context * ctx:
        Context to get the ID for

    :param struct intel_engine_cs * ring:
        Engine to get the ID for



Description
-----------

Do not confuse with ctx->id! Unfortunately we have a name overload



here
----

the old context ID we pass to userspace as a handler so that
they can refer to a context, and the new context ID we pass to the
ELSP so that the GPU can inform us of the context status via
interrupts.


The context ID is a portion of the context descriptor, so we can
just extract the required part from the cached descriptor.



Return
------

20-bits globally unique context ID.




.. _xref_intel_lrc_irq_handler:

intel_lrc_irq_handler
=====================

.. c:function:: void intel_lrc_irq_handler (struct intel_engine_cs * ring)

    handle Context Switch interrupts

    :param struct intel_engine_cs * ring:
        Engine Command Streamer to handle.



Description
-----------

Check the unread Context Status Buffers and manage the submission of new
contexts to the ELSP accordingly.




.. _xref_intel_logical_ring_begin:

intel_logical_ring_begin
========================

.. c:function:: int intel_logical_ring_begin (struct drm_i915_gem_request * req, int num_dwords)

    prepare the logical ringbuffer to accept some commands

    :param struct drm_i915_gem_request * req:
        The request to start some new work for

    :param int num_dwords:
        number of DWORDs that we plan to write to the ringbuffer.



Description
-----------

The ringbuffer might not be ready to accept the commands right away (maybe it needs to
be wrapped, or wait a bit for the tail to be updated). This function takes care of that
and also preallocates a request (every workload submission is still mediated through
requests, same as it did with legacy ringbuffer submission).



Return
------

non-zero if the ringbuffer is not ready to be written to.




.. _xref_intel_execlists_submission:

intel_execlists_submission
==========================

.. c:function:: int intel_execlists_submission (struct i915_execbuffer_params * params, struct drm_i915_gem_execbuffer2 * args, struct list_head * vmas)

    submit a batchbuffer for execution, Execlists style

    :param struct i915_execbuffer_params * params:

        _undescribed_

    :param struct drm_i915_gem_execbuffer2 * args:
        execbuffer call arguments.

    :param struct list_head * vmas:
        list of vmas.



Description
-----------

This is the evil twin version of i915_gem_ringbuffer_submission. It abstracts
away the submission details of the execbuffer ioctl call.



Return
------

non-zero if the submission fails.




.. _xref_gen8_init_indirectctx_bb:

gen8_init_indirectctx_bb
========================

.. c:function:: int gen8_init_indirectctx_bb (struct intel_engine_cs * ring, struct i915_wa_ctx_bb * wa_ctx, uint32_t *const batch, uint32_t * offset)

    initialize indirect ctx batch with WA

    :param struct intel_engine_cs * ring:
        only applicable for RCS

    :param struct i915_wa_ctx_bb * wa_ctx:
        structure representing wa_ctx

    :param uint32_t *const batch:
        page in which WA are loaded

    :param uint32_t * offset:
        This field specifies the start of the batch, it should be
         cache-aligned otherwise it is adjusted accordingly.
         Typically we only have one indirect_ctx and per_ctx batch buffer which are
         initialized at the beginning and shared across all contexts but this field
         helps us to have multiple batches at different offsets and select them based
         on a criteria. At the moment this batch always start at the beginning of the page
         and at this point we don't have multiple wa_ctx batch buffers.



offset
------

specifies start of the batch, should be cache-aligned. This is updated
   with the offset value received as input.



size
----

size of the batch in DWORDS but HW expects in terms of cachelines



Description
-----------

 The number of WA applied are not known at the beginning; we use this field
 to return the no of DWORDS written.


 It is to be noted that this batch does not contain MI_BATCH_BUFFER_END
 so it adds NOOPs as padding to make it cacheline aligned.
 MI_BATCH_BUFFER_END will be added to perctx batch and both of them together
 makes a complete batch buffer.



Return
------

non-zero if we exceed the PAGE_SIZE limit.




.. _xref_gen8_init_perctx_bb:

gen8_init_perctx_bb
===================

.. c:function:: int gen8_init_perctx_bb (struct intel_engine_cs * ring, struct i915_wa_ctx_bb * wa_ctx, uint32_t *const batch, uint32_t * offset)

    initialize per ctx batch with WA

    :param struct intel_engine_cs * ring:
        only applicable for RCS

    :param struct i915_wa_ctx_bb * wa_ctx:
        structure representing wa_ctx

    :param uint32_t *const batch:
        page in which WA are loaded

    :param uint32_t * offset:
        This field specifies the start of this batch.
          This batch is started immediately after indirect_ctx batch. Since we ensure
          that indirect_ctx ends on a cacheline this batch is aligned automatically.



offset
------

specifies start of the batch, should be cache-aligned.



size
----

size of the batch in DWORDS but HW expects in terms of cachelines



Description
-----------

  The number of DWORDS written are returned using this field.


 This batch is terminated with MI_BATCH_BUFFER_END and so we need not add padding
 to align it with cacheline as padding after MI_BATCH_BUFFER_END is redundant.




.. _xref_intel_logical_ring_cleanup:

intel_logical_ring_cleanup
==========================

.. c:function:: void intel_logical_ring_cleanup (struct intel_engine_cs * ring)

    deallocate the Engine Command Streamer

    :param struct intel_engine_cs * ring:
        Engine Command Streamer.




.. _xref_intel_logical_rings_init:

intel_logical_rings_init
========================

.. c:function:: int intel_logical_rings_init (struct drm_device * dev)

    allocate, populate and init the Engine Command Streamers

    :param struct drm_device * dev:
        DRM device.



Description
-----------

This function inits the engines for an Execlists submission style (the equivalent in the
legacy ringbuffer submission world would be i915_gem_init_rings). It does it only for
those engines that are present in the hardware.



Return
------

non-zero if the initialization failed.




.. _xref_intel_lr_context_free:

intel_lr_context_free
=====================

.. c:function:: void intel_lr_context_free (struct intel_context * ctx)

    free the LRC specific bits of a context

    :param struct intel_context * ctx:
        the LR context to free.



The real context freeing is done in i915_gem_context_free
---------------------------------------------------------

this only



takes care of the bits that are LRC related
-------------------------------------------

the per-engine backing
objects and the logical ringbuffer.




.. _xref_intel_lr_context_size:

intel_lr_context_size
=====================

.. c:function:: uint32_t intel_lr_context_size (struct intel_engine_cs * ring)

    return the size of the context for an engine

    :param struct intel_engine_cs * ring:
        which engine to find the context size for



Description
-----------

Each engine may require a different amount of space for a context image,
so when allocating (or copying) an image, this function can be used to
find the right size for the specific engine.



Return
------

size (in bytes) of an engine-specific context image



Note
----

this size includes the HWSP, which is part of the context image
in LRC mode, but does not include the "shared data page" used with
GuC submission. The caller should account for this if using the GuC.




.. _xref_intel_lr_context_deferred_alloc:

intel_lr_context_deferred_alloc
===============================

.. c:function:: int intel_lr_context_deferred_alloc (struct intel_context * ctx, struct intel_engine_cs * ring)

    create the LRC specific bits of a context

    :param struct intel_context * ctx:
        LR context to create.

    :param struct intel_engine_cs * ring:
        engine to be used with the context.



Description
-----------

This function can be called more than once, with different engines, if we plan
to use the context with them. The context backing objects and the ringbuffers
(specially the ringbuffer backing objects) suck a lot of memory up, and that's why



the creation is a deferred call
-------------------------------

it's better to make sure first that we need to use
a given ring with the context.



Return
------

non-zero on error.


