.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_validation.c

.. _`vmw_validation_bo_node`:

struct vmw_validation_bo_node
=============================

.. c:type:: struct vmw_validation_bo_node

    Buffer object validation metadata.

.. _`vmw_validation_bo_node.definition`:

Definition
----------

.. code-block:: c

    struct vmw_validation_bo_node {
        struct ttm_validate_buffer base;
        struct drm_hash_item hash;
        u32 as_mob : 1;
        u32 cpu_blit : 1;
    }

.. _`vmw_validation_bo_node.members`:

Members
-------

base
    Metadata used for TTM reservation- and validation.

hash
    A hash entry used for the duplicate detection hash table.

as_mob
    Validate as mob.

cpu_blit
    Validate for cpu blit access.

.. _`vmw_validation_bo_node.description`:

Description
-----------

Bit fields are used since these structures are allocated and freed in
large numbers and space conservation is desired.

.. _`vmw_validation_res_node`:

struct vmw_validation_res_node
==============================

.. c:type:: struct vmw_validation_res_node

    Resource validation metadata.

.. _`vmw_validation_res_node.definition`:

Definition
----------

.. code-block:: c

    struct vmw_validation_res_node {
        struct list_head head;
        struct drm_hash_item hash;
        struct vmw_resource *res;
        struct vmw_buffer_object *new_backup;
        unsigned long new_backup_offset;
        u32 no_buffer_needed : 1;
        u32 switching_backup : 1;
        u32 first_usage : 1;
        u32 reserved : 1;
        unsigned long private[0];
    }

.. _`vmw_validation_res_node.members`:

Members
-------

head
    List head for the resource validation list.

hash
    A hash entry used for the duplicate detection hash table.

res
    Reference counted resource pointer.

new_backup
    Non ref-counted pointer to new backup buffer to be assigned
    to a resource.

new_backup_offset
    Offset into the new backup mob for resources that can
    share MOBs.

no_buffer_needed
    Kernel does not need to allocate a MOB during validation,
    the command stream provides a mob bind operation.

switching_backup
    The validation process is switching backup MOB.

first_usage
    True iff the resource has been seen only once in the current
    validation batch.

reserved
    Whether the resource is currently reserved by this process.

private
    Optionally additional memory for caller-private data.

.. _`vmw_validation_res_node.description`:

Description
-----------

Bit fields are used since these structures are allocated and freed in
large numbers and space conservation is desired.

.. _`vmw_validation_mem_alloc`:

vmw_validation_mem_alloc
========================

.. c:function:: void *vmw_validation_mem_alloc(struct vmw_validation_context *ctx, unsigned int size)

    Allocate kernel memory from the validation context based allocator

    :param ctx:
        The validation context
    :type ctx: struct vmw_validation_context \*

    :param size:
        The number of bytes to allocated.
    :type size: unsigned int

.. _`vmw_validation_mem_alloc.description`:

Description
-----------

The memory allocated may not exceed PAGE_SIZE, and the returned
address is aligned to sizeof(long). All memory allocated this way is

.. _`vmw_validation_mem_alloc.reclaimed-after-validation-when-calling-any-of-the-exported-functions`:

reclaimed after validation when calling any of the exported functions
---------------------------------------------------------------------

\ :c:func:`vmw_validation_unref_lists`\ 
\ :c:func:`vmw_validation_revert`\ 
\ :c:func:`vmw_validation_done`\ 

.. _`vmw_validation_mem_alloc.return`:

Return
------

Pointer to the allocated memory on success. NULL on failure.

.. _`vmw_validation_mem_free`:

vmw_validation_mem_free
=======================

.. c:function:: void vmw_validation_mem_free(struct vmw_validation_context *ctx)

    Free all memory allocated using \ :c:func:`vmw_validation_mem_alloc`\ 

    :param ctx:
        The validation context
    :type ctx: struct vmw_validation_context \*

.. _`vmw_validation_mem_free.description`:

Description
-----------

All memory previously allocated for this context using
\ :c:func:`vmw_validation_mem_alloc`\  is freed.

.. _`vmw_validation_find_bo_dup`:

vmw_validation_find_bo_dup
==========================

.. c:function:: struct vmw_validation_bo_node *vmw_validation_find_bo_dup(struct vmw_validation_context *ctx, struct vmw_buffer_object *vbo)

    Find a duplicate buffer object entry in the validation context's lists.

    :param ctx:
        The validation context to search.
    :type ctx: struct vmw_validation_context \*

    :param vbo:
        The buffer object to search for.
    :type vbo: struct vmw_buffer_object \*

.. _`vmw_validation_find_bo_dup.return`:

Return
------

Pointer to the struct vmw_validation_bo_node referencing the
duplicate, or NULL if none found.

.. _`vmw_validation_find_res_dup`:

vmw_validation_find_res_dup
===========================

.. c:function:: struct vmw_validation_res_node *vmw_validation_find_res_dup(struct vmw_validation_context *ctx, struct vmw_resource *res)

    Find a duplicate resource entry in the validation context's lists.

    :param ctx:
        The validation context to search.
    :type ctx: struct vmw_validation_context \*

    :param res:
        *undescribed*
    :type res: struct vmw_resource \*

.. _`vmw_validation_find_res_dup.return`:

Return
------

Pointer to the struct vmw_validation_bo_node referencing the
duplicate, or NULL if none found.

.. _`vmw_validation_add_bo`:

vmw_validation_add_bo
=====================

.. c:function:: int vmw_validation_add_bo(struct vmw_validation_context *ctx, struct vmw_buffer_object *vbo, bool as_mob, bool cpu_blit)

    Add a buffer object to the validation context.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

    :param vbo:
        The buffer object.
    :type vbo: struct vmw_buffer_object \*

    :param as_mob:
        Validate as mob, otherwise suitable for GMR operations.
    :type as_mob: bool

    :param cpu_blit:
        Validate in a page-mappable location.
    :type cpu_blit: bool

.. _`vmw_validation_add_bo.return`:

Return
------

Zero on success, negative error code otherwise.

.. _`vmw_validation_add_resource`:

vmw_validation_add_resource
===========================

.. c:function:: int vmw_validation_add_resource(struct vmw_validation_context *ctx, struct vmw_resource *res, size_t priv_size, void **p_node, bool *first_usage)

    Add a resource to the validation context.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

    :param res:
        The resource.
    :type res: struct vmw_resource \*

    :param priv_size:
        Size of private, additional metadata.
    :type priv_size: size_t

    :param p_node:
        Output pointer of additional metadata address.
    :type p_node: void \*\*

    :param first_usage:
        Whether this was the first time this resource was seen.
    :type first_usage: bool \*

.. _`vmw_validation_add_resource.return`:

Return
------

Zero on success, negative error code otherwise.

.. _`vmw_validation_res_switch_backup`:

vmw_validation_res_switch_backup
================================

.. c:function:: void vmw_validation_res_switch_backup(struct vmw_validation_context *ctx, void *val_private, struct vmw_buffer_object *vbo, unsigned long backup_offset)

    Register a backup MOB switch during validation.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

    :param val_private:
        The additional meta-data pointer returned when the
        resource was registered with the validation context. Used to identify
        the resource.
    :type val_private: void \*

    :param vbo:
        The new backup buffer object MOB. This buffer object needs to have
        already been registered with the validation context.
    :type vbo: struct vmw_buffer_object \*

    :param backup_offset:
        Offset into the new backup MOB.
    :type backup_offset: unsigned long

.. _`vmw_validation_res_reserve`:

vmw_validation_res_reserve
==========================

.. c:function:: int vmw_validation_res_reserve(struct vmw_validation_context *ctx, bool intr)

    Reserve all resources registered with this validation context.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

    :param intr:
        Use interruptible waits when possible.
    :type intr: bool

.. _`vmw_validation_res_reserve.return`:

Return
------

Zero on success, -ERESTARTSYS if interrupted. Negative error
code on failure.

.. _`vmw_validation_res_unreserve`:

vmw_validation_res_unreserve
============================

.. c:function:: void vmw_validation_res_unreserve(struct vmw_validation_context *ctx, bool backoff)

    Unreserve all reserved resources registered with this validation context.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

    :param backoff:
        Whether this is a backoff- of a commit-type operation. This
        is used to determine whether to switch backup MOBs or not.
    :type backoff: bool

.. _`vmw_validation_bo_validate_single`:

vmw_validation_bo_validate_single
=================================

.. c:function:: int vmw_validation_bo_validate_single(struct ttm_buffer_object *bo, bool interruptible, bool validate_as_mob)

    Validate a single buffer object.

    :param bo:
        The TTM buffer object base.
    :type bo: struct ttm_buffer_object \*

    :param interruptible:
        Whether to perform waits interruptible if possible.
    :type interruptible: bool

    :param validate_as_mob:
        Whether to validate in MOB memory.
    :type validate_as_mob: bool

.. _`vmw_validation_bo_validate_single.return`:

Return
------

Zero on success, -ERESTARTSYS if interrupted. Negative error
code on failure.

.. _`vmw_validation_bo_validate`:

vmw_validation_bo_validate
==========================

.. c:function:: int vmw_validation_bo_validate(struct vmw_validation_context *ctx, bool intr)

    Validate all buffer objects registered with the validation context.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

    :param intr:
        Whether to perform waits interruptible if possible.
    :type intr: bool

.. _`vmw_validation_bo_validate.return`:

Return
------

Zero on success, -ERESTARTSYS if interrupted,
negative error code on failure.

.. _`vmw_validation_res_validate`:

vmw_validation_res_validate
===========================

.. c:function:: int vmw_validation_res_validate(struct vmw_validation_context *ctx, bool intr)

    Validate all resources registered with the validation context.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

    :param intr:
        Whether to perform waits interruptible if possible.
    :type intr: bool

.. _`vmw_validation_res_validate.description`:

Description
-----------

Before this function is called, all resource backup buffers must have
been validated.

.. _`vmw_validation_res_validate.return`:

Return
------

Zero on success, -ERESTARTSYS if interrupted,
negative error code on failure.

.. _`vmw_validation_drop_ht`:

vmw_validation_drop_ht
======================

.. c:function:: void vmw_validation_drop_ht(struct vmw_validation_context *ctx)

    Reset the hash table used for duplicate finding and unregister it from this validation context.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

.. _`vmw_validation_drop_ht.description`:

Description
-----------

The hash table used for duplicate finding is an expensive resource and
may be protected by mutexes that may cause deadlocks during resource
unreferencing if held. After resource- and buffer object registering,
there is no longer any use for this hash table, so allow freeing it
either to shorten any mutex locking time, or before resources- and
buffer objects are freed during validation context cleanup.

.. _`vmw_validation_unref_lists`:

vmw_validation_unref_lists
==========================

.. c:function:: void vmw_validation_unref_lists(struct vmw_validation_context *ctx)

    Unregister previously registered buffer object and resources.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

.. _`vmw_validation_unref_lists.description`:

Description
-----------

Note that this function may cause buffer object- and resource destructors
to be invoked.

.. _`vmw_validation_prepare`:

vmw_validation_prepare
======================

.. c:function:: int vmw_validation_prepare(struct vmw_validation_context *ctx, struct mutex *mutex, bool intr)

    Prepare a validation context for command submission.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

    :param mutex:
        The mutex used to protect resource reservation.
    :type mutex: struct mutex \*

    :param intr:
        Whether to perform waits interruptible if possible.
    :type intr: bool

.. _`vmw_validation_prepare.description`:

Description
-----------

Note that the single reservation mutex \ ``mutex``\  is an unfortunate
construct. Ideally resource reservation should be moved to per-resource
ww_mutexes.
If this functions doesn't return Zero to indicate success, all resources
are left unreserved but still referenced.

.. _`vmw_validation_prepare.return`:

Return
------

Zero on success, -ERESTARTSYS if interrupted, negative error code
on error.

.. _`vmw_validation_revert`:

vmw_validation_revert
=====================

.. c:function:: void vmw_validation_revert(struct vmw_validation_context *ctx)

    Revert validation actions if command submission failed.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

.. _`vmw_validation_revert.description`:

Description
-----------

The caller still needs to unref resources after a call to this function.

.. _`vmw_validation_done`:

vmw_validation_done
===================

.. c:function:: void vmw_validation_done(struct vmw_validation_context *ctx, struct vmw_fence_obj *fence)

    Commit validation actions after command submission success.

    :param ctx:
        The validation context.
    :type ctx: struct vmw_validation_context \*

    :param fence:
        Fence with which to fence all buffer objects taking part in the
        command submission.
    :type fence: struct vmw_fence_obj \*

.. _`vmw_validation_done.description`:

Description
-----------

The caller does NOT need to unref resources after a call to this function.

.. _`vmw_validation_preload_bo`:

vmw_validation_preload_bo
=========================

.. c:function:: int vmw_validation_preload_bo(struct vmw_validation_context *ctx)

    Preload the validation memory allocator for a call to \ :c:func:`vmw_validation_add_bo`\ .

    :param ctx:
        Pointer to the validation context.
    :type ctx: struct vmw_validation_context \*

.. _`vmw_validation_preload_bo.description`:

Description
-----------

Iff this function returns successfully, the next call to
\ :c:func:`vmw_validation_add_bo`\  is guaranteed not to sleep. An error is not fatal
but voids the guarantee.

.. _`vmw_validation_preload_bo.return`:

Return
------

Zero if successful, \ ``-EINVAL``\  otherwise.

.. _`vmw_validation_preload_res`:

vmw_validation_preload_res
==========================

.. c:function:: int vmw_validation_preload_res(struct vmw_validation_context *ctx, unsigned int size)

    Preload the validation memory allocator for a call to \ :c:func:`vmw_validation_add_res`\ .

    :param ctx:
        Pointer to the validation context.
    :type ctx: struct vmw_validation_context \*

    :param size:
        Size of the validation node extra data. See below.
    :type size: unsigned int

.. _`vmw_validation_preload_res.description`:

Description
-----------

Iff this function returns successfully, the next call to
\ :c:func:`vmw_validation_add_res`\  with the same or smaller \ ``size``\  is guaranteed not to
sleep. An error is not fatal but voids the guarantee.

.. _`vmw_validation_preload_res.return`:

Return
------

Zero if successful, \ ``-EINVAL``\  otherwise.

.. This file was automatic generated / don't edit.

