.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kvm/mmu.c

.. _`kvm_pgd_init`:

kvm_pgd_init
============

.. c:function:: void kvm_pgd_init(void *page)

    Initialise KVM GPA page directory.

    :param void \*page:
        Pointer to page directory (PGD) for KVM GPA.

.. _`kvm_pgd_init.description`:

Description
-----------

Initialise a KVM GPA page directory with pointers to the invalid table, i.e.
representing no mappings. This is similar to \ :c:func:`pgd_init`\ , however it
initialises all the page directory pointers, not just the ones corresponding
to the userland address space (since it is for the guest physical address
space rather than a virtual address space).

.. _`kvm_pgd_alloc`:

kvm_pgd_alloc
=============

.. c:function:: pgd_t *kvm_pgd_alloc( void)

    Allocate and initialise a KVM GPA page directory.

    :param  void:
        no arguments

.. _`kvm_pgd_alloc.description`:

Description
-----------

Allocate a blank KVM GPA page directory (PGD) for representing guest physical
to host physical page mappings.

.. _`kvm_pgd_alloc.return`:

Return
------

Pointer to new KVM GPA page directory.
NULL on allocation failure.

.. _`kvm_mips_walk_pgd`:

kvm_mips_walk_pgd
=================

.. c:function:: pte_t *kvm_mips_walk_pgd(pgd_t *pgd, struct kvm_mmu_memory_cache *cache, unsigned long addr)

    Walk page table with optional allocation.

    :param pgd_t \*pgd:
        Page directory pointer.

    :param struct kvm_mmu_memory_cache \*cache:
        MMU page cache to allocate new page tables from, or NULL.

    :param unsigned long addr:
        Address to index page table using.

.. _`kvm_mips_walk_pgd.description`:

Description
-----------

Walk the page tables pointed to by \ ``pgd``\  to find the PTE corresponding to the
address \ ``addr``\ . If page tables don't exist for \ ``addr``\ , they will be created
from the MMU cache if \ ``cache``\  is not NULL.

.. _`kvm_mips_walk_pgd.return`:

Return
------

Pointer to pte_t corresponding to \ ``addr``\ .
NULL if a page table doesn't exist for \ ``addr``\  and !@cache.
NULL if a page table allocation failed.

.. _`kvm_mips_flush_gpa_pt`:

kvm_mips_flush_gpa_pt
=====================

.. c:function:: bool kvm_mips_flush_gpa_pt(struct kvm *kvm, gfn_t start_gfn, gfn_t end_gfn)

    Flush a range of guest physical addresses.

    :param struct kvm \*kvm:
        KVM pointer.

    :param gfn_t start_gfn:
        Guest frame number of first page in GPA range to flush.

    :param gfn_t end_gfn:
        Guest frame number of last page in GPA range to flush.

.. _`kvm_mips_flush_gpa_pt.description`:

Description
-----------

Flushes a range of GPA mappings from the GPA page tables.

The caller must hold the \ ``kvm``\ ->mmu_lock spinlock.

.. _`kvm_mips_flush_gpa_pt.return`:

Return
------

Whether its safe to remove the top level page directory because
all lower levels have been removed.

.. _`kvm_mips_mkclean_gpa_pt`:

kvm_mips_mkclean_gpa_pt
=======================

.. c:function:: int kvm_mips_mkclean_gpa_pt(struct kvm *kvm, gfn_t start_gfn, gfn_t end_gfn)

    Make a range of guest physical addresses clean.

    :param struct kvm \*kvm:
        KVM pointer.

    :param gfn_t start_gfn:
        Guest frame number of first page in GPA range to flush.

    :param gfn_t end_gfn:
        Guest frame number of last page in GPA range to flush.

.. _`kvm_mips_mkclean_gpa_pt.description`:

Description
-----------

Make a range of GPA mappings clean so that guest writes will fault and
trigger dirty page logging.

The caller must hold the \ ``kvm``\ ->mmu_lock spinlock.

.. _`kvm_mips_mkclean_gpa_pt.return`:

Return
------

Whether any GPA mappings were modified, which would require
derived mappings (GVA page tables & TLB enties) to be
invalidated.

.. _`kvm_arch_mmu_enable_log_dirty_pt_masked`:

kvm_arch_mmu_enable_log_dirty_pt_masked
=======================================

.. c:function:: void kvm_arch_mmu_enable_log_dirty_pt_masked(struct kvm *kvm, struct kvm_memory_slot *slot, gfn_t gfn_offset, unsigned long mask)

    write protect dirty pages

    :param struct kvm \*kvm:
        The KVM pointer

    :param struct kvm_memory_slot \*slot:
        The memory slot associated with mask

    :param gfn_t gfn_offset:
        The gfn offset in memory slot

    :param unsigned long mask:
        The mask of dirty pages at offset 'gfn_offset' in this memory
        slot to be write protected

.. _`kvm_arch_mmu_enable_log_dirty_pt_masked.description`:

Description
-----------

Walks bits set in mask write protects the associated pte's. Caller must
acquire \ ``kvm``\ ->mmu_lock.

.. _`_kvm_mips_map_page_fast`:

\_kvm_mips_map_page_fast
========================

.. c:function:: int _kvm_mips_map_page_fast(struct kvm_vcpu *vcpu, unsigned long gpa, bool write_fault, pte_t *out_entry, pte_t *out_buddy)

    Fast path GPA fault handler.

    :param struct kvm_vcpu \*vcpu:
        VCPU pointer.

    :param unsigned long gpa:
        Guest physical address of fault.

    :param bool write_fault:
        Whether the fault was due to a write.

    :param pte_t \*out_entry:
        New PTE for \ ``gpa``\  (written on success unless NULL).

    :param pte_t \*out_buddy:
        New PTE for \ ``gpa``\ 's buddy (written on success unless
        NULL).

.. _`_kvm_mips_map_page_fast.description`:

Description
-----------

Perform fast path GPA fault handling, doing all that can be done without
calling into KVM. This handles marking old pages young (for idle page
tracking), and dirtying of clean pages (for dirty page logging).

.. _`_kvm_mips_map_page_fast.return`:

Return
------

0 on success, in which case we can update derived mappings and
resume guest execution.
-EFAULT on failure due to absent GPA mapping or write to
read-only page, in which case KVM must be consulted.

.. _`kvm_mips_map_page`:

kvm_mips_map_page
=================

.. c:function:: int kvm_mips_map_page(struct kvm_vcpu *vcpu, unsigned long gpa, bool write_fault, pte_t *out_entry, pte_t *out_buddy)

    Map a guest physical page.

    :param struct kvm_vcpu \*vcpu:
        VCPU pointer.

    :param unsigned long gpa:
        Guest physical address of fault.

    :param bool write_fault:
        Whether the fault was due to a write.

    :param pte_t \*out_entry:
        New PTE for \ ``gpa``\  (written on success unless NULL).

    :param pte_t \*out_buddy:
        New PTE for \ ``gpa``\ 's buddy (written on success unless
        NULL).

.. _`kvm_mips_map_page.description`:

Description
-----------

Handle GPA faults by creating a new GPA mapping (or updating an existing
one).

This takes care of marking pages young or dirty (idle/dirty page tracking),
asking KVM for the corresponding PFN, and creating a mapping in the GPA page
tables. Derived mappings (GVA page tables and TLBs) must be handled by the
caller.

.. _`kvm_mips_map_page.return`:

Return
------

0 on success, in which case the caller may use the \ ``out_entry``\ 
and \ ``out_buddy``\  PTEs to update derived mappings and resume guest
execution.
-EFAULT if there is no memory region at \ ``gpa``\  or a write was
attempted to a read-only memory region. This is usually handled
as an MMIO access.

.. _`kvm_mips_migrate_count`:

kvm_mips_migrate_count
======================

.. c:function:: void kvm_mips_migrate_count(struct kvm_vcpu *vcpu)

    Migrate timer.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

.. _`kvm_mips_migrate_count.description`:

Description
-----------

Migrate CP0_Count hrtimer to the current CPU by cancelling and restarting it
if it was running prior to being cancelled.

Must be called when the VCPU is migrated to a different CPU to ensure that
timer expiry during guest execution interrupts the guest and causes the
interrupt to be delivered in a timely manner.

.. _`kvm_trap_emul_gva_fault`:

kvm_trap_emul_gva_fault
=======================

.. c:function:: enum kvm_mips_fault_result kvm_trap_emul_gva_fault(struct kvm_vcpu *vcpu, unsigned long gva, bool write)

    Safely attempt to handle a GVA access fault.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

    :param unsigned long gva:
        Guest virtual address to be accessed.

    :param bool write:
        True if write attempted (must be dirtied and made writable).

.. _`kvm_trap_emul_gva_fault.description`:

Description
-----------

Safely attempt to handle a GVA fault, mapping GVA pages if necessary, and
dirtying the page if \ ``write``\  so that guest instructions can be modified.

.. _`kvm_trap_emul_gva_fault.return`:

Return
------

KVM_MIPS_MAPPED on success.
KVM_MIPS_GVA if bad guest virtual address.
KVM_MIPS_GPA if bad guest physical address.
KVM_MIPS_TLB if guest TLB not present.
KVM_MIPS_TLBINV if guest TLB present but not valid.
KVM_MIPS_TLBMOD if guest TLB read only.

.. This file was automatic generated / don't edit.

