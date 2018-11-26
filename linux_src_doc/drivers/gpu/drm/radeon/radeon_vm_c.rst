.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_vm.c

.. _`radeon_vm_num_pdes`:

radeon_vm_num_pdes
==================

.. c:function:: unsigned radeon_vm_num_pdes(struct radeon_device *rdev)

    return the number of page directory entries

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_vm_num_pdes.description`:

Description
-----------

Calculate the number of page directory entries (cayman+).

.. _`radeon_vm_directory_size`:

radeon_vm_directory_size
========================

.. c:function:: unsigned radeon_vm_directory_size(struct radeon_device *rdev)

    returns the size of the page directory in bytes

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_vm_directory_size.description`:

Description
-----------

Calculate the size of the page directory in bytes (cayman+).

.. _`radeon_vm_manager_init`:

radeon_vm_manager_init
======================

.. c:function:: int radeon_vm_manager_init(struct radeon_device *rdev)

    init the vm manager

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_vm_manager_init.description`:

Description
-----------

Init the vm manager (cayman+).
Returns 0 for success, error for failure.

.. _`radeon_vm_manager_fini`:

radeon_vm_manager_fini
======================

.. c:function:: void radeon_vm_manager_fini(struct radeon_device *rdev)

    tear down the vm manager

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_vm_manager_fini.description`:

Description
-----------

Tear down the VM manager (cayman+).

.. _`radeon_vm_get_bos`:

radeon_vm_get_bos
=================

.. c:function:: struct radeon_bo_list *radeon_vm_get_bos(struct radeon_device *rdev, struct radeon_vm *vm, struct list_head *head)

    add the vm BOs to a validation list

    :param rdev:
        *undescribed*
    :type rdev: struct radeon_device \*

    :param vm:
        vm providing the BOs
    :type vm: struct radeon_vm \*

    :param head:
        head of validation list
    :type head: struct list_head \*

.. _`radeon_vm_get_bos.description`:

Description
-----------

Add the page directory to the list of BOs to
validate for command submission (cayman+).

.. _`radeon_vm_grab_id`:

radeon_vm_grab_id
=================

.. c:function:: struct radeon_fence *radeon_vm_grab_id(struct radeon_device *rdev, struct radeon_vm *vm, int ring)

    allocate the next free VMID

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vm:
        vm to allocate id for
    :type vm: struct radeon_vm \*

    :param ring:
        ring we want to submit job to
    :type ring: int

.. _`radeon_vm_grab_id.description`:

Description
-----------

Allocate an id for the vm (cayman+).
Returns the fence we need to sync to (if any).

Global and local mutex must be locked!

.. _`radeon_vm_flush`:

radeon_vm_flush
===============

.. c:function:: void radeon_vm_flush(struct radeon_device *rdev, struct radeon_vm *vm, int ring, struct radeon_fence *updates)

    hardware flush the vm

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vm:
        vm we want to flush
    :type vm: struct radeon_vm \*

    :param ring:
        ring to use for flush
    :type ring: int

    :param updates:
        last vm update that is waited for
    :type updates: struct radeon_fence \*

.. _`radeon_vm_flush.description`:

Description
-----------

Flush the vm (cayman+).

Global and local mutex must be locked!

.. _`radeon_vm_fence`:

radeon_vm_fence
===============

.. c:function:: void radeon_vm_fence(struct radeon_device *rdev, struct radeon_vm *vm, struct radeon_fence *fence)

    remember fence for vm

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vm:
        vm we want to fence
    :type vm: struct radeon_vm \*

    :param fence:
        fence to remember
    :type fence: struct radeon_fence \*

.. _`radeon_vm_fence.description`:

Description
-----------

Fence the vm (cayman+).
Set the fence used to protect page table and id.

Global and local mutex must be locked!

.. _`radeon_vm_bo_find`:

radeon_vm_bo_find
=================

.. c:function:: struct radeon_bo_va *radeon_vm_bo_find(struct radeon_vm *vm, struct radeon_bo *bo)

    find the bo_va for a specific vm & bo

    :param vm:
        requested vm
    :type vm: struct radeon_vm \*

    :param bo:
        requested buffer object
    :type bo: struct radeon_bo \*

.. _`radeon_vm_bo_find.description`:

Description
-----------

Find \ ``bo``\  inside the requested vm (cayman+).
Search inside the \ ``bos``\  vm list for the requested vm
Returns the found bo_va or NULL if none is found

Object has to be reserved!

.. _`radeon_vm_bo_add`:

radeon_vm_bo_add
================

.. c:function:: struct radeon_bo_va *radeon_vm_bo_add(struct radeon_device *rdev, struct radeon_vm *vm, struct radeon_bo *bo)

    add a bo to a specific vm

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vm:
        requested vm
    :type vm: struct radeon_vm \*

    :param bo:
        radeon buffer object
    :type bo: struct radeon_bo \*

.. _`radeon_vm_bo_add.description`:

Description
-----------

Add \ ``bo``\  into the requested vm (cayman+).
Add \ ``bo``\  to the list of bos associated with the vm
Returns newly added bo_va or NULL for failure

Object has to be reserved!

.. _`radeon_vm_set_pages`:

radeon_vm_set_pages
===================

.. c:function:: void radeon_vm_set_pages(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint32_t flags)

    helper to call the right asic function

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        indirect buffer to fill with commands
    :type ib: struct radeon_ib \*

    :param pe:
        addr of the page entry
    :type pe: uint64_t

    :param addr:
        dst addr to write into pe
    :type addr: uint64_t

    :param count:
        number of page entries to update
    :type count: unsigned

    :param incr:
        increase next addr by incr bytes
    :type incr: uint32_t

    :param flags:
        hw access flags
    :type flags: uint32_t

.. _`radeon_vm_set_pages.description`:

Description
-----------

Traces the parameters and calls the right asic functions
to setup the page table using the DMA.

.. _`radeon_vm_clear_bo`:

radeon_vm_clear_bo
==================

.. c:function:: int radeon_vm_clear_bo(struct radeon_device *rdev, struct radeon_bo *bo)

    initially clear the page dir/table

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param bo:
        bo to clear
    :type bo: struct radeon_bo \*

.. _`radeon_vm_bo_set_addr`:

radeon_vm_bo_set_addr
=====================

.. c:function:: int radeon_vm_bo_set_addr(struct radeon_device *rdev, struct radeon_bo_va *bo_va, uint64_t soffset, uint32_t flags)

    set bos virtual address inside a vm

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param bo_va:
        bo_va to store the address
    :type bo_va: struct radeon_bo_va \*

    :param soffset:
        requested offset of the buffer in the VM address space
    :type soffset: uint64_t

    :param flags:
        attributes of pages (read/write/valid/etc.)
    :type flags: uint32_t

.. _`radeon_vm_bo_set_addr.description`:

Description
-----------

Set offset of \ ``bo_va``\  (cayman+).
Validate and set the offset requested within the vm address space.
Returns 0 for success, error for failure.

Object has to be reserved and gets unreserved by this function!

.. _`radeon_vm_map_gart`:

radeon_vm_map_gart
==================

.. c:function:: uint64_t radeon_vm_map_gart(struct radeon_device *rdev, uint64_t addr)

    get the physical address of a gart page

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param addr:
        the unmapped addr
    :type addr: uint64_t

.. _`radeon_vm_map_gart.description`:

Description
-----------

Look up the physical address of the page that the pte resolves
to (cayman+).
Returns the physical address of the page.

.. _`radeon_vm_page_flags`:

radeon_vm_page_flags
====================

.. c:function:: uint32_t radeon_vm_page_flags(uint32_t flags)

    translate page flags to what the hw uses

    :param flags:
        flags comming from userspace
    :type flags: uint32_t

.. _`radeon_vm_page_flags.description`:

Description
-----------

Translate the flags the userspace ABI uses to hw flags.

.. _`radeon_vm_update_page_directory`:

radeon_vm_update_page_directory
===============================

.. c:function:: int radeon_vm_update_page_directory(struct radeon_device *rdev, struct radeon_vm *vm)

    make sure that page directory is valid

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vm:
        requested vm
    :type vm: struct radeon_vm \*

.. _`radeon_vm_update_page_directory.description`:

Description
-----------

Allocates new page tables if necessary
and updates the page directory (cayman+).
Returns 0 for success, error for failure.

Global and local mutex must be locked!

.. _`radeon_vm_frag_ptes`:

radeon_vm_frag_ptes
===================

.. c:function:: void radeon_vm_frag_ptes(struct radeon_device *rdev, struct radeon_ib *ib, uint64_t pe_start, uint64_t pe_end, uint64_t addr, uint32_t flags)

    add fragment information to PTEs

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        IB for the update
    :type ib: struct radeon_ib \*

    :param pe_start:
        first PTE to handle
    :type pe_start: uint64_t

    :param pe_end:
        last PTE to handle
    :type pe_end: uint64_t

    :param addr:
        addr those PTEs should point to
    :type addr: uint64_t

    :param flags:
        hw mapping flags
    :type flags: uint32_t

.. _`radeon_vm_frag_ptes.description`:

Description
-----------

Global and local mutex must be locked!

.. _`radeon_vm_update_ptes`:

radeon_vm_update_ptes
=====================

.. c:function:: int radeon_vm_update_ptes(struct radeon_device *rdev, struct radeon_vm *vm, struct radeon_ib *ib, uint64_t start, uint64_t end, uint64_t dst, uint32_t flags)

    make sure that page tables are valid

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vm:
        requested vm
    :type vm: struct radeon_vm \*

    :param ib:
        *undescribed*
    :type ib: struct radeon_ib \*

    :param start:
        start of GPU address range
    :type start: uint64_t

    :param end:
        end of GPU address range
    :type end: uint64_t

    :param dst:
        destination address to map to
    :type dst: uint64_t

    :param flags:
        mapping flags
    :type flags: uint32_t

.. _`radeon_vm_update_ptes.description`:

Description
-----------

Update the page tables in the range \ ``start``\  - \ ``end``\  (cayman+).

Global and local mutex must be locked!

.. _`radeon_vm_fence_pts`:

radeon_vm_fence_pts
===================

.. c:function:: void radeon_vm_fence_pts(struct radeon_vm *vm, uint64_t start, uint64_t end, struct radeon_fence *fence)

    fence page tables after an update

    :param vm:
        requested vm
    :type vm: struct radeon_vm \*

    :param start:
        start of GPU address range
    :type start: uint64_t

    :param end:
        end of GPU address range
    :type end: uint64_t

    :param fence:
        fence to use
    :type fence: struct radeon_fence \*

.. _`radeon_vm_fence_pts.description`:

Description
-----------

Fence the page tables in the range \ ``start``\  - \ ``end``\  (cayman+).

Global and local mutex must be locked!

.. _`radeon_vm_bo_update`:

radeon_vm_bo_update
===================

.. c:function:: int radeon_vm_bo_update(struct radeon_device *rdev, struct radeon_bo_va *bo_va, struct ttm_mem_reg *mem)

    map a bo into the vm page table

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param bo_va:
        *undescribed*
    :type bo_va: struct radeon_bo_va \*

    :param mem:
        ttm mem
    :type mem: struct ttm_mem_reg \*

.. _`radeon_vm_bo_update.description`:

Description
-----------

Fill in the page table entries for \ ``bo``\  (cayman+).
Returns 0 for success, -EINVAL for failure.

Object have to be reserved and mutex must be locked!

.. _`radeon_vm_clear_freed`:

radeon_vm_clear_freed
=====================

.. c:function:: int radeon_vm_clear_freed(struct radeon_device *rdev, struct radeon_vm *vm)

    clear freed BOs in the PT

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vm:
        requested vm
    :type vm: struct radeon_vm \*

.. _`radeon_vm_clear_freed.description`:

Description
-----------

Make sure all freed BOs are cleared in the PT.
Returns 0 for success.

PTs have to be reserved and mutex must be locked!

.. _`radeon_vm_clear_invalids`:

radeon_vm_clear_invalids
========================

.. c:function:: int radeon_vm_clear_invalids(struct radeon_device *rdev, struct radeon_vm *vm)

    clear invalidated BOs in the PT

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vm:
        requested vm
    :type vm: struct radeon_vm \*

.. _`radeon_vm_clear_invalids.description`:

Description
-----------

Make sure all invalidated BOs are cleared in the PT.
Returns 0 for success.

PTs have to be reserved and mutex must be locked!

.. _`radeon_vm_bo_rmv`:

radeon_vm_bo_rmv
================

.. c:function:: void radeon_vm_bo_rmv(struct radeon_device *rdev, struct radeon_bo_va *bo_va)

    remove a bo to a specific vm

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param bo_va:
        requested bo_va
    :type bo_va: struct radeon_bo_va \*

.. _`radeon_vm_bo_rmv.description`:

Description
-----------

Remove \ ``bo_va->bo``\  from the requested vm (cayman+).

Object have to be reserved!

.. _`radeon_vm_bo_invalidate`:

radeon_vm_bo_invalidate
=======================

.. c:function:: void radeon_vm_bo_invalidate(struct radeon_device *rdev, struct radeon_bo *bo)

    mark the bo as invalid

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param bo:
        radeon buffer object
    :type bo: struct radeon_bo \*

.. _`radeon_vm_bo_invalidate.description`:

Description
-----------

Mark \ ``bo``\  as invalid (cayman+).

.. _`radeon_vm_init`:

radeon_vm_init
==============

.. c:function:: int radeon_vm_init(struct radeon_device *rdev, struct radeon_vm *vm)

    initialize a vm instance

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vm:
        requested vm
    :type vm: struct radeon_vm \*

.. _`radeon_vm_init.description`:

Description
-----------

Init \ ``vm``\  fields (cayman+).

.. _`radeon_vm_fini`:

radeon_vm_fini
==============

.. c:function:: void radeon_vm_fini(struct radeon_device *rdev, struct radeon_vm *vm)

    tear down a vm instance

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param vm:
        requested vm
    :type vm: struct radeon_vm \*

.. _`radeon_vm_fini.description`:

Description
-----------

Tear down \ ``vm``\  (cayman+).
Unbind the VM and remove all bos from the vm bo list

.. This file was automatic generated / don't edit.

