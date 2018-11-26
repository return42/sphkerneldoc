.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_bo.c

.. _`vmw_user_buffer_object`:

struct vmw_user_buffer_object
=============================

.. c:type:: struct vmw_user_buffer_object

    User-space-visible buffer object

.. _`vmw_user_buffer_object.definition`:

Definition
----------

.. code-block:: c

    struct vmw_user_buffer_object {
        struct ttm_prime_object prime;
        struct vmw_buffer_object vbo;
    }

.. _`vmw_user_buffer_object.members`:

Members
-------

prime
    The prime object providing user visibility.

vbo
    The struct vmw_buffer_object

.. _`vmw_buffer_object`:

vmw_buffer_object
=================

.. c:function:: struct vmw_buffer_object *vmw_buffer_object(struct ttm_buffer_object *bo)

    Convert a struct ttm_buffer_object to a struct vmw_buffer_object.

    :param bo:
        Pointer to the TTM buffer object.
    :type bo: struct ttm_buffer_object \*

.. _`vmw_buffer_object.return`:

Return
------

Pointer to the struct vmw_buffer_object embedding the
TTM buffer object.

.. _`vmw_user_buffer_object`:

vmw_user_buffer_object
======================

.. c:function:: struct vmw_user_buffer_object *vmw_user_buffer_object(struct ttm_buffer_object *bo)

    Convert a struct ttm_buffer_object to a struct vmw_user_buffer_object.

    :param bo:
        Pointer to the TTM buffer object.
    :type bo: struct ttm_buffer_object \*

.. _`vmw_user_buffer_object.return`:

Return
------

Pointer to the struct vmw_buffer_object embedding the TTM buffer
object.

.. _`vmw_bo_pin_in_placement`:

vmw_bo_pin_in_placement
=======================

.. c:function:: int vmw_bo_pin_in_placement(struct vmw_private *dev_priv, struct vmw_buffer_object *buf, struct ttm_placement *placement, bool interruptible)

    Validate a buffer to placement.

    :param dev_priv:
        Driver private.
    :type dev_priv: struct vmw_private \*

    :param buf:
        DMA buffer to move.
    :type buf: struct vmw_buffer_object \*

    :param placement:
        The placement to pin it.
    :type placement: struct ttm_placement \*

    :param interruptible:
        Use interruptible wait.
    :type interruptible: bool

.. _`vmw_bo_pin_in_placement.return`:

Return
------

Zero on success, Negative error code on failure. In particular
-ERESTARTSYS if interrupted by a signal

.. _`vmw_bo_pin_in_vram_or_gmr`:

vmw_bo_pin_in_vram_or_gmr
=========================

.. c:function:: int vmw_bo_pin_in_vram_or_gmr(struct vmw_private *dev_priv, struct vmw_buffer_object *buf, bool interruptible)

    Move a buffer to vram or gmr.

    :param dev_priv:
        Driver private.
    :type dev_priv: struct vmw_private \*

    :param buf:
        DMA buffer to move.
    :type buf: struct vmw_buffer_object \*

    :param interruptible:
        Use interruptible wait.
    :type interruptible: bool

.. _`vmw_bo_pin_in_vram_or_gmr.description`:

Description
-----------

This function takes the reservation_sem in write mode.
Flushes and unpins the query bo to avoid failures.

.. _`vmw_bo_pin_in_vram_or_gmr.return`:

Return
------

Zero on success, Negative error code on failure. In particular
-ERESTARTSYS if interrupted by a signal

.. _`vmw_bo_pin_in_vram`:

vmw_bo_pin_in_vram
==================

.. c:function:: int vmw_bo_pin_in_vram(struct vmw_private *dev_priv, struct vmw_buffer_object *buf, bool interruptible)

    Move a buffer to vram.

    :param dev_priv:
        Driver private.
    :type dev_priv: struct vmw_private \*

    :param buf:
        DMA buffer to move.
    :type buf: struct vmw_buffer_object \*

    :param interruptible:
        Use interruptible wait.
    :type interruptible: bool

.. _`vmw_bo_pin_in_vram.description`:

Description
-----------

This function takes the reservation_sem in write mode.
Flushes and unpins the query bo to avoid failures.

.. _`vmw_bo_pin_in_vram.return`:

Return
------

Zero on success, Negative error code on failure. In particular
-ERESTARTSYS if interrupted by a signal

.. _`vmw_bo_pin_in_start_of_vram`:

vmw_bo_pin_in_start_of_vram
===========================

.. c:function:: int vmw_bo_pin_in_start_of_vram(struct vmw_private *dev_priv, struct vmw_buffer_object *buf, bool interruptible)

    Move a buffer to start of vram.

    :param dev_priv:
        Driver private.
    :type dev_priv: struct vmw_private \*

    :param buf:
        DMA buffer to pin.
    :type buf: struct vmw_buffer_object \*

    :param interruptible:
        Use interruptible wait.
    :type interruptible: bool

.. _`vmw_bo_pin_in_start_of_vram.description`:

Description
-----------

This function takes the reservation_sem in write mode.
Flushes and unpins the query bo to avoid failures.

.. _`vmw_bo_pin_in_start_of_vram.return`:

Return
------

Zero on success, Negative error code on failure. In particular
-ERESTARTSYS if interrupted by a signal

.. _`vmw_bo_unpin`:

vmw_bo_unpin
============

.. c:function:: int vmw_bo_unpin(struct vmw_private *dev_priv, struct vmw_buffer_object *buf, bool interruptible)

    Unpin the buffer given buffer, does not move the buffer.

    :param dev_priv:
        Driver private.
    :type dev_priv: struct vmw_private \*

    :param buf:
        DMA buffer to unpin.
    :type buf: struct vmw_buffer_object \*

    :param interruptible:
        Use interruptible wait.
    :type interruptible: bool

.. _`vmw_bo_unpin.description`:

Description
-----------

This function takes the reservation_sem in write mode.

.. _`vmw_bo_unpin.return`:

Return
------

Zero on success, Negative error code on failure. In particular
-ERESTARTSYS if interrupted by a signal

.. _`vmw_bo_get_guest_ptr`:

vmw_bo_get_guest_ptr
====================

.. c:function:: void vmw_bo_get_guest_ptr(const struct ttm_buffer_object *bo, SVGAGuestPtr *ptr)

    Get the guest ptr representing the current placement of a buffer.

    :param bo:
        Pointer to a struct ttm_buffer_object. Must be pinned or reserved.
    :type bo: const struct ttm_buffer_object \*

    :param ptr:
        SVGAGuestPtr returning the result.
    :type ptr: SVGAGuestPtr \*

.. _`vmw_bo_pin_reserved`:

vmw_bo_pin_reserved
===================

.. c:function:: void vmw_bo_pin_reserved(struct vmw_buffer_object *vbo, bool pin)

    Pin or unpin a buffer object without moving it.

    :param vbo:
        The buffer object. Must be reserved.
    :type vbo: struct vmw_buffer_object \*

    :param pin:
        Whether to pin or unpin.
    :type pin: bool

.. _`vmw_bo_map_and_cache`:

vmw_bo_map_and_cache
====================

.. c:function:: void *vmw_bo_map_and_cache(struct vmw_buffer_object *vbo)

    Map a buffer object and cache the map

    :param vbo:
        The buffer object to map
    :type vbo: struct vmw_buffer_object \*

.. _`vmw_bo_map_and_cache.return`:

Return
------

A kernel virtual address or NULL if mapping failed.

This function maps a buffer object into the kernel address space, or
returns the virtual kernel address of an already existing map. The virtual
address remains valid as long as the buffer object is pinned or reserved.
The cached map is torn down on either
1) Buffer object move
2) Buffer object swapout
3) Buffer object destruction

.. _`vmw_bo_unmap`:

vmw_bo_unmap
============

.. c:function:: void vmw_bo_unmap(struct vmw_buffer_object *vbo)

    Tear down a cached buffer object map.

    :param vbo:
        The buffer object whose map we are tearing down.
    :type vbo: struct vmw_buffer_object \*

.. _`vmw_bo_unmap.description`:

Description
-----------

This function tears down a cached map set up using
\ :c:func:`vmw_buffer_object_map_and_cache`\ .

.. _`vmw_bo_acc_size`:

vmw_bo_acc_size
===============

.. c:function:: size_t vmw_bo_acc_size(struct vmw_private *dev_priv, size_t size, bool user)

    Calculate the pinned memory usage of buffers

    :param dev_priv:
        Pointer to a struct vmw_private identifying the device.
    :type dev_priv: struct vmw_private \*

    :param size:
        The requested buffer size.
    :type size: size_t

    :param user:
        Whether this is an ordinary dma buffer or a user dma buffer.
    :type user: bool

.. _`vmw_bo_bo_free`:

vmw_bo_bo_free
==============

.. c:function:: void vmw_bo_bo_free(struct ttm_buffer_object *bo)

    vmw buffer object destructor

    :param bo:
        Pointer to the embedded struct ttm_buffer_object
    :type bo: struct ttm_buffer_object \*

.. _`vmw_user_bo_destroy`:

vmw_user_bo_destroy
===================

.. c:function:: void vmw_user_bo_destroy(struct ttm_buffer_object *bo)

    vmw buffer object destructor

    :param bo:
        Pointer to the embedded struct ttm_buffer_object
    :type bo: struct ttm_buffer_object \*

.. _`vmw_bo_init`:

vmw_bo_init
===========

.. c:function:: int vmw_bo_init(struct vmw_private *dev_priv, struct vmw_buffer_object *vmw_bo, size_t size, struct ttm_placement *placement, bool interruptible, void (*bo_free)(struct ttm_buffer_object *bo))

    Initialize a vmw buffer object

    :param dev_priv:
        Pointer to the device private struct
    :type dev_priv: struct vmw_private \*

    :param vmw_bo:
        Pointer to the struct vmw_buffer_object to initialize.
    :type vmw_bo: struct vmw_buffer_object \*

    :param size:
        Buffer object size in bytes.
    :type size: size_t

    :param placement:
        Initial placement.
    :type placement: struct ttm_placement \*

    :param interruptible:
        Whether waits should be performed interruptible.
    :type interruptible: bool

    :param void (\*bo_free)(struct ttm_buffer_object \*bo):
        The buffer object destructor.

.. _`vmw_bo_init.return`:

Return
------

Zero on success, negative error code on error.

Note that on error, the code will free the buffer object.

.. _`vmw_user_bo_release`:

vmw_user_bo_release
===================

.. c:function:: void vmw_user_bo_release(struct ttm_base_object **p_base)

    TTM reference base object release callback for vmw user buffer objects

    :param p_base:
        The TTM base object pointer about to be unreferenced.
    :type p_base: struct ttm_base_object \*\*

.. _`vmw_user_bo_release.description`:

Description
-----------

Clears the TTM base object pointer and drops the reference the
base object has on the underlying struct vmw_buffer_object.

.. _`vmw_user_bo_ref_obj_release`:

vmw_user_bo_ref_obj_release
===========================

.. c:function:: void vmw_user_bo_ref_obj_release(struct ttm_base_object *base, enum ttm_ref_type ref_type)

    release - TTM synccpu reference object release callback for vmw user buffer objects

    :param base:
        Pointer to the TTM base object
    :type base: struct ttm_base_object \*

    :param ref_type:
        Reference type of the reference reaching zero.
    :type ref_type: enum ttm_ref_type

.. _`vmw_user_bo_ref_obj_release.description`:

Description
-----------

Called when user-space drops its last synccpu reference on the buffer
object, Either explicitly or as part of a cleanup file close.

.. _`vmw_user_bo_alloc`:

vmw_user_bo_alloc
=================

.. c:function:: int vmw_user_bo_alloc(struct vmw_private *dev_priv, struct ttm_object_file *tfile, uint32_t size, bool shareable, uint32_t *handle, struct vmw_buffer_object **p_vbo, struct ttm_base_object **p_base)

    Allocate a user buffer object

    :param dev_priv:
        Pointer to a struct device private.
    :type dev_priv: struct vmw_private \*

    :param tfile:
        Pointer to a struct ttm_object_file on which to register the user
        object.
    :type tfile: struct ttm_object_file \*

    :param size:
        Size of the buffer object.
    :type size: uint32_t

    :param shareable:
        Boolean whether the buffer is shareable with other open files.
    :type shareable: bool

    :param handle:
        Pointer to where the handle value should be assigned.
    :type handle: uint32_t \*

    :param p_vbo:
        Pointer to where the refcounted struct vmw_buffer_object pointer
        should be assigned.
    :type p_vbo: struct vmw_buffer_object \*\*

    :param p_base:
        *undescribed*
    :type p_base: struct ttm_base_object \*\*

.. _`vmw_user_bo_alloc.return`:

Return
------

Zero on success, negative error code on error.

.. _`vmw_user_bo_verify_access`:

vmw_user_bo_verify_access
=========================

.. c:function:: int vmw_user_bo_verify_access(struct ttm_buffer_object *bo, struct ttm_object_file *tfile)

    verify access permissions on this buffer object.

    :param bo:
        Pointer to the buffer object being accessed
    :type bo: struct ttm_buffer_object \*

    :param tfile:
        Identifying the caller.
    :type tfile: struct ttm_object_file \*

.. _`vmw_user_bo_synccpu_grab`:

vmw_user_bo_synccpu_grab
========================

.. c:function:: int vmw_user_bo_synccpu_grab(struct vmw_user_buffer_object *user_bo, struct ttm_object_file *tfile, uint32_t flags)

    Grab a struct vmw_user_buffer_object for cpu access, idling previous GPU operations on the buffer and optionally blocking it for further command submissions.

    :param user_bo:
        Pointer to the buffer object being grabbed for CPU access
    :type user_bo: struct vmw_user_buffer_object \*

    :param tfile:
        Identifying the caller.
    :type tfile: struct ttm_object_file \*

    :param flags:
        Flags indicating how the grab should be performed.
    :type flags: uint32_t

.. _`vmw_user_bo_synccpu_grab.return`:

Return
------

Zero on success, Negative error code on error. In particular,
-EBUSY will be returned if a dontblock operation is requested and the
buffer object is busy, and -ERESTARTSYS will be returned if a wait is
interrupted by a signal.

A blocking grab will be automatically released when \ ``tfile``\  is closed.

.. _`vmw_user_bo_synccpu_release`:

vmw_user_bo_synccpu_release
===========================

.. c:function:: int vmw_user_bo_synccpu_release(uint32_t handle, struct ttm_object_file *tfile, uint32_t flags)

    Release a previous grab for CPU access, and unblock command submission on the buffer if blocked.

    :param handle:
        Handle identifying the buffer object.
    :type handle: uint32_t

    :param tfile:
        Identifying the caller.
    :type tfile: struct ttm_object_file \*

    :param flags:
        Flags indicating the type of release.
    :type flags: uint32_t

.. _`vmw_user_bo_synccpu_ioctl`:

vmw_user_bo_synccpu_ioctl
=========================

.. c:function:: int vmw_user_bo_synccpu_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    ioctl function implementing the synccpu functionality.

    :param dev:
        Identifies the drm device.
    :type dev: struct drm_device \*

    :param data:
        Pointer to the ioctl argument.
    :type data: void \*

    :param file_priv:
        Identifies the caller.
    :type file_priv: struct drm_file \*

.. _`vmw_user_bo_synccpu_ioctl.return`:

Return
------

Zero on success, negative error code on error.

This function checks the ioctl arguments for validity and calls the
relevant synccpu functions.

.. _`vmw_bo_alloc_ioctl`:

vmw_bo_alloc_ioctl
==================

.. c:function:: int vmw_bo_alloc_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    ioctl function implementing the buffer object allocation functionality.

    :param dev:
        Identifies the drm device.
    :type dev: struct drm_device \*

    :param data:
        Pointer to the ioctl argument.
    :type data: void \*

    :param file_priv:
        Identifies the caller.
    :type file_priv: struct drm_file \*

.. _`vmw_bo_alloc_ioctl.return`:

Return
------

Zero on success, negative error code on error.

This function checks the ioctl arguments for validity and allocates a
struct vmw_user_buffer_object bo.

.. _`vmw_bo_unref_ioctl`:

vmw_bo_unref_ioctl
==================

.. c:function:: int vmw_bo_unref_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    Generic handle close ioctl.

    :param dev:
        Identifies the drm device.
    :type dev: struct drm_device \*

    :param data:
        Pointer to the ioctl argument.
    :type data: void \*

    :param file_priv:
        Identifies the caller.
    :type file_priv: struct drm_file \*

.. _`vmw_bo_unref_ioctl.return`:

Return
------

Zero on success, negative error code on error.

This function checks the ioctl arguments for validity and closes a
handle to a TTM base object, optionally freeing the object.

.. _`vmw_user_bo_lookup`:

vmw_user_bo_lookup
==================

.. c:function:: int vmw_user_bo_lookup(struct ttm_object_file *tfile, uint32_t handle, struct vmw_buffer_object **out, struct ttm_base_object **p_base)

    Look up a vmw user buffer object from a handle.

    :param tfile:
        The TTM object file the handle is registered with.
    :type tfile: struct ttm_object_file \*

    :param handle:
        The user buffer object handle
    :type handle: uint32_t

    :param out:
        Pointer to a where a pointer to the embedded
        struct vmw_buffer_object should be placed.
    :type out: struct vmw_buffer_object \*\*

    :param p_base:
        Pointer to where a pointer to the TTM base object should be
        placed, or NULL if no such pointer is required.
    :type p_base: struct ttm_base_object \*\*

.. _`vmw_user_bo_lookup.return`:

Return
------

Zero on success, Negative error code on error.

Both the output base object pointer and the vmw buffer object pointer
will be refcounted.

.. _`vmw_user_bo_noref_lookup`:

vmw_user_bo_noref_lookup
========================

.. c:function:: struct vmw_buffer_object *vmw_user_bo_noref_lookup(struct ttm_object_file *tfile, u32 handle)

    Look up a vmw user buffer object without reference

    :param tfile:
        The TTM object file the handle is registered with.
    :type tfile: struct ttm_object_file \*

    :param handle:
        The user buffer object handle.
    :type handle: u32

.. _`vmw_user_bo_noref_lookup.description`:

Description
-----------

This function looks up a struct vmw_user_bo and returns a pointer to the
struct vmw_buffer_object it derives from without refcounting the pointer.
The returned pointer is only valid until \ :c:func:`vmw_user_bo_noref_release`\  is
called, and the object pointed to by the returned pointer may be doomed.
Any persistent usage of the object requires a refcount to be taken using
\ :c:func:`ttm_bo_reference_unless_doomed`\ . Iff this function returns successfully it
needs to be paired with \ :c:func:`vmw_user_bo_noref_release`\  and no sleeping-
or scheduling functions may be called inbetween these function calls.

.. _`vmw_user_bo_noref_lookup.return`:

Return
------

A struct vmw_buffer_object pointer if successful or negative
error pointer on failure.

.. _`vmw_user_bo_reference`:

vmw_user_bo_reference
=====================

.. c:function:: int vmw_user_bo_reference(struct ttm_object_file *tfile, struct vmw_buffer_object *vbo, uint32_t *handle)

    Open a handle to a vmw user buffer object.

    :param tfile:
        The TTM object file to register the handle with.
    :type tfile: struct ttm_object_file \*

    :param vbo:
        The embedded vmw buffer object.
    :type vbo: struct vmw_buffer_object \*

    :param handle:
        Pointer to where the new handle should be placed.
    :type handle: uint32_t \*

.. _`vmw_user_bo_reference.return`:

Return
------

Zero on success, Negative error code on error.

.. _`vmw_bo_fence_single`:

vmw_bo_fence_single
===================

.. c:function:: void vmw_bo_fence_single(struct ttm_buffer_object *bo, struct vmw_fence_obj *fence)

    Utility function to fence a single TTM buffer object without unreserving it.

    :param bo:
        Pointer to the struct ttm_buffer_object to fence.
    :type bo: struct ttm_buffer_object \*

    :param fence:
        Pointer to the fence. If NULL, this function will
        insert a fence into the command stream..
    :type fence: struct vmw_fence_obj \*

.. _`vmw_bo_fence_single.description`:

Description
-----------

Contrary to the ttm_eu version of this function, it takes only
a single buffer object instead of a list, and it also doesn't
unreserve the buffer object, which needs to be done separately.

.. _`vmw_dumb_create`:

vmw_dumb_create
===============

.. c:function:: int vmw_dumb_create(struct drm_file *file_priv, struct drm_device *dev, struct drm_mode_create_dumb *args)

    Create a dumb kms buffer

    :param file_priv:
        Pointer to a struct drm_file identifying the caller.
    :type file_priv: struct drm_file \*

    :param dev:
        Pointer to the drm device.
    :type dev: struct drm_device \*

    :param args:
        Pointer to a struct drm_mode_create_dumb structure
    :type args: struct drm_mode_create_dumb \*

.. _`vmw_dumb_create.return`:

Return
------

Zero on success, negative error code on failure.

This is a driver callback for the core drm create_dumb functionality.
Note that this is very similar to the vmw_bo_alloc ioctl, except
that the arguments have a different format.

.. _`vmw_dumb_map_offset`:

vmw_dumb_map_offset
===================

.. c:function:: int vmw_dumb_map_offset(struct drm_file *file_priv, struct drm_device *dev, uint32_t handle, uint64_t *offset)

    Return the address space offset of a dumb buffer

    :param file_priv:
        Pointer to a struct drm_file identifying the caller.
    :type file_priv: struct drm_file \*

    :param dev:
        Pointer to the drm device.
    :type dev: struct drm_device \*

    :param handle:
        Handle identifying the dumb buffer.
    :type handle: uint32_t

    :param offset:
        The address space offset returned.
    :type offset: uint64_t \*

.. _`vmw_dumb_map_offset.return`:

Return
------

Zero on success, negative error code on failure.

This is a driver callback for the core drm dumb_map_offset functionality.

.. _`vmw_dumb_destroy`:

vmw_dumb_destroy
================

.. c:function:: int vmw_dumb_destroy(struct drm_file *file_priv, struct drm_device *dev, uint32_t handle)

    Destroy a dumb boffer

    :param file_priv:
        Pointer to a struct drm_file identifying the caller.
    :type file_priv: struct drm_file \*

    :param dev:
        Pointer to the drm device.
    :type dev: struct drm_device \*

    :param handle:
        Handle identifying the dumb buffer.
    :type handle: uint32_t

.. _`vmw_dumb_destroy.return`:

Return
------

Zero on success, negative error code on failure.

This is a driver callback for the core drm dumb_destroy functionality.

.. _`vmw_bo_swap_notify`:

vmw_bo_swap_notify
==================

.. c:function:: void vmw_bo_swap_notify(struct ttm_buffer_object *bo)

    swapout notify callback.

    :param bo:
        The buffer object to be swapped out.
    :type bo: struct ttm_buffer_object \*

.. _`vmw_bo_move_notify`:

vmw_bo_move_notify
==================

.. c:function:: void vmw_bo_move_notify(struct ttm_buffer_object *bo, struct ttm_mem_reg *mem)

    TTM move_notify_callback

    :param bo:
        The TTM buffer object about to move.
    :type bo: struct ttm_buffer_object \*

    :param mem:
        The struct ttm_mem_reg indicating to what memory
        region the move is taking place.
    :type mem: struct ttm_mem_reg \*

.. _`vmw_bo_move_notify.description`:

Description
-----------

Detaches cached maps and device bindings that require that the
buffer doesn't move.

.. This file was automatic generated / don't edit.

