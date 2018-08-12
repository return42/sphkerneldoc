.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_ttm.c

.. _`amdgpu_ttm_mem_global_init`:

amdgpu_ttm_mem_global_init
==========================

.. c:function:: int amdgpu_ttm_mem_global_init(struct drm_global_reference *ref)

    Initialize and acquire reference to memory object

    :param struct drm_global_reference \*ref:
        Object for initialization.

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

    :param struct drm_global_reference \*ref:
        Object being removed

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

    :param struct amdgpu_device \*adev:
        AMDGPU device for which the global structures need to be
        registered.

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

    :param struct ttm_bo_device \*bdev:
        The TTM BO device object (contains a reference to
        amdgpu_device)

    :param uint32_t type:
        The type of memory requested

    :param struct ttm_mem_type_manager \*man:
        *undescribed*

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

    :param struct ttm_buffer_object \*bo:
        The buffer object to evict

    :param struct ttm_placement \*placement:
        Possible destination(s) for evicted BO

.. _`amdgpu_evict_flags.description`:

Description
-----------

Fill in placement data when \ :c:func:`ttm_bo_evict`\  is called

.. _`amdgpu_verify_access`:

amdgpu_verify_access
====================

.. c:function:: int amdgpu_verify_access(struct ttm_buffer_object *bo, struct file *filp)

    Verify access for a mmap call

    :param struct ttm_buffer_object \*bo:
        The buffer object to map

    :param struct file \*filp:
        The file pointer from the process performing the mmap

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

    :param struct ttm_buffer_object \*bo:
        The bo to assign the memory to

    :param struct ttm_mem_reg \*new_mem:
        The memory to be assigned.

.. _`amdgpu_move_null.description`:

Description
-----------

Assign the memory from new_mem to the memory of the buffer object
bo.

.. _`amdgpu_mm_node_addr`:

amdgpu_mm_node_addr
===================

.. c:function:: uint64_t amdgpu_mm_node_addr(struct ttm_buffer_object *bo, struct drm_mm_node *mm_node, struct ttm_mem_reg *mem)

    Compute the GPU relative offset of a GTT buffer.

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param struct drm_mm_node \*mm_node:
        *undescribed*

    :param struct ttm_mem_reg \*mem:
        *undescribed*

.. _`amdgpu_find_mm_node`:

amdgpu_find_mm_node
===================

.. c:function:: struct drm_mm_node *amdgpu_find_mm_node(struct ttm_mem_reg *mem, unsigned long *offset)

    Helper function finds the drm_mm_node corresponding to \ ``offset``\ . It also modifies the offset to be within the drm_mm_node returned

    :param struct ttm_mem_reg \*mem:
        *undescribed*

    :param unsigned long \*offset:
        *undescribed*

.. _`amdgpu_ttm_copy_mem_to_mem`:

amdgpu_ttm_copy_mem_to_mem
==========================

.. c:function:: int amdgpu_ttm_copy_mem_to_mem(struct amdgpu_device *adev, struct amdgpu_copy_mem *src, struct amdgpu_copy_mem *dst, uint64_t size, struct reservation_object *resv, struct dma_fence **f)

    Helper function for copy

    :param struct amdgpu_device \*adev:
        *undescribed*

    :param struct amdgpu_copy_mem \*src:
        *undescribed*

    :param struct amdgpu_copy_mem \*dst:
        *undescribed*

    :param uint64_t size:
        *undescribed*

    :param struct reservation_object \*resv:
        *undescribed*

    :param struct dma_fence \*\*f:
        Returns the last fence if multiple jobs are submitted.

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

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param bool evict:
        *undescribed*

    :param bool no_wait_gpu:
        *undescribed*

    :param struct ttm_mem_reg \*new_mem:
        *undescribed*

    :param struct ttm_mem_reg \*old_mem:
        *undescribed*

.. _`amdgpu_move_blit.description`:

Description
-----------

This is a helper called by \ :c:func:`amdgpu_bo_move`\  and
\ :c:func:`amdgpu_move_vram_ram`\  to help move buffers to and from VRAM.

.. _`amdgpu_move_vram_ram`:

amdgpu_move_vram_ram
====================

.. c:function:: int amdgpu_move_vram_ram(struct ttm_buffer_object *bo, bool evict, struct ttm_operation_ctx *ctx, struct ttm_mem_reg *new_mem)

    Copy VRAM buffer to RAM buffer

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param bool evict:
        *undescribed*

    :param struct ttm_operation_ctx \*ctx:
        *undescribed*

    :param struct ttm_mem_reg \*new_mem:
        *undescribed*

.. _`amdgpu_move_vram_ram.description`:

Description
-----------

Called by \ :c:func:`amdgpu_bo_move`\ .

.. _`amdgpu_move_ram_vram`:

amdgpu_move_ram_vram
====================

.. c:function:: int amdgpu_move_ram_vram(struct ttm_buffer_object *bo, bool evict, struct ttm_operation_ctx *ctx, struct ttm_mem_reg *new_mem)

    Copy buffer from RAM to VRAM

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param bool evict:
        *undescribed*

    :param struct ttm_operation_ctx \*ctx:
        *undescribed*

    :param struct ttm_mem_reg \*new_mem:
        *undescribed*

.. _`amdgpu_move_ram_vram.description`:

Description
-----------

Called by \ :c:func:`amdgpu_bo_move`\ .

.. _`amdgpu_bo_move`:

amdgpu_bo_move
==============

.. c:function:: int amdgpu_bo_move(struct ttm_buffer_object *bo, bool evict, struct ttm_operation_ctx *ctx, struct ttm_mem_reg *new_mem)

    Move a buffer object to a new memory location

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param bool evict:
        *undescribed*

    :param struct ttm_operation_ctx \*ctx:
        *undescribed*

    :param struct ttm_mem_reg \*new_mem:
        *undescribed*

.. _`amdgpu_bo_move.description`:

Description
-----------

Called by \ :c:func:`ttm_bo_handle_move_mem`\ 

.. _`amdgpu_ttm_io_mem_reserve`:

amdgpu_ttm_io_mem_reserve
=========================

.. c:function:: int amdgpu_ttm_io_mem_reserve(struct ttm_bo_device *bdev, struct ttm_mem_reg *mem)

    Reserve a block of memory during a fault

    :param struct ttm_bo_device \*bdev:
        *undescribed*

    :param struct ttm_mem_reg \*mem:
        *undescribed*

.. _`amdgpu_ttm_io_mem_reserve.description`:

Description
-----------

Called by \ :c:func:`ttm_mem_io_reserve`\  ultimately via \ :c:func:`ttm_bo_vm_fault`\ 

.. _`amdgpu_ttm_tt_get_user_pages`:

amdgpu_ttm_tt_get_user_pages
============================

.. c:function:: int amdgpu_ttm_tt_get_user_pages(struct ttm_tt *ttm, struct page **pages)

    Pin pages of memory pointed to by a USERPTR pointer to memory

    :param struct ttm_tt \*ttm:
        *undescribed*

    :param struct page \*\*pages:
        *undescribed*

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

    :param struct ttm_tt \*ttm:
        *undescribed*

    :param struct page \*\*pages:
        *undescribed*

.. _`amdgpu_ttm_tt_set_user_pages.description`:

Description
-----------

Called by \ :c:func:`amdgpu_cs_list_validate`\ .  This creates the page list
that backs user memory and will ultimately be mapped into the device
address space.

.. _`amdgpu_ttm_tt_mark_user_pages`:

amdgpu_ttm_tt_mark_user_pages
=============================

.. c:function:: void amdgpu_ttm_tt_mark_user_pages(struct ttm_tt *ttm)

    Mark pages as dirty

    :param struct ttm_tt \*ttm:
        *undescribed*

.. _`amdgpu_ttm_tt_mark_user_pages.description`:

Description
-----------

Called while unpinning userptr pages

.. _`amdgpu_ttm_tt_pin_userptr`:

amdgpu_ttm_tt_pin_userptr
=========================

.. c:function:: int amdgpu_ttm_tt_pin_userptr(struct ttm_tt *ttm)

    prepare the sg table with the user pages

    :param struct ttm_tt \*ttm:
        *undescribed*

.. _`amdgpu_ttm_tt_pin_userptr.description`:

Description
-----------

Called by \ :c:func:`amdgpu_ttm_backend_bind`\ 

.. _`amdgpu_ttm_tt_unpin_userptr`:

amdgpu_ttm_tt_unpin_userptr
===========================

.. c:function:: void amdgpu_ttm_tt_unpin_userptr(struct ttm_tt *ttm)

    Unpin and unmap userptr pages

    :param struct ttm_tt \*ttm:
        *undescribed*

.. _`amdgpu_ttm_backend_bind`:

amdgpu_ttm_backend_bind
=======================

.. c:function:: int amdgpu_ttm_backend_bind(struct ttm_tt *ttm, struct ttm_mem_reg *bo_mem)

    Bind GTT memory

    :param struct ttm_tt \*ttm:
        *undescribed*

    :param struct ttm_mem_reg \*bo_mem:
        *undescribed*

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

    :param struct ttm_buffer_object \*bo:
        *undescribed*

.. _`amdgpu_ttm_recover_gart`:

amdgpu_ttm_recover_gart
=======================

.. c:function:: int amdgpu_ttm_recover_gart(struct ttm_buffer_object *tbo)

    Rebind GTT pages

    :param struct ttm_buffer_object \*tbo:
        *undescribed*

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

    :param struct ttm_tt \*ttm:
        *undescribed*

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

    :param struct ttm_buffer_object \*bo:
        The buffer object to create a GTT ttm_tt object around

    :param uint32_t page_flags:
        *undescribed*

.. _`amdgpu_ttm_tt_create.description`:

Description
-----------

Called by \ :c:func:`ttm_tt_create`\ .

.. _`amdgpu_ttm_tt_populate`:

amdgpu_ttm_tt_populate
======================

.. c:function:: int amdgpu_ttm_tt_populate(struct ttm_tt *ttm, struct ttm_operation_ctx *ctx)

    Map GTT pages visible to the device

    :param struct ttm_tt \*ttm:
        *undescribed*

    :param struct ttm_operation_ctx \*ctx:
        *undescribed*

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

    :param struct ttm_tt \*ttm:
        *undescribed*

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

    :param struct ttm_tt \*ttm:
        The ttm_tt object to bind this userptr object to

    :param uint64_t addr:
        The address in the current tasks VM space to use

    :param uint32_t flags:
        Requirements of userptr object.

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

    :param struct ttm_tt \*ttm:
        *undescribed*

.. _`amdgpu_ttm_tt_affect_userptr`:

amdgpu_ttm_tt_affect_userptr
============================

.. c:function:: bool amdgpu_ttm_tt_affect_userptr(struct ttm_tt *ttm, unsigned long start, unsigned long end)

    Determine if a ttm_tt object lays inside an address range for the current task.

    :param struct ttm_tt \*ttm:
        *undescribed*

    :param unsigned long start:
        *undescribed*

    :param unsigned long end:
        *undescribed*

.. _`amdgpu_ttm_tt_userptr_invalidated`:

amdgpu_ttm_tt_userptr_invalidated
=================================

.. c:function:: bool amdgpu_ttm_tt_userptr_invalidated(struct ttm_tt *ttm, int *last_invalidated)

    Has the ttm_tt object been invalidated?

    :param struct ttm_tt \*ttm:
        *undescribed*

    :param int \*last_invalidated:
        *undescribed*

.. _`amdgpu_ttm_tt_userptr_needs_pages`:

amdgpu_ttm_tt_userptr_needs_pages
=================================

.. c:function:: bool amdgpu_ttm_tt_userptr_needs_pages(struct ttm_tt *ttm)

    Have the pages backing this ttm_tt object been invalidated since the last time they've been set?

    :param struct ttm_tt \*ttm:
        *undescribed*

.. _`amdgpu_ttm_tt_is_readonly`:

amdgpu_ttm_tt_is_readonly
=========================

.. c:function:: bool amdgpu_ttm_tt_is_readonly(struct ttm_tt *ttm)

    Is the ttm_tt object read only?

    :param struct ttm_tt \*ttm:
        *undescribed*

.. _`amdgpu_ttm_tt_pte_flags`:

amdgpu_ttm_tt_pte_flags
=======================

.. c:function:: uint64_t amdgpu_ttm_tt_pte_flags(struct amdgpu_device *adev, struct ttm_tt *ttm, struct ttm_mem_reg *mem)

    Compute PTE flags for ttm_tt object

    :param struct amdgpu_device \*adev:
        *undescribed*

    :param struct ttm_tt \*ttm:
        The ttm_tt object to compute the flags for

    :param struct ttm_mem_reg \*mem:
        The memory registry backing this ttm_tt object

.. _`amdgpu_ttm_bo_eviction_valuable`:

amdgpu_ttm_bo_eviction_valuable
===============================

.. c:function:: bool amdgpu_ttm_bo_eviction_valuable(struct ttm_buffer_object *bo, const struct ttm_place *place)

    Check to see if we can evict a buffer object.

    :param struct ttm_buffer_object \*bo:
        *undescribed*

    :param const struct ttm_place \*place:
        *undescribed*

.. _`amdgpu_ttm_bo_eviction_valuable.description`:

Description
-----------

Return true if eviction is sensible.  Called by
\ :c:func:`ttm_mem_evict_first`\  on behalf of \ :c:func:`ttm_bo_mem_force_space`\ 
which tries to evict buffer objects until it can find space
for a new object and by \ :c:func:`ttm_bo_force_list_clean`\  which is
used to clean out a memory space.

.. _`amdgpu_ttm_access_memory`:

amdgpu_ttm_access_memory
========================

.. c:function:: int amdgpu_ttm_access_memory(struct ttm_buffer_object *bo, unsigned long offset, void *buf, int len, int write)

    Read or Write memory that backs a buffer object.

    :param struct ttm_buffer_object \*bo:
        The buffer object to read/write

    :param unsigned long offset:
        Offset into buffer object

    :param void \*buf:
        Secondary buffer to write/read from

    :param int len:
        Length in bytes of access

    :param int write:
        true if writing

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

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_ttm_fw_reserve_vram_fini.description`:

Description
-----------

free fw reserved vram if it has been reserved.

.. _`amdgpu_ttm_fw_reserve_vram_init`:

amdgpu_ttm_fw_reserve_vram_init
===============================

.. c:function:: int amdgpu_ttm_fw_reserve_vram_init(struct amdgpu_device *adev)

    create bo vram reservation from fw

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_ttm_fw_reserve_vram_init.description`:

Description
-----------

create bo vram reservation from fw.

.. _`amdgpu_ttm_init`:

amdgpu_ttm_init
===============

.. c:function:: int amdgpu_ttm_init(struct amdgpu_device *adev)

    Init the memory management (ttm) as well as various gtt/vram related fields.

    :param struct amdgpu_device \*adev:
        *undescribed*

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

    :param struct amdgpu_device \*adev:
        *undescribed*

.. _`amdgpu_ttm_fini`:

amdgpu_ttm_fini
===============

.. c:function:: void amdgpu_ttm_fini(struct amdgpu_device *adev)

    De-initialize the TTM memory pools

    :param struct amdgpu_device \*adev:
        *undescribed*

.. _`amdgpu_ttm_set_buffer_funcs_status`:

amdgpu_ttm_set_buffer_funcs_status
==================================

.. c:function:: void amdgpu_ttm_set_buffer_funcs_status(struct amdgpu_device *adev, bool enable)

    enable/disable use of buffer functions

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param bool enable:
        true when we can use buffer functions.

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

    :param struct file \*f:
        *undescribed*

    :param char __user \*buf:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

.. _`amdgpu_ttm_vram_read.description`:

Description
-----------

Accesses VRAM via MMIO for debugging purposes.

.. _`amdgpu_ttm_vram_write`:

amdgpu_ttm_vram_write
=====================

.. c:function:: ssize_t amdgpu_ttm_vram_write(struct file *f, const char __user *buf, size_t size, loff_t *pos)

    Linear write access to VRAM

    :param struct file \*f:
        *undescribed*

    :param const char __user \*buf:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

.. _`amdgpu_ttm_vram_write.description`:

Description
-----------

Accesses VRAM via MMIO for debugging purposes.

.. _`amdgpu_ttm_gtt_read`:

amdgpu_ttm_gtt_read
===================

.. c:function:: ssize_t amdgpu_ttm_gtt_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Linear read access to GTT memory

    :param struct file \*f:
        *undescribed*

    :param char __user \*buf:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

.. _`amdgpu_iomem_read`:

amdgpu_iomem_read
=================

.. c:function:: ssize_t amdgpu_iomem_read(struct file *f, char __user *buf, size_t size, loff_t *pos)

    Virtual read access to GPU mapped memory

    :param struct file \*f:
        *undescribed*

    :param char __user \*buf:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

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

    :param struct file \*f:
        *undescribed*

    :param const char __user \*buf:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param loff_t \*pos:
        *undescribed*

.. _`amdgpu_iomem_write.description`:

Description
-----------

This function is used to write memory that has been mapped to the
GPU and the known addresses are not physical addresses but instead
bus addresses (e.g., what you'd put in an IB or ring buffer).

.. This file was automatic generated / don't edit.

