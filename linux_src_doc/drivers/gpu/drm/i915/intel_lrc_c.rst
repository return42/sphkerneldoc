.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_lrc.c

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

     bits  0-11:    flags, GEN8_CTX_* (cached in ctx->desc_template)
     bits 12-31:    LRCA, GTT address of (the HWSP of) this context
     bits 32-52:    ctx ID, a globally unique tag
     bits 53-54:    mbz, reserved for use by hardware
     bits 55-63:    group ID, currently unused and set to 0

Starting from Gen11, the upper dword of the descriptor has a new format:

     bits 32-36:    reserved
     bits 37-47:    SW context ID
     bits 48:53:    engine instance
     bit 54:        mbz, reserved for use by hardware
     bits 55-60:    SW counter
     bits 61-63:    engine class

engine info, SW context ID and SW counter need to form a unique number
(Context ID) per lrc.

.. _`intel_logical_ring_cleanup`:

intel_logical_ring_cleanup
==========================

.. c:function:: void intel_logical_ring_cleanup(struct intel_engine_cs *engine)

    deallocate the Engine Command Streamer

    :param struct intel_engine_cs \*engine:
        Engine Command Streamer.

.. This file was automatic generated / don't edit.

