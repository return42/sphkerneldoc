.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_resource.c

.. _`vmw_resource_release_id`:

vmw_resource_release_id
=======================

.. c:function:: void vmw_resource_release_id(struct vmw_resource *res)

    release a resource id to the id manager.

    :param struct vmw_resource \*res:
        Pointer to the resource.

.. _`vmw_resource_release_id.description`:

Description
-----------

Release the resource id to the resource id manager and set it to -1

.. _`vmw_resource_alloc_id`:

vmw_resource_alloc_id
=====================

.. c:function:: int vmw_resource_alloc_id(struct vmw_resource *res)

    release a resource id to the id manager.

    :param struct vmw_resource \*res:
        Pointer to the resource.

.. _`vmw_resource_alloc_id.description`:

Description
-----------

Allocate the lowest free resource from the resource manager, and set
\ ``res``\ ->id to that id. Returns 0 on success and -ENOMEM on failure.

.. _`vmw_resource_init`:

vmw_resource_init
=================

.. c:function:: int vmw_resource_init(struct vmw_private *dev_priv, struct vmw_resource *res, bool delay_id, void (*res_free)(struct vmw_resource *res), const struct vmw_res_func *func)

    initialize a struct vmw_resource

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct.

    :param struct vmw_resource \*res:
        The struct vmw_resource to initialize.

    :param bool delay_id:
        Boolean whether to defer device id allocation until
        the first validation.

    :param void (\*res_free)(struct vmw_resource \*res):
        Resource destructor.

    :param const struct vmw_res_func \*func:
        Resource function table.

.. _`vmw_resource_activate`:

vmw_resource_activate
=====================

.. c:function:: void vmw_resource_activate(struct vmw_resource *res, void (*hw_destroy)(struct vmw_resource *))

    :param struct vmw_resource \*res:
        Pointer to the newly created resource

    :param void (\*hw_destroy)(struct vmw_resource \*):
        Destroy function. NULL if none.

.. _`vmw_resource_activate.description`:

Description
-----------

Activate a resource after the hardware has been made aware of it.
Set tye destroy function to \ ``destroy``\ . Typically this frees the
resource and destroys the hardware resources associated with it.
Activate basically means that the function vmw_resource_lookup will
find it.

.. _`vmw_user_resource_lookup_handle`:

vmw_user_resource_lookup_handle
===============================

.. c:function:: int vmw_user_resource_lookup_handle(struct vmw_private *dev_priv, struct ttm_object_file *tfile, uint32_t handle, const struct vmw_user_resource_conv *converter, struct vmw_resource **p_res)

    lookup a struct resource from a TTM user-space handle and perform basic type checks

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct

    :param struct ttm_object_file \*tfile:
        Pointer to a struct ttm_object_file identifying the caller

    :param uint32_t handle:
        The TTM user-space handle

    :param const struct vmw_user_resource_conv \*converter:
        Pointer to an object describing the resource type

    :param struct vmw_resource \*\*p_res:
        On successful return the location pointed to will contain
        a pointer to a refcounted struct vmw_resource.

.. _`vmw_user_resource_lookup_handle.description`:

Description
-----------

If the handle can't be found or is associated with an incorrect resource
type, -EINVAL will be returned.

.. _`vmw_user_lookup_handle`:

vmw_user_lookup_handle
======================

.. c:function:: int vmw_user_lookup_handle(struct vmw_private *dev_priv, struct ttm_object_file *tfile, uint32_t handle, struct vmw_surface **out_surf, struct vmw_dma_buffer **out_buf)

    :param struct vmw_private \*dev_priv:
        *undescribed*

    :param struct ttm_object_file \*tfile:
        *undescribed*

    :param uint32_t handle:
        *undescribed*

    :param struct vmw_surface \*\*out_surf:
        *undescribed*

    :param struct vmw_dma_buffer \*\*out_buf:
        *undescribed*

.. _`vmw_user_lookup_handle.description`:

Description
-----------

The pointer this pointed at by out_surf and out_buf needs to be null.

.. _`vmw_dmabuf_acc_size`:

vmw_dmabuf_acc_size
===================

.. c:function:: size_t vmw_dmabuf_acc_size(struct vmw_private *dev_priv, size_t size, bool user)

    :param struct vmw_private \*dev_priv:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param bool user:
        *undescribed*

.. _`vmw_user_dmabuf_alloc`:

vmw_user_dmabuf_alloc
=====================

.. c:function:: int vmw_user_dmabuf_alloc(struct vmw_private *dev_priv, struct ttm_object_file *tfile, uint32_t size, bool shareable, uint32_t *handle, struct vmw_dma_buffer **p_dma_buf, struct ttm_base_object **p_base)

    Allocate a user dma buffer

    :param struct vmw_private \*dev_priv:
        Pointer to a struct device private.

    :param struct ttm_object_file \*tfile:
        Pointer to a struct ttm_object_file on which to register the user
        object.

    :param uint32_t size:
        Size of the dma buffer.

    :param bool shareable:
        Boolean whether the buffer is shareable with other open files.

    :param uint32_t \*handle:
        Pointer to where the handle value should be assigned.

    :param struct vmw_dma_buffer \*\*p_dma_buf:
        Pointer to where the refcounted struct vmw_dma_buffer pointer
        should be assigned.

    :param struct ttm_base_object \*\*p_base:
        *undescribed*

.. _`vmw_user_dmabuf_verify_access`:

vmw_user_dmabuf_verify_access
=============================

.. c:function:: int vmw_user_dmabuf_verify_access(struct ttm_buffer_object *bo, struct ttm_object_file *tfile)

    verify access permissions on this buffer object.

    :param struct ttm_buffer_object \*bo:
        Pointer to the buffer object being accessed

    :param struct ttm_object_file \*tfile:
        Identifying the caller.

.. _`vmw_user_dmabuf_synccpu_grab`:

vmw_user_dmabuf_synccpu_grab
============================

.. c:function:: int vmw_user_dmabuf_synccpu_grab(struct vmw_user_dma_buffer *user_bo, struct ttm_object_file *tfile, uint32_t flags)

    Grab a struct vmw_user_dma_buffer for cpu access, idling previous GPU operations on the buffer and optionally blocking it for further command submissions.

    :param struct vmw_user_dma_buffer \*user_bo:
        Pointer to the buffer object being grabbed for CPU access

    :param struct ttm_object_file \*tfile:
        Identifying the caller.

    :param uint32_t flags:
        Flags indicating how the grab should be performed.

.. _`vmw_user_dmabuf_synccpu_grab.description`:

Description
-----------

A blocking grab will be automatically released when \ ``tfile``\  is closed.

.. _`vmw_user_dmabuf_synccpu_release`:

vmw_user_dmabuf_synccpu_release
===============================

.. c:function:: int vmw_user_dmabuf_synccpu_release(uint32_t handle, struct ttm_object_file *tfile, uint32_t flags)

    Release a previous grab for CPU access, and unblock command submission on the buffer if blocked.

    :param uint32_t handle:
        Handle identifying the buffer object.

    :param struct ttm_object_file \*tfile:
        Identifying the caller.

    :param uint32_t flags:
        Flags indicating the type of release.

.. _`vmw_user_dmabuf_synccpu_ioctl`:

vmw_user_dmabuf_synccpu_ioctl
=============================

.. c:function:: int vmw_user_dmabuf_synccpu_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    ioctl function implementing the synccpu functionality.

    :param struct drm_device \*dev:
        Identifies the drm device.

    :param void \*data:
        Pointer to the ioctl argument.

    :param struct drm_file \*file_priv:
        Identifies the caller.

.. _`vmw_user_dmabuf_synccpu_ioctl.description`:

Description
-----------

This function checks the ioctl arguments for validity and calls the
relevant synccpu functions.

.. _`vmw_user_stream_base_release`:

vmw_user_stream_base_release
============================

.. c:function:: void vmw_user_stream_base_release(struct ttm_base_object **p_base)

    base object. It releases the base-object's reference on the resource object.

    :param struct ttm_base_object \*\*p_base:
        *undescribed*

.. _`vmw_dumb_create`:

vmw_dumb_create
===============

.. c:function:: int vmw_dumb_create(struct drm_file *file_priv, struct drm_device *dev, struct drm_mode_create_dumb *args)

    Create a dumb kms buffer

    :param struct drm_file \*file_priv:
        Pointer to a struct drm_file identifying the caller.

    :param struct drm_device \*dev:
        Pointer to the drm device.

    :param struct drm_mode_create_dumb \*args:
        Pointer to a struct drm_mode_create_dumb structure

.. _`vmw_dumb_create.description`:

Description
-----------

This is a driver callback for the core drm create_dumb functionality.
Note that this is very similar to the vmw_dmabuf_alloc ioctl, except
that the arguments have a different format.

.. _`vmw_dumb_map_offset`:

vmw_dumb_map_offset
===================

.. c:function:: int vmw_dumb_map_offset(struct drm_file *file_priv, struct drm_device *dev, uint32_t handle, uint64_t *offset)

    Return the address space offset of a dumb buffer

    :param struct drm_file \*file_priv:
        Pointer to a struct drm_file identifying the caller.

    :param struct drm_device \*dev:
        Pointer to the drm device.

    :param uint32_t handle:
        Handle identifying the dumb buffer.

    :param uint64_t \*offset:
        The address space offset returned.

.. _`vmw_dumb_map_offset.description`:

Description
-----------

This is a driver callback for the core drm dumb_map_offset functionality.

.. _`vmw_dumb_destroy`:

vmw_dumb_destroy
================

.. c:function:: int vmw_dumb_destroy(struct drm_file *file_priv, struct drm_device *dev, uint32_t handle)

    Destroy a dumb boffer

    :param struct drm_file \*file_priv:
        Pointer to a struct drm_file identifying the caller.

    :param struct drm_device \*dev:
        Pointer to the drm device.

    :param uint32_t handle:
        Handle identifying the dumb buffer.

.. _`vmw_dumb_destroy.description`:

Description
-----------

This is a driver callback for the core drm dumb_destroy functionality.

.. _`vmw_resource_buf_alloc`:

vmw_resource_buf_alloc
======================

.. c:function:: int vmw_resource_buf_alloc(struct vmw_resource *res, bool interruptible)

    Allocate a backup buffer for a resource.

    :param struct vmw_resource \*res:
        The resource for which to allocate a backup buffer.

    :param bool interruptible:
        Whether any sleeps during allocation should be
        performed while interruptible.

.. _`vmw_resource_do_validate`:

vmw_resource_do_validate
========================

.. c:function:: int vmw_resource_do_validate(struct vmw_resource *res, struct ttm_validate_buffer *val_buf)

    Make a resource up-to-date and visible to the device.

    :param struct vmw_resource \*res:
        The resource to make visible to the device.

    :param struct ttm_validate_buffer \*val_buf:
        Information about a buffer possibly
        containing backup data if a bind operation is needed.

.. _`vmw_resource_do_validate.description`:

Description
-----------

On hardware resource shortage, this function returns -EBUSY and
should be retried once resources have been freed up.

.. _`vmw_resource_unreserve`:

vmw_resource_unreserve
======================

.. c:function:: void vmw_resource_unreserve(struct vmw_resource *res, bool switch_backup, struct vmw_dma_buffer *new_backup, unsigned long new_backup_offset)

    Unreserve a resource previously reserved for command submission.

    :param struct vmw_resource \*res:
        Pointer to the struct vmw_resource to unreserve.

    :param bool switch_backup:
        Backup buffer has been switched.

    :param struct vmw_dma_buffer \*new_backup:
        Pointer to new backup buffer if command submission
        switched. May be NULL.

    :param unsigned long new_backup_offset:
        New backup offset if \ ``switch_backup``\  is true.

.. _`vmw_resource_unreserve.description`:

Description
-----------

Currently unreserving a resource means putting it back on the device's
resource lru list, so that it can be evicted if necessary.

.. _`vmw_resource_check_buffer`:

vmw_resource_check_buffer
=========================

.. c:function:: int vmw_resource_check_buffer(struct vmw_resource *res, bool interruptible, struct ttm_validate_buffer *val_buf)

    Check whether a backup buffer is needed for a resource and in that case, allocate one, reserve and validate it.

    :param struct vmw_resource \*res:
        The resource for which to allocate a backup buffer.

    :param bool interruptible:
        Whether any sleeps during allocation should be
        performed while interruptible.

    :param struct ttm_validate_buffer \*val_buf:
        On successful return contains data about the
        reserved and validated backup buffer.

.. _`vmw_resource_reserve`:

vmw_resource_reserve
====================

.. c:function:: int vmw_resource_reserve(struct vmw_resource *res, bool interruptible, bool no_backup)

    Reserve a resource for command submission

    :param struct vmw_resource \*res:
        The resource to reserve.

    :param bool interruptible:
        *undescribed*

    :param bool no_backup:
        *undescribed*

.. _`vmw_resource_reserve.description`:

Description
-----------

This function takes the resource off the LRU list and make sure
a backup buffer is present for guest-backed resources. However,
the buffer may not be bound to the resource at this point.

.. _`vmw_resource_backoff_reservation`:

vmw_resource_backoff_reservation
================================

.. c:function:: void vmw_resource_backoff_reservation(struct ttm_validate_buffer *val_buf)

    Unreserve and unreference a backup buffer .

    :param struct ttm_validate_buffer \*val_buf:
        Backup buffer information.

.. _`vmw_resource_do_evict`:

vmw_resource_do_evict
=====================

.. c:function:: int vmw_resource_do_evict(struct vmw_resource *res, bool interruptible)

    Evict a resource, and transfer its data to a backup buffer.

    :param struct vmw_resource \*res:
        The resource to evict.

    :param bool interruptible:
        Whether to wait interruptible.

.. _`vmw_resource_validate`:

vmw_resource_validate
=====================

.. c:function:: int vmw_resource_validate(struct vmw_resource *res)

    Make a resource up-to-date and visible to the device.

    :param struct vmw_resource \*res:
        The resource to make visible to the device.

.. _`vmw_resource_validate.description`:

Description
-----------

On succesful return, any backup DMA buffer pointed to by \ ``res``\ ->backup will
be reserved and validated.
On hardware resource shortage, this function will repeatedly evict
resources of the same type until the validation succeeds.

.. _`vmw_fence_single_bo`:

vmw_fence_single_bo
===================

.. c:function:: void vmw_fence_single_bo(struct ttm_buffer_object *bo, struct vmw_fence_obj *fence)

    Utility function to fence a single TTM buffer object without unreserving it.

    :param struct ttm_buffer_object \*bo:
        Pointer to the struct ttm_buffer_object to fence.

    :param struct vmw_fence_obj \*fence:
        Pointer to the fence. If NULL, this function will
        insert a fence into the command stream..

.. _`vmw_fence_single_bo.description`:

Description
-----------

Contrary to the ttm_eu version of this function, it takes only
a single buffer object instead of a list, and it also doesn't
unreserve the buffer object, which needs to be done separately.

.. _`vmw_resource_move_notify`:

vmw_resource_move_notify
========================

.. c:function:: void vmw_resource_move_notify(struct ttm_buffer_object *bo, struct ttm_mem_reg *mem)

    TTM move_notify_callback

    :param struct ttm_buffer_object \*bo:
        The TTM buffer object about to move.

    :param struct ttm_mem_reg \*mem:
        The struct ttm_mem_reg indicating to what memory
        region the move is taking place.

.. _`vmw_resource_move_notify.description`:

Description
-----------

Evicts the Guest Backed hardware resource if the backup
buffer is being moved out of MOB memory.
Note that this function should not race with the resource
validation code as long as it accesses only members of struct
resource that remain static while bo::res is !NULL and
while we have \ ``bo``\  reserved. struct resource::backup is \*not\* a
static member. The resource validation code will take care
to set \ ``bo``\ ::res to NULL, while having \ ``bo``\  reserved when the
buffer is no longer bound to the resource, so \ ``bo``\ :res can be
used to determine whether there is a need to unbind and whether
it is safe to unbind.

.. _`vmw_query_readback_all`:

vmw_query_readback_all
======================

.. c:function:: int vmw_query_readback_all(struct vmw_dma_buffer *dx_query_mob)

    Read back cached query states

    :param struct vmw_dma_buffer \*dx_query_mob:
        Buffer containing the DX query MOB

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

    :param struct ttm_buffer_object \*bo:
        The TTM buffer object about to move.

    :param struct ttm_mem_reg \*mem:
        The memory region \ ``bo``\  is moving to.

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

    :param const struct vmw_resource \*res:
        The resource being queried.

.. _`vmw_resource_evict_type`:

vmw_resource_evict_type
=======================

.. c:function:: void vmw_resource_evict_type(struct vmw_private *dev_priv, enum vmw_res_type type)

    Evict all resources of a specific type

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct

    :param enum vmw_res_type type:
        The resource type to evict

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

    :param struct vmw_private \*dev_priv:
        Pointer to a device private struct

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

    :param struct vmw_resource \*res:
        The resource to add a pin reference on

    :param bool interruptible:
        *undescribed*

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

    :param struct vmw_resource \*res:
        The resource to remove a pin reference from

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

    :param const struct vmw_resource \*res:
        Pointer to the resource

.. This file was automatic generated / don't edit.

