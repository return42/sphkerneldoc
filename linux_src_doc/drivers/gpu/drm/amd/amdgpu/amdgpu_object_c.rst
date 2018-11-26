.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_object.c

.. _`amdgpu_object`:

amdgpu_object
=============

This defines the interfaces to operate on an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object which
represents memory used by driver (VRAM, system memory, etc.). The driver
provides DRM/GEM APIs to userspace. DRM/GEM APIs then use these interfaces
to create/destroy/set buffer object which are then managed by the kernel TTM
memory manager.
The interfaces are also used internally by kernel clients, including gfx,
uvd, etc. for kernel managed allocations used by the GPU.

.. _`amdgpu_bo_subtract_pin_size`:

amdgpu_bo_subtract_pin_size
===========================

.. c:function:: void amdgpu_bo_subtract_pin_size(struct amdgpu_bo *bo)

    Remove BO from pin_size accounting

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_bo_subtract_pin_size.description`:

Description
-----------

This function is called when a BO stops being pinned, and updates the
\ :c:type:`struct amdgpu_device <amdgpu_device>`\  pin_size values accordingly.

.. _`amdgpu_bo_is_amdgpu_bo`:

amdgpu_bo_is_amdgpu_bo
======================

.. c:function:: bool amdgpu_bo_is_amdgpu_bo(struct ttm_buffer_object *bo)

    check if the buffer object is an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\ 

    :param bo:
        buffer object to be checked
    :type bo: struct ttm_buffer_object \*

.. _`amdgpu_bo_is_amdgpu_bo.description`:

Description
-----------

Uses destroy function associated with the object to determine if this is
an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\ .

.. _`amdgpu_bo_is_amdgpu_bo.return`:

Return
------

true if the object belongs to \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\ , false if not.

.. _`amdgpu_bo_placement_from_domain`:

amdgpu_bo_placement_from_domain
===============================

.. c:function:: void amdgpu_bo_placement_from_domain(struct amdgpu_bo *abo, u32 domain)

    set buffer's placement

    :param abo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object whose placement is to be set
    :type abo: struct amdgpu_bo \*

    :param domain:
        requested domain
    :type domain: u32

.. _`amdgpu_bo_placement_from_domain.description`:

Description
-----------

Sets buffer's placement according to requested domain and the buffer's
flags.

.. _`amdgpu_bo_create_reserved`:

amdgpu_bo_create_reserved
=========================

.. c:function:: int amdgpu_bo_create_reserved(struct amdgpu_device *adev, unsigned long size, int align, u32 domain, struct amdgpu_bo **bo_ptr, u64 *gpu_addr, void **cpu_addr)

    create reserved BO for kernel use

    :param adev:
        amdgpu device object
    :type adev: struct amdgpu_device \*

    :param size:
        size for the new BO
    :type size: unsigned long

    :param align:
        alignment for the new BO
    :type align: int

    :param domain:
        where to place it
    :type domain: u32

    :param bo_ptr:
        used to initialize BOs in structures
    :type bo_ptr: struct amdgpu_bo \*\*

    :param gpu_addr:
        GPU addr of the pinned BO
    :type gpu_addr: u64 \*

    :param cpu_addr:
        optional CPU address mapping
    :type cpu_addr: void \*\*

.. _`amdgpu_bo_create_reserved.description`:

Description
-----------

Allocates and pins a BO for kernel internal use, and returns it still
reserved.

.. _`amdgpu_bo_create_reserved.note`:

Note
----

For bo_ptr new BO is only created if bo_ptr points to NULL.

.. _`amdgpu_bo_create_reserved.return`:

Return
------

0 on success, negative error code otherwise.

.. _`amdgpu_bo_create_kernel`:

amdgpu_bo_create_kernel
=======================

.. c:function:: int amdgpu_bo_create_kernel(struct amdgpu_device *adev, unsigned long size, int align, u32 domain, struct amdgpu_bo **bo_ptr, u64 *gpu_addr, void **cpu_addr)

    create BO for kernel use

    :param adev:
        amdgpu device object
    :type adev: struct amdgpu_device \*

    :param size:
        size for the new BO
    :type size: unsigned long

    :param align:
        alignment for the new BO
    :type align: int

    :param domain:
        where to place it
    :type domain: u32

    :param bo_ptr:
        used to initialize BOs in structures
    :type bo_ptr: struct amdgpu_bo \*\*

    :param gpu_addr:
        GPU addr of the pinned BO
    :type gpu_addr: u64 \*

    :param cpu_addr:
        optional CPU address mapping
    :type cpu_addr: void \*\*

.. _`amdgpu_bo_create_kernel.description`:

Description
-----------

Allocates and pins a BO for kernel internal use.

.. _`amdgpu_bo_create_kernel.note`:

Note
----

For bo_ptr new BO is only created if bo_ptr points to NULL.

.. _`amdgpu_bo_create_kernel.return`:

Return
------

0 on success, negative error code otherwise.

.. _`amdgpu_bo_free_kernel`:

amdgpu_bo_free_kernel
=====================

.. c:function:: void amdgpu_bo_free_kernel(struct amdgpu_bo **bo, u64 *gpu_addr, void **cpu_addr)

    free BO for kernel use

    :param bo:
        amdgpu BO to free
    :type bo: struct amdgpu_bo \*\*

    :param gpu_addr:
        pointer to where the BO's GPU memory space address was stored
    :type gpu_addr: u64 \*

    :param cpu_addr:
        pointer to where the BO's CPU memory space address was stored
    :type cpu_addr: void \*\*

.. _`amdgpu_bo_free_kernel.description`:

Description
-----------

unmaps and unpin a BO for kernel internal use.

.. _`amdgpu_bo_create`:

amdgpu_bo_create
================

.. c:function:: int amdgpu_bo_create(struct amdgpu_device *adev, struct amdgpu_bo_param *bp, struct amdgpu_bo **bo_ptr)

    create an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object

    :param adev:
        amdgpu device object
    :type adev: struct amdgpu_device \*

    :param bp:
        parameters to be used for the buffer object
    :type bp: struct amdgpu_bo_param \*

    :param bo_ptr:
        pointer to the buffer object pointer
    :type bo_ptr: struct amdgpu_bo \*\*

.. _`amdgpu_bo_create.description`:

Description
-----------

Creates an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object; and if requested, also creates a
shadow object.
Shadow object is used to backup the original buffer object, and is always
in GTT.

.. _`amdgpu_bo_create.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_backup_to_shadow`:

amdgpu_bo_backup_to_shadow
==========================

.. c:function:: int amdgpu_bo_backup_to_shadow(struct amdgpu_device *adev, struct amdgpu_ring *ring, struct amdgpu_bo *bo, struct reservation_object *resv, struct dma_fence **fence, bool direct)

    Backs up an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object

    :param adev:
        amdgpu device object
    :type adev: struct amdgpu_device \*

    :param ring:
        amdgpu_ring for the engine handling the buffer operations
    :type ring: struct amdgpu_ring \*

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer to be backed up
    :type bo: struct amdgpu_bo \*

    :param resv:
        reservation object with embedded fence
    :type resv: struct reservation_object \*

    :param fence:
        dma_fence associated with the operation
    :type fence: struct dma_fence \*\*

    :param direct:
        whether to submit the job directly
    :type direct: bool

.. _`amdgpu_bo_backup_to_shadow.description`:

Description
-----------

Copies an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object to its shadow object.
Not used for now.

.. _`amdgpu_bo_backup_to_shadow.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_validate`:

amdgpu_bo_validate
==================

.. c:function:: int amdgpu_bo_validate(struct amdgpu_bo *bo)

    validate an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object

    :param bo:
        pointer to the buffer object
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_bo_validate.description`:

Description
-----------

Sets placement according to domain; and changes placement and caching
policy of the buffer object according to the placement.
This is used for validating shadow bos.  It calls \ :c:func:`ttm_bo_validate`\  to
make sure the buffer is resident where it needs to be.

.. _`amdgpu_bo_validate.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_restore_shadow`:

amdgpu_bo_restore_shadow
========================

.. c:function:: int amdgpu_bo_restore_shadow(struct amdgpu_bo *shadow, struct dma_fence **fence)

    restore an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  shadow

    :param shadow:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  shadow to be restored
    :type shadow: struct amdgpu_bo \*

    :param fence:
        dma_fence associated with the operation
    :type fence: struct dma_fence \*\*

.. _`amdgpu_bo_restore_shadow.description`:

Description
-----------

Copies a buffer object's shadow content back to the object.
This is used for recovering a buffer from its shadow in case of a gpu
reset where vram context may be lost.

.. _`amdgpu_bo_restore_shadow.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_kmap`:

amdgpu_bo_kmap
==============

.. c:function:: int amdgpu_bo_kmap(struct amdgpu_bo *bo, void **ptr)

    map an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object to be mapped
    :type bo: struct amdgpu_bo \*

    :param ptr:
        kernel virtual address to be returned
    :type ptr: void \*\*

.. _`amdgpu_bo_kmap.description`:

Description
-----------

Calls \ :c:func:`ttm_bo_kmap`\  to set up the kernel virtual mapping; calls
\ :c:func:`amdgpu_bo_kptr`\  to get the kernel virtual address.

.. _`amdgpu_bo_kmap.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_kptr`:

amdgpu_bo_kptr
==============

.. c:function:: void *amdgpu_bo_kptr(struct amdgpu_bo *bo)

    returns a kernel virtual address of the buffer object

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_bo_kptr.description`:

Description
-----------

Calls \ :c:func:`ttm_kmap_obj_virtual`\  to get the kernel virtual address

.. _`amdgpu_bo_kptr.return`:

Return
------

the virtual address of a buffer object area.

.. _`amdgpu_bo_kunmap`:

amdgpu_bo_kunmap
================

.. c:function:: void amdgpu_bo_kunmap(struct amdgpu_bo *bo)

    unmap an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object to be unmapped
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_bo_kunmap.description`:

Description
-----------

Unmaps a kernel map set up by \ :c:func:`amdgpu_bo_kmap`\ .

.. _`amdgpu_bo_ref`:

amdgpu_bo_ref
=============

.. c:function:: struct amdgpu_bo *amdgpu_bo_ref(struct amdgpu_bo *bo)

    reference an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_bo_ref.description`:

Description
-----------

References the contained \ :c:type:`struct ttm_buffer_object <ttm_buffer_object>`\ .

.. _`amdgpu_bo_ref.return`:

Return
------

a refcounted pointer to the \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object.

.. _`amdgpu_bo_unref`:

amdgpu_bo_unref
===============

.. c:function:: void amdgpu_bo_unref(struct amdgpu_bo **bo)

    unreference an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object
    :type bo: struct amdgpu_bo \*\*

.. _`amdgpu_bo_unref.description`:

Description
-----------

Unreferences the contained \ :c:type:`struct ttm_buffer_object <ttm_buffer_object>`\  and clear the pointer

.. _`amdgpu_bo_pin_restricted`:

amdgpu_bo_pin_restricted
========================

.. c:function:: int amdgpu_bo_pin_restricted(struct amdgpu_bo *bo, u32 domain, u64 min_offset, u64 max_offset)

    pin an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object to be pinned
    :type bo: struct amdgpu_bo \*

    :param domain:
        domain to be pinned to
    :type domain: u32

    :param min_offset:
        the start of requested address range
    :type min_offset: u64

    :param max_offset:
        the end of requested address range
    :type max_offset: u64

.. _`amdgpu_bo_pin_restricted.description`:

Description
-----------

Pins the buffer object according to requested domain and address range. If
the memory is unbound gart memory, binds the pages into gart table. Adjusts
pin_count and pin_size accordingly.

Pinning means to lock pages in memory along with keeping them at a fixed
offset. It is required when a buffer can not be moved, for example, when
a display buffer is being scanned out.

Compared with \ :c:func:`amdgpu_bo_pin`\ , this function gives more flexibility on
where to pin a buffer if there are specific restrictions on where a buffer
must be located.

.. _`amdgpu_bo_pin_restricted.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_pin`:

amdgpu_bo_pin
=============

.. c:function:: int amdgpu_bo_pin(struct amdgpu_bo *bo, u32 domain)

    pin an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object to be pinned
    :type bo: struct amdgpu_bo \*

    :param domain:
        domain to be pinned to
    :type domain: u32

.. _`amdgpu_bo_pin.description`:

Description
-----------

A simple wrapper to \ :c:func:`amdgpu_bo_pin_restricted`\ .
Provides a simpler API for buffers that do not have any strict restrictions
on where a buffer must be located.

.. _`amdgpu_bo_pin.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_unpin`:

amdgpu_bo_unpin
===============

.. c:function:: int amdgpu_bo_unpin(struct amdgpu_bo *bo)

    unpin an \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object to be unpinned
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_bo_unpin.description`:

Description
-----------

Decreases the pin_count, and clears the flags if pin_count reaches 0.
Changes placement and pin size accordingly.

.. _`amdgpu_bo_unpin.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_evict_vram`:

amdgpu_bo_evict_vram
====================

.. c:function:: int amdgpu_bo_evict_vram(struct amdgpu_device *adev)

    evict VRAM buffers

    :param adev:
        amdgpu device object
    :type adev: struct amdgpu_device \*

.. _`amdgpu_bo_evict_vram.description`:

Description
-----------

Evicts all VRAM buffers on the lru list of the memory type.
Mainly used for evicting vram at suspend time.

.. _`amdgpu_bo_evict_vram.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_init`:

amdgpu_bo_init
==============

.. c:function:: int amdgpu_bo_init(struct amdgpu_device *adev)

    initialize memory manager

    :param adev:
        amdgpu device object
    :type adev: struct amdgpu_device \*

.. _`amdgpu_bo_init.description`:

Description
-----------

Calls \ :c:func:`amdgpu_ttm_init`\  to initialize amdgpu memory manager.

.. _`amdgpu_bo_init.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_late_init`:

amdgpu_bo_late_init
===================

.. c:function:: int amdgpu_bo_late_init(struct amdgpu_device *adev)

    late init

    :param adev:
        amdgpu device object
    :type adev: struct amdgpu_device \*

.. _`amdgpu_bo_late_init.description`:

Description
-----------

Calls \ :c:func:`amdgpu_ttm_late_init`\  to free resources used earlier during
initialization.

.. _`amdgpu_bo_late_init.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_fini`:

amdgpu_bo_fini
==============

.. c:function:: void amdgpu_bo_fini(struct amdgpu_device *adev)

    tear down memory manager

    :param adev:
        amdgpu device object
    :type adev: struct amdgpu_device \*

.. _`amdgpu_bo_fini.description`:

Description
-----------

Reverses \ :c:func:`amdgpu_bo_init`\  to tear down memory manager.

.. _`amdgpu_bo_fbdev_mmap`:

amdgpu_bo_fbdev_mmap
====================

.. c:function:: int amdgpu_bo_fbdev_mmap(struct amdgpu_bo *bo, struct vm_area_struct *vma)

    mmap fbdev memory

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object
    :type bo: struct amdgpu_bo \*

    :param vma:
        vma as input from the fbdev mmap method
    :type vma: struct vm_area_struct \*

.. _`amdgpu_bo_fbdev_mmap.description`:

Description
-----------

Calls \ :c:func:`ttm_fbdev_mmap`\  to mmap fbdev memory if it is backed by a bo.

.. _`amdgpu_bo_fbdev_mmap.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_set_tiling_flags`:

amdgpu_bo_set_tiling_flags
==========================

.. c:function:: int amdgpu_bo_set_tiling_flags(struct amdgpu_bo *bo, u64 tiling_flags)

    set tiling flags

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object
    :type bo: struct amdgpu_bo \*

    :param tiling_flags:
        new flags
    :type tiling_flags: u64

.. _`amdgpu_bo_set_tiling_flags.description`:

Description
-----------

Sets buffer object's tiling flags with the new one. Used by GEM ioctl or
kernel driver to set the tiling flags on a buffer.

.. _`amdgpu_bo_set_tiling_flags.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_get_tiling_flags`:

amdgpu_bo_get_tiling_flags
==========================

.. c:function:: void amdgpu_bo_get_tiling_flags(struct amdgpu_bo *bo, u64 *tiling_flags)

    get tiling flags

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object
    :type bo: struct amdgpu_bo \*

    :param tiling_flags:
        returned flags
    :type tiling_flags: u64 \*

.. _`amdgpu_bo_get_tiling_flags.description`:

Description
-----------

Gets buffer object's tiling flags. Used by GEM ioctl or kernel driver to
set the tiling flags on a buffer.

.. _`amdgpu_bo_set_metadata`:

amdgpu_bo_set_metadata
======================

.. c:function:: int amdgpu_bo_set_metadata(struct amdgpu_bo *bo, void *metadata, uint32_t metadata_size, uint64_t flags)

    set metadata

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object
    :type bo: struct amdgpu_bo \*

    :param metadata:
        new metadata
    :type metadata: void \*

    :param metadata_size:
        size of the new metadata
    :type metadata_size: uint32_t

    :param flags:
        flags of the new metadata
    :type flags: uint64_t

.. _`amdgpu_bo_set_metadata.description`:

Description
-----------

Sets buffer object's metadata, its size and flags.
Used via GEM ioctl.

.. _`amdgpu_bo_set_metadata.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_get_metadata`:

amdgpu_bo_get_metadata
======================

.. c:function:: int amdgpu_bo_get_metadata(struct amdgpu_bo *bo, void *buffer, size_t buffer_size, uint32_t *metadata_size, uint64_t *flags)

    get metadata

    :param bo:
        \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object
    :type bo: struct amdgpu_bo \*

    :param buffer:
        returned metadata
    :type buffer: void \*

    :param buffer_size:
        size of the buffer
    :type buffer_size: size_t

    :param metadata_size:
        size of the returned metadata
    :type metadata_size: uint32_t \*

    :param flags:
        flags of the returned metadata
    :type flags: uint64_t \*

.. _`amdgpu_bo_get_metadata.description`:

Description
-----------

Gets buffer object's metadata, its size and flags. buffer_size shall not be
less than metadata_size.
Used via GEM ioctl.

.. _`amdgpu_bo_get_metadata.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_move_notify`:

amdgpu_bo_move_notify
=====================

.. c:function:: void amdgpu_bo_move_notify(struct ttm_buffer_object *bo, bool evict, struct ttm_mem_reg *new_mem)

    notification about a memory move

    :param bo:
        pointer to a buffer object
    :type bo: struct ttm_buffer_object \*

    :param evict:
        if this move is evicting the buffer from the graphics address space
    :type evict: bool

    :param new_mem:
        new information of the bufer object
    :type new_mem: struct ttm_mem_reg \*

.. _`amdgpu_bo_move_notify.description`:

Description
-----------

Marks the corresponding \ :c:type:`struct amdgpu_bo <amdgpu_bo>`\  buffer object as invalid, also performs
bookkeeping.
TTM driver callback which is called when ttm moves a buffer.

.. _`amdgpu_bo_fault_reserve_notify`:

amdgpu_bo_fault_reserve_notify
==============================

.. c:function:: int amdgpu_bo_fault_reserve_notify(struct ttm_buffer_object *bo)

    notification about a memory fault

    :param bo:
        pointer to a buffer object
    :type bo: struct ttm_buffer_object \*

.. _`amdgpu_bo_fault_reserve_notify.description`:

Description
-----------

Notifies the driver we are taking a fault on this BO and have reserved it,
also performs bookkeeping.
TTM driver callback for dealing with vm faults.

.. _`amdgpu_bo_fault_reserve_notify.return`:

Return
------

0 for success or a negative error code on failure.

.. _`amdgpu_bo_fence`:

amdgpu_bo_fence
===============

.. c:function:: void amdgpu_bo_fence(struct amdgpu_bo *bo, struct dma_fence *fence, bool shared)

    add fence to buffer object

    :param bo:
        buffer object in question
    :type bo: struct amdgpu_bo \*

    :param fence:
        fence to add
    :type fence: struct dma_fence \*

    :param shared:
        true if fence should be added shared
    :type shared: bool

.. _`amdgpu_bo_gpu_offset`:

amdgpu_bo_gpu_offset
====================

.. c:function:: u64 amdgpu_bo_gpu_offset(struct amdgpu_bo *bo)

    return GPU offset of bo

    :param bo:
        amdgpu object for which we query the offset
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_bo_gpu_offset.note`:

Note
----

object should either be pinned or reserved when calling this
function, it might be useful to add check for this for debugging.

.. _`amdgpu_bo_gpu_offset.return`:

Return
------

current GPU offset of the object.

.. _`amdgpu_bo_get_preferred_pin_domain`:

amdgpu_bo_get_preferred_pin_domain
==================================

.. c:function:: uint32_t amdgpu_bo_get_preferred_pin_domain(struct amdgpu_device *adev, uint32_t domain)

    get preferred domain for scanout

    :param adev:
        amdgpu device object
    :type adev: struct amdgpu_device \*

    :param domain:
        allowed :ref:`memory domains <amdgpu_memory_domains>`
    :type domain: uint32_t

.. _`amdgpu_bo_get_preferred_pin_domain.return`:

Return
------

Which of the allowed domains is preferred for pinning the BO for scanout.

.. This file was automatic generated / don't edit.

