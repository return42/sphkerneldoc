.. -*- coding: utf-8; mode: rst -*-

===========
intel_lrc.c
===========

.. _`logical-rings--logical-ring-contexts-and-execlists`:

Logical Rings, Logical Ring Contexts and Execlists
==================================================

Motivation:
GEN8 brings an expansion of the HW contexts: "Logical Ring Contexts".
These expanded contexts enable a number of new abilities, especially
"Execlists" (also implemented in this file).

One of the main differences with the legacy HW contexts is that logical
ring contexts incorporate many more things to the context's state, like
PDPs or ringbuffer control registers:

The reason why PDPs are included in the context is straightforward: as
PPGTTs (per-process GTTs) are actually per-context, having the PDPs
contained there mean you don't need to do a ppgtt->switch_mm yourself,
instead, the GPU will do it for you on the context switch.

But, what about the ringbuffer control registers (head, tail, etc..)?
shouldn't we just need a set of those per engine command streamer? This is
where the name "Logical Rings" starts to make sense: by virtualizing the
rings, the engine cs shifts to a new "ring buffer" with every context
switch. When you want to submit a workload to the GPU you: A) choose your
context, B) find its appropriate virtualized ring, C) write commands to it
and then, finally, D) tell the GPU to switch to that context.

Instead of the legacy MI_SET_CONTEXT, the way you tell the GPU to switch
to a contexts is via a context execution list, ergo "Execlists".

LRC implementation:
Regarding the creation of contexts, we have:

- One global default context.
- One local default context for each opened fd.
- One local extra context for each context create ioctl call.

Now that ringbuffers belong per-context (and not per-engine, like before)
and that contexts are uniquely tied to a given engine (and not reusable,
like before) we need:

- One ringbuffer per-engine inside each context.
- One backing object per-engine inside each context.

The global default context starts its life with these new objects fully
allocated and populated. The local default context for each opened fd is
more complex, because we don't know at creation time which engine is going
to use them. To handle this, we have implemented a deferred creation of LR
contexts:

The local context starts its life as a hollow or blank holder, that only
gets populated for a given engine once we receive an execbuffer. If later
on we receive another execbuffer ioctl for the same context but a different
engine, we allocate/populate a new ringbuffer and context backing object and
so on.

Finally, regarding local contexts created using the ioctl call: as they are
only allowed with the render ring, we can allocate & populate them right
away (no need to defer anything, at least for now).

Execlists implementation:
Execlists are the new method by which, on gen8+ hardware, workloads are
submitted for execution (as opposed to the legacy, ringbuffer-based, method).
This method works as follows:

When a request is committed, its commands (the BB start and any leading or
trailing commands, like the seqno breadcrumbs) are placed in the ringbuffer
for the appropriate context. The tail pointer in the hardware context is not
updated at this time, but instead, kept by the driver in the ringbuffer
structure. A structure representing this request is added to a request queue
for the appropriate engine: this structure contains a copy of the context's
tail after the request was written to the ring buffer and a pointer to the
context itself.

If the engine's request queue was empty before the request was added, the
queue is processed immediately. Otherwise the queue will be processed during
a context switch interrupt. In any case, elements on the queue will get sent
(in pairs) to the GPU's ExecLists Submit Port (ELSP, for short) with a
globally unique 20-bits submission ID.

When execution of a request completes, the GPU updates the context status
buffer with a context complete event and generates a context switch interrupt.
During the interrupt handling, the driver examines the events in the buffer:
for each context complete event, if the announced ID matches that on the head
of the request queue, then that request is retired and removed from the queue.

After processing, if any requests were retired and the queue is not empty
then a new execution list can be submitted. The two requests at the front of
the queue are next to be submitted but since a context may not occur twice in
an execution list, if subsequent requests have the same ID as the first then
the two requests must be combined. This is done simply by discarding requests
at the head of the queue until either only one requests is left (in which case
we use a NULL second context) or the first two requests have unique IDs.

By always executing the first two requests in the queue the driver ensures
that the GPU is kept as busy as possible. In the case where a single context
completes but a second context is still executing, the request for this second
context will be at the head of the queue when we remove the first one. This
request will then be resubmitted along with a new request for a different context,
which will cause the hardware to continue executing the second request and queue
the new request (the GPU detects the condition of a context getting preempted
with the same context and optimizes the context switch flow by not doing
preemption, but just sampling the new tail pointer).


.. _`intel_sanitize_enable_execlists`:

intel_sanitize_enable_execlists
===============================

.. c:function:: int intel_sanitize_enable_execlists (struct drm_device *dev, int enable_execlists)

    sanitize i915.enable_execlists

    :param struct drm_device \*dev:
        DRM device.

    :param int enable_execlists:
        value of i915.enable_execlists module parameter.


.. _`intel_sanitize_enable_execlists.description`:

Description
-----------

Only certain platforms support Execlists (the prerequisites being
support for Logical Ring Contexts and Aliasing PPGTT or better).

Return: 1 if Execlists is supported and has to be enabled.


.. _`intel_lr_context_descriptor_update`:

intel_lr_context_descriptor_update
==================================

.. c:function:: void intel_lr_context_descriptor_update (struct intel_context *ctx, struct intel_engine_cs *ring)

    calculate & cache the descriptor descriptor for a pinned context

    :param struct intel_context \*ctx:
        Context to work on

    :param struct intel_engine_cs \*ring:
        Engine the descriptor will be used with


.. _`intel_lr_context_descriptor_update.description`:

Description
-----------

The context descriptor encodes various attributes of a context,
including its GTT address and some flags. Because it's fairly
expensive to calculate, we'll just do it once and cache the result,
which remains valid until the context is unpinned.

This is what a descriptor looks like, from LSB to MSB::

   bits 0-11:    flags, GEN8_CTX_\* (cached in ctx_desc_template)
   bits 12-31:    LRCA, GTT address of (the HWSP of) this context
   bits 32-51:    ctx ID, a globally unique tag (the LRCA again!)
   bits 52-63:    reserved, may encode the engine ID (for GuC)


.. _`intel_execlists_ctx_id`:

intel_execlists_ctx_id
======================

.. c:function:: u32 intel_execlists_ctx_id (struct intel_context *ctx, struct intel_engine_cs *ring)

    get the Execlists Context ID

    :param struct intel_context \*ctx:
        Context to get the ID for

    :param struct intel_engine_cs \*ring:
        Engine to get the ID for


.. _`intel_execlists_ctx_id.description`:

Description
-----------

Do not confuse with ctx->id! Unfortunately we have a name overload
here: the old context ID we pass to userspace as a handler so that
they can refer to a context, and the new context ID we pass to the
ELSP so that the GPU can inform us of the context status via
interrupts.

The context ID is a portion of the context descriptor, so we can
just extract the required part from the cached descriptor.

Return: 20-bits globally unique context ID.


.. _`intel_lrc_irq_handler`:

intel_lrc_irq_handler
=====================

.. c:function:: void intel_lrc_irq_handler (struct intel_engine_cs *ring)

    handle Context Switch interrupts

    :param struct intel_engine_cs \*ring:
        Engine Command Streamer to handle.


.. _`intel_lrc_irq_handler.description`:

Description
-----------

Check the unread Context Status Buffers and manage the submission of new
contexts to the ELSP accordingly.


.. _`intel_logical_ring_begin`:

intel_logical_ring_begin
========================

.. c:function:: int intel_logical_ring_begin (struct drm_i915_gem_request *req, int num_dwords)

    prepare the logical ringbuffer to accept some commands

    :param struct drm_i915_gem_request \*req:
        The request to start some new work for

    :param int num_dwords:
        number of DWORDs that we plan to write to the ringbuffer.


.. _`intel_logical_ring_begin.description`:

Description
-----------

The ringbuffer might not be ready to accept the commands right away (maybe it needs to
be wrapped, or wait a bit for the tail to be updated). This function takes care of that
and also preallocates a request (every workload submission is still mediated through
requests, same as it did with legacy ringbuffer submission).

Return: non-zero if the ringbuffer is not ready to be written to.


.. _`intel_execlists_submission`:

intel_execlists_submission
==========================

.. c:function:: int intel_execlists_submission (struct i915_execbuffer_params *params, struct drm_i915_gem_execbuffer2 *args, struct list_head *vmas)

    submit a batchbuffer for execution, Execlists style

    :param struct i915_execbuffer_params \*params:

        *undescribed*

    :param struct drm_i915_gem_execbuffer2 \*args:
        execbuffer call arguments.

    :param struct list_head \*vmas:
        list of vmas.


.. _`intel_execlists_submission.description`:

Description
-----------

This is the evil twin version of i915_gem_ringbuffer_submission. It abstracts
away the submission details of the execbuffer ioctl call.

Return: non-zero if the submission fails.


.. _`gen8_init_indirectctx_bb`:

gen8_init_indirectctx_bb
========================

.. c:function:: int gen8_init_indirectctx_bb (struct intel_engine_cs *ring, struct i915_wa_ctx_bb *wa_ctx, uint32_t *const batch, uint32_t *offset)

    initialize indirect ctx batch with WA

    :param struct intel_engine_cs \*ring:
        only applicable for RCS

    :param struct i915_wa_ctx_bb \*wa_ctx:
        structure representing wa_ctx
        offset: specifies start of the batch, should be cache-aligned. This is updated
        with the offset value received as input.
        size: size of the batch in DWORDS but HW expects in terms of cachelines

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


.. _`gen8_init_indirectctx_bb.description`:

Description
-----------

The number of WA applied are not known at the beginning; we use this field
to return the no of DWORDS written.

It is to be noted that this batch does not contain MI_BATCH_BUFFER_END
so it adds NOOPs as padding to make it cacheline aligned.
MI_BATCH_BUFFER_END will be added to perctx batch and both of them together
makes a complete batch buffer.

Return: non-zero if we exceed the PAGE_SIZE limit.


.. _`gen8_init_perctx_bb`:

gen8_init_perctx_bb
===================

.. c:function:: int gen8_init_perctx_bb (struct intel_engine_cs *ring, struct i915_wa_ctx_bb *wa_ctx, uint32_t *const batch, uint32_t *offset)

    initialize per ctx batch with WA

    :param struct intel_engine_cs \*ring:
        only applicable for RCS

    :param struct i915_wa_ctx_bb \*wa_ctx:
        structure representing wa_ctx
        offset: specifies start of the batch, should be cache-aligned.
        size: size of the batch in DWORDS but HW expects in terms of cachelines

    :param uint32_t \*const batch:
        page in which WA are loaded

    :param uint32_t \*offset:
        This field specifies the start of this batch.::

          This batch is started immediately after indirect_ctx batch. Since we ensure
          that indirect_ctx ends on a cacheline this batch is aligned automatically.


.. _`gen8_init_perctx_bb.description`:

Description
-----------

The number of DWORDS written are returned using this field.::

 This batch is terminated with MI_BATCH_BUFFER_END and so we need not add padding
 to align it with cacheline as padding after MI_BATCH_BUFFER_END is redundant.


.. _`intel_logical_ring_cleanup`:

intel_logical_ring_cleanup
==========================

.. c:function:: void intel_logical_ring_cleanup (struct intel_engine_cs *ring)

    deallocate the Engine Command Streamer

    :param struct intel_engine_cs \*ring:
        Engine Command Streamer.


.. _`intel_logical_rings_init`:

intel_logical_rings_init
========================

.. c:function:: int intel_logical_rings_init (struct drm_device *dev)

    allocate, populate and init the Engine Command Streamers

    :param struct drm_device \*dev:
        DRM device.


.. _`intel_logical_rings_init.description`:

Description
-----------

This function inits the engines for an Execlists submission style (the equivalent in the
legacy ringbuffer submission world would be i915_gem_init_rings). It does it only for
those engines that are present in the hardware.

Return: non-zero if the initialization failed.


.. _`intel_lr_context_free`:

intel_lr_context_free
=====================

.. c:function:: void intel_lr_context_free (struct intel_context *ctx)

    free the LRC specific bits of a context

    :param struct intel_context \*ctx:
        the LR context to free.


.. _`intel_lr_context_free.description`:

Description
-----------

The real context freeing is done in i915_gem_context_free: this only
takes care of the bits that are LRC related: the per-engine backing
objects and the logical ringbuffer.


.. _`intel_lr_context_size`:

intel_lr_context_size
=====================

.. c:function:: uint32_t intel_lr_context_size (struct intel_engine_cs *ring)

    return the size of the context for an engine

    :param struct intel_engine_cs \*ring:
        which engine to find the context size for


.. _`intel_lr_context_size.description`:

Description
-----------

Each engine may require a different amount of space for a context image,
so when allocating (or copying) an image, this function can be used to
find the right size for the specific engine.

Return: size (in bytes) of an engine-specific context image

Note: this size includes the HWSP, which is part of the context image
in LRC mode, but does not include the "shared data page" used with
GuC submission. The caller should account for this if using the GuC.


.. _`intel_lr_context_deferred_alloc`:

intel_lr_context_deferred_alloc
===============================

.. c:function:: int intel_lr_context_deferred_alloc (struct intel_context *ctx, struct intel_engine_cs *ring)

    create the LRC specific bits of a context

    :param struct intel_context \*ctx:
        LR context to create.

    :param struct intel_engine_cs \*ring:
        engine to be used with the context.


.. _`intel_lr_context_deferred_alloc.description`:

Description
-----------

This function can be called more than once, with different engines, if we plan
to use the context with them. The context backing objects and the ringbuffers
(specially the ringbuffer backing objects) suck a lot of memory up, and that's why
the creation is a deferred call: it's better to make sure first that we need to use
a given ring with the context.

Return: non-zero on error.

