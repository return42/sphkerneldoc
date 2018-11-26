.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/mmu.c

.. _`kvm_flush_remote_tlbs`:

kvm_flush_remote_tlbs
=====================

.. c:function:: void kvm_flush_remote_tlbs(struct kvm *kvm)

    flush all VM TLB entries for v7/8

    :param kvm:
        pointer to kvm structure.
    :type kvm: struct kvm \*

.. _`kvm_flush_remote_tlbs.description`:

Description
-----------

Interface to HYP function to flush all VM TLB entries

.. _`stage2_dissolve_pmd`:

stage2_dissolve_pmd
===================

.. c:function:: void stage2_dissolve_pmd(struct kvm *kvm, phys_addr_t addr, pmd_t *pmd)

    clear and flush huge PMD entry

    :param kvm:
        pointer to kvm structure.
    :type kvm: struct kvm \*

    :param addr:
        IPA
    :type addr: phys_addr_t

    :param pmd:
        pmd pointer for IPA
    :type pmd: pmd_t \*

.. _`stage2_dissolve_pmd.description`:

Description
-----------

Function clears a PMD entry, flushes addr 1st and 2nd stage TLBs. Marks all
pages in the range dirty.

.. _`unmap_stage2_range`:

unmap_stage2_range
==================

.. c:function:: void unmap_stage2_range(struct kvm *kvm, phys_addr_t start, u64 size)

    - Clear stage2 page table entries to unmap a range

    :param kvm:
        The VM pointer
    :type kvm: struct kvm \*

    :param start:
        The intermediate physical base address of the range to unmap
    :type start: phys_addr_t

    :param size:
        The size of the area to unmap
    :type size: u64

.. _`unmap_stage2_range.description`:

Description
-----------

Clear a range of stage-2 mappings, lowering the various ref-counts.  Must
be called while holding mmu_lock (unless for freeing the stage2 pgd before
destroying the VM), otherwise another faulting VCPU may come in and mess
with things behind our backs.

.. _`stage2_flush_vm`:

stage2_flush_vm
===============

.. c:function:: void stage2_flush_vm(struct kvm *kvm)

    Invalidate cache for pages mapped in stage 2

    :param kvm:
        The struct kvm pointer
    :type kvm: struct kvm \*

.. _`stage2_flush_vm.description`:

Description
-----------

Go through the stage 2 page tables and invalidate any cache lines
backing memory already mapped to the VM.

.. _`free_hyp_pgds`:

free_hyp_pgds
=============

.. c:function:: void free_hyp_pgds( void)

    free Hyp-mode page tables

    :param void:
        no arguments
    :type void: 

.. _`free_hyp_pgds.description`:

Description
-----------

Assumes hyp_pgd is a page table used strictly in Hyp-mode and
therefore contains either mappings in the kernel memory area (above
PAGE_OFFSET), or device mappings in the idmap range.

boot_hyp_pgd should only map the idmap range, and is only used in
the extended idmap case.

.. _`create_hyp_mappings`:

create_hyp_mappings
===================

.. c:function:: int create_hyp_mappings(void *from, void *to, pgprot_t prot)

    duplicate a kernel virtual address range in Hyp mode

    :param from:
        The virtual kernel start address of the range
    :type from: void \*

    :param to:
        The virtual kernel end address of the range (exclusive)
    :type to: void \*

    :param prot:
        The protection to be applied to this range
    :type prot: pgprot_t

.. _`create_hyp_mappings.description`:

Description
-----------

The same virtual address as the kernel virtual address is also used
in Hyp-mode mapping (modulo HYP_PAGE_OFFSET) to the same underlying
physical pages.

.. _`create_hyp_io_mappings`:

create_hyp_io_mappings
======================

.. c:function:: int create_hyp_io_mappings(phys_addr_t phys_addr, size_t size, void __iomem **kaddr, void __iomem **haddr)

    Map IO into both kernel and HYP

    :param phys_addr:
        The physical start address which gets mapped
    :type phys_addr: phys_addr_t

    :param size:
        Size of the region being mapped
    :type size: size_t

    :param kaddr:
        Kernel VA for this mapping
    :type kaddr: void __iomem \*\*

    :param haddr:
        HYP VA for this mapping
    :type haddr: void __iomem \*\*

.. _`create_hyp_exec_mappings`:

create_hyp_exec_mappings
========================

.. c:function:: int create_hyp_exec_mappings(phys_addr_t phys_addr, size_t size, void **haddr)

    Map an executable range into HYP

    :param phys_addr:
        The physical start address which gets mapped
    :type phys_addr: phys_addr_t

    :param size:
        Size of the region being mapped
    :type size: size_t

    :param haddr:
        HYP VA for this mapping
    :type haddr: void \*\*

.. _`kvm_alloc_stage2_pgd`:

kvm_alloc_stage2_pgd
====================

.. c:function:: int kvm_alloc_stage2_pgd(struct kvm *kvm)

    allocate level-1 table for stage-2 translation.

    :param kvm:
        The KVM struct pointer for the VM.
    :type kvm: struct kvm \*

.. _`kvm_alloc_stage2_pgd.description`:

Description
-----------

Allocates only the stage-2 HW PGD level table(s) (can support either full
40-bit input addresses or limited to 32-bit input addresses). Clears the
allocated pages.

Note we don't need locking here as this is only called when the VM is
created, which can only be done once.

.. _`stage2_unmap_vm`:

stage2_unmap_vm
===============

.. c:function:: void stage2_unmap_vm(struct kvm *kvm)

    Unmap Stage-2 RAM mappings

    :param kvm:
        The struct kvm pointer
    :type kvm: struct kvm \*

.. _`stage2_unmap_vm.description`:

Description
-----------

Go through the memregions and unmap any reguler RAM
backing memory already mapped to the VM.

.. _`kvm_free_stage2_pgd`:

kvm_free_stage2_pgd
===================

.. c:function:: void kvm_free_stage2_pgd(struct kvm *kvm)

    free all stage-2 tables

    :param kvm:
        The KVM struct pointer for the VM.
    :type kvm: struct kvm \*

.. _`kvm_free_stage2_pgd.description`:

Description
-----------

Walks the level-1 page table pointed to by kvm->arch.pgd and frees all
underlying level-2 and level-3 tables before freeing the actual level-1 table
and setting the struct pointer to NULL.

.. _`kvm_phys_addr_ioremap`:

kvm_phys_addr_ioremap
=====================

.. c:function:: int kvm_phys_addr_ioremap(struct kvm *kvm, phys_addr_t guest_ipa, phys_addr_t pa, unsigned long size, bool writable)

    map a device range to guest IPA

    :param kvm:
        The KVM pointer
    :type kvm: struct kvm \*

    :param guest_ipa:
        The IPA at which to insert the mapping
    :type guest_ipa: phys_addr_t

    :param pa:
        The physical address of the device
    :type pa: phys_addr_t

    :param size:
        The size of the mapping
    :type size: unsigned long

    :param writable:
        *undescribed*
    :type writable: bool

.. _`stage2_wp_ptes`:

stage2_wp_ptes
==============

.. c:function:: void stage2_wp_ptes(pmd_t *pmd, phys_addr_t addr, phys_addr_t end)

    write protect PMD range

    :param pmd:
        pointer to pmd entry
    :type pmd: pmd_t \*

    :param addr:
        range start address
    :type addr: phys_addr_t

    :param end:
        range end address
    :type end: phys_addr_t

.. _`stage2_wp_pmds`:

stage2_wp_pmds
==============

.. c:function:: void stage2_wp_pmds(struct kvm *kvm, pud_t *pud, phys_addr_t addr, phys_addr_t end)

    write protect PUD range

    :param kvm:
        *undescribed*
    :type kvm: struct kvm \*

    :param pud:
        pointer to pud entry
    :type pud: pud_t \*

    :param addr:
        range start address
    :type addr: phys_addr_t

    :param end:
        range end address
    :type end: phys_addr_t

.. _`stage2_wp_pmds.kvm`:

kvm
---

kvm instance for the VM

.. _`stage2_wp_puds`:

stage2_wp_puds
==============

.. c:function:: void stage2_wp_puds(struct kvm *kvm, pgd_t *pgd, phys_addr_t addr, phys_addr_t end)

    write protect PGD range

    :param kvm:
        *undescribed*
    :type kvm: struct kvm \*

    :param pgd:
        pointer to pgd entry
    :type pgd: pgd_t \*

    :param addr:
        range start address
    :type addr: phys_addr_t

    :param end:
        range end address
    :type end: phys_addr_t

.. _`stage2_wp_puds.description`:

Description
-----------

Process PUD entries, for a huge PUD we cause a panic.

.. _`stage2_wp_range`:

stage2_wp_range
===============

.. c:function:: void stage2_wp_range(struct kvm *kvm, phys_addr_t addr, phys_addr_t end)

    write protect stage2 memory region range

    :param kvm:
        The KVM pointer
    :type kvm: struct kvm \*

    :param addr:
        Start address of range
    :type addr: phys_addr_t

    :param end:
        End address of range
    :type end: phys_addr_t

.. _`kvm_mmu_wp_memory_region`:

kvm_mmu_wp_memory_region
========================

.. c:function:: void kvm_mmu_wp_memory_region(struct kvm *kvm, int slot)

    write protect stage 2 entries for memory slot

    :param kvm:
        The KVM pointer
    :type kvm: struct kvm \*

    :param slot:
        The memory slot to write protect
    :type slot: int

.. _`kvm_mmu_wp_memory_region.description`:

Description
-----------

Called to start logging dirty pages after memory region
KVM_MEM_LOG_DIRTY_PAGES operation is called. After this function returns
all present PMD and PTEs are write protected in the memory region.
Afterwards read of dirty page log can be called.

Acquires kvm_mmu_lock. Called with kvm->slots_lock mutex acquired,
serializing operations for VM memory regions.

.. _`kvm_mmu_write_protect_pt_masked`:

kvm_mmu_write_protect_pt_masked
===============================

.. c:function:: void kvm_mmu_write_protect_pt_masked(struct kvm *kvm, struct kvm_memory_slot *slot, gfn_t gfn_offset, unsigned long mask)

    write protect dirty pages

    :param kvm:
        The KVM pointer
    :type kvm: struct kvm \*

    :param slot:
        The memory slot associated with mask
    :type slot: struct kvm_memory_slot \*

    :param gfn_offset:
        The gfn offset in memory slot
    :type gfn_offset: gfn_t

    :param mask:
        The mask of dirty pages at offset 'gfn_offset' in this memory
        slot to be write protected
    :type mask: unsigned long

.. _`kvm_mmu_write_protect_pt_masked.description`:

Description
-----------

Walks bits set in mask write protects the associated pte's. Caller must
acquire kvm_mmu_lock.

.. _`kvm_handle_guest_abort`:

kvm_handle_guest_abort
======================

.. c:function:: int kvm_handle_guest_abort(struct kvm_vcpu *vcpu, struct kvm_run *run)

    handles all 2nd stage aborts

    :param vcpu:
        the VCPU pointer
    :type vcpu: struct kvm_vcpu \*

    :param run:
        the kvm_run structure
    :type run: struct kvm_run \*

.. _`kvm_handle_guest_abort.description`:

Description
-----------

Any abort that gets to the host is almost guaranteed to be caused by a
missing second stage translation table entry, which can mean that either the
guest simply needs more memory and we must allocate an appropriate page or it
can mean that the guest tried to access I/O memory, which is emulated by user
space. The distinction is based on the IPA causing the fault and whether this
memory region has been registered as standard RAM by user space.

.. This file was automatic generated / don't edit.

