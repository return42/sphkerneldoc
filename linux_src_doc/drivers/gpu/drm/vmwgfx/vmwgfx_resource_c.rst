.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_resource.c

.. _`vmw_resource_release_id`:

vmw_resource_release_id
=======================

.. c:function:: void vmw_resource_release_id(struct vmw_resource *res)

    release a resource id to the id manager.

    :param res:
        Pointer to the resource.
    :type res: struct vmw_resource \*

.. _`vmw_resource_release_id.description`:

Description
-----------

Release the resource id to the resource id manager and set it to -1

.. _`vmw_resource_alloc_id`:

vmw_resource_alloc_id
=====================

.. c:function:: int vmw_resource_alloc_id(struct vmw_resource *res)

    release a resource id to the id manager.

    :param res:
        Pointer to the resource.
    :type res: struct vmw_resource \*

.. _`vmw_resource_alloc_id.description`:

Description
-----------

Allocate the lowest free resource from the resource manager, and set
\ ``res->id``\  to that id. Returns 0 on success and -ENOMEM on failure.

.. _`vmw_resource_init`:

vmw_resource_init
=================

.. c:function:: int vmw_resource_init(struct vmw_private *dev_priv, struct vmw_resource *res, bool delay_id, void (*res_free)(struct vmw_resource *res), const struct vmw_res_func *func)

    initialize a struct vmw_resource

    :param dev_priv:
        Pointer to a device private struct.
    :type dev_priv: struct vmw_private \*

    :param res:
        The struct vmw_resource to initialize.
    :type res: struct vmw_resource \*

    :param delay_id:
        Boolean whether to defer device id allocation until
        the first validation.
    :type delay_id: bool

    :param void (\*res_free)(struct vmw_resource \*res):
        Resource destructor.

    :param func:
        Resource function table.
    :type func: const struct vmw_res_func \*

.. _`vmw_user_resource_lookup_handle`:

vmw_user_resource_lookup_handle
===============================

.. c:function:: int vmw_user_resource_lookup_handle(struct vmw_private *dev_priv, struct ttm_object_file *tfile, uint32_t handle, const struct vmw_user_resource_conv *converter, struct vmw_resource **p_res)

    lookup a struct resource from a TTM user-space handle and perform basic type checks

    :param dev_priv:
        Pointer to a device private struct
    :type dev_priv: struct vmw_private \*

    :param tfile:
        Pointer to a struct ttm_object_file identifying the caller
    :type tfile: struct ttm_object_file \*

    :param handle:
        The TTM user-space handle
    :type handle: uint32_t

    :param converter:
        Pointer to an object describing the resource type
    :type converter: const struct vmw_user_resource_conv \*

    :param p_res:
        On successful return the location pointed to will contain
        a pointer to a refcounted struct vmw_resource.
    :type p_res: struct vmw_resource \*\*

.. _`vmw_user_resource_lookup_handle.description`:

Description
-----------

If the handle can't be found or is associated with an incorrect resource
type, -EINVAL will be returned.

.. _`vmw_user_resource_noref_lookup_handle`:

vmw_user_resource_noref_lookup_handle
=====================================

.. c:function:: struct vmw_resource *vmw_user_resource_noref_lookup_handle(struct vmw_private *dev_priv, struct ttm_object_file *tfile, uint32_t handle, const struct vmw_user_resource_conv *converter)

    lookup a struct resource from a TTM user-space handle and perform basic type checks

    :param dev_priv:
        Pointer to a device private struct
    :type dev_priv: struct vmw_private \*

    :param tfile:
        Pointer to a struct ttm_object_file identifying the caller
    :type tfile: struct ttm_object_file \*

    :param handle:
        The TTM user-space handle
    :type handle: uint32_t

    :param converter:
        Pointer to an object describing the resource type
    :type converter: const struct vmw_user_resource_conv \*

.. _`vmw_user_resource_noref_lookup_handle.description`:

Description
-----------

If the handle can't be found or is associated with an incorrect resource
type, -EINVAL will be returned.

.. _`vmw_user_lookup_handle`:

vmw_user_lookup_handle
======================

.. c:function:: int vmw_user_lookup_handle(struct vmw_private *dev_priv, struct ttm_object_file *tfile, uint32_t handle, struct vmw_surface **out_surf, struct vmw_buffer_object **out_buf)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param tfile:
        *undescribed*
    :type tfile: struct ttm_object_file \*

    :param handle:
        *undescribed*
    :type handle: uint32_t

    :param out_surf:
        *undescribed*
    :type out_surf: struct vmw_surface \*\*

    :param out_buf:
        *undescribed*
    :type out_buf: struct vmw_buffer_object \*\*

.. _`vmw_user_lookup_handle.description`:

Description
-----------

The pointer this pointed at by out_surf and out_buf needs to be null.

.. _`vmw_resource_buf_alloc`:

vmw_resource_buf_alloc
======================

.. c:function:: int vmw_resource_buf_alloc(struct vmw_resource *res, bool interruptible)

    Allocate a backup buffer for a resource.

    :param res:
        The resource for which to allocate a backup buffer.
    :type res: struct vmw_resource \*

    :param interruptible:
        Whether any sleeps during allocation should be
        performed while interruptible.
    :type interruptible: bool

.. _`vmw_resource_do_validate`:

vmw_resource_do_validate
========================

.. c:function:: int vmw_resource_do_validate(struct vmw_resource *res, struct ttm_validate_buffer *val_buf)

    Make a resource up-to-date and visible to the device.

    :param res:
        The resource to make visible to the device.
    :type res: struct vmw_resource \*

    :param val_buf:
        Information about a buffer possibly
        containing backup data if a bind operation is needed.
    :type val_buf: struct ttm_validate_buffer \*

.. _`vmw_resource_do_validate.description`:

Description
-----------

On hardware resource shortage, this function returns -EBUSY and
should be retried once resources have been freed up.

.. _`vmw_resource_unreserve`:

vmw_resource_unreserve
======================

.. c:function:: void vmw_resource_unreserve(struct vmw_resource *res, bool switch_backup, struct vmw_buffer_object *new_backup, unsigned long new_backup_offset)

    Unreserve a resource previously reserved for command submission.

    :param res:
        Pointer to the struct vmw_resource to unreserve.
    :type res: struct vmw_resource \*

    :param switch_backup:
        Backup buffer has been switched.
    :type switch_backup: bool

    :param new_backup:
        Pointer to new backup buffer if command submission
        switched. May be NULL.
    :type new_backup: struct vmw_buffer_object \*

    :param new_backup_offset:
        New backup offset if \ ``switch_backup``\  is true.
    :type new_backup_offset: unsigned long

.. _`vmw_resource_unreserve.description`:

Description
-----------

Currently unreserving a resource means putting it back on the device's
resource lru list, so that it can be evicted if necessary.

.. _`vmw_resource_check_buffer`:

vmw_resource_check_buffer
=========================

.. c:function:: int vmw_resource_check_buffer(struct ww_acquire_ctx *ticket, struct vmw_resource *res, bool interruptible, struct ttm_validate_buffer *val_buf)

    Check whether a backup buffer is needed for a resource and in that case, allocate one, reserve and validate it.

    :param ticket:
        The ww aqcquire context to use, or NULL if trylocking.
    :type ticket: struct ww_acquire_ctx \*

    :param res:
        The resource for which to allocate a backup buffer.
    :type res: struct vmw_resource \*

    :param interruptible:
        Whether any sleeps during allocation should be
        performed while interruptible.
    :type interruptible: bool

    :param val_buf:
        On successful return contains data about the
        reserved and validated backup buffer.
    :type val_buf: struct ttm_validate_buffer \*

.. _`vmw_resource_reserve`:

vmw_resource_reserve
====================

.. c:function:: int vmw_resource_reserve(struct vmw_resource *res, bool interruptible, bool no_backup)

    Reserve a resource for command submission

    :param res:
        The resource to reserve.
    :type res: struct vmw_resource \*

    :param interruptible:
        *undescribed*
    :type interruptible: bool

    :param no_backup:
        *undescribed*
    :type no_backup: bool

.. _`vmw_resource_reserve.description`:

Description
-----------

This function takes the resource off the LRU list and make sure
a backup buffer is present for guest-backed resources. However,
the buffer may not be bound to the resource at this point.

.. _`vmw_resource_backoff_reservation`:

vmw_resource_backoff_reservation
================================

.. c:function:: void vmw_resource_backoff_reservation(struct ww_acquire_ctx *ticket, struct ttm_validate_buffer *val_buf)

    Unreserve and unreference a backup buffer .

    :param ticket:
        The ww acquire ctx used for reservation.
    :type ticket: struct ww_acquire_ctx \*

    :param val_buf:
        Backup buffer information.
    :type val_buf: struct ttm_validate_buffer \*

.. _`vmw_resource_do_evict`:

vmw_resource_do_evict
=====================

.. c:function:: int vmw_resource_do_evict(struct ww_acquire_ctx *ticket, struct vmw_resource *res, bool interruptible)

    Evict a resource, and transfer its data to a backup buffer.

    :param ticket:
        The ww acquire ticket to use, or NULL if trylocking.
    :type ticket: struct ww_acquire_ctx \*

    :param res:
        The resource to evict.
    :type res: struct vmw_resource \*

    :param interruptible:
        Whether to wait interruptible.
    :type interruptible: bool

.. _`vmw_resource_validate`:

vmw_resource_validate
=====================

.. c:function:: int vmw_resource_validate(struct vmw_resource *res, bool intr)

    Make a resource up-to-date and visible to the device.

    :param res:
        The resource to make visible to the device.
    :type res: struct vmw_resource \*

    :param intr:
        Perform waits interruptible if possible.
    :type intr: bool

.. _`vmw_resource_validate.description`:

Description
-----------

On succesful return, any backup DMA buffer pointed to by \ ``res->backup``\  will
be reserved and validated.
On hardware resource shortage, this function will repeatedly evict
resources of the same type until the validation succeeds.

.. _`vmw_resource_validate.return`:

Return
------

Zero on success, -ERESTARTSYS if interrupted, negative error code
on failure.

.. _`vmw_resource_unbind_list`:

vmw_resource_unbind_list
========================

.. c:function:: void vmw_resource_unbind_list(struct vmw_buffer_object *vbo)

    :param vbo:
        Pointer to the current backing MOB.
    :type vbo: struct vmw_buffer_object \*

.. _`vmw_resource_unbind_list.description`:

Description
-----------

Evicts the Guest Backed hardware resource if the backup
buffer is being moved out of MOB memory.
Note that this function will not race with the resource
validation code, since resource validation and eviction
both require the backup buffer to be reserved.

.. _`vmw_query_readback_all`:

vmw_query_readback_all
======================

.. c:function:: int vmw_query_readback_all(struct vmw_buffer_object *dx_query_mob)

    Read back cached query states

    :param dx_query_mob:
        Buffer containing the DX query MOB
    :type dx_query_mob: struct vmw_buffer_object \*

.. _`vmw_query_readback_all.description`:

Description
-----------

Read back cached states from the device if they exist.  This function
assumings binding_mutex is held.

.. _`vmw_query_move_notify`:

vmw_query_move_notify
=====================

.. c:function:: void vmw_query_move_notify(struct ttm_buffer_object *bo, struct ttm_mem_reg *mem)

    Read back cached query states

    :param bo:
        The TTM buffer object about to move.
    :type bo: struct ttm_buffer_object \*

    :param mem:
        The memory region \ ``bo``\  is moving to.
    :type mem: struct ttm_mem_reg \*

.. _`vmw_query_move_notify.description`:

Description
-----------

Called before the query MOB is swapped out to read back cached query
states from the device.

.. _`vmw_resource_needs_backup`:

vmw_resource_needs_backup
=========================

.. c:function:: bool vmw_resource_needs_backup(const struct vmw_resource *res)

    Return whether a resource needs a backup buffer.

    :param res:
        The resource being queried.
    :type res: const struct vmw_resource \*

.. _`vmw_resource_evict_type`:

vmw_resource_evict_type
=======================

.. c:function:: void vmw_resource_evict_type(struct vmw_private *dev_priv, enum vmw_res_type type)

    Evict all resources of a specific type

    :param dev_priv:
        Pointer to a device private struct
    :type dev_priv: struct vmw_private \*

    :param type:
        The resource type to evict
    :type type: enum vmw_res_type

.. _`vmw_resource_evict_type.description`:

Description
-----------

To avoid thrashing starvation or as part of the hibernation sequence,
try to evict all evictable resources of a specific type.

.. _`vmw_resource_evict_all`:

vmw_resource_evict_all
======================

.. c:function:: void vmw_resource_evict_all(struct vmw_private *dev_priv)

    Evict all evictable resources

    :param dev_priv:
        Pointer to a device private struct
    :type dev_priv: struct vmw_private \*

.. _`vmw_resource_evict_all.description`:

Description
-----------

To avoid thrashing starvation or as part of the hibernation sequence,
evict all evictable resources. In particular this means that all
guest-backed resources that are registered with the device are
evicted and the OTable becomes clean.

.. _`vmw_resource_pin`:

vmw_resource_pin
================

.. c:function:: int vmw_resource_pin(struct vmw_resource *res, bool interruptible)

    Add a pin reference on a resource

    :param res:
        The resource to add a pin reference on
    :type res: struct vmw_resource \*

    :param interruptible:
        *undescribed*
    :type interruptible: bool

.. _`vmw_resource_pin.description`:

Description
-----------

This function adds a pin reference, and if needed validates the resource.
Having a pin reference means that the resource can never be evicted, and
its id will never change as long as there is a pin reference.
This function returns 0 on success and a negative error code on failure.

.. _`vmw_resource_unpin`:

vmw_resource_unpin
==================

.. c:function:: void vmw_resource_unpin(struct vmw_resource *res)

    Remove a pin reference from a resource

    :param res:
        The resource to remove a pin reference from
    :type res: struct vmw_resource \*

.. _`vmw_resource_unpin.description`:

Description
-----------

Having a pin reference means that the resource can never be evicted, and
its id will never change as long as there is a pin reference.

.. _`vmw_res_type`:

vmw_res_type
============

.. c:function:: enum vmw_res_type vmw_res_type(const struct vmw_resource *res)

    Return the resource type

    :param res:
        Pointer to the resource
    :type res: const struct vmw_resource \*

.. This file was automatic generated / don't edit.

