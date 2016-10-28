.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_execbuf.c

.. _`vmw_resource_relocation`:

struct vmw_resource_relocation
==============================

.. c:type:: struct vmw_resource_relocation

    Relocation info for resources

.. _`vmw_resource_relocation.definition`:

Definition
----------

.. code-block:: c

    struct vmw_resource_relocation {
        struct list_head head;
        const struct vmw_resource *res;
        unsigned long offset;
    }

.. _`vmw_resource_relocation.members`:

Members
-------

head
    List head for the software context's relocation list.

res
    Non-ref-counted pointer to the resource.

offset
    Offset of 4 byte entries into the command buffer where the
    id that needs fixup is located.

.. _`vmw_resource_val_node`:

struct vmw_resource_val_node
============================

.. c:type:: struct vmw_resource_val_node

    Validation info for resources

.. _`vmw_resource_val_node.definition`:

Definition
----------

.. code-block:: c

    struct vmw_resource_val_node {
        struct list_head head;
        struct drm_hash_item hash;
        struct vmw_resource *res;
        struct vmw_dma_buffer *new_backup;
        struct vmw_ctx_binding_state *staged_bindings;
        unsigned long new_backup_offset;
        u32 first_usage:1;
        u32 switching_backup:1;
        u32 no_buffer_needed:1;
    }

.. _`vmw_resource_val_node.members`:

Members
-------

head
    List head for the software context's resource list.

hash
    Hash entry for quick resouce to val_node lookup.

res
    Ref-counted pointer to the resource.

new_backup
    Refcounted pointer to the new backup buffer.

staged_bindings
    If \ ``res``\  is a context, tracks bindings set up during
    the command batch. Otherwise NULL.

new_backup_offset
    New backup buffer offset if \ ``new_backup``\  is non-NUll.

first_usage
    Set to true the first time the resource is referenced in
    the command stream.

switching_backup
    The command stream provides a new backup buffer for a
    resource.

no_buffer_needed
    This means \ ``switching_backup``\  is true on first buffer
    reference. So resource reservation does not need to allocate a backup
    buffer for the resource.

.. _`vmw_cmd_entry`:

struct vmw_cmd_entry
====================

.. c:type:: struct vmw_cmd_entry

    Describe a command for the verifier

.. _`vmw_cmd_entry.definition`:

Definition
----------

.. code-block:: c

    struct vmw_cmd_entry {
        int (*func)(struct vmw_private *, struct vmw_sw_context *,SVGA3dCmdHeader *);
        bool user_allow;
        bool gb_disable;
        bool gb_enable;
    }

.. _`vmw_cmd_entry.members`:

Members
-------

func
    *undescribed*

user_allow
    Whether allowed from the execbuf ioctl.

gb_disable
    Whether disabled if guest-backed objects are available.

gb_enable
    Whether enabled iff guest-backed objects are available.

.. _`vmw_resources_unreserve`:

vmw_resources_unreserve
=======================

.. c:function:: void vmw_resources_unreserve(struct vmw_sw_context *sw_context, bool backoff)

    unreserve resources previously reserved for command submission.

    :param struct vmw_sw_context \*sw_context:
        pointer to the software context

    :param bool backoff:
        Whether command submission failed.

.. _`vmw_cmd_ctx_first_setup`:

vmw_cmd_ctx_first_setup
=======================

.. c:function:: int vmw_cmd_ctx_first_setup(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, struct vmw_resource_val_node *node)

    Perform the setup needed when a context is added to the validate list.

    :param struct vmw_private \*dev_priv:
        Pointer to the device private:

    :param struct vmw_sw_context \*sw_context:
        The validation context:

    :param struct vmw_resource_val_node \*node:
        The validation node holding this context.

.. _`vmw_resource_val_add`:

vmw_resource_val_add
====================

.. c:function:: int vmw_resource_val_add(struct vmw_sw_context *sw_context, struct vmw_resource *res, struct vmw_resource_val_node **p_node)

    Add a resource to the software context's resource list if it's not already on it.

    :param struct vmw_sw_context \*sw_context:
        Pointer to the software context.

    :param struct vmw_resource \*res:
        Pointer to the resource.
        \ ``p_node``\  On successful return points to a valid pointer to a
        struct vmw_resource_val_node, if non-NULL on entry.

    :param struct vmw_resource_val_node \*\*p_node:
        *undescribed*

.. _`vmw_view_res_val_add`:

vmw_view_res_val_add
====================

.. c:function:: int vmw_view_res_val_add(struct vmw_sw_context *sw_context, struct vmw_resource *view)

    Add a view and the surface it's pointing to to the validation list

    :param struct vmw_sw_context \*sw_context:
        The software context holding the validation list.

    :param struct vmw_resource \*view:
        Pointer to the view resource.

.. _`vmw_view_res_val_add.description`:

Description
-----------

Returns 0 if success, negative error code otherwise.

.. _`vmw_view_id_val_add`:

vmw_view_id_val_add
===================

.. c:function:: int vmw_view_id_val_add(struct vmw_sw_context *sw_context, enum vmw_view_type view_type, u32 id)

    Look up a view and add it and the surface it's pointing to to the validation list.

    :param struct vmw_sw_context \*sw_context:
        The software context holding the validation list.

    :param enum vmw_view_type view_type:
        The view type to look up.

    :param u32 id:
        view id of the view.

.. _`vmw_view_id_val_add.description`:

Description
-----------

The view is represented by a view id and the DX context it's created on,
or scheduled for creation on. If there is no DX context set, the function
will return -EINVAL. Otherwise returns 0 on success and -EINVAL on failure.

.. _`vmw_resource_context_res_add`:

vmw_resource_context_res_add
============================

.. c:function:: int vmw_resource_context_res_add(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, struct vmw_resource *ctx)

    Put resources previously bound to a context on the validation list

    :param struct vmw_private \*dev_priv:
        Pointer to a device private structure

    :param struct vmw_sw_context \*sw_context:
        Pointer to a software context used for this command submission

    :param struct vmw_resource \*ctx:
        Pointer to the context resource

.. _`vmw_resource_context_res_add.description`:

Description
-----------

This function puts all resources that were previously bound to \ ``ctx``\  on
the resource validation list. This is part of the context state reemission

.. _`vmw_resource_relocation_add`:

vmw_resource_relocation_add
===========================

.. c:function:: int vmw_resource_relocation_add(struct list_head *list, const struct vmw_resource *res, unsigned long offset)

    Add a relocation to the relocation list

    :param struct list_head \*list:
        Pointer to head of relocation list.

    :param const struct vmw_resource \*res:
        The resource.

    :param unsigned long offset:
        Offset into the command buffer currently being parsed where the
        id that needs fixup is located. Granularity is 4 bytes.

.. _`vmw_resource_relocations_free`:

vmw_resource_relocations_free
=============================

.. c:function:: void vmw_resource_relocations_free(struct list_head *list)

    Free all relocations on a list

    :param struct list_head \*list:
        Pointer to the head of the relocation list.

.. _`vmw_resource_relocations_apply`:

vmw_resource_relocations_apply
==============================

.. c:function:: void vmw_resource_relocations_apply(uint32_t *cb, struct list_head *list)

    Apply all relocations on a list

    :param uint32_t \*cb:
        Pointer to the start of the command buffer bein patch. This need
        not be the same buffer as the one being parsed when the relocation
        list was built, but the contents must be the same modulo the
        resource ids.

    :param struct list_head \*list:
        Pointer to the head of the relocation list.

.. _`vmw_bo_to_validate_list`:

vmw_bo_to_validate_list
=======================

.. c:function:: int vmw_bo_to_validate_list(struct vmw_sw_context *sw_context, struct vmw_dma_buffer *vbo, bool validate_as_mob, uint32_t *p_val_node)

    add a bo to a validate list

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission batch.

    :param struct vmw_dma_buffer \*vbo:
        *undescribed*

    :param bool validate_as_mob:
        Validate this buffer as a MOB.

    :param uint32_t \*p_val_node:
        If non-NULL Will be updated with the validate node number
        on return.

.. _`vmw_bo_to_validate_list.description`:

Description
-----------

Returns -EINVAL if the limit of number of buffer objects per command
submission is reached.

.. _`vmw_resources_reserve`:

vmw_resources_reserve
=====================

.. c:function:: int vmw_resources_reserve(struct vmw_sw_context *sw_context)

    Reserve all resources on the sw_context's resource list.

    :param struct vmw_sw_context \*sw_context:
        Pointer to the software context.

.. _`vmw_resources_reserve.description`:

Description
-----------

Note that since vmware's command submission currently is protected by
the cmdbuf mutex, no fancy deadlock avoidance is required for resources,
since only a single thread at once will attempt this.

.. _`vmw_resources_validate`:

vmw_resources_validate
======================

.. c:function:: int vmw_resources_validate(struct vmw_sw_context *sw_context)

    Validate all resources on the sw_context's resource list.

    :param struct vmw_sw_context \*sw_context:
        Pointer to the software context.

.. _`vmw_resources_validate.description`:

Description
-----------

Before this function is called, all resource backup buffers must have
been validated.

.. _`vmw_cmd_res_reloc_add`:

vmw_cmd_res_reloc_add
=====================

.. c:function:: int vmw_cmd_res_reloc_add(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, uint32_t *id_loc, struct vmw_resource *res, struct vmw_resource_val_node **p_val)

    Add a resource to a software context's relocation- and validation lists.

    :param struct vmw_private \*dev_priv:
        Pointer to a struct vmw_private identifying the device.

    :param struct vmw_sw_context \*sw_context:
        Pointer to the software context.

    :param uint32_t \*id_loc:
        Pointer to where the id that needs translation is located.

    :param struct vmw_resource \*res:
        Valid pointer to a struct vmw_resource.

    :param struct vmw_resource_val_node \*\*p_val:
        If non null, a pointer to the struct vmw_resource_validate_node
        used for this resource is returned here.

.. _`vmw_cmd_res_check`:

vmw_cmd_res_check
=================

.. c:function:: int vmw_cmd_res_check(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, enum vmw_res_type res_type, const struct vmw_user_resource_conv *converter, uint32_t *id_loc, struct vmw_resource_val_node **p_val)

    Check that a resource is present and if so, put it on the resource validate list unless it's already there.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private structure.

    :param struct vmw_sw_context \*sw_context:
        Pointer to the software context.

    :param enum vmw_res_type res_type:
        Resource type.

    :param const struct vmw_user_resource_conv \*converter:
        User-space visisble type specific information.

    :param uint32_t \*id_loc:
        Pointer to the location in the command buffer currently being
        parsed from where the user-space resource id handle is located.

    :param struct vmw_resource_val_node \*\*p_val:
        Pointer to pointer to resource validalidation node. Populated
        on exit.

.. _`vmw_rebind_all_dx_query`:

vmw_rebind_all_dx_query
=======================

.. c:function:: int vmw_rebind_all_dx_query(struct vmw_resource *ctx_res)

    Rebind DX query associated with the context

    :param struct vmw_resource \*ctx_res:
        context the query belongs to

.. _`vmw_rebind_all_dx_query.description`:

Description
-----------

This function assumes binding_mutex is held.

.. _`vmw_rebind_contexts`:

vmw_rebind_contexts
===================

.. c:function:: int vmw_rebind_contexts(struct vmw_sw_context *sw_context)

    Rebind all resources previously bound to referenced contexts.

    :param struct vmw_sw_context \*sw_context:
        Pointer to the software context.

.. _`vmw_rebind_contexts.description`:

Description
-----------

Rebind context binding points that have been scrubbed because of eviction.

.. _`vmw_view_bindings_add`:

vmw_view_bindings_add
=====================

.. c:function:: int vmw_view_bindings_add(struct vmw_sw_context *sw_context, enum vmw_view_type view_type, enum vmw_ctx_binding_type binding_type, uint32 shader_slot, uint32 view_ids[], u32 num_views, u32 first_slot)

    Add an array of view bindings to a context binding state tracker.

    :param struct vmw_sw_context \*sw_context:
        The execbuf state used for this command.

    :param enum vmw_view_type view_type:
        View type for the bindings.

    :param enum vmw_ctx_binding_type binding_type:
        Binding type for the bindings.

    :param uint32 shader_slot:
        The shader slot to user for the bindings.

    :param uint32 view_ids:
        Array of view ids to be bound.

    :param u32 num_views:
        Number of view ids in \ ``view_ids``\ .

    :param u32 first_slot:
        The binding slot to be used for the first view id in \ ``view_ids``\ .

.. _`vmw_cmd_cid_check`:

vmw_cmd_cid_check
=================

.. c:function:: int vmw_cmd_cid_check(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Check a command header for valid context information.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private structure.

    :param struct vmw_sw_context \*sw_context:
        Pointer to the software context.

    :param SVGA3dCmdHeader \*header:
        A command header with an embedded user-space context handle.

.. _`vmw_cmd_cid_check.convenience-function`:

Convenience function
--------------------

Call vmw_cmd_res_check with the user-space context
handle embedded in \ ``header``\ .

.. _`vmw_query_bo_switch_prepare`:

vmw_query_bo_switch_prepare
===========================

.. c:function:: int vmw_query_bo_switch_prepare(struct vmw_private *dev_priv, struct vmw_dma_buffer *new_query_bo, struct vmw_sw_context *sw_context)

    Prepare to switch pinned buffer for queries.

    :param struct vmw_private \*dev_priv:
        The device private structure.

    :param struct vmw_dma_buffer \*new_query_bo:
        The new buffer holding query results.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission.

.. _`vmw_query_bo_switch_prepare.description`:

Description
-----------

This function checks whether \ ``new_query_bo``\  is suitable for holding
query results, and if another buffer currently is pinned for query
results. If so, the function prepares the state of \ ``sw_context``\  for
switching pinned buffers after successful submission of the current
command batch.

.. _`vmw_query_bo_switch_commit`:

vmw_query_bo_switch_commit
==========================

.. c:function:: void vmw_query_bo_switch_commit(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context)

    Finalize switching pinned query buffer

    :param struct vmw_private \*dev_priv:
        The device private structure.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission batch.

.. _`vmw_query_bo_switch_commit.description`:

Description
-----------

This function will check if we're switching query buffers, and will then,
issue a dummy occlusion query wait used as a query barrier. When the fence
object following that query wait has signaled, we are sure that all
preceding queries have finished, and the old query buffer can be unpinned.
However, since both the new query buffer and the old one are fenced with
that fence, we can do an asynchronus unpin now, and be sure that the
old query buffer won't be moved until the fence has signaled.

As mentioned above, both the new - and old query buffers need to be fenced
using a sequence emitted \*after\* calling this function.

.. _`vmw_translate_mob_ptr`:

vmw_translate_mob_ptr
=====================

.. c:function:: int vmw_translate_mob_ptr(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGAMobId *id, struct vmw_dma_buffer **vmw_bo_p)

    Prepare to translate a user-space buffer handle to a MOB id.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private structure.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command batch validation.

    :param SVGAMobId \*id:
        Pointer to the user-space handle to be translated.

    :param struct vmw_dma_buffer \*\*vmw_bo_p:
        Points to a location that, on successful return will carry
        a reference-counted pointer to the DMA buffer identified by the
        user-space handle in \ ``id``\ .

.. _`vmw_translate_mob_ptr.description`:

Description
-----------

This function saves information needed to translate a user-space buffer
handle to a MOB id. The translation does not take place immediately, but
during a call to \ :c:func:`vmw_apply_relocations`\ . This function builds a relocation
list and a list of buffers to validate. The former needs to be freed using
either \ :c:func:`vmw_apply_relocations`\  or \ :c:func:`vmw_free_relocations`\ . The latter
needs to be freed using vmw_clear_validations.

.. _`vmw_translate_guest_ptr`:

vmw_translate_guest_ptr
=======================

.. c:function:: int vmw_translate_guest_ptr(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGAGuestPtr *ptr, struct vmw_dma_buffer **vmw_bo_p)

    Prepare to translate a user-space buffer handle to a valid SVGAGuestPtr

    :param struct vmw_private \*dev_priv:
        Pointer to a device private structure.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command batch validation.

    :param SVGAGuestPtr \*ptr:
        Pointer to the user-space handle to be translated.

    :param struct vmw_dma_buffer \*\*vmw_bo_p:
        Points to a location that, on successful return will carry
        a reference-counted pointer to the DMA buffer identified by the
        user-space handle in \ ``id``\ .

.. _`vmw_translate_guest_ptr.description`:

Description
-----------

This function saves information needed to translate a user-space buffer
handle to a valid SVGAGuestPtr. The translation does not take place
immediately, but during a call to \ :c:func:`vmw_apply_relocations`\ .
This function builds a relocation list and a list of buffers to validate.
The former needs to be freed using either \ :c:func:`vmw_apply_relocations`\  or
\ :c:func:`vmw_free_relocations`\ . The latter needs to be freed using
vmw_clear_validations.

.. _`vmw_cmd_dx_define_query`:

vmw_cmd_dx_define_query
=======================

.. c:function:: int vmw_cmd_dx_define_query(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    validate a SVGA_3D_CMD_DX_DEFINE_QUERY command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_define_query.description`:

Description
-----------

This function adds the new query into the query COTABLE

.. _`vmw_cmd_dx_bind_query`:

vmw_cmd_dx_bind_query
=====================

.. c:function:: int vmw_cmd_dx_bind_query(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    validate a SVGA_3D_CMD_DX_BIND_QUERY command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_bind_query.description`:

Description
-----------

The query bind operation will eventually associate the query ID
with its backing MOB.  In this function, we take the user mode
MOB ID and use \ :c:func:`vmw_translate_mob_ptr`\  to translate it to its
kernel mode equivalent.

.. _`vmw_cmd_begin_gb_query`:

vmw_cmd_begin_gb_query
======================

.. c:function:: int vmw_cmd_begin_gb_query(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    validate a  SVGA_3D_CMD_BEGIN_GB_QUERY command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_begin_query`:

vmw_cmd_begin_query
===================

.. c:function:: int vmw_cmd_begin_query(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    validate a  SVGA_3D_CMD_BEGIN_QUERY command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_end_gb_query`:

vmw_cmd_end_gb_query
====================

.. c:function:: int vmw_cmd_end_gb_query(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    validate a  SVGA_3D_CMD_END_GB_QUERY command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_end_query`:

vmw_cmd_end_query
=================

.. c:function:: int vmw_cmd_end_query(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    validate a  SVGA_3D_CMD_END_QUERY command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_wait_gb_query`:

vmw_cmd_wait_gb_query
=====================

.. c:function:: int vmw_cmd_wait_gb_query(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    validate a  SVGA_3D_CMD_WAIT_GB_QUERY command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_wait_query`:

vmw_cmd_wait_query
==================

.. c:function:: int vmw_cmd_wait_query(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    validate a  SVGA_3D_CMD_WAIT_QUERY command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context used for this command submission.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_res_switch_backup`:

vmw_cmd_res_switch_backup
=========================

.. c:function:: int vmw_cmd_res_switch_backup(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, struct vmw_resource_val_node *val_node, uint32_t *buf_id, unsigned long backup_offset)

    Utility function to handle backup buffer switching

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param struct vmw_resource_val_node \*val_node:
        The validation node representing the resource.

    :param uint32_t \*buf_id:
        Pointer to the user-space backup buffer handle in the command
        stream.

    :param unsigned long backup_offset:
        Offset of backup into MOB.

.. _`vmw_cmd_res_switch_backup.description`:

Description
-----------

This function prepares for registering a switch of backup buffers
in the resource metadata just prior to unreserving. It's basically a wrapper
around vmw_cmd_res_switch_backup with a different interface.

.. _`vmw_cmd_switch_backup`:

vmw_cmd_switch_backup
=====================

.. c:function:: int vmw_cmd_switch_backup(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, enum vmw_res_type res_type, const struct vmw_user_resource_conv *converter, uint32_t *res_id, uint32_t *buf_id, unsigned long backup_offset)

    Utility function to handle backup buffer switching

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param enum vmw_res_type res_type:
        The resource type.

    :param const struct vmw_user_resource_conv \*converter:
        Information about user-space binding for this resource type.

    :param uint32_t \*res_id:
        Pointer to the user-space resource handle in the command stream.

    :param uint32_t \*buf_id:
        Pointer to the user-space backup buffer handle in the command
        stream.

    :param unsigned long backup_offset:
        Offset of backup into MOB.

.. _`vmw_cmd_switch_backup.description`:

Description
-----------

This function prepares for registering a switch of backup buffers
in the resource metadata just prior to unreserving. It's basically a wrapper
around vmw_cmd_res_switch_backup with a different interface.

.. _`vmw_cmd_bind_gb_surface`:

vmw_cmd_bind_gb_surface
=======================

.. c:function:: int vmw_cmd_bind_gb_surface(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_BIND_GB_SURFACE command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_update_gb_image`:

vmw_cmd_update_gb_image
=======================

.. c:function:: int vmw_cmd_update_gb_image(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_UPDATE_GB_IMAGE command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_update_gb_surface`:

vmw_cmd_update_gb_surface
=========================

.. c:function:: int vmw_cmd_update_gb_surface(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_UPDATE_GB_SURFACE command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_readback_gb_image`:

vmw_cmd_readback_gb_image
=========================

.. c:function:: int vmw_cmd_readback_gb_image(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_READBACK_GB_IMAGE command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_readback_gb_surface`:

vmw_cmd_readback_gb_surface
===========================

.. c:function:: int vmw_cmd_readback_gb_surface(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_READBACK_GB_SURFACE command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_invalidate_gb_image`:

vmw_cmd_invalidate_gb_image
===========================

.. c:function:: int vmw_cmd_invalidate_gb_image(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_INVALIDATE_GB_IMAGE command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_invalidate_gb_surface`:

vmw_cmd_invalidate_gb_surface
=============================

.. c:function:: int vmw_cmd_invalidate_gb_surface(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_INVALIDATE_GB_SURFACE command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_shader_define`:

vmw_cmd_shader_define
=====================

.. c:function:: int vmw_cmd_shader_define(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_SHADER_DEFINE command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_shader_destroy`:

vmw_cmd_shader_destroy
======================

.. c:function:: int vmw_cmd_shader_destroy(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_SHADER_DESTROY command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_set_shader`:

vmw_cmd_set_shader
==================

.. c:function:: int vmw_cmd_set_shader(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_SET_SHADER command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_set_shader_const`:

vmw_cmd_set_shader_const
========================

.. c:function:: int vmw_cmd_set_shader_const(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_SET_SHADER_CONST command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_bind_gb_shader`:

vmw_cmd_bind_gb_shader
======================

.. c:function:: int vmw_cmd_bind_gb_shader(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_BIND_GB_SHADER command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_set_single_constant_buffer`:

vmw_cmd_dx_set_single_constant_buffer
=====================================

.. c:function:: int vmw_cmd_dx_set_single_constant_buffer(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_SET_SINGLE_CONSTANT_BUFFER command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_set_shader_res`:

vmw_cmd_dx_set_shader_res
=========================

.. c:function:: int vmw_cmd_dx_set_shader_res(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_SET_SHADER_RESOURCES command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_set_shader`:

vmw_cmd_dx_set_shader
=====================

.. c:function:: int vmw_cmd_dx_set_shader(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_SET_SHADER command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_set_vertex_buffers`:

vmw_cmd_dx_set_vertex_buffers
=============================

.. c:function:: int vmw_cmd_dx_set_vertex_buffers(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validates an SVGA_3D_CMD_DX_SET_VERTEX_BUFFERS command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_set_index_buffer`:

vmw_cmd_dx_set_index_buffer
===========================

.. c:function:: int vmw_cmd_dx_set_index_buffer(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_IA_SET_VERTEX_BUFFERS command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_set_rendertargets`:

vmw_cmd_dx_set_rendertargets
============================

.. c:function:: int vmw_cmd_dx_set_rendertargets(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_SET_RENDERTARGETS command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_clear_rendertarget_view`:

vmw_cmd_dx_clear_rendertarget_view
==================================

.. c:function:: int vmw_cmd_dx_clear_rendertarget_view(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_CLEAR_RENDERTARGET_VIEW command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_clear_depthstencil_view`:

vmw_cmd_dx_clear_depthstencil_view
==================================

.. c:function:: int vmw_cmd_dx_clear_depthstencil_view(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_CLEAR_DEPTHSTENCIL_VIEW command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_set_so_targets`:

vmw_cmd_dx_set_so_targets
=========================

.. c:function:: int vmw_cmd_dx_set_so_targets(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_SET_SOTARGETS command.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_check_subresource`:

vmw_cmd_dx_check_subresource
============================

.. c:function:: int vmw_cmd_dx_check_subresource(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_[X]_SUBRESOURCE command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_view_remove`:

vmw_cmd_dx_view_remove
======================

.. c:function:: int vmw_cmd_dx_view_remove(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    validate a view remove command and schedule the view resource for removal.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_view_remove.description`:

Description
-----------

Check that the view exists, and if it was not created using this
command batch, make sure it's validated (present in the device) so that
the remove command will not confuse the device.

.. _`vmw_cmd_dx_define_shader`:

vmw_cmd_dx_define_shader
========================

.. c:function:: int vmw_cmd_dx_define_shader(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_DEFINE_SHADER command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_destroy_shader`:

vmw_cmd_dx_destroy_shader
=========================

.. c:function:: int vmw_cmd_dx_destroy_shader(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_DESTROY_SHADER command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_bind_shader`:

vmw_cmd_dx_bind_shader
======================

.. c:function:: int vmw_cmd_dx_bind_shader(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_BIND_SHADER command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_cmd_dx_genmips`:

vmw_cmd_dx_genmips
==================

.. c:function:: int vmw_cmd_dx_genmips(struct vmw_private *dev_priv, struct vmw_sw_context *sw_context, SVGA3dCmdHeader *header)

    Validate an SVGA_3D_CMD_DX_GENMIPS command

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_sw_context \*sw_context:
        The software context being used for this batch.

    :param SVGA3dCmdHeader \*header:
        Pointer to the command header in the command stream.

.. _`vmw_resource_list_unreference`:

vmw_resource_list_unreference
=============================

.. c:function:: void vmw_resource_list_unreference(struct vmw_sw_context *sw_context, struct list_head *list)

    Free up a resource list and unreference all resources referenced by it.

    :param struct vmw_sw_context \*sw_context:
        *undescribed*

    :param struct list_head \*list:
        The resource list.

.. _`vmw_execbuf_fence_commands`:

vmw_execbuf_fence_commands
==========================

.. c:function:: int vmw_execbuf_fence_commands(struct drm_file *file_priv, struct vmw_private *dev_priv, struct vmw_fence_obj **p_fence, uint32_t *p_handle)

    create and submit a command stream fence

    :param struct drm_file \*file_priv:
        *undescribed*

    :param struct vmw_private \*dev_priv:
        *undescribed*

    :param struct vmw_fence_obj \*\*p_fence:
        *undescribed*

    :param uint32_t \*p_handle:
        *undescribed*

.. _`vmw_execbuf_fence_commands.description`:

Description
-----------

Creates a fence object and submits a command stream marker.
If this fails for some reason, We sync the fifo and return NULL.
It is then safe to fence buffers with a NULL pointer.

If \ ``p_handle``\  is not NULL \ ``file_priv``\  must also not be NULL. Creates
a userspace handle if \ ``p_handle``\  is not NULL, otherwise not.

.. _`vmw_execbuf_copy_fence_user`:

vmw_execbuf_copy_fence_user
===========================

.. c:function:: void vmw_execbuf_copy_fence_user(struct vmw_private *dev_priv, struct vmw_fpriv *vmw_fp, int ret, struct drm_vmw_fence_rep __user *user_fence_rep, struct vmw_fence_obj *fence, uint32_t fence_handle)

    copy fence object information to user-space.

    :param struct vmw_private \*dev_priv:
        Pointer to a vmw_private struct.

    :param struct vmw_fpriv \*vmw_fp:
        Pointer to the struct vmw_fpriv representing the calling file.

    :param int ret:
        Return value from fence object creation.

    :param struct drm_vmw_fence_rep __user \*user_fence_rep:
        User space address of a struct drm_vmw_fence_rep to
        which the information should be copied.

    :param struct vmw_fence_obj \*fence:
        Pointer to the fenc object.

    :param uint32_t fence_handle:
        User-space fence handle.

.. _`vmw_execbuf_copy_fence_user.description`:

Description
-----------

This function copies fence information to user-space. If copying fails,
The user-space struct drm_vmw_fence_rep::error member is hopefully
left untouched, and if it's preloaded with an -EFAULT by user-space,
the error will hopefully be detected.
Also if copying fails, user-space will be unable to signal the fence
object so we wait for it immediately, and then unreference the
user-space reference.

.. _`vmw_execbuf_submit_fifo`:

vmw_execbuf_submit_fifo
=======================

.. c:function:: int vmw_execbuf_submit_fifo(struct vmw_private *dev_priv, void *kernel_commands, u32 command_size, struct vmw_sw_context *sw_context)

    Patch a command batch and submit it using the fifo.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private structure.

    :param void \*kernel_commands:
        Pointer to the unpatched command batch.

    :param u32 command_size:
        Size of the unpatched command batch.

    :param struct vmw_sw_context \*sw_context:
        Structure holding the relocation lists.

.. _`vmw_execbuf_submit_fifo.side-effects`:

Side effects
------------

If this function returns 0, then the command batch
pointed to by \ ``kernel_commands``\  will have been modified.

.. _`vmw_execbuf_submit_cmdbuf`:

vmw_execbuf_submit_cmdbuf
=========================

.. c:function:: int vmw_execbuf_submit_cmdbuf(struct vmw_private *dev_priv, struct vmw_cmdbuf_header *header, u32 command_size, struct vmw_sw_context *sw_context)

    Patch a command batch and submit it using the command buffer manager.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private structure.

    :param struct vmw_cmdbuf_header \*header:
        Opaque handle to the command buffer allocation.

    :param u32 command_size:
        Size of the unpatched command batch.

    :param struct vmw_sw_context \*sw_context:
        Structure holding the relocation lists.

.. _`vmw_execbuf_submit_cmdbuf.side-effects`:

Side effects
------------

If this function returns 0, then the command buffer
represented by \ ``header``\  will have been modified.

.. _`vmw_execbuf_cmdbuf`:

vmw_execbuf_cmdbuf
==================

.. c:function:: void *vmw_execbuf_cmdbuf(struct vmw_private *dev_priv, void __user *user_commands, void *kernel_commands, u32 command_size, struct vmw_cmdbuf_header **header)

    Prepare, if possible, a user-space command batch for submission using a command buffer.

    :param struct vmw_private \*dev_priv:
        Pointer to a device private structure.

    :param void __user \*user_commands:
        User-space pointer to the commands to be submitted.

    :param void \*kernel_commands:
        *undescribed*

    :param u32 command_size:
        Size of the unpatched command batch.

    :param struct vmw_cmdbuf_header \*\*header:
        Out parameter returning the opaque pointer to the command buffer.

.. _`vmw_execbuf_cmdbuf.description`:

Description
-----------

This function checks whether we can use the command buffer manager for
submission and if so, creates a command buffer of suitable size and
copies the user data into that buffer.

On successful return, the function returns a pointer to the data in the
command buffer and \*\ ``header``\  is set to non-NULL.
If command buffers could not be used, the function will return the value
of \ ``kernel_commands``\  on function call. That value may be NULL. In that case,
the value of \*\ ``header``\  will be set to NULL.
If an error is encountered, the function will return a pointer error value.
If the function is interrupted by a signal while sleeping, it will return
-ERESTARTSYS casted to a pointer error value.

.. _`vmw_execbuf_unpin_panic`:

vmw_execbuf_unpin_panic
=======================

.. c:function:: void vmw_execbuf_unpin_panic(struct vmw_private *dev_priv)

    Idle the fifo and unpin the query buffer.

    :param struct vmw_private \*dev_priv:
        The device private structure.

.. _`vmw_execbuf_unpin_panic.description`:

Description
-----------

This function is called to idle the fifo and unpin the query buffer
if the normal way to do this hits an error, which should typically be
extremely rare.

.. _`__vmw_execbuf_release_pinned_bo`:

__vmw_execbuf_release_pinned_bo
===============================

.. c:function:: void __vmw_execbuf_release_pinned_bo(struct vmw_private *dev_priv, struct vmw_fence_obj *fence)

    Flush queries and unpin the pinned query bo.

    :param struct vmw_private \*dev_priv:
        The device private structure.

    :param struct vmw_fence_obj \*fence:
        If non-NULL should point to a struct vmw_fence_obj issued
        \_after\_ a query barrier that flushes all queries touching the current
        buffer pointed to by \ ``dev_priv``\ ->pinned_bo

.. _`__vmw_execbuf_release_pinned_bo.description`:

Description
-----------

This function should be used to unpin the pinned query bo, or
as a query barrier when we need to make sure that all queries have
finished before the next fifo command. (For example on hardware
context destructions where the hardware may otherwise leak unfinished
queries).

This function does not return any failure codes, but make attempts
to do safe unpinning in case of errors.

The function will synchronize on the previous query barrier, and will
thus not finish until that barrier has executed.

the \ ``dev_priv``\ ->cmdbuf_mutex needs to be held by the current thread
before calling this function.

.. _`vmw_execbuf_release_pinned_bo`:

vmw_execbuf_release_pinned_bo
=============================

.. c:function:: void vmw_execbuf_release_pinned_bo(struct vmw_private *dev_priv)

    Flush queries and unpin the pinned query bo.

    :param struct vmw_private \*dev_priv:
        The device private structure.

.. _`vmw_execbuf_release_pinned_bo.description`:

Description
-----------

This function should be used to unpin the pinned query bo, or
as a query barrier when we need to make sure that all queries have
finished before the next fifo command. (For example on hardware
context destructions where the hardware may otherwise leak unfinished
queries).

This function does not return any failure codes, but make attempts
to do safe unpinning in case of errors.

The function will synchronize on the previous query barrier, and will
thus not finish until that barrier has executed.

.. This file was automatic generated / don't edit.

