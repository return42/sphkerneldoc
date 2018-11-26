.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_ttm.c

.. _`amdgpu_ttm_mem_global_init`:

amdgpu_ttm_mem_global_init
==========================

.. c:function:: int amdgpu_ttm_mem_global_init(struct drm_global_reference *ref)

    Initialize and acquire reference to memory object

    :param ref:
        Object for initialization.
    :type ref: struct drm_global_reference \*

.. _`amdgpu_ttm_mem_global_init.description`:

Description
-----------

This is called by \ :c:func:`drm_global_item_ref`\  when an object is being
initialized.

.. _`amdgpu_ttm_mem_global_release`:

amdgpu_ttm_mem_global_release
=============================

.. c:function:: void amdgpu_ttm_mem_global_release(struct drm_global_reference *ref)

    Drop reference to a memory object

    :param ref:
        Object being removed
    :type ref: struct drm_global_reference \*

.. _`amdgpu_ttm_mem_global_release.description`:

Description
-----------

This is called by \ :c:func:`drm_global_item_unref`\  when an object is being
released.

.. _`amdgpu_ttm_global_init`:

amdgpu_ttm_global_init
======================

.. c:function:: int amdgpu_ttm_global_init(struct amdgpu_device *adev)

    Initialize global TTM memory reference structures.

    :param adev:
        AMDGPU device for which the global structures need to be registered.
    :type adev: struct amdgpu_device \*

.. _`amdgpu_ttm_global_init.description`:

Description
-----------

This is called as part of the AMDGPU ttm init from \ :c:func:`amdgpu_ttm_init`\ 
during bring up.

.. _`amdgpu_init_mem_type`:

amdgpu_init_mem_type
====================

.. c:function:: int amdgpu_init_mem_type(struct ttm_bo_device *bdev, uint32_t type, struct ttm_mem_type_manager *man)

    Initialize a memory manager for a specific type of memory request.

    :param bdev:
        The TTM BO device object (contains a reference to amdgpu_device)
    :type bdev: struct ttm_bo_device \*

    :param type:
        The type of memory requested
    :type type: uint32_t

    :param man:
        The memory type manager for each domain
    :type man: struct ttm_mem_type_manager \*

.. _`amdgpu_init_mem_type.description`:

Description
-----------

This is called by \ :c:func:`ttm_bo_init_mm`\  when a buffer object is being
initialized.

.. _`amdgpu_evict_flags`:

amdgpu_evict_flags
==================

.. c:function:: void amdgpu_evict_flags(struct ttm_buffer_object *bo, struct ttm_placement *placement)

    Compute placement flags

    :param bo:
        The buffer object to evict
    :type bo: struct ttm_buffer_object \*

    :param placement:
        Possible destination(s) for evicted BO
    :type placement: struct ttm_placement \*

.. _`amdgpu_evict_flags.description`:

Description
-----------

Fill in placement data when \ :c:func:`ttm_bo_evict`\  is called

.. _`amdgpu_verify_access`:

amdgpu_verify_access
====================

.. c:function:: int amdgpu_verify_access(struct ttm_buffer_object *bo, struct file *filp)

    Verify access for a mmap call

    :param bo:
        The buffer object to map
    :type bo: struct ttm_buffer_object \*

    :param filp:
        The file pointer from the process performing the mmap
    :type filp: struct file \*

.. _`amdgpu_verify_access.description`:

Description
-----------

This is called by \ :c:func:`ttm_bo_mmap`\  to verify whether a process
has the right to mmap a BO to their process space.

.. _`amdgpu_move_null`:

amdgpu_move_null
================

.. c:function:: void amdgpu_move_null(struct ttm_buffer_object *bo, struct ttm_mem_reg *new_mem)

    Register memory for a buffer object

    :param bo:
        The bo to assign the memory to
    :type bo: struct ttm_buffer_object \*

    :param new_mem:
        The memory to be assigned.
    :type new_mem: struct ttm_mem_reg \*

.. _`amdgpu_move_null.description`:

Description
-----------

Assign the memory from new_mem to the memory of the buffer object bo.

.. _`amdgpu_mm_node_addr`:

amdgpu_mm_node_addr
===================

.. c:function:: uint64_t amdgpu_mm_node_addr(struct ttm_buffer_object *bo, struct drm_mm_node *mm_node, struct ttm_mem_reg *mem)

    Compute the GPU relative offset of a GTT buffer.

    :param bo:
        The bo to assign the memory to.
    :type bo: struct ttm_buffer_object \*

    :param mm_node:
        Memory manager node for drm allocator.
    :type mm_node: struct drm_mm_node \*

    :param mem:
        The region where the bo resides.
    :type mem: struct ttm_mem_reg \*

.. _`amdgpu_find_mm_node`:

amdgpu_find_mm_node
===================

.. c:function:: struct drm_mm_node *amdgpu_find_mm_node(struct ttm_mem_reg *mem, unsigned long *offset)

    Helper function finds the drm_mm_node corresponding to \ ``offset``\ . It also modifies the offset to be within the drm_mm_node returned

    :param mem:
        The region where the bo resides.
    :type mem: struct ttm_mem_reg \*

    :param offset:
        The offset that drm_mm_node is used for finding.
    :type offset: unsigned long \*

.. _`amdgpu_ttm_copy_mem_to_mem`:

amdgpu_ttm_copy_mem_to_mem
==========================

.. c:function:: int amdgpu_ttm_copy_mem_to_mem(struct amdgpu_device *adev, struct amdgpu_copy_mem *src, struct amdgpu_copy_mem *dst, uint64_t size, struct reservation_object *resv, struct dma_fence **f)

    Helper function for copy

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

    :param src:
        *undescribed*
    :type src: struct amdgpu_copy_mem \*

    :param dst:
        *undescribed*
    :type dst: struct amdgpu_copy_mem \*

    :param size:
        *undescribed*
    :type size: uint64_t

    :param resv:
        *undescribed*
    :type resv: struct reservation_object \*

    :param f:
        Returns the last fence if multiple jobs are submitted.
    :type f: struct dma_fence \*\*

.. _`amdgpu_ttm_copy_mem_to_mem.description`:

Description
-----------

The function copies \ ``size``\  bytes from {src->mem + src->offset} to
{dst->mem + dst->offset}. src->bo and dst->bo could be same BO for a
move and different for a BO to BO copy.

.. _`amdgpu_move_blit`:

amdgpu_move_blit
================

.. c:function:: int amdgpu_move_blit(struct ttm_buffer_object *bo, bool evict, bool no_wait_gpu, struct ttm_mem_reg *new_mem, struct ttm_mem_reg *old_mem)

    Copy an entire buffer to another buffer

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

    :param evict:
        *undescribed*
    :type evict: bool

    :param no_wait_gpu:
        *undescribed*
    :type no_wait_gpu: bool

    :param new_mem:
        *undescribed*
    :type new_mem: struct ttm_mem_reg \*

    :param old_mem:
        *undescribed*
    :type old_mem: struct ttm_mem_reg \*

.. _`amdgpu_move_blit.description`:

Description
-----------

This is a helper called by \ :c:func:`amdgpu_bo_move`\  and \ :c:func:`amdgpu_move_vram_ram`\  to
help move buffers to and from VRAM.

.. _`amdgpu_move_vram_ram`:

amdgpu_move_vram_ram
====================

.. c:function:: int amdgpu_move_vram_ram(struct ttm_buffer_object *bo, bool evict, struct ttm_operation_ctx *ctx, struct ttm_mem_reg *new_mem)

    Copy VRAM buffer to RAM buffer

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

    :param evict:
        *undescribed*
    :type evict: bool

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

    :param new_mem:
        *undescribed*
    :type new_mem: struct ttm_mem_reg \*

.. _`amdgpu_move_vram_ram.description`:

Description
-----------

Called by \ :c:func:`amdgpu_bo_move`\ .

.. _`amdgpu_move_ram_vram`:

amdgpu_move_ram_vram
====================

.. c:function:: int amdgpu_move_ram_vram(struct ttm_buffer_object *bo, bool evict, struct ttm_operation_ctx *ctx, struct ttm_mem_reg *new_mem)

    Copy buffer from RAM to VRAM

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

    :param evict:
        *undescribed*
    :type evict: bool

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

    :param new_mem:
        *undescribed*
    :type new_mem: struct ttm_mem_reg \*

.. _`amdgpu_move_ram_vram.description`:

Description
-----------

Called by \ :c:func:`amdgpu_bo_move`\ .

.. _`amdgpu_bo_move`:

amdgpu_bo_move
==============

.. c:function:: int amdgpu_bo_move(struct ttm_buffer_object *bo, bool evict, struct ttm_operation_ctx *ctx, struct ttm_mem_reg *new_mem)

    Move a buffer object to a new memory location

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

    :param evict:
        *undescribed*
    :type evict: bool

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

    :param new_mem:
        *undescribed*
    :type new_mem: struct ttm_mem_reg \*

.. _`amdgpu_bo_move.description`:

Description
-----------

Called by \ :c:func:`ttm_bo_handle_move_mem`\ 

.. _`amdgpu_ttm_io_mem_reserve`:

amdgpu_ttm_io_mem_reserve
=========================

.. c:function:: int amdgpu_ttm_io_mem_reserve(struct ttm_bo_device *bdev, struct ttm_mem_reg *mem)

    Reserve a block of memory during a fault

    :param bdev:
        *undescribed*
    :type bdev: struct ttm_bo_device \*

    :param mem:
        *undescribed*
    :type mem: struct ttm_mem_reg \*

.. _`amdgpu_ttm_io_mem_reserve.description`:

Description
-----------

Called by \ :c:func:`ttm_mem_io_reserve`\  ultimately via \ :c:func:`ttm_bo_vm_fault`\ 

.. _`amdgpu_ttm_tt_get_user_pages`:

amdgpu_ttm_tt_get_user_pages
============================

.. c:function:: int amdgpu_ttm_tt_get_user_pages(struct ttm_tt *ttm, struct page **pages)

    Pin pages of memory pointed to by a USERPTR pointer to memory

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

    :param pages:
        *undescribed*
    :type pages: struct page \*\*

.. _`amdgpu_ttm_tt_get_user_pages.description`:

Description
-----------

Called by \ :c:func:`amdgpu_gem_userptr_ioctl`\  and \ :c:func:`amdgpu_cs_parser_bos`\ .
This provides a wrapper around the \ :c:func:`get_user_pages`\  call to provide
device accessible pages that back user memory.

.. _`amdgpu_ttm_tt_set_user_pages`:

amdgpu_ttm_tt_set_user_pages
============================

.. c:function:: void amdgpu_ttm_tt_set_user_pages(struct ttm_tt *ttm, struct page **pages)

    Copy pages in, putting old pages as necessary.

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

    :param pages:
        *undescribed*
    :type pages: struct page \*\*

.. _`amdgpu_ttm_tt_set_user_pages.description`:

Description
-----------

Called by \ :c:func:`amdgpu_cs_list_validate`\ . This creates the page list
that backs user memory and will ultimately be mapped into the device
address space.

.. _`amdgpu_ttm_tt_mark_user_pages`:

amdgpu_ttm_tt_mark_user_pages
=============================

.. c:function:: void amdgpu_ttm_tt_mark_user_pages(struct ttm_tt *ttm)

    Mark pages as dirty

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

.. _`amdgpu_ttm_tt_mark_user_pages.description`:

Description
-----------

Called while unpinning userptr pages

.. _`amdgpu_ttm_tt_pin_userptr`:

amdgpu_ttm_tt_pin_userptr
=========================

.. c:function:: int amdgpu_ttm_tt_pin_userptr(struct ttm_tt *ttm)

    prepare the sg table with the user pages

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

.. _`amdgpu_ttm_tt_pin_userptr.description`:

Description
-----------

Called by \ :c:func:`amdgpu_ttm_backend_bind`\ 

.. _`amdgpu_ttm_tt_unpin_userptr`:

amdgpu_ttm_tt_unpin_userptr
===========================

.. c:function:: void amdgpu_ttm_tt_unpin_userptr(struct ttm_tt *ttm)

    Unpin and unmap userptr pages

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

.. _`amdgpu_ttm_backend_bind`:

amdgpu_ttm_backend_bind
=======================

.. c:function:: int amdgpu_ttm_backend_bind(struct ttm_tt *ttm, struct ttm_mem_reg *bo_mem)

    Bind GTT memory

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

    :param bo_mem:
        *undescribed*
    :type bo_mem: struct ttm_mem_reg \*

.. _`amdgpu_ttm_backend_bind.description`:

Description
-----------

Called by \ :c:func:`ttm_tt_bind`\  on behalf of \ :c:func:`ttm_bo_handle_move_mem`\ .
This handles binding GTT memory to the device address space.

.. _`amdgpu_ttm_alloc_gart`:

amdgpu_ttm_alloc_gart
=====================

.. c:function:: int amdgpu_ttm_alloc_gart(struct ttm_buffer_object *bo)

    Allocate GART memory for buffer object

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

.. _`amdgpu_ttm_recover_gart`:

amdgpu_ttm_recover_gart
=======================

.. c:function:: int amdgpu_ttm_recover_gart(struct ttm_buffer_object *tbo)

    Rebind GTT pages

    :param tbo:
        *undescribed*
    :type tbo: struct ttm_buffer_object \*

.. _`amdgpu_ttm_recover_gart.description`:

Description
-----------

Called by \ :c:func:`amdgpu_gtt_mgr_recover`\  from \ :c:func:`amdgpu_device_reset`\  to
rebind GTT pages during a GPU reset.

.. _`amdgpu_ttm_backend_unbind`:

amdgpu_ttm_backend_unbind
=========================

.. c:function:: int amdgpu_ttm_backend_unbind(struct ttm_tt *ttm)

    Unbind GTT mapped pages

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

.. _`amdgpu_ttm_backend_unbind.description`:

Description
-----------

Called by \ :c:func:`ttm_tt_unbind`\  on behalf of \ :c:func:`ttm_bo_move_ttm`\  and
\ :c:func:`ttm_tt_destroy`\ .

.. _`amdgpu_ttm_tt_create`:

amdgpu_ttm_tt_create
====================

.. c:function:: struct ttm_tt *amdgpu_ttm_tt_create(struct ttm_buffer_object *bo, uint32_t page_flags)

    Create a ttm_tt object for a given BO

    :param bo:
        The buffer object to create a GTT ttm_tt object around
    :type bo: struct ttm_buffer_object \*

    :param page_flags:
        *undescribed*
    :type page_flags: uint32_t

.. _`amdgpu_ttm_tt_create.description`:

Description
-----------

Called by \ :c:func:`ttm_tt_create`\ .

.. _`amdgpu_ttm_tt_populate`:

amdgpu_ttm_tt_populate
======================

.. c:function:: int amdgpu_ttm_tt_populate(struct ttm_tt *ttm, struct ttm_operation_ctx *ctx)

    Map GTT pages visible to the device

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

    :param ctx:
        *undescribed*
    :type ctx: struct ttm_operation_ctx \*

.. _`amdgpu_ttm_tt_populate.description`:

Description
-----------

Map the pages of a ttm_tt object to an address space visible
to the underlying device.

.. _`amdgpu_ttm_tt_unpopulate`:

amdgpu_ttm_tt_unpopulate
========================

.. c:function:: void amdgpu_ttm_tt_unpopulate(struct ttm_tt *ttm)

    unmap GTT pages and unpopulate page arrays

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

.. _`amdgpu_ttm_tt_unpopulate.description`:

Description
-----------

Unmaps pages of a ttm_tt object from the device address space and
unpopulates the page array backing it.

.. _`amdgpu_ttm_tt_set_userptr`:

amdgpu_ttm_tt_set_userptr
=========================

.. c:function:: int amdgpu_ttm_tt_set_userptr(struct ttm_tt *ttm, uint64_t addr, uint32_t flags)

    Initialize userptr GTT ttm_tt for the current task

    :param ttm:
        The ttm_tt object to bind this userptr object to
    :type ttm: struct ttm_tt \*

    :param addr:
        The address in the current tasks VM space to use
    :type addr: uint64_t

    :param flags:
        Requirements of userptr object.
    :type flags: uint32_t

.. _`amdgpu_ttm_tt_set_userptr.description`:

Description
-----------

Called by \ :c:func:`amdgpu_gem_userptr_ioctl`\  to bind userptr pages
to current task

.. _`amdgpu_ttm_tt_get_usermm`:

amdgpu_ttm_tt_get_usermm
========================

.. c:function:: struct mm_struct *amdgpu_ttm_tt_get_usermm(struct ttm_tt *ttm)

    Return memory manager for ttm_tt object

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

.. _`amdgpu_ttm_tt_affect_userptr`:

amdgpu_ttm_tt_affect_userptr
============================

.. c:function:: bool amdgpu_ttm_tt_affect_userptr(struct ttm_tt *ttm, unsigned long start, unsigned long end)

    Determine if a ttm_tt object lays inside an address range for the current task.

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

    :param start:
        *undescribed*
    :type start: unsigned long

    :param end:
        *undescribed*
    :type end: unsigned long

.. _`amdgpu_ttm_tt_userptr_invalidated`:

amdgpu_ttm_tt_userptr_invalidated
=================================

.. c:function:: bool amdgpu_ttm_tt_userptr_invalidated(struct ttm_tt *ttm, int *last_invalidated)

    Has the ttm_tt object been invalidated?

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

    :param last_invalidated:
        *undescribed*
    :type last_invalidated: int \*

.. _`amdgpu_ttm_tt_userptr_needs_pages`:

amdgpu_ttm_tt_userptr_needs_pages
=================================

.. c:function:: bool amdgpu_ttm_tt_userptr_needs_pages(struct ttm_tt *ttm)

    Have the pages backing this ttm_tt object been invalidated since the last time they've been set?

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

.. _`amdgpu_ttm_tt_is_readonly`:

amdgpu_ttm_tt_is_readonly
=========================

.. c:function:: bool amdgpu_ttm_tt_is_readonly(struct ttm_tt *ttm)

    Is the ttm_tt object read only?

    :param ttm:
        *undescribed*
    :type ttm: struct ttm_tt \*

.. _`amdgpu_ttm_tt_pde_flags`:

amdgpu_ttm_tt_pde_flags
=======================

.. c:function:: uint64_t amdgpu_ttm_tt_pde_flags(struct ttm_tt *ttm, struct ttm_mem_reg *mem)

    Compute PDE flags for ttm_tt object

    :param ttm:
        The ttm_tt object to compute the flags for
    :type ttm: struct ttm_tt \*

    :param mem:
        The memory registry backing this ttm_tt object
    :type mem: struct ttm_mem_reg \*

.. _`amdgpu_ttm_tt_pde_flags.description`:

Description
-----------

Figure out the flags to use for a VM PDE (Page Directory Entry).

.. _`amdgpu_ttm_tt_pte_flags`:

amdgpu_ttm_tt_pte_flags
=======================

.. c:function:: uint64_t amdgpu_ttm_tt_pte_flags(struct amdgpu_device *adev, struct ttm_tt *ttm, struct ttm_mem_reg *mem)

    Compute PTE flags for ttm_tt object

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

    :param ttm:
        The ttm_tt object to compute the flags for
    :type ttm: struct ttm_tt \*

    :param mem:
        The memory registry backing this ttm_tt object
        Figure out the flags to use for a VM PTE (Page Table Entry).
    :type mem: struct ttm_mem_reg \*

.. _`amdgpu_ttm_bo_eviction_valuable`:

amdgpu_ttm_bo_eviction_valuable
===============================

.. c:function:: bool amdgpu_ttm_bo_eviction_valuable(struct ttm_buffer_object *bo, const struct ttm_place *place)

    Check to see if we can evict a buffer object.

    :param bo:
        *undescribed*
    :type bo: struct ttm_buffer_object \*

    :param place:
        *undescribed*
    :type place: const struct ttm_place \*

.. _`amdgpu_ttm_bo_eviction_valuable.description`:

Description
-----------

Return true if eviction is sensible. Called by \ :c:func:`ttm_mem_evict_first`\  on
behalf of \ :c:func:`ttm_bo_mem_force_space`\  which tries to evict buffer objects until
it can find space for a new object and by \ :c:func:`ttm_bo_force_list_clean`\  which is
used to clean out a memory space.

.. _`amdgpu_ttm_access_memory`:

amdgpu_ttm_access_memory
========================

.. c:function:: int amdgpu_ttm_access_memory(struct ttm_buffer_object *bo, unsigned long offset, void *buf, int len, int write)

    Read or Write memory that backs a buffer object.

    :param bo:
        The buffer object to read/write
    :type bo: struct ttm_buffer_object \*

    :param offset:
        Offset into buffer object
    :type offset: unsigned long

    :param buf:
        Secondary buffer to write/read from
    :type buf: void \*

    :param len:
        Length in bytes of access
    :type len: int

    :param write:
        true if writing
    :type write: int

.. _`amdgpu_ttm_access_memory.description`:

Description
-----------

This is used to access VRAM that backs a buffer object via MMIO
access for debugging purposes.

.. _`amdgpu_ttm_fw_reserve_vram_fini`:

amdgpu_ttm_fw_reserve_vram_fini
===============================

.. c:function:: void amdgpu_ttm_fw_reserve_vram_fini(struct amdgpu_device *adev)

    free fw reserved vram

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_ttm_fw_reserve_vram_fini.description`:

Description
-----------

free fw reserved vram if it has been reserved.

.. _`amdgpu_ttm_fw_reserve_vram_init`:

amdgpu_ttm_fw_reserve_vram_init
===============================

.. c:function:: int amdgpu_ttm_fw_reserve_vram_init(struct amdgpu_device *adev)

    create bo vram reservation from fw

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_ttm_fw_reserve_vram_init.description`:

Description
-----------

create bo vram reservation from fw.

.. _`amdgpu_ttm_init`:

amdgpu_ttm_init
===============

.. c:function:: int amdgpu_ttm_init(struct amdgpu_device *adev)

    Init the memory management (ttm) as well as various gtt/vram related fields.

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

.. _`amdgpu_ttm_init.description`:

Description
-----------

This initializes all of the memory space pools that the TTM layer
will need such as the GTT space (system memory mapped to the device),
VRAM (on-board memory), and on-chip memories (GDS, GWS, OA) which
can be mapped per VMID.

.. _`amdgpu_ttm_late_init`:

amdgpu_ttm_late_init
====================

.. c:function:: void amdgpu_ttm_late_init(struct amdgpu_device *adev)

    Handle any late initialization for amdgpu_ttm

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

.. _`amdgpu_ttm_fini`:

amdgpu_ttm_fini
===============

.. c:function:: void amdgpu_ttm_fini(struct amdgpu_device *adev)

    De-initialize the TTM memory pools

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

.. _`amdgpu_ttm_set_buffer_funcs_status`:

amdgpu_ttm_set_buffer_funcs_status
==================================

.. c:function:: void amdgpu_ttm_set_buffer_funcs_status(struct amdgpu_device *adev, bool enable)

    enable/disable use of buffer functions

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param enable:
        true when we can use buffer functions.
    :type enable: bool

.. _`amdgpu_ttm_set_buffer_funcs_status.description`:

Description
-----------

Enable/disable use of buffer functions during suspend/resume. This should
only be called at bootup or when userspace isn't running.

.. _`amdgpu_ttm_vram_read`:

amdgpu_ttm_vram_read
====================

.. c:function:: ssize_t amdgpu_ttm_vram_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Linear read access to VRAM

    :param f:
        *undescribed*
    :type f: struct file \*

    :param buf:
        *undescribed*
    :type buf: char __user \*

    :param size:
        *undescribed*
    :type size: size_t

    :param pos:
        *undescribed*
    :type pos: loff_t \*

.. _`amdgpu_ttm_vram_read.description`:

Description
-----------

Accesses VRAM via MMIO for debugging purposes.

.. _`amdgpu_ttm_vram_write`:

amdgpu_ttm_vram_write
=====================

.. c:function:: ssize_t amdgpu_ttm_vram_write(struct file *f, const char __user *buf, size_t size, loff_t *pos)

    Linear write access to VRAM

    :param f:
        *undescribed*
    :type f: struct file \*

    :param buf:
        *undescribed*
    :type buf: const char __user \*

    :param size:
        *undescribed*
    :type size: size_t

    :param pos:
        *undescribed*
    :type pos: loff_t \*

.. _`amdgpu_ttm_vram_write.description`:

Description
-----------

Accesses VRAM via MMIO for debugging purposes.

.. _`amdgpu_ttm_gtt_read`:

amdgpu_ttm_gtt_read
===================

.. c:function:: ssize_t amdgpu_ttm_gtt_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Linear read access to GTT memory

    :param f:
        *undescribed*
    :type f: struct file \*

    :param buf:
        *undescribed*
    :type buf: char __user \*

    :param size:
        *undescribed*
    :type size: size_t

    :param pos:
        *undescribed*
    :type pos: loff_t \*

.. _`amdgpu_iomem_read`:

amdgpu_iomem_read
=================

.. c:function:: ssize_t amdgpu_iomem_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Virtual read access to GPU mapped memory

    :param f:
        *undescribed*
    :type f: struct file \*

    :param buf:
        *undescribed*
    :type buf: char __user \*

    :param size:
        *undescribed*
    :type size: size_t

    :param pos:
        *undescribed*
    :type pos: loff_t \*

.. _`amdgpu_iomem_read.description`:

Description
-----------

This function is used to read memory that has been mapped to the
GPU and the known addresses are not physical addresses but instead
bus addresses (e.g., what you'd put in an IB or ring buffer).

.. _`amdgpu_iomem_write`:

amdgpu_iomem_write
==================

.. c:function:: ssize_t amdgpu_iomem_write(struct file *f, const char __user *buf, size_t size, loff_t *pos)

    Virtual write access to GPU mapped memory

    :param f:
        *undescribed*
    :type f: struct file \*

    :param buf:
        *undescribed*
    :type buf: const char __user \*

    :param size:
        *undescribed*
    :type size: size_t

    :param pos:
        *undescribed*
    :type pos: loff_t \*

.. _`amdgpu_iomem_write.description`:

Description
-----------

This function is used to write memory that has been mapped to the
GPU and the known addresses are not physical addresses but instead
bus addresses (e.g., what you'd put in an IB or ring buffer).

.. This file was automatic generated / don't edit.

