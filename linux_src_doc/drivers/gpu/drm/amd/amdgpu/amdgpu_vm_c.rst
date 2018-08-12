.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_vm.c

.. _`amdgpu_vm_level_shift`:

amdgpu_vm_level_shift
=====================

.. c:function:: unsigned amdgpu_vm_level_shift(struct amdgpu_device *adev, unsigned level)

    return the addr shift for each level

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param unsigned level:
        *undescribed*

.. _`amdgpu_vm_level_shift.description`:

Description
-----------

Returns the number of bits the pfn needs to be right shifted for a level.

.. _`amdgpu_vm_num_entries`:

amdgpu_vm_num_entries
=====================

.. c:function:: unsigned amdgpu_vm_num_entries(struct amdgpu_device *adev, unsigned level)

    return the number of entries in a PD/PT

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param unsigned level:
        *undescribed*

.. _`amdgpu_vm_num_entries.description`:

Description
-----------

Calculate the number of entries in a page directory or page table.

.. _`amdgpu_vm_bo_size`:

amdgpu_vm_bo_size
=================

.. c:function:: unsigned amdgpu_vm_bo_size(struct amdgpu_device *adev, unsigned level)

    returns the size of the BOs in bytes

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param unsigned level:
        *undescribed*

.. _`amdgpu_vm_bo_size.description`:

Description
-----------

Calculate the size of the BO for a page directory or page table in bytes.

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

.. _`amdgpu_vm_validate_pt_bos`:

amdgpu_vm_validate_pt_bos
=========================

.. c:function:: int amdgpu_vm_validate_pt_bos(struct amdgpu_device *adev, struct amdgpu_vm *vm, int (*validate)(void *p, struct amdgpu_bo *bo), void *param)

    validate the page table BOs

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

    :param struct amdgpu_vm \*vm:
        vm providing the BOs

    :param int (\*validate)(void \*p, struct amdgpu_bo \*bo):
        callback to do the validation

    :param void \*param:
        parameter for the validation callback

.. _`amdgpu_vm_validate_pt_bos.description`:

Description
-----------

Validate the page table BOs on command submission if neccessary.

.. _`amdgpu_vm_ready`:

amdgpu_vm_ready
===============

.. c:function:: bool amdgpu_vm_ready(struct amdgpu_vm *vm)

    check VM is ready for updates

    :param struct amdgpu_vm \*vm:
        VM to check

.. _`amdgpu_vm_ready.description`:

Description
-----------

Check if all VM PDs/PTs are ready for updates

.. _`amdgpu_vm_clear_bo`:

amdgpu_vm_clear_bo
==================

.. c:function:: int amdgpu_vm_clear_bo(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_bo *bo, unsigned level, bool pte_support_ats)

    initially clear the PDs/PTs

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        *undescribed*

    :param struct amdgpu_bo \*bo:
        BO to clear

    :param unsigned level:
        level this BO is at

    :param bool pte_support_ats:
        *undescribed*

.. _`amdgpu_vm_clear_bo.description`:

Description
-----------

Root PD needs to be reserved when calling this.

.. _`amdgpu_vm_alloc_levels`:

amdgpu_vm_alloc_levels
======================

.. c:function:: int amdgpu_vm_alloc_levels(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_vm_pt *parent, uint64_t saddr, uint64_t eaddr, unsigned level, bool ats)

    allocate the PD/PT levels

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

    :param struct amdgpu_vm_pt \*parent:
        *undescribed*

    :param uint64_t saddr:
        start of the address range

    :param uint64_t eaddr:
        end of the address range

    :param unsigned level:
        *undescribed*

    :param bool ats:
        *undescribed*

.. _`amdgpu_vm_alloc_levels.description`:

Description
-----------

Make sure the page directories and page tables are allocated

.. _`amdgpu_vm_alloc_pts`:

amdgpu_vm_alloc_pts
===================

.. c:function:: int amdgpu_vm_alloc_pts(struct amdgpu_device *adev, struct amdgpu_vm *vm, uint64_t saddr, uint64_t size)

    Allocate page tables.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        VM to allocate page tables for

    :param uint64_t saddr:
        Start address which needs to be allocated

    :param uint64_t size:
        Size from start address we need.

.. _`amdgpu_vm_alloc_pts.description`:

Description
-----------

Make sure the page tables are allocated.

.. _`amdgpu_vm_check_compute_bug`:

amdgpu_vm_check_compute_bug
===========================

.. c:function:: void amdgpu_vm_check_compute_bug(struct amdgpu_device *adev)

    check whether asic has compute vm bug

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`amdgpu_vm_flush`:

amdgpu_vm_flush
===============

.. c:function:: int amdgpu_vm_flush(struct amdgpu_ring *ring, struct amdgpu_job *job, bool need_pipe_sync)

    hardware flush the vm

    :param struct amdgpu_ring \*ring:
        ring to use for flush

    :param struct amdgpu_job \*job:
        *undescribed*

    :param bool need_pipe_sync:
        *undescribed*

.. _`amdgpu_vm_flush.description`:

Description
-----------

Emit a VM flush when it is necessary.

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

.. _`amdgpu_vm_do_set_ptes`:

amdgpu_vm_do_set_ptes
=====================

.. c:function:: void amdgpu_vm_do_set_ptes(struct amdgpu_pte_update_params *params, struct amdgpu_bo *bo, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint64_t flags)

    helper to call the right asic function

    :param struct amdgpu_pte_update_params \*params:
        see amdgpu_pte_update_params definition

    :param struct amdgpu_bo \*bo:
        PD/PT to update

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t addr:
        dst addr to write into pe

    :param unsigned count:
        number of page entries to update

    :param uint32_t incr:
        increase next addr by incr bytes

    :param uint64_t flags:
        hw access flags

.. _`amdgpu_vm_do_set_ptes.description`:

Description
-----------

Traces the parameters and calls the right asic functions
to setup the page table using the DMA.

.. _`amdgpu_vm_do_copy_ptes`:

amdgpu_vm_do_copy_ptes
======================

.. c:function:: void amdgpu_vm_do_copy_ptes(struct amdgpu_pte_update_params *params, struct amdgpu_bo *bo, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint64_t flags)

    copy the PTEs from the GART

    :param struct amdgpu_pte_update_params \*params:
        see amdgpu_pte_update_params definition

    :param struct amdgpu_bo \*bo:
        PD/PT to update

    :param uint64_t pe:
        addr of the page entry

    :param uint64_t addr:
        dst addr to write into pe

    :param unsigned count:
        number of page entries to update

    :param uint32_t incr:
        increase next addr by incr bytes

    :param uint64_t flags:
        hw access flags

.. _`amdgpu_vm_do_copy_ptes.description`:

Description
-----------

Traces the parameters and calls the DMA function to copy the PTEs.

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

.. _`amdgpu_vm_cpu_set_ptes`:

amdgpu_vm_cpu_set_ptes
======================

.. c:function:: void amdgpu_vm_cpu_set_ptes(struct amdgpu_pte_update_params *params, struct amdgpu_bo *bo, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint64_t flags)

    helper to update page tables via CPU

    :param struct amdgpu_pte_update_params \*params:
        see amdgpu_pte_update_params definition

    :param struct amdgpu_bo \*bo:
        PD/PT to update

    :param uint64_t pe:
        kmap addr of the page entry

    :param uint64_t addr:
        dst addr to write into pe

    :param unsigned count:
        number of page entries to update

    :param uint32_t incr:
        increase next addr by incr bytes

    :param uint64_t flags:
        hw access flags

.. _`amdgpu_vm_cpu_set_ptes.description`:

Description
-----------

Write count number of PT/PD entries directly.

.. _`amdgpu_vm_get_entry`:

amdgpu_vm_get_entry
===================

.. c:function:: void amdgpu_vm_get_entry(struct amdgpu_pte_update_params *p, uint64_t addr, struct amdgpu_vm_pt **entry, struct amdgpu_vm_pt **parent)

    find the entry for an address

    :param struct amdgpu_pte_update_params \*p:
        see amdgpu_pte_update_params definition

    :param uint64_t addr:
        virtual address in question

    :param struct amdgpu_vm_pt \*\*entry:
        resulting entry or NULL

    :param struct amdgpu_vm_pt \*\*parent:
        parent entry

.. _`amdgpu_vm_get_entry.description`:

Description
-----------

Find the vm_pt entry and it's parent for the given address.

.. _`amdgpu_vm_handle_huge_pages`:

amdgpu_vm_handle_huge_pages
===========================

.. c:function:: void amdgpu_vm_handle_huge_pages(struct amdgpu_pte_update_params *p, struct amdgpu_vm_pt *entry, struct amdgpu_vm_pt *parent, unsigned nptes, uint64_t dst, uint64_t flags)

    handle updating the PD with huge pages

    :param struct amdgpu_pte_update_params \*p:
        see amdgpu_pte_update_params definition

    :param struct amdgpu_vm_pt \*entry:
        vm_pt entry to check

    :param struct amdgpu_vm_pt \*parent:
        parent entry

    :param unsigned nptes:
        number of PTEs updated with this operation

    :param uint64_t dst:
        destination address where the PTEs should point to

    :param uint64_t flags:
        access flags fro the PTEs

.. _`amdgpu_vm_handle_huge_pages.description`:

Description
-----------

Check if we can update the PD with a huge page.

.. _`amdgpu_vm_update_ptes`:

amdgpu_vm_update_ptes
=====================

.. c:function:: int amdgpu_vm_update_ptes(struct amdgpu_pte_update_params *params, uint64_t start, uint64_t end, uint64_t dst, uint64_t flags)

    make sure that page tables are valid

    :param struct amdgpu_pte_update_params \*params:
        see amdgpu_pte_update_params definition

    :param uint64_t start:
        start of GPU address range

    :param uint64_t end:
        end of GPU address range

    :param uint64_t dst:
        destination address to map to, the next dst inside the function

    :param uint64_t flags:
        mapping flags

.. _`amdgpu_vm_update_ptes.description`:

Description
-----------

Update the page tables in the range \ ``start``\  - \ ``end``\ .
Returns 0 for success, -EINVAL for failure.

.. _`amdgpu_vm_bo_update_mapping`:

amdgpu_vm_bo_update_mapping
===========================

.. c:function:: int amdgpu_vm_bo_update_mapping(struct amdgpu_device *adev, struct dma_fence *exclusive, dma_addr_t *pages_addr, struct amdgpu_vm *vm, uint64_t start, uint64_t last, uint64_t flags, uint64_t addr, struct dma_fence **fence)

    update a mapping in the vm page table

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct dma_fence \*exclusive:
        fence we need to sync to

    :param dma_addr_t \*pages_addr:
        DMA addresses to use for mapping

    :param struct amdgpu_vm \*vm:
        requested vm

    :param uint64_t start:
        start of mapped range

    :param uint64_t last:
        last mapped entry

    :param uint64_t flags:
        flags for the entries

    :param uint64_t addr:
        addr to set the area to

    :param struct dma_fence \*\*fence:
        optional resulting fence

.. _`amdgpu_vm_bo_update_mapping.description`:

Description
-----------

Fill in the page table entries between \ ``start``\  and \ ``last``\ .
Returns 0 for success, -EINVAL for failure.

.. _`amdgpu_vm_bo_split_mapping`:

amdgpu_vm_bo_split_mapping
==========================

.. c:function:: int amdgpu_vm_bo_split_mapping(struct amdgpu_device *adev, struct dma_fence *exclusive, dma_addr_t *pages_addr, struct amdgpu_vm *vm, struct amdgpu_bo_va_mapping *mapping, uint64_t flags, struct drm_mm_node *nodes, struct dma_fence **fence)

    split a mapping into smaller chunks

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct dma_fence \*exclusive:
        fence we need to sync to

    :param dma_addr_t \*pages_addr:
        DMA addresses to use for mapping

    :param struct amdgpu_vm \*vm:
        requested vm

    :param struct amdgpu_bo_va_mapping \*mapping:
        mapped range and flags to use for the update

    :param uint64_t flags:
        HW flags for the mapping

    :param struct drm_mm_node \*nodes:
        array of drm_mm_nodes with the MC addresses

    :param struct dma_fence \*\*fence:
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

.. c:function:: int amdgpu_vm_bo_update(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, bool clear)

    update all BO mappings in the vm page table

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_bo_va \*bo_va:
        requested BO and VM object

    :param bool clear:
        if true clear the entries

.. _`amdgpu_vm_bo_update.description`:

Description
-----------

Fill in the page table entries for \ ``bo_va``\ .
Returns 0 for success, -EINVAL for failure.

.. _`amdgpu_vm_update_prt_state`:

amdgpu_vm_update_prt_state
==========================

.. c:function:: void amdgpu_vm_update_prt_state(struct amdgpu_device *adev)

    update the global PRT state

    :param struct amdgpu_device \*adev:
        *undescribed*

.. _`amdgpu_vm_prt_get`:

amdgpu_vm_prt_get
=================

.. c:function:: void amdgpu_vm_prt_get(struct amdgpu_device *adev)

    add a PRT user

    :param struct amdgpu_device \*adev:
        *undescribed*

.. _`amdgpu_vm_prt_put`:

amdgpu_vm_prt_put
=================

.. c:function:: void amdgpu_vm_prt_put(struct amdgpu_device *adev)

    drop a PRT user

    :param struct amdgpu_device \*adev:
        *undescribed*

.. _`amdgpu_vm_prt_cb`:

amdgpu_vm_prt_cb
================

.. c:function:: void amdgpu_vm_prt_cb(struct dma_fence *fence, struct dma_fence_cb *_cb)

    callback for updating the PRT status

    :param struct dma_fence \*fence:
        *undescribed*

    :param struct dma_fence_cb \*_cb:
        *undescribed*

.. _`amdgpu_vm_add_prt_cb`:

amdgpu_vm_add_prt_cb
====================

.. c:function:: void amdgpu_vm_add_prt_cb(struct amdgpu_device *adev, struct dma_fence *fence)

    add callback for updating the PRT status

    :param struct amdgpu_device \*adev:
        *undescribed*

    :param struct dma_fence \*fence:
        *undescribed*

.. _`amdgpu_vm_free_mapping`:

amdgpu_vm_free_mapping
======================

.. c:function:: void amdgpu_vm_free_mapping(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_bo_va_mapping *mapping, struct dma_fence *fence)

    free a mapping

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

    :param struct amdgpu_bo_va_mapping \*mapping:
        mapping to be freed

    :param struct dma_fence \*fence:
        fence of the unmap operation

.. _`amdgpu_vm_free_mapping.description`:

Description
-----------

Free a mapping and make sure we decrease the PRT usage count if applicable.

.. _`amdgpu_vm_prt_fini`:

amdgpu_vm_prt_fini
==================

.. c:function:: void amdgpu_vm_prt_fini(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    finish all prt mappings

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

.. _`amdgpu_vm_prt_fini.description`:

Description
-----------

Register a cleanup callback to disable PRT support after VM dies.

.. _`amdgpu_vm_clear_freed`:

amdgpu_vm_clear_freed
=====================

.. c:function:: int amdgpu_vm_clear_freed(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct dma_fence **fence)

    clear freed BOs in the PT

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

    :param struct dma_fence \*\*fence:
        optional resulting fence (unchanged if no work needed to be done
        or if an error occurred)

.. _`amdgpu_vm_clear_freed.description`:

Description
-----------

Make sure all freed BOs are cleared in the PT.
Returns 0 for success.

PTs have to be reserved and mutex must be locked!

.. _`amdgpu_vm_handle_moved`:

amdgpu_vm_handle_moved
======================

.. c:function:: int amdgpu_vm_handle_moved(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    handle moved BOs in the PT

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

.. _`amdgpu_vm_handle_moved.description`:

Description
-----------

Make sure all BOs which are moved are updated in the PTs.
Returns 0 for success.

PTs have to be reserved!

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

.. _`amdgpu_vm_bo_insert_map`:

amdgpu_vm_bo_insert_map
=======================

.. c:function:: void amdgpu_vm_bo_insert_map(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, struct amdgpu_bo_va_mapping *mapping)

    insert a new mapping

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_bo_va \*bo_va:
        bo_va to store the address

    :param struct amdgpu_bo_va_mapping \*mapping:
        the mapping to insert

.. _`amdgpu_vm_bo_insert_map.description`:

Description
-----------

Insert a new mapping into all structures.

.. _`amdgpu_vm_bo_map`:

amdgpu_vm_bo_map
================

.. c:function:: int amdgpu_vm_bo_map(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, uint64_t saddr, uint64_t offset, uint64_t size, uint64_t flags)

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

    :param uint64_t flags:
        attributes of pages (read/write/valid/etc.)

.. _`amdgpu_vm_bo_map.description`:

Description
-----------

Add a mapping of the BO at the specefied addr into the VM.
Returns 0 for success, error for failure.

Object has to be reserved and unreserved outside!

.. _`amdgpu_vm_bo_replace_map`:

amdgpu_vm_bo_replace_map
========================

.. c:function:: int amdgpu_vm_bo_replace_map(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, uint64_t saddr, uint64_t offset, uint64_t size, uint64_t flags)

    map bo inside a vm, replacing existing mappings

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

    :param uint64_t flags:
        attributes of pages (read/write/valid/etc.)

.. _`amdgpu_vm_bo_replace_map.description`:

Description
-----------

Add a mapping of the BO at the specefied addr into the VM. Replace existing
mappings as we do so.
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

.. _`amdgpu_vm_bo_clear_mappings`:

amdgpu_vm_bo_clear_mappings
===========================

.. c:function:: int amdgpu_vm_bo_clear_mappings(struct amdgpu_device *adev, struct amdgpu_vm *vm, uint64_t saddr, uint64_t size)

    remove all mappings in a specific range

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        VM structure to use

    :param uint64_t saddr:
        start of the range

    :param uint64_t size:
        size of the range

.. _`amdgpu_vm_bo_clear_mappings.description`:

Description
-----------

Remove all mappings in a range, split them as appropriate.
Returns 0 for success, error for failure.

.. _`amdgpu_vm_bo_lookup_mapping`:

amdgpu_vm_bo_lookup_mapping
===========================

.. c:function:: struct amdgpu_bo_va_mapping *amdgpu_vm_bo_lookup_mapping(struct amdgpu_vm *vm, uint64_t addr)

    find mapping by address

    :param struct amdgpu_vm \*vm:
        the requested VM

    :param uint64_t addr:
        *undescribed*

.. _`amdgpu_vm_bo_lookup_mapping.description`:

Description
-----------

Find a mapping by it's address.

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

.. c:function:: void amdgpu_vm_bo_invalidate(struct amdgpu_device *adev, struct amdgpu_bo *bo, bool evicted)

    mark the bo as invalid

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_bo \*bo:
        amdgpu buffer object

    :param bool evicted:
        *undescribed*

.. _`amdgpu_vm_bo_invalidate.description`:

Description
-----------

Mark \ ``bo``\  as invalid.

.. _`amdgpu_vm_adjust_size`:

amdgpu_vm_adjust_size
=====================

.. c:function:: void amdgpu_vm_adjust_size(struct amdgpu_device *adev, uint32_t vm_size, uint32_t fragment_size_default, unsigned max_level, unsigned max_bits)

    adjust vm size, block size and fragment size

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param uint32_t vm_size:
        the default vm size if it's set auto

    :param uint32_t fragment_size_default:
        *undescribed*

    :param unsigned max_level:
        *undescribed*

    :param unsigned max_bits:
        *undescribed*

.. _`amdgpu_vm_init`:

amdgpu_vm_init
==============

.. c:function:: int amdgpu_vm_init(struct amdgpu_device *adev, struct amdgpu_vm *vm, int vm_context, unsigned int pasid)

    initialize a vm instance

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_vm \*vm:
        requested vm

    :param int vm_context:
        Indicates if it GFX or Compute context

    :param unsigned int pasid:
        *undescribed*

.. _`amdgpu_vm_init.description`:

Description
-----------

Init \ ``vm``\  fields.

.. _`amdgpu_vm_make_compute`:

amdgpu_vm_make_compute
======================

.. c:function:: int amdgpu_vm_make_compute(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    Turn a GFX VM into a compute VM

    :param struct amdgpu_device \*adev:
        *undescribed*

    :param struct amdgpu_vm \*vm:
        *undescribed*

.. _`amdgpu_vm_make_compute.description`:

Description
-----------

This only works on GFX VMs that don't have any BOs added and no
page tables allocated yet.

.. _`amdgpu_vm_make_compute.changes-the-following-vm-parameters`:

Changes the following VM parameters
-----------------------------------

- use_cpu_for_update
- pte_supports_ats
- pasid (old PASID is released, because compute manages its own PASIDs)

Reinitializes the page directory to reflect the changed ATS
setting. May leave behind an unused shadow BO for the page
directory when switching from SDMA updates to CPU updates.

Returns 0 for success, -errno for errors.

.. _`amdgpu_vm_free_levels`:

amdgpu_vm_free_levels
=====================

.. c:function:: void amdgpu_vm_free_levels(struct amdgpu_device *adev, struct amdgpu_vm_pt *parent, unsigned level)

    free PD/PT levels

    :param struct amdgpu_device \*adev:
        amdgpu device structure

    :param struct amdgpu_vm_pt \*parent:
        PD/PT starting level to free

    :param unsigned level:
        level of parent structure

.. _`amdgpu_vm_free_levels.description`:

Description
-----------

Free the page directory or page table level and all sub levels.

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

.. _`amdgpu_vm_pasid_fault_credit`:

amdgpu_vm_pasid_fault_credit
============================

.. c:function:: bool amdgpu_vm_pasid_fault_credit(struct amdgpu_device *adev, unsigned int pasid)

    Check fault credit for given PASID

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param unsigned int pasid:
        PASID do identify the VM

.. _`amdgpu_vm_pasid_fault_credit.description`:

Description
-----------

This function is expected to be called in interrupt context. Returns
true if there was fault credit, false otherwise

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

