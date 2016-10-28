.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_vm.c

.. _`amdgpu_vm_num_pdes`:

amdgpu_vm_num_pdes
==================

.. c:function:: unsigned amdgpu_vm_num_pdes(struct amdgpu_device *adev)

    return the number of page directory entries

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_vm_num_pdes.description`:

Description
-----------

Calculate the number of page directory entries.

.. _`amdgpu_vm_directory_size`:

amdgpu_vm_directory_size
========================

.. c:function:: unsigned amdgpu_vm_directory_size(struct amdgpu_device *adev)

    returns the size of the page directory in bytes

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_vm_directory_size.description`:

Description
-----------

Calculate the size of the page directory in bytes.

.. _`amdgpu_vm_get_pd_bo`:

amdgpu_vm_get_pd_bo
===================

.. c:function:: void amdgpu_vm_get_pd_bo(struct amdgpu_vm *vm, struct list_head *validated, struct amdgpu_bo_list_entry *entry)

    add the VM PD to a validation list

    :param struct amdgpu_vm \*vm:
        vm providing the BOs

    :param struct list_head \*validated:
        head of validation list

    :param struct amdgpu_bo_list_entry \*entry:
        entry to add

.. _`amdgpu_vm_get_pd_bo.description`:

Description
-----------

Add the page directory to the list of BOs to
validate for command submission.

.. _`amdgpu_vm_get_pt_bos`:

amdgpu_vm_get_pt_bos
====================

.. c:function:: void amdgpu_vm_get_pt_bos(struct amdgpu_vm *vm, struct list_head *duplicates)

    add the vm BOs to a duplicates list

    :param struct amdgpu_vm \*vm:
        vm providing the BOs

    :param struct list_head \*duplicates:
        head of duplicates list

.. _`amdgpu_vm_get_pt_bos.description`:

Description
-----------

Add the page directory to the BO duplicates list
for command submission.

.. _`amdgpu_vm_move_pt_bos_in_lru`:

amdgpu_vm_move_pt_bos_in_lru
============================

.. c:function:: void amdgpu_vm_move_pt_bos_in_lru(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    move the PT BOs to the LRU tail

    :param struct amdgpu_device \*adev:
        amdgpu device instance

    :param struct amdgpu_vm \*vm:
        vm providing the BOs

.. _`amdgpu_vm_move_pt_bos_in_lru.description`:

Description
-----------

Move the PT BOs to the tail of the LRU.

.. _`amdgpu_vm_grab_id`:

amdgpu_vm_grab_id
=================

.. c:function:: int amdgpu_vm_grab_id(struct amdgpu_vm *vm, struct amdgpu_ring *ring, struct amdgpu_sync *sync, struct fence *fence, unsigned *vm_id, uint64_t *vm_pd_addr)

    allocate the next free VMID

    :param struct amdgpu_vm \*vm:
        vm to allocate id for

    :param struct amdgpu_ring \*ring:
        ring we want to submit job to

    :param struct amdgpu_sync \*sync:
        sync object where we add dependencies

    :param struct fence \*fence:
        fence protecting ID from reuse

    :param unsigned \*vm_id:
        *undescribed*

    :param uint64_t \*vm_pd_addr:
        *undescribed*

.. _`amdgpu_vm_grab_id.description`:

Description
-----------

Allocate an id for the vm, adding fences to the sync obj as necessary.

.. _`amdgpu_vm_flush`:

amdgpu_vm_flush
===============

.. c:function:: int amdgpu_vm_flush(struct amdgpu_ring *ring, unsigned vm_id, uint64_t pd_addr, uint32_t gds_base, uint32_t gds_size, uint32_t gws_base, uint32_t gws_size, uint32_t oa_base, uint32_t oa_size)

    hardware flush the vm

    :param struct amdgpu_ring \*ring:
        ring to use for flush

    :param unsigned vm_id:
        vmid number to use

    :param uint64_t pd_addr:
        address of the page directory

    :param uint32_t gds_base:
        *undescribed*

    :param uint32_t gds_size:
        *undescribed*

    :param uint32_t gws_base:
        *undescribed*

    :param uint32_t gws_size:
        *undescribed*

    :param uint32_t oa_base:
        *undescribed*

    :param uint32_t oa_size:
        *undescribed*

.. _`amdgpu_vm_flush.description`:

Description
-----------

Emit a VM flush when it is necessary.

.. _`amdgpu_vm_reset_id`:

amdgpu_vm_reset_id
==================

.. c:function:: void amdgpu_vm_reset_id(struct amdgpu_device *adev, unsigned vm_id)

    reset VMID to zero

    :param struct amdgpu_device \*adev:
        amdgpu device structure

    :param unsigned vm_id:
        vmid number to use

.. _`amdgpu_vm_reset_id.description`:

Description
-----------

Reset saved GDW, GWS and OA to force switch on next flush.

.. _`amdgpu_vm_bo_find`:

amdgpu_vm_bo_find
=================

.. c:function:: struct amdgpu_bo_va *amdgpu_vm_bo_find(struct amdgpu_vm *vm, struct amdgpu_bo *bo)

    find the bo_va for a specific vm & bo

    :param struct amdgpu_vm \*vm:
        requested vm

    :param struct amdgpu_bo \*bo:
        requested buffer object

.. _`amdgpu_vm_bo_find.description`:

Description
-----------

Find \ ``bo``\  inside the requested vm.
Search inside the \ ``bos``\  vm list for the requested vm
Returns the found bo_va or NULL if none is found

Object has to be reserved!

.. _`amdgpu_vm_update_pages`:

amdgpu_vm_update_pages
======================

.. c:function:: void amdgpu_vm_update_pages(struct amdgpu_device *adev, struct amdgpu_vm_update_params *vm_update_params, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint32_t flags)

    helper to call the right asic function

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm_update_params \*vm_update_params:
        see amdgpu_vm_update_params definition

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t addr:
        dst addr to write into pe

    :param unsigned count:
        number of page entries to update

    :param uint32_t incr:
        increase next addr by incr bytes

    :param uint32_t flags:
        hw access flags

.. _`amdgpu_vm_update_pages.description`:

Description
-----------

Traces the parameters and calls the right asic functions
to setup the page table using the DMA.

.. _`amdgpu_vm_clear_bo`:

amdgpu_vm_clear_bo
==================

.. c:function:: int amdgpu_vm_clear_bo(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_bo *bo)

    initially clear the page dir/table

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        *undescribed*

    :param struct amdgpu_bo \*bo:
        bo to clear

.. _`amdgpu_vm_clear_bo.description`:

Description
-----------

need to reserve bo first before calling it.

.. _`amdgpu_vm_map_gart`:

amdgpu_vm_map_gart
==================

.. c:function:: uint64_t amdgpu_vm_map_gart(const dma_addr_t *pages_addr, uint64_t addr)

    Resolve gart mapping of addr

    :param const dma_addr_t \*pages_addr:
        optional DMA address to use for lookup

    :param uint64_t addr:
        the unmapped addr

.. _`amdgpu_vm_map_gart.description`:

Description
-----------

Look up the physical address of the page that the pte resolves
to and return the pointer for the page table entry.

.. _`amdgpu_vm_update_page_directory`:

amdgpu_vm_update_page_directory
===============================

.. c:function:: int amdgpu_vm_update_page_directory(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    make sure that page directory is valid

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

.. _`amdgpu_vm_update_page_directory.description`:

Description
-----------

Allocates new page tables if necessary
and updates the page directory.
Returns 0 for success, error for failure.

.. _`amdgpu_vm_frag_ptes`:

amdgpu_vm_frag_ptes
===================

.. c:function:: void amdgpu_vm_frag_ptes(struct amdgpu_device *adev, struct amdgpu_vm_update_params *vm_update_params, uint64_t pe_start, uint64_t pe_end, uint64_t addr, uint32_t flags)

    add fragment information to PTEs

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm_update_params \*vm_update_params:
        see amdgpu_vm_update_params definition

    :param uint64_t pe_start:
        first PTE to handle

    :param uint64_t pe_end:
        last PTE to handle

    :param uint64_t addr:
        addr those PTEs should point to

    :param uint32_t flags:
        hw mapping flags

.. _`amdgpu_vm_update_ptes`:

amdgpu_vm_update_ptes
=====================

.. c:function:: void amdgpu_vm_update_ptes(struct amdgpu_device *adev, struct amdgpu_vm_update_params *vm_update_params, struct amdgpu_vm *vm, uint64_t start, uint64_t end, uint64_t dst, uint32_t flags)

    make sure that page tables are valid

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm_update_params \*vm_update_params:
        see amdgpu_vm_update_params definition

    :param struct amdgpu_vm \*vm:
        requested vm

    :param uint64_t start:
        start of GPU address range

    :param uint64_t end:
        end of GPU address range

    :param uint64_t dst:
        destination address to map to

    :param uint32_t flags:
        mapping flags

.. _`amdgpu_vm_update_ptes.description`:

Description
-----------

Update the page tables in the range \ ``start``\  - \ ``end``\ .

.. _`amdgpu_vm_bo_update_mapping`:

amdgpu_vm_bo_update_mapping
===========================

.. c:function:: int amdgpu_vm_bo_update_mapping(struct amdgpu_device *adev, uint64_t src, dma_addr_t *pages_addr, struct amdgpu_vm *vm, uint64_t start, uint64_t last, uint32_t flags, uint64_t addr, struct fence **fence)

    update a mapping in the vm page table

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint64_t src:
        address where to copy page table entries from

    :param dma_addr_t \*pages_addr:
        DMA addresses to use for mapping

    :param struct amdgpu_vm \*vm:
        requested vm

    :param uint64_t start:
        start of mapped range

    :param uint64_t last:
        last mapped entry

    :param uint32_t flags:
        flags for the entries

    :param uint64_t addr:
        addr to set the area to

    :param struct fence \*\*fence:
        optional resulting fence

.. _`amdgpu_vm_bo_update_mapping.description`:

Description
-----------

Fill in the page table entries between \ ``start``\  and \ ``last``\ .
Returns 0 for success, -EINVAL for failure.

.. _`amdgpu_vm_bo_split_mapping`:

amdgpu_vm_bo_split_mapping
==========================

.. c:function:: int amdgpu_vm_bo_split_mapping(struct amdgpu_device *adev, uint32_t gtt_flags, dma_addr_t *pages_addr, struct amdgpu_vm *vm, struct amdgpu_bo_va_mapping *mapping, uint32_t flags, uint64_t addr, struct fence **fence)

    split a mapping into smaller chunks

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint32_t gtt_flags:
        flags as they are used for GTT

    :param dma_addr_t \*pages_addr:
        DMA addresses to use for mapping

    :param struct amdgpu_vm \*vm:
        requested vm

    :param struct amdgpu_bo_va_mapping \*mapping:
        mapped range and flags to use for the update

    :param uint32_t flags:
        HW flags for the mapping

    :param uint64_t addr:
        addr to set the area to

    :param struct fence \*\*fence:
        optional resulting fence

.. _`amdgpu_vm_bo_split_mapping.description`:

Description
-----------

Split the mapping into smaller chunks so that each update fits
into a SDMA IB.
Returns 0 for success, -EINVAL for failure.

.. _`amdgpu_vm_bo_update`:

amdgpu_vm_bo_update
===================

.. c:function:: int amdgpu_vm_bo_update(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, struct ttm_mem_reg *mem)

    update all BO mappings in the vm page table

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_bo_va \*bo_va:
        requested BO and VM object

    :param struct ttm_mem_reg \*mem:
        ttm mem

.. _`amdgpu_vm_bo_update.description`:

Description
-----------

Fill in the page table entries for \ ``bo_va``\ .
Returns 0 for success, -EINVAL for failure.

Object have to be reserved and mutex must be locked!

.. _`amdgpu_vm_clear_freed`:

amdgpu_vm_clear_freed
=====================

.. c:function:: int amdgpu_vm_clear_freed(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    clear freed BOs in the PT

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

.. _`amdgpu_vm_clear_freed.description`:

Description
-----------

Make sure all freed BOs are cleared in the PT.
Returns 0 for success.

PTs have to be reserved and mutex must be locked!

.. _`amdgpu_vm_clear_invalids`:

amdgpu_vm_clear_invalids
========================

.. c:function:: int amdgpu_vm_clear_invalids(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_sync *sync)

    clear invalidated BOs in the PT

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

    :param struct amdgpu_sync \*sync:
        *undescribed*

.. _`amdgpu_vm_clear_invalids.description`:

Description
-----------

Make sure all invalidated BOs are cleared in the PT.
Returns 0 for success.

PTs have to be reserved and mutex must be locked!

.. _`amdgpu_vm_bo_add`:

amdgpu_vm_bo_add
================

.. c:function:: struct amdgpu_bo_va *amdgpu_vm_bo_add(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_bo *bo)

    add a bo to a specific vm

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

    :param struct amdgpu_bo \*bo:
        amdgpu buffer object

.. _`amdgpu_vm_bo_add.description`:

Description
-----------

Add \ ``bo``\  into the requested vm.
Add \ ``bo``\  to the list of bos associated with the vm
Returns newly added bo_va or NULL for failure

Object has to be reserved!

.. _`amdgpu_vm_bo_map`:

amdgpu_vm_bo_map
================

.. c:function:: int amdgpu_vm_bo_map(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, uint64_t saddr, uint64_t offset, uint64_t size, uint32_t flags)

    map bo inside a vm

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_bo_va \*bo_va:
        bo_va to store the address

    :param uint64_t saddr:
        where to map the BO

    :param uint64_t offset:
        requested offset in the BO

    :param uint64_t size:
        *undescribed*

    :param uint32_t flags:
        attributes of pages (read/write/valid/etc.)

.. _`amdgpu_vm_bo_map.description`:

Description
-----------

Add a mapping of the BO at the specefied addr into the VM.
Returns 0 for success, error for failure.

Object has to be reserved and unreserved outside!

.. _`amdgpu_vm_bo_unmap`:

amdgpu_vm_bo_unmap
==================

.. c:function:: int amdgpu_vm_bo_unmap(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, uint64_t saddr)

    remove bo mapping from vm

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_bo_va \*bo_va:
        bo_va to remove the address from

    :param uint64_t saddr:
        where to the BO is mapped

.. _`amdgpu_vm_bo_unmap.description`:

Description
-----------

Remove a mapping of the BO at the specefied addr from the VM.
Returns 0 for success, error for failure.

Object has to be reserved and unreserved outside!

.. _`amdgpu_vm_bo_rmv`:

amdgpu_vm_bo_rmv
================

.. c:function:: void amdgpu_vm_bo_rmv(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va)

    remove a bo to a specific vm

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_bo_va \*bo_va:
        requested bo_va

.. _`amdgpu_vm_bo_rmv.description`:

Description
-----------

Remove \ ``bo_va``\ ->bo from the requested vm.

Object have to be reserved!

.. _`amdgpu_vm_bo_invalidate`:

amdgpu_vm_bo_invalidate
=======================

.. c:function:: void amdgpu_vm_bo_invalidate(struct amdgpu_device *adev, struct amdgpu_bo *bo)

    mark the bo as invalid

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_bo \*bo:
        amdgpu buffer object

.. _`amdgpu_vm_bo_invalidate.description`:

Description
-----------

Mark \ ``bo``\  as invalid.

.. _`amdgpu_vm_init`:

amdgpu_vm_init
==============

.. c:function:: int amdgpu_vm_init(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    initialize a vm instance

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

.. _`amdgpu_vm_init.description`:

Description
-----------

Init \ ``vm``\  fields.

.. _`amdgpu_vm_fini`:

amdgpu_vm_fini
==============

.. c:function:: void amdgpu_vm_fini(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    tear down a vm instance

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

.. _`amdgpu_vm_fini.description`:

Description
-----------

Tear down \ ``vm``\ .
Unbind the VM and remove all bos from the vm bo list

.. _`amdgpu_vm_manager_init`:

amdgpu_vm_manager_init
======================

.. c:function:: void amdgpu_vm_manager_init(struct amdgpu_device *adev)

    init the VM manager

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_vm_manager_init.description`:

Description
-----------

Initialize the VM manager structures

.. _`amdgpu_vm_manager_fini`:

amdgpu_vm_manager_fini
======================

.. c:function:: void amdgpu_vm_manager_fini(struct amdgpu_device *adev)

    cleanup VM manager

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_vm_manager_fini.description`:

Description
-----------

Cleanup the VM manager and free resources.

.. This file was automatic generated / don't edit.

