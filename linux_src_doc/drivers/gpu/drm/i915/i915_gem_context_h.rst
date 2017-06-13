.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_context.h

.. _`i915_gem_context`:

struct i915_gem_context
=======================

.. c:type:: struct i915_gem_context

    client state

.. _`i915_gem_context.definition`:

Definition
----------

.. code-block:: c

    struct i915_gem_context {
        struct drm_i915_private *i915;
        struct drm_i915_file_private *file_priv;
        struct i915_hw_ppgtt *ppgtt;
        struct pid *pid;
        const char *name;
        struct list_head link;
        struct kref ref;
        unsigned long flags;
    #define CONTEXT_NO_ZEROMAP BIT(0)
    #define CONTEXT_NO_ERROR_CAPTURE 1
    #define CONTEXT_CLOSED 2
    #define CONTEXT_BANNABLE 3
    #define CONTEXT_BANNED 4
    #define CONTEXT_FORCE_SINGLE_SUBMISSION 5
        unsigned int hw_id;
        u32 user_handle;
        int priority;
        u32 ggtt_offset_bias;
        struct intel_context engine[I915_NUM_ENGINES];
        u32 ring_size;
        u32 desc_template;
        unsigned int guilty_count;
        unsigned int active_count;
    #define CONTEXT_SCORE_GUILTY 10
    #define CONTEXT_SCORE_BAN_THRESHOLD 40
        int ban_score;
        u8 remap_slice;
    }

.. _`i915_gem_context.members`:

Members
-------

i915
    *undescribed*

file_priv
    *undescribed*

ppgtt
    unique address space (GTT)
    In full-ppgtt mode, each context has its own address space ensuring
    complete seperation of one client from all others.

    In other modes, this is a NULL pointer with the expectation that
    the caller uses the shared global GTT.

pid
    process id of creator
    Note that who created the context may not be the principle user,
    as the context may be shared across a local socket. However,
    that should only affect the default context, all contexts created
    explicitly by the client are expected to be isolated.

name
    arbitrary name
    A name is constructed for the context from the creator's process
    name, pid and user handle in order to uniquely identify the
    context in messages.

link
    *undescribed*

ref
    reference count
    A reference to a context is held by both the client who created it
    and on each request submitted to the hardware using the request
    (to ensure the hardware has access to the state until it has
    finished all pending writes). See \ :c:func:`i915_gem_context_get`\  and
    \ :c:func:`i915_gem_context_put`\  for access.

flags
    small set of booleans

hw_id
    - unique identifier for the context
    The hardware needs to uniquely identify the context for a few
    functions like fault reporting, PASID, scheduling. The
    \ :c:type:`drm_i915_private.context_hw_ida <drm_i915_private>`\  is used to assign a unqiue
    id for the lifetime of the context.

user_handle
    userspace identifier
    A unique per-file identifier is generated from
    \ :c:type:`drm_i915_file_private.contexts <drm_i915_file_private>`\ .

priority
    execution and service priority
    All clients are equal, but some are more equal than others!

    Requests from a context with a greater (more positive) value of
    \ ``priority``\  will be executed before those with a lower \ ``priority``\ 
    value, forming a simple QoS.

    The \ :c:type:`drm_i915_private.kernel_context <drm_i915_private>`\  is assigned the lowest priority.

ggtt_offset_bias
    *undescribed*

ring_size
    *undescribed*

desc_template
    *undescribed*

guilty_count
    *undescribed*

active_count
    How many times this context was active during a GPUhang, but did not cause it.

ban_score
    *undescribed*

remap_slice
    *undescribed*

.. _`i915_gem_context.description`:

Description
-----------

The struct i915_gem_context represents the combined view of the driver and
logical hardware state for a particular client.

.. This file was automatic generated / don't edit.

