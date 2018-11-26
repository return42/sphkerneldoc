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
        struct llist_node free_link;
        struct kref ref;
        struct rcu_head rcu;
        unsigned long user_flags;
    #define UCONTEXT_NO_ZEROMAP 0
    #define UCONTEXT_NO_ERROR_CAPTURE 1
    #define UCONTEXT_BANNABLE 2
        unsigned long flags;
    #define CONTEXT_BANNED 0
    #define CONTEXT_CLOSED 1
    #define CONTEXT_FORCE_SINGLE_SUBMISSION 2
        unsigned int hw_id;
        atomic_t hw_id_pin_count;
        struct list_head hw_id_link;
        u32 user_handle;
        struct i915_sched_attr sched;
        struct intel_context {
            struct i915_gem_context *gem_context;
            struct i915_vma *state;
            struct intel_ring *ring;
            u32 *lrc_reg_state;
            u64 lrc_desc;
            int pin_count;
            const struct intel_context_ops *ops;
        } __engine[I915_NUM_ENGINES];
        u32 ring_size;
        u32 desc_template;
        atomic_t guilty_count;
        atomic_t active_count;
    #define CONTEXT_SCORE_GUILTY 10
    #define CONTEXT_SCORE_BAN_THRESHOLD 40
        atomic_t ban_score;
        u8 remap_slice;
        struct radix_tree_root handles_vma;
        struct list_head handles_list;
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

free_link
    *undescribed*

ref
    reference count
    A reference to a context is held by both the client who created it
    and on each request submitted to the hardware using the request
    (to ensure the hardware has access to the state until it has
    finished all pending writes). See \ :c:func:`i915_gem_context_get`\  and
    \ :c:func:`i915_gem_context_put`\  for access.

rcu
    rcu_head for deferred freeing.

user_flags
    small set of booleans controlled by the user

flags
    small set of booleans

hw_id
    - unique identifier for the context
    The hardware needs to uniquely identify the context for a few
    functions like fault reporting, PASID, scheduling. The
    \ :c:type:`drm_i915_private.context_hw_ida <drm_i915_private>`\  is used to assign a unqiue
    id for the lifetime of the context.

    \ ``hw_id_pin_count``\ : - number of times this context had been pinned
    for use (should be, at most, once per engine).

    \ ``hw_id_link``\ : - all contexts with an assigned id are tracked
    for possible repossession.

hw_id_pin_count
    *undescribed*

hw_id_link
    *undescribed*

user_handle
    userspace identifier
    A unique per-file identifier is generated from
    \ :c:type:`drm_i915_file_private.contexts <drm_i915_file_private>`\ .

sched
    *undescribed*

\__engine
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

handles_vma
    *undescribed*

handles_list
    *undescribed*

.. _`i915_gem_context.description`:

Description
-----------

The struct i915_gem_context represents the combined view of the driver and
logical hardware state for a particular client.

.. This file was automatic generated / don't edit.

