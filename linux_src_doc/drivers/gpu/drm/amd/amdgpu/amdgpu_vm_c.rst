.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_vm.c

.. _`gpuvm`:

GPUVM
=====

GPUVM is similar to the legacy gart on older asics, however
rather than there being a single global gart table
for the entire GPU, there are multiple VM page tables active
at any given time.  The VM page tables can contain a mix
vram pages and system memory pages and system memory pages
can be mapped as snooped (cached system pages) or unsnooped
(uncached system pages).
Each VM has an ID associated with it and there is a page table
associated with each VMID.  When execting a command buffer,
the kernel tells the the ring what VMID to use for that command
buffer.  VMIDs are allocated dynamically as commands are submitted.
The userspace drivers maintain their own address space and the kernel
sets up their pages tables accordingly when they submit their
command buffers and a VMID is assigned.
Cayman/Trinity support up to 8 active VMs at any given time;
SI supports 16.

.. _`amdgpu_pte_update_params`:

struct amdgpu_pte_update_params
===============================

.. c:type:: struct amdgpu_pte_update_params

    Local structure

.. _`amdgpu_pte_update_params.definition`:

Definition
----------

.. code-block:: c

    struct amdgpu_pte_update_params {
        struct amdgpu_device *adev;
        struct amdgpu_vm *vm;
        uint64_t src;
        struct amdgpu_ib *ib;
        void (*func)(struct amdgpu_pte_update_params *params,struct amdgpu_bo *bo, uint64_t pe,uint64_t addr, unsigned count, uint32_t incr, uint64_t flags);
        dma_addr_t *pages_addr;
        void *kptr;
    }

.. _`amdgpu_pte_update_params.members`:

Members
-------

adev
    amdgpu device we do this update for

vm
    optional amdgpu_vm we do this update for

src
    address where to copy page table entries from

ib
    indirect buffer to fill with commands

func
    Function which actually does the update

pages_addr

    DMA addresses to use for mapping, used during VM update by CPU

kptr

    Kernel pointer of PD/PT BO that needs to be updated,
    used during VM update by CPU

.. _`amdgpu_pte_update_params.description`:

Description
-----------

Encapsulate some VM table update parameters to reduce
the number of function parameters

.. _`amdgpu_prt_cb`:

struct amdgpu_prt_cb
====================

.. c:type:: struct amdgpu_prt_cb

    Helper to disable partial resident texture feature from a fence callback

.. _`amdgpu_prt_cb.definition`:

Definition
----------

.. code-block:: c

    struct amdgpu_prt_cb {
        struct amdgpu_device *adev;
        struct dma_fence_cb cb;
    }

.. _`amdgpu_prt_cb.members`:

Members
-------

adev
    amdgpu device

cb
    callback

.. _`amdgpu_vm_level_shift`:

amdgpu_vm_level_shift
=====================

.. c:function:: unsigned amdgpu_vm_level_shift(struct amdgpu_device *adev, unsigned level)

    return the addr shift for each level

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param level:
        VMPT level
    :type level: unsigned

.. _`amdgpu_vm_level_shift.return`:

Return
------

The number of bits the pfn needs to be right shifted for a level.

.. _`amdgpu_vm_num_entries`:

amdgpu_vm_num_entries
=====================

.. c:function:: unsigned amdgpu_vm_num_entries(struct amdgpu_device *adev, unsigned level)

    return the number of entries in a PD/PT

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param level:
        VMPT level
    :type level: unsigned

.. _`amdgpu_vm_num_entries.return`:

Return
------

The number of entries in a page directory or page table.

.. _`amdgpu_vm_entries_mask`:

amdgpu_vm_entries_mask
======================

.. c:function:: uint32_t amdgpu_vm_entries_mask(struct amdgpu_device *adev, unsigned int level)

    the mask to get the entry number of a PD/PT

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param level:
        VMPT level
    :type level: unsigned int

.. _`amdgpu_vm_entries_mask.return`:

Return
------

The mask to extract the entry number of a PD/PT from an address.

.. _`amdgpu_vm_bo_size`:

amdgpu_vm_bo_size
=================

.. c:function:: unsigned amdgpu_vm_bo_size(struct amdgpu_device *adev, unsigned level)

    returns the size of the BOs in bytes

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param level:
        VMPT level
    :type level: unsigned

.. _`amdgpu_vm_bo_size.return`:

Return
------

The size of the BO for a page directory or page table in bytes.

.. _`amdgpu_vm_bo_evicted`:

amdgpu_vm_bo_evicted
====================

.. c:function:: void amdgpu_vm_bo_evicted(struct amdgpu_vm_bo_base *vm_bo)

    vm_bo is evicted

    :param vm_bo:
        vm_bo which is evicted
    :type vm_bo: struct amdgpu_vm_bo_base \*

.. _`amdgpu_vm_bo_evicted.description`:

Description
-----------

State for PDs/PTs and per VM BOs which are not at the location they should
be.

.. _`amdgpu_vm_bo_relocated`:

amdgpu_vm_bo_relocated
======================

.. c:function:: void amdgpu_vm_bo_relocated(struct amdgpu_vm_bo_base *vm_bo)

    vm_bo is reloacted

    :param vm_bo:
        vm_bo which is relocated
    :type vm_bo: struct amdgpu_vm_bo_base \*

.. _`amdgpu_vm_bo_relocated.description`:

Description
-----------

State for PDs/PTs which needs to update their parent PD.

.. _`amdgpu_vm_bo_moved`:

amdgpu_vm_bo_moved
==================

.. c:function:: void amdgpu_vm_bo_moved(struct amdgpu_vm_bo_base *vm_bo)

    vm_bo is moved

    :param vm_bo:
        vm_bo which is moved
    :type vm_bo: struct amdgpu_vm_bo_base \*

.. _`amdgpu_vm_bo_moved.description`:

Description
-----------

State for per VM BOs which are moved, but that change is not yet reflected
in the page tables.

.. _`amdgpu_vm_bo_idle`:

amdgpu_vm_bo_idle
=================

.. c:function:: void amdgpu_vm_bo_idle(struct amdgpu_vm_bo_base *vm_bo)

    vm_bo is idle

    :param vm_bo:
        vm_bo which is now idle
    :type vm_bo: struct amdgpu_vm_bo_base \*

.. _`amdgpu_vm_bo_idle.description`:

Description
-----------

State for PDs/PTs and per VM BOs which have gone through the state machine
and are now idle.

.. _`amdgpu_vm_bo_invalidated`:

amdgpu_vm_bo_invalidated
========================

.. c:function:: void amdgpu_vm_bo_invalidated(struct amdgpu_vm_bo_base *vm_bo)

    vm_bo is invalidated

    :param vm_bo:
        vm_bo which is now invalidated
    :type vm_bo: struct amdgpu_vm_bo_base \*

.. _`amdgpu_vm_bo_invalidated.description`:

Description
-----------

State for normal BOs which are invalidated and that change not yet reflected
in the PTs.

.. _`amdgpu_vm_bo_done`:

amdgpu_vm_bo_done
=================

.. c:function:: void amdgpu_vm_bo_done(struct amdgpu_vm_bo_base *vm_bo)

    vm_bo is done

    :param vm_bo:
        vm_bo which is now done
    :type vm_bo: struct amdgpu_vm_bo_base \*

.. _`amdgpu_vm_bo_done.description`:

Description
-----------

State for normal BOs which are invalidated and that change has been updated
in the PTs.

.. _`amdgpu_vm_bo_base_init`:

amdgpu_vm_bo_base_init
======================

.. c:function:: void amdgpu_vm_bo_base_init(struct amdgpu_vm_bo_base *base, struct amdgpu_vm *vm, struct amdgpu_bo *bo)

    Adds bo to the list of bos associated with the vm

    :param base:
        base structure for tracking BO usage in a VM
    :type base: struct amdgpu_vm_bo_base \*

    :param vm:
        vm to which bo is to be added
    :type vm: struct amdgpu_vm \*

    :param bo:
        amdgpu buffer object
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_vm_bo_base_init.description`:

Description
-----------

Initialize a bo_va_base structure and add it to the appropriate lists

.. _`amdgpu_vm_pt_parent`:

amdgpu_vm_pt_parent
===================

.. c:function:: struct amdgpu_vm_pt *amdgpu_vm_pt_parent(struct amdgpu_vm_pt *pt)

    get the parent page directory

    :param pt:
        child page table
    :type pt: struct amdgpu_vm_pt \*

.. _`amdgpu_vm_pt_parent.description`:

Description
-----------

Helper to get the parent entry for the child page table. NULL if we are at
the root page directory.

.. _`amdgpu_vm_pt_start`:

amdgpu_vm_pt_start
==================

.. c:function:: void amdgpu_vm_pt_start(struct amdgpu_device *adev, struct amdgpu_vm *vm, uint64_t start, struct amdgpu_vm_pt_cursor *cursor)

    start PD/PT walk

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        amdgpu_vm structure
    :type vm: struct amdgpu_vm \*

    :param start:
        start address of the walk
    :type start: uint64_t

    :param cursor:
        state to initialize
    :type cursor: struct amdgpu_vm_pt_cursor \*

.. _`amdgpu_vm_pt_start.description`:

Description
-----------

Initialize a amdgpu_vm_pt_cursor to start a walk.

.. _`amdgpu_vm_pt_descendant`:

amdgpu_vm_pt_descendant
=======================

.. c:function:: bool amdgpu_vm_pt_descendant(struct amdgpu_device *adev, struct amdgpu_vm_pt_cursor *cursor)

    go to child node

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param cursor:
        current state
    :type cursor: struct amdgpu_vm_pt_cursor \*

.. _`amdgpu_vm_pt_descendant.description`:

Description
-----------

Walk to the child node of the current node.

.. _`amdgpu_vm_pt_descendant.return`:

Return
------

True if the walk was possible, false otherwise.

.. _`amdgpu_vm_pt_sibling`:

amdgpu_vm_pt_sibling
====================

.. c:function:: bool amdgpu_vm_pt_sibling(struct amdgpu_device *adev, struct amdgpu_vm_pt_cursor *cursor)

    go to sibling node

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param cursor:
        current state
    :type cursor: struct amdgpu_vm_pt_cursor \*

.. _`amdgpu_vm_pt_sibling.description`:

Description
-----------

Walk to the sibling node of the current node.

.. _`amdgpu_vm_pt_sibling.return`:

Return
------

True if the walk was possible, false otherwise.

.. _`amdgpu_vm_pt_ancestor`:

amdgpu_vm_pt_ancestor
=====================

.. c:function:: bool amdgpu_vm_pt_ancestor(struct amdgpu_vm_pt_cursor *cursor)

    go to parent node

    :param cursor:
        current state
    :type cursor: struct amdgpu_vm_pt_cursor \*

.. _`amdgpu_vm_pt_ancestor.description`:

Description
-----------

Walk to the parent node of the current node.

.. _`amdgpu_vm_pt_ancestor.return`:

Return
------

True if the walk was possible, false otherwise.

.. _`amdgpu_vm_pt_next`:

amdgpu_vm_pt_next
=================

.. c:function:: void amdgpu_vm_pt_next(struct amdgpu_device *adev, struct amdgpu_vm_pt_cursor *cursor)

    get next PD/PT in hieratchy

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param cursor:
        current state
    :type cursor: struct amdgpu_vm_pt_cursor \*

.. _`amdgpu_vm_pt_next.description`:

Description
-----------

Walk the PD/PT tree to the next node.

.. _`amdgpu_vm_pt_first_leaf`:

amdgpu_vm_pt_first_leaf
=======================

.. c:function:: void amdgpu_vm_pt_first_leaf(struct amdgpu_device *adev, struct amdgpu_vm *vm, uint64_t start, struct amdgpu_vm_pt_cursor *cursor)

    get first leaf PD/PT

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        amdgpu_vm structure
    :type vm: struct amdgpu_vm \*

    :param start:
        start addr of the walk
    :type start: uint64_t

    :param cursor:
        state to initialize
    :type cursor: struct amdgpu_vm_pt_cursor \*

.. _`amdgpu_vm_pt_first_leaf.description`:

Description
-----------

Start a walk and go directly to the leaf node.

.. _`amdgpu_vm_pt_next_leaf`:

amdgpu_vm_pt_next_leaf
======================

.. c:function:: void amdgpu_vm_pt_next_leaf(struct amdgpu_device *adev, struct amdgpu_vm_pt_cursor *cursor)

    get next leaf PD/PT

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param cursor:
        current state
    :type cursor: struct amdgpu_vm_pt_cursor \*

.. _`amdgpu_vm_pt_next_leaf.description`:

Description
-----------

Walk the PD/PT tree to the next leaf node.

.. _`for_each_amdgpu_vm_pt_leaf`:

for_each_amdgpu_vm_pt_leaf
==========================

.. c:function::  for_each_amdgpu_vm_pt_leaf( adev,  vm,  start,  end,  cursor)

    walk over all leaf PDs/PTs in the hierarchy

    :param adev:
        *undescribed*
    :type adev: 

    :param vm:
        *undescribed*
    :type vm: 

    :param start:
        *undescribed*
    :type start: 

    :param end:
        *undescribed*
    :type end: 

    :param cursor:
        *undescribed*
    :type cursor: 

.. _`amdgpu_vm_pt_first_dfs`:

amdgpu_vm_pt_first_dfs
======================

.. c:function:: void amdgpu_vm_pt_first_dfs(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_vm_pt_cursor *cursor)

    start a deep first search

    :param adev:
        amdgpu_device structure
    :type adev: struct amdgpu_device \*

    :param vm:
        amdgpu_vm structure
    :type vm: struct amdgpu_vm \*

    :param cursor:
        state to initialize
    :type cursor: struct amdgpu_vm_pt_cursor \*

.. _`amdgpu_vm_pt_first_dfs.description`:

Description
-----------

Starts a deep first traversal of the PD/PT tree.

.. _`amdgpu_vm_pt_next_dfs`:

amdgpu_vm_pt_next_dfs
=====================

.. c:function:: void amdgpu_vm_pt_next_dfs(struct amdgpu_device *adev, struct amdgpu_vm_pt_cursor *cursor)

    get the next node for a deep first search

    :param adev:
        amdgpu_device structure
    :type adev: struct amdgpu_device \*

    :param cursor:
        current state
    :type cursor: struct amdgpu_vm_pt_cursor \*

.. _`amdgpu_vm_pt_next_dfs.description`:

Description
-----------

Move the cursor to the next node in a deep first search.

.. _`for_each_amdgpu_vm_pt_dfs_safe`:

for_each_amdgpu_vm_pt_dfs_safe
==============================

.. c:function::  for_each_amdgpu_vm_pt_dfs_safe( adev,  vm,  cursor,  entry)

    safe deep first search of all PDs/PTs

    :param adev:
        *undescribed*
    :type adev: 

    :param vm:
        *undescribed*
    :type vm: 

    :param cursor:
        *undescribed*
    :type cursor: 

    :param entry:
        *undescribed*
    :type entry: 

.. _`amdgpu_vm_get_pd_bo`:

amdgpu_vm_get_pd_bo
===================

.. c:function:: void amdgpu_vm_get_pd_bo(struct amdgpu_vm *vm, struct list_head *validated, struct amdgpu_bo_list_entry *entry)

    add the VM PD to a validation list

    :param vm:
        vm providing the BOs
    :type vm: struct amdgpu_vm \*

    :param validated:
        head of validation list
    :type validated: struct list_head \*

    :param entry:
        entry to add
    :type entry: struct amdgpu_bo_list_entry \*

.. _`amdgpu_vm_get_pd_bo.description`:

Description
-----------

Add the page directory to the list of BOs to
validate for command submission.

.. _`amdgpu_vm_move_to_lru_tail`:

amdgpu_vm_move_to_lru_tail
==========================

.. c:function:: void amdgpu_vm_move_to_lru_tail(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    move all BOs to the end of LRU

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        vm providing the BOs
    :type vm: struct amdgpu_vm \*

.. _`amdgpu_vm_move_to_lru_tail.description`:

Description
-----------

Move all BOs to the end of LRU and remember their positions to put them
together.

.. _`amdgpu_vm_validate_pt_bos`:

amdgpu_vm_validate_pt_bos
=========================

.. c:function:: int amdgpu_vm_validate_pt_bos(struct amdgpu_device *adev, struct amdgpu_vm *vm, int (*validate)(void *p, struct amdgpu_bo *bo), void *param)

    validate the page table BOs

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        vm providing the BOs
    :type vm: struct amdgpu_vm \*

    :param int (\*validate)(void \*p, struct amdgpu_bo \*bo):
        callback to do the validation

    :param param:
        parameter for the validation callback
    :type param: void \*

.. _`amdgpu_vm_validate_pt_bos.description`:

Description
-----------

Validate the page table BOs on command submission if neccessary.

.. _`amdgpu_vm_validate_pt_bos.return`:

Return
------

Validation result.

.. _`amdgpu_vm_ready`:

amdgpu_vm_ready
===============

.. c:function:: bool amdgpu_vm_ready(struct amdgpu_vm *vm)

    check VM is ready for updates

    :param vm:
        VM to check
    :type vm: struct amdgpu_vm \*

.. _`amdgpu_vm_ready.description`:

Description
-----------

Check if all VM PDs/PTs are ready for updates

.. _`amdgpu_vm_ready.return`:

Return
------

True if eviction list is empty.

.. _`amdgpu_vm_clear_bo`:

amdgpu_vm_clear_bo
==================

.. c:function:: int amdgpu_vm_clear_bo(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_bo *bo, unsigned level, bool pte_support_ats)

    initially clear the PDs/PTs

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        VM to clear BO from
    :type vm: struct amdgpu_vm \*

    :param bo:
        BO to clear
    :type bo: struct amdgpu_bo \*

    :param level:
        level this BO is at
    :type level: unsigned

    :param pte_support_ats:
        indicate ATS support from PTE
    :type pte_support_ats: bool

.. _`amdgpu_vm_clear_bo.description`:

Description
-----------

Root PD needs to be reserved when calling this.

.. _`amdgpu_vm_clear_bo.return`:

Return
------

0 on success, errno otherwise.

.. _`amdgpu_vm_bo_param`:

amdgpu_vm_bo_param
==================

.. c:function:: void amdgpu_vm_bo_param(struct amdgpu_device *adev, struct amdgpu_vm *vm, int level, struct amdgpu_bo_param *bp)

    fill in parameters for PD/PT allocation

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        requesting vm
    :type vm: struct amdgpu_vm \*

    :param level:
        *undescribed*
    :type level: int

    :param bp:
        resulting BO allocation parameters
    :type bp: struct amdgpu_bo_param \*

.. _`amdgpu_vm_alloc_pts`:

amdgpu_vm_alloc_pts
===================

.. c:function:: int amdgpu_vm_alloc_pts(struct amdgpu_device *adev, struct amdgpu_vm *vm, uint64_t saddr, uint64_t size)

    Allocate page tables.

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        VM to allocate page tables for
    :type vm: struct amdgpu_vm \*

    :param saddr:
        Start address which needs to be allocated
    :type saddr: uint64_t

    :param size:
        Size from start address we need.
    :type size: uint64_t

.. _`amdgpu_vm_alloc_pts.description`:

Description
-----------

Make sure the page directories and page tables are allocated

.. _`amdgpu_vm_alloc_pts.return`:

Return
------

0 on success, errno otherwise.

.. _`amdgpu_vm_free_pts`:

amdgpu_vm_free_pts
==================

.. c:function:: void amdgpu_vm_free_pts(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    free PD/PT levels

    :param adev:
        amdgpu device structure
    :type adev: struct amdgpu_device \*

    :param vm:
        amdgpu vm structure
    :type vm: struct amdgpu_vm \*

.. _`amdgpu_vm_free_pts.description`:

Description
-----------

Free the page directory or page table level and all sub levels.

.. _`amdgpu_vm_check_compute_bug`:

amdgpu_vm_check_compute_bug
===========================

.. c:function:: void amdgpu_vm_check_compute_bug(struct amdgpu_device *adev)

    check whether asic has compute vm bug

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vm_need_pipeline_sync`:

amdgpu_vm_need_pipeline_sync
============================

.. c:function:: bool amdgpu_vm_need_pipeline_sync(struct amdgpu_ring *ring, struct amdgpu_job *job)

    Check if pipe sync is needed for job.

    :param ring:
        ring on which the job will be submitted
    :type ring: struct amdgpu_ring \*

    :param job:
        job to submit
    :type job: struct amdgpu_job \*

.. _`amdgpu_vm_need_pipeline_sync.return`:

Return
------

True if sync is needed.

.. _`amdgpu_vm_flush`:

amdgpu_vm_flush
===============

.. c:function:: int amdgpu_vm_flush(struct amdgpu_ring *ring, struct amdgpu_job *job, bool need_pipe_sync)

    hardware flush the vm

    :param ring:
        ring to use for flush
    :type ring: struct amdgpu_ring \*

    :param job:
        related job
    :type job: struct amdgpu_job \*

    :param need_pipe_sync:
        is pipe sync needed
    :type need_pipe_sync: bool

.. _`amdgpu_vm_flush.description`:

Description
-----------

Emit a VM flush when it is necessary.

.. _`amdgpu_vm_flush.return`:

Return
------

0 on success, errno otherwise.

.. _`amdgpu_vm_bo_find`:

amdgpu_vm_bo_find
=================

.. c:function:: struct amdgpu_bo_va *amdgpu_vm_bo_find(struct amdgpu_vm *vm, struct amdgpu_bo *bo)

    find the bo_va for a specific vm & bo

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

    :param bo:
        requested buffer object
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_vm_bo_find.description`:

Description
-----------

Find \ ``bo``\  inside the requested vm.
Search inside the \ ``bos``\  vm list for the requested vm
Returns the found bo_va or NULL if none is found

Object has to be reserved!

.. _`amdgpu_vm_bo_find.return`:

Return
------

Found bo_va or NULL.

.. _`amdgpu_vm_do_set_ptes`:

amdgpu_vm_do_set_ptes
=====================

.. c:function:: void amdgpu_vm_do_set_ptes(struct amdgpu_pte_update_params *params, struct amdgpu_bo *bo, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint64_t flags)

    helper to call the right asic function

    :param params:
        see amdgpu_pte_update_params definition
    :type params: struct amdgpu_pte_update_params \*

    :param bo:
        PD/PT to update
    :type bo: struct amdgpu_bo \*

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
    :type flags: uint64_t

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

    :param params:
        see amdgpu_pte_update_params definition
    :type params: struct amdgpu_pte_update_params \*

    :param bo:
        PD/PT to update
    :type bo: struct amdgpu_bo \*

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
    :type flags: uint64_t

.. _`amdgpu_vm_do_copy_ptes.description`:

Description
-----------

Traces the parameters and calls the DMA function to copy the PTEs.

.. _`amdgpu_vm_map_gart`:

amdgpu_vm_map_gart
==================

.. c:function:: uint64_t amdgpu_vm_map_gart(const dma_addr_t *pages_addr, uint64_t addr)

    Resolve gart mapping of addr

    :param pages_addr:
        optional DMA address to use for lookup
    :type pages_addr: const dma_addr_t \*

    :param addr:
        the unmapped addr
    :type addr: uint64_t

.. _`amdgpu_vm_map_gart.description`:

Description
-----------

Look up the physical address of the page that the pte resolves
to.

.. _`amdgpu_vm_map_gart.return`:

Return
------

The pointer for the page table entry.

.. _`amdgpu_vm_cpu_set_ptes`:

amdgpu_vm_cpu_set_ptes
======================

.. c:function:: void amdgpu_vm_cpu_set_ptes(struct amdgpu_pte_update_params *params, struct amdgpu_bo *bo, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint64_t flags)

    helper to update page tables via CPU

    :param params:
        see amdgpu_pte_update_params definition
    :type params: struct amdgpu_pte_update_params \*

    :param bo:
        PD/PT to update
    :type bo: struct amdgpu_bo \*

    :param pe:
        kmap addr of the page entry
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
    :type flags: uint64_t

.. _`amdgpu_vm_cpu_set_ptes.description`:

Description
-----------

Write count number of PT/PD entries directly.

.. _`amdgpu_vm_wait_pd`:

amdgpu_vm_wait_pd
=================

.. c:function:: int amdgpu_vm_wait_pd(struct amdgpu_device *adev, struct amdgpu_vm *vm, void *owner)

    Wait for PT BOs to be free.

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        related vm
    :type vm: struct amdgpu_vm \*

    :param owner:
        fence owner
    :type owner: void \*

.. _`amdgpu_vm_wait_pd.return`:

Return
------

0 on success, errno otherwise.

.. _`amdgpu_vm_update_func`:

amdgpu_vm_update_func
=====================

.. c:function:: void amdgpu_vm_update_func(struct amdgpu_pte_update_params *params, struct amdgpu_bo *bo, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint64_t flags)

    helper to call update function

    :param params:
        *undescribed*
    :type params: struct amdgpu_pte_update_params \*

    :param bo:
        *undescribed*
    :type bo: struct amdgpu_bo \*

    :param pe:
        *undescribed*
    :type pe: uint64_t

    :param addr:
        *undescribed*
    :type addr: uint64_t

    :param count:
        *undescribed*
    :type count: unsigned

    :param incr:
        *undescribed*
    :type incr: uint32_t

    :param flags:
        *undescribed*
    :type flags: uint64_t

.. _`amdgpu_vm_update_func.description`:

Description
-----------

Calls the update function for both the given BO as well as its shadow.

.. _`amdgpu_vm_update_huge`:

amdgpu_vm_update_huge
=====================

.. c:function:: void amdgpu_vm_update_huge(struct amdgpu_pte_update_params *params, struct amdgpu_bo *bo, unsigned level, uint64_t pe, uint64_t addr, unsigned count, uint32_t incr, uint64_t flags)

    figure out parameters for PTE updates

    :param params:
        *undescribed*
    :type params: struct amdgpu_pte_update_params \*

    :param bo:
        *undescribed*
    :type bo: struct amdgpu_bo \*

    :param level:
        *undescribed*
    :type level: unsigned

    :param pe:
        *undescribed*
    :type pe: uint64_t

    :param addr:
        *undescribed*
    :type addr: uint64_t

    :param count:
        *undescribed*
    :type count: unsigned

    :param incr:
        *undescribed*
    :type incr: uint32_t

    :param flags:
        *undescribed*
    :type flags: uint64_t

.. _`amdgpu_vm_update_huge.description`:

Description
-----------

Make sure to set the right flags for the PTEs at the desired level.

.. _`amdgpu_vm_fragment`:

amdgpu_vm_fragment
==================

.. c:function:: void amdgpu_vm_fragment(struct amdgpu_pte_update_params *params, uint64_t start, uint64_t end, uint64_t flags, unsigned int *frag, uint64_t *frag_end)

    get fragment for PTEs

    :param params:
        see amdgpu_pte_update_params definition
    :type params: struct amdgpu_pte_update_params \*

    :param start:
        first PTE to handle
    :type start: uint64_t

    :param end:
        last PTE to handle
    :type end: uint64_t

    :param flags:
        hw mapping flags
    :type flags: uint64_t

    :param frag:
        resulting fragment size
    :type frag: unsigned int \*

    :param frag_end:
        end of this fragment
    :type frag_end: uint64_t \*

.. _`amdgpu_vm_fragment.description`:

Description
-----------

Returns the first possible fragment for the start and end address.

.. _`amdgpu_vm_update_ptes`:

amdgpu_vm_update_ptes
=====================

.. c:function:: int amdgpu_vm_update_ptes(struct amdgpu_pte_update_params *params, uint64_t start, uint64_t end, uint64_t dst, uint64_t flags)

    make sure that page tables are valid

    :param params:
        see amdgpu_pte_update_params definition
    :type params: struct amdgpu_pte_update_params \*

    :param start:
        start of GPU address range
    :type start: uint64_t

    :param end:
        end of GPU address range
    :type end: uint64_t

    :param dst:
        destination address to map to, the next dst inside the function
    :type dst: uint64_t

    :param flags:
        mapping flags
    :type flags: uint64_t

.. _`amdgpu_vm_update_ptes.description`:

Description
-----------

Update the page tables in the range \ ``start``\  - \ ``end``\ .

.. _`amdgpu_vm_update_ptes.return`:

Return
------

0 for success, -EINVAL for failure.

.. _`amdgpu_vm_bo_update_mapping`:

amdgpu_vm_bo_update_mapping
===========================

.. c:function:: int amdgpu_vm_bo_update_mapping(struct amdgpu_device *adev, struct dma_fence *exclusive, dma_addr_t *pages_addr, struct amdgpu_vm *vm, uint64_t start, uint64_t last, uint64_t flags, uint64_t addr, struct dma_fence **fence)

    update a mapping in the vm page table

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param exclusive:
        fence we need to sync to
    :type exclusive: struct dma_fence \*

    :param pages_addr:
        DMA addresses to use for mapping
    :type pages_addr: dma_addr_t \*

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

    :param start:
        start of mapped range
    :type start: uint64_t

    :param last:
        last mapped entry
    :type last: uint64_t

    :param flags:
        flags for the entries
    :type flags: uint64_t

    :param addr:
        addr to set the area to
    :type addr: uint64_t

    :param fence:
        optional resulting fence
    :type fence: struct dma_fence \*\*

.. _`amdgpu_vm_bo_update_mapping.description`:

Description
-----------

Fill in the page table entries between \ ``start``\  and \ ``last``\ .

.. _`amdgpu_vm_bo_update_mapping.return`:

Return
------

0 for success, -EINVAL for failure.

.. _`amdgpu_vm_bo_split_mapping`:

amdgpu_vm_bo_split_mapping
==========================

.. c:function:: int amdgpu_vm_bo_split_mapping(struct amdgpu_device *adev, struct dma_fence *exclusive, dma_addr_t *pages_addr, struct amdgpu_vm *vm, struct amdgpu_bo_va_mapping *mapping, uint64_t flags, struct drm_mm_node *nodes, struct dma_fence **fence)

    split a mapping into smaller chunks

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param exclusive:
        fence we need to sync to
    :type exclusive: struct dma_fence \*

    :param pages_addr:
        DMA addresses to use for mapping
    :type pages_addr: dma_addr_t \*

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

    :param mapping:
        mapped range and flags to use for the update
    :type mapping: struct amdgpu_bo_va_mapping \*

    :param flags:
        HW flags for the mapping
    :type flags: uint64_t

    :param nodes:
        array of drm_mm_nodes with the MC addresses
    :type nodes: struct drm_mm_node \*

    :param fence:
        optional resulting fence
    :type fence: struct dma_fence \*\*

.. _`amdgpu_vm_bo_split_mapping.description`:

Description
-----------

Split the mapping into smaller chunks so that each update fits
into a SDMA IB.

.. _`amdgpu_vm_bo_split_mapping.return`:

Return
------

0 for success, -EINVAL for failure.

.. _`amdgpu_vm_bo_update`:

amdgpu_vm_bo_update
===================

.. c:function:: int amdgpu_vm_bo_update(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, bool clear)

    update all BO mappings in the vm page table

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param bo_va:
        requested BO and VM object
    :type bo_va: struct amdgpu_bo_va \*

    :param clear:
        if true clear the entries
    :type clear: bool

.. _`amdgpu_vm_bo_update.description`:

Description
-----------

Fill in the page table entries for \ ``bo_va``\ .

.. _`amdgpu_vm_bo_update.return`:

Return
------

0 for success, -EINVAL for failure.

.. _`amdgpu_vm_update_prt_state`:

amdgpu_vm_update_prt_state
==========================

.. c:function:: void amdgpu_vm_update_prt_state(struct amdgpu_device *adev)

    update the global PRT state

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vm_prt_get`:

amdgpu_vm_prt_get
=================

.. c:function:: void amdgpu_vm_prt_get(struct amdgpu_device *adev)

    add a PRT user

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vm_prt_put`:

amdgpu_vm_prt_put
=================

.. c:function:: void amdgpu_vm_prt_put(struct amdgpu_device *adev)

    drop a PRT user

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vm_prt_cb`:

amdgpu_vm_prt_cb
================

.. c:function:: void amdgpu_vm_prt_cb(struct dma_fence *fence, struct dma_fence_cb *_cb)

    callback for updating the PRT status

    :param fence:
        fence for the callback
    :type fence: struct dma_fence \*

    :param _cb:
        the callback function
    :type _cb: struct dma_fence_cb \*

.. _`amdgpu_vm_add_prt_cb`:

amdgpu_vm_add_prt_cb
====================

.. c:function:: void amdgpu_vm_add_prt_cb(struct amdgpu_device *adev, struct dma_fence *fence)

    add callback for updating the PRT status

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param fence:
        fence for the callback
    :type fence: struct dma_fence \*

.. _`amdgpu_vm_free_mapping`:

amdgpu_vm_free_mapping
======================

.. c:function:: void amdgpu_vm_free_mapping(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_bo_va_mapping *mapping, struct dma_fence *fence)

    free a mapping

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

    :param mapping:
        mapping to be freed
    :type mapping: struct amdgpu_bo_va_mapping \*

    :param fence:
        fence of the unmap operation
    :type fence: struct dma_fence \*

.. _`amdgpu_vm_free_mapping.description`:

Description
-----------

Free a mapping and make sure we decrease the PRT usage count if applicable.

.. _`amdgpu_vm_prt_fini`:

amdgpu_vm_prt_fini
==================

.. c:function:: void amdgpu_vm_prt_fini(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    finish all prt mappings

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

.. _`amdgpu_vm_prt_fini.description`:

Description
-----------

Register a cleanup callback to disable PRT support after VM dies.

.. _`amdgpu_vm_clear_freed`:

amdgpu_vm_clear_freed
=====================

.. c:function:: int amdgpu_vm_clear_freed(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct dma_fence **fence)

    clear freed BOs in the PT

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

    :param fence:
        optional resulting fence (unchanged if no work needed to be done
        or if an error occurred)
    :type fence: struct dma_fence \*\*

.. _`amdgpu_vm_clear_freed.description`:

Description
-----------

Make sure all freed BOs are cleared in the PT.
PTs have to be reserved and mutex must be locked!

.. _`amdgpu_vm_clear_freed.return`:

Return
------

0 for success.

.. _`amdgpu_vm_handle_moved`:

amdgpu_vm_handle_moved
======================

.. c:function:: int amdgpu_vm_handle_moved(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    handle moved BOs in the PT

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

.. _`amdgpu_vm_handle_moved.description`:

Description
-----------

Make sure all BOs which are moved are updated in the PTs.

.. _`amdgpu_vm_handle_moved.return`:

Return
------

0 for success.

PTs have to be reserved!

.. _`amdgpu_vm_bo_add`:

amdgpu_vm_bo_add
================

.. c:function:: struct amdgpu_bo_va *amdgpu_vm_bo_add(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_bo *bo)

    add a bo to a specific vm

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

    :param bo:
        amdgpu buffer object
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_vm_bo_add.description`:

Description
-----------

Add \ ``bo``\  into the requested vm.
Add \ ``bo``\  to the list of bos associated with the vm

.. _`amdgpu_vm_bo_add.return`:

Return
------

Newly added bo_va or NULL for failure

Object has to be reserved!

.. _`amdgpu_vm_bo_insert_map`:

amdgpu_vm_bo_insert_map
=======================

.. c:function:: void amdgpu_vm_bo_insert_map(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, struct amdgpu_bo_va_mapping *mapping)

    insert a new mapping

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param bo_va:
        bo_va to store the address
    :type bo_va: struct amdgpu_bo_va \*

    :param mapping:
        the mapping to insert
    :type mapping: struct amdgpu_bo_va_mapping \*

.. _`amdgpu_vm_bo_insert_map.description`:

Description
-----------

Insert a new mapping into all structures.

.. _`amdgpu_vm_bo_map`:

amdgpu_vm_bo_map
================

.. c:function:: int amdgpu_vm_bo_map(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, uint64_t saddr, uint64_t offset, uint64_t size, uint64_t flags)

    map bo inside a vm

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param bo_va:
        bo_va to store the address
    :type bo_va: struct amdgpu_bo_va \*

    :param saddr:
        where to map the BO
    :type saddr: uint64_t

    :param offset:
        requested offset in the BO
    :type offset: uint64_t

    :param size:
        BO size in bytes
    :type size: uint64_t

    :param flags:
        attributes of pages (read/write/valid/etc.)
    :type flags: uint64_t

.. _`amdgpu_vm_bo_map.description`:

Description
-----------

Add a mapping of the BO at the specefied addr into the VM.

.. _`amdgpu_vm_bo_map.return`:

Return
------

0 for success, error for failure.

Object has to be reserved and unreserved outside!

.. _`amdgpu_vm_bo_replace_map`:

amdgpu_vm_bo_replace_map
========================

.. c:function:: int amdgpu_vm_bo_replace_map(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, uint64_t saddr, uint64_t offset, uint64_t size, uint64_t flags)

    map bo inside a vm, replacing existing mappings

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param bo_va:
        bo_va to store the address
    :type bo_va: struct amdgpu_bo_va \*

    :param saddr:
        where to map the BO
    :type saddr: uint64_t

    :param offset:
        requested offset in the BO
    :type offset: uint64_t

    :param size:
        BO size in bytes
    :type size: uint64_t

    :param flags:
        attributes of pages (read/write/valid/etc.)
    :type flags: uint64_t

.. _`amdgpu_vm_bo_replace_map.description`:

Description
-----------

Add a mapping of the BO at the specefied addr into the VM. Replace existing
mappings as we do so.

.. _`amdgpu_vm_bo_replace_map.return`:

Return
------

0 for success, error for failure.

Object has to be reserved and unreserved outside!

.. _`amdgpu_vm_bo_unmap`:

amdgpu_vm_bo_unmap
==================

.. c:function:: int amdgpu_vm_bo_unmap(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, uint64_t saddr)

    remove bo mapping from vm

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param bo_va:
        bo_va to remove the address from
    :type bo_va: struct amdgpu_bo_va \*

    :param saddr:
        where to the BO is mapped
    :type saddr: uint64_t

.. _`amdgpu_vm_bo_unmap.description`:

Description
-----------

Remove a mapping of the BO at the specefied addr from the VM.

.. _`amdgpu_vm_bo_unmap.return`:

Return
------

0 for success, error for failure.

Object has to be reserved and unreserved outside!

.. _`amdgpu_vm_bo_clear_mappings`:

amdgpu_vm_bo_clear_mappings
===========================

.. c:function:: int amdgpu_vm_bo_clear_mappings(struct amdgpu_device *adev, struct amdgpu_vm *vm, uint64_t saddr, uint64_t size)

    remove all mappings in a specific range

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        VM structure to use
    :type vm: struct amdgpu_vm \*

    :param saddr:
        start of the range
    :type saddr: uint64_t

    :param size:
        size of the range
    :type size: uint64_t

.. _`amdgpu_vm_bo_clear_mappings.description`:

Description
-----------

Remove all mappings in a range, split them as appropriate.

.. _`amdgpu_vm_bo_clear_mappings.return`:

Return
------

0 for success, error for failure.

.. _`amdgpu_vm_bo_lookup_mapping`:

amdgpu_vm_bo_lookup_mapping
===========================

.. c:function:: struct amdgpu_bo_va_mapping *amdgpu_vm_bo_lookup_mapping(struct amdgpu_vm *vm, uint64_t addr)

    find mapping by address

    :param vm:
        the requested VM
    :type vm: struct amdgpu_vm \*

    :param addr:
        the address
    :type addr: uint64_t

.. _`amdgpu_vm_bo_lookup_mapping.description`:

Description
-----------

Find a mapping by it's address.

.. _`amdgpu_vm_bo_lookup_mapping.return`:

Return
------

The amdgpu_bo_va_mapping matching for addr or NULL

.. _`amdgpu_vm_bo_trace_cs`:

amdgpu_vm_bo_trace_cs
=====================

.. c:function:: void amdgpu_vm_bo_trace_cs(struct amdgpu_vm *vm, struct ww_acquire_ctx *ticket)

    trace all reserved mappings

    :param vm:
        the requested vm
    :type vm: struct amdgpu_vm \*

    :param ticket:
        CS ticket
    :type ticket: struct ww_acquire_ctx \*

.. _`amdgpu_vm_bo_trace_cs.description`:

Description
-----------

Trace all mappings of BOs reserved during a command submission.

.. _`amdgpu_vm_bo_rmv`:

amdgpu_vm_bo_rmv
================

.. c:function:: void amdgpu_vm_bo_rmv(struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va)

    remove a bo to a specific vm

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param bo_va:
        requested bo_va
    :type bo_va: struct amdgpu_bo_va \*

.. _`amdgpu_vm_bo_rmv.description`:

Description
-----------

Remove \ ``bo_va->bo``\  from the requested vm.

Object have to be reserved!

.. _`amdgpu_vm_bo_invalidate`:

amdgpu_vm_bo_invalidate
=======================

.. c:function:: void amdgpu_vm_bo_invalidate(struct amdgpu_device *adev, struct amdgpu_bo *bo, bool evicted)

    mark the bo as invalid

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param bo:
        amdgpu buffer object
    :type bo: struct amdgpu_bo \*

    :param evicted:
        is the BO evicted
    :type evicted: bool

.. _`amdgpu_vm_bo_invalidate.description`:

Description
-----------

Mark \ ``bo``\  as invalid.

.. _`amdgpu_vm_get_block_size`:

amdgpu_vm_get_block_size
========================

.. c:function:: uint32_t amdgpu_vm_get_block_size(uint64_t vm_size)

    calculate VM page table size as power of two

    :param vm_size:
        VM size
    :type vm_size: uint64_t

.. _`amdgpu_vm_get_block_size.return`:

Return
------

VM page table as power of two

.. _`amdgpu_vm_adjust_size`:

amdgpu_vm_adjust_size
=====================

.. c:function:: void amdgpu_vm_adjust_size(struct amdgpu_device *adev, uint32_t min_vm_size, uint32_t fragment_size_default, unsigned max_level, unsigned max_bits)

    adjust vm size, block size and fragment size

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param min_vm_size:
        the minimum vm size in GB if it's set auto
    :type min_vm_size: uint32_t

    :param fragment_size_default:
        Default PTE fragment size
    :type fragment_size_default: uint32_t

    :param max_level:
        max VMPT level
    :type max_level: unsigned

    :param max_bits:
        max address space size in bits
    :type max_bits: unsigned

.. _`amdgpu_vm_init`:

amdgpu_vm_init
==============

.. c:function:: int amdgpu_vm_init(struct amdgpu_device *adev, struct amdgpu_vm *vm, int vm_context, unsigned int pasid)

    initialize a vm instance

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

    :param vm_context:
        Indicates if it GFX or Compute context
    :type vm_context: int

    :param pasid:
        Process address space identifier
    :type pasid: unsigned int

.. _`amdgpu_vm_init.description`:

Description
-----------

Init \ ``vm``\  fields.

.. _`amdgpu_vm_init.return`:

Return
------

0 for success, error for failure.

.. _`amdgpu_vm_make_compute`:

amdgpu_vm_make_compute
======================

.. c:function:: int amdgpu_vm_make_compute(struct amdgpu_device *adev, struct amdgpu_vm *vm, unsigned int pasid)

    Turn a GFX VM into a compute VM

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

    :param pasid:
        *undescribed*
    :type pasid: unsigned int

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
setting.

.. _`amdgpu_vm_make_compute.return`:

Return
------

0 for success, -errno for errors.

.. _`amdgpu_vm_release_compute`:

amdgpu_vm_release_compute
=========================

.. c:function:: void amdgpu_vm_release_compute(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    release a compute vm

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        a vm turned into compute vm by calling amdgpu_vm_make_compute
    :type vm: struct amdgpu_vm \*

.. _`amdgpu_vm_release_compute.description`:

Description
-----------

This is a correspondant of amdgpu_vm_make_compute. It decouples compute
pasid from vm. Compute should stop use of vm after this call.

.. _`amdgpu_vm_fini`:

amdgpu_vm_fini
==============

.. c:function:: void amdgpu_vm_fini(struct amdgpu_device *adev, struct amdgpu_vm *vm)

    tear down a vm instance

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        requested vm
    :type vm: struct amdgpu_vm \*

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

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param pasid:
        PASID do identify the VM
    :type pasid: unsigned int

.. _`amdgpu_vm_pasid_fault_credit.description`:

Description
-----------

This function is expected to be called in interrupt context.

.. _`amdgpu_vm_pasid_fault_credit.return`:

Return
------

True if there was fault credit, false otherwise

.. _`amdgpu_vm_manager_init`:

amdgpu_vm_manager_init
======================

.. c:function:: void amdgpu_vm_manager_init(struct amdgpu_device *adev)

    init the VM manager

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vm_manager_init.description`:

Description
-----------

Initialize the VM manager structures

.. _`amdgpu_vm_manager_fini`:

amdgpu_vm_manager_fini
======================

.. c:function:: void amdgpu_vm_manager_fini(struct amdgpu_device *adev)

    cleanup VM manager

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_vm_manager_fini.description`:

Description
-----------

Cleanup the VM manager and free resources.

.. _`amdgpu_vm_ioctl`:

amdgpu_vm_ioctl
===============

.. c:function:: int amdgpu_vm_ioctl(struct drm_device *dev, void *data, struct drm_file *filp)

    Manages VMID reservation for vm hubs.

    :param dev:
        drm device pointer
    :type dev: struct drm_device \*

    :param data:
        drm_amdgpu_vm
    :type data: void \*

    :param filp:
        drm file pointer
    :type filp: struct drm_file \*

.. _`amdgpu_vm_ioctl.return`:

Return
------

0 for success, -errno for errors.

.. _`amdgpu_vm_get_task_info`:

amdgpu_vm_get_task_info
=======================

.. c:function:: void amdgpu_vm_get_task_info(struct amdgpu_device *adev, unsigned int pasid, struct amdgpu_task_info *task_info)

    Extracts task info for a PASID.

    :param adev:
        drm device pointer
    :type adev: struct amdgpu_device \*

    :param pasid:
        PASID identifier for VM
    :type pasid: unsigned int

    :param task_info:
        task_info to fill.
    :type task_info: struct amdgpu_task_info \*

.. _`amdgpu_vm_set_task_info`:

amdgpu_vm_set_task_info
=======================

.. c:function:: void amdgpu_vm_set_task_info(struct amdgpu_vm *vm)

    Sets VMs task info.

    :param vm:
        vm for which to set the info
    :type vm: struct amdgpu_vm \*

.. _`amdgpu_vm_add_fault`:

amdgpu_vm_add_fault
===================

.. c:function:: int amdgpu_vm_add_fault(struct amdgpu_retryfault_hashtable *fault_hash, u64 key)

    Add a page fault record to fault hash table

    :param fault_hash:
        fault hash table
    :type fault_hash: struct amdgpu_retryfault_hashtable \*

    :param key:
        64-bit encoding of PASID and address
    :type key: u64

.. _`amdgpu_vm_add_fault.description`:

Description
-----------

This should be called when a retry page fault interrupt is
received. If this is a new page fault, it will be added to a hash
table. The return value indicates whether this is a new fault, or
a fault that was already known and is already being handled.

If there are too many pending page faults, this will fail. Retry
interrupts should be ignored in this case until there is enough
free space.

Returns 0 if the fault was added, 1 if the fault was already known,
-ENOSPC if there are too many pending faults.

.. _`amdgpu_vm_clear_fault`:

amdgpu_vm_clear_fault
=====================

.. c:function:: void amdgpu_vm_clear_fault(struct amdgpu_retryfault_hashtable *fault_hash, u64 key)

    Remove a page fault record

    :param fault_hash:
        fault hash table
    :type fault_hash: struct amdgpu_retryfault_hashtable \*

    :param key:
        64-bit encoding of PASID and address
    :type key: u64

.. _`amdgpu_vm_clear_fault.description`:

Description
-----------

This should be called when a page fault has been handled. Any
future interrupt with this key will be processed as a new
page fault.

.. This file was automatic generated / don't edit.

