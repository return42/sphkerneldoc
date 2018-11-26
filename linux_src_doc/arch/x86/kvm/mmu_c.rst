.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kvm/mmu.c

.. _`kvm_mmu_write_protect_pt_masked`:

kvm_mmu_write_protect_pt_masked
===============================

.. c:function:: void kvm_mmu_write_protect_pt_masked(struct kvm *kvm, struct kvm_memory_slot *slot, gfn_t gfn_offset, unsigned long mask)

    write protect selected PT level pages

    :param kvm:
        kvm instance
    :type kvm: struct kvm \*

    :param slot:
        slot to protect
    :type slot: struct kvm_memory_slot \*

    :param gfn_offset:
        start of the BITS_PER_LONG pages we care about
    :type gfn_offset: gfn_t

    :param mask:
        indicates which pages we should protect
    :type mask: unsigned long

.. _`kvm_mmu_write_protect_pt_masked.used-when-we-do-not-need-to-care-about-huge-page-mappings`:

Used when we do not need to care about huge page mappings
---------------------------------------------------------

e.g. during dirty
logging we do not have any such mappings.

.. _`kvm_mmu_clear_dirty_pt_masked`:

kvm_mmu_clear_dirty_pt_masked
=============================

.. c:function:: void kvm_mmu_clear_dirty_pt_masked(struct kvm *kvm, struct kvm_memory_slot *slot, gfn_t gfn_offset, unsigned long mask)

    clear MMU D-bit for PT level pages, or write protect the page if the D-bit isn't supported.

    :param kvm:
        kvm instance
    :type kvm: struct kvm \*

    :param slot:
        slot to clear D-bit
    :type slot: struct kvm_memory_slot \*

    :param gfn_offset:
        start of the BITS_PER_LONG pages we care about
    :type gfn_offset: gfn_t

    :param mask:
        indicates which pages we should clear D-bit
    :type mask: unsigned long

.. _`kvm_mmu_clear_dirty_pt_masked.description`:

Description
-----------

Used for PML to re-log the dirty GPAs after userspace querying dirty_bitmap.

.. _`kvm_arch_mmu_enable_log_dirty_pt_masked`:

kvm_arch_mmu_enable_log_dirty_pt_masked
=======================================

.. c:function:: void kvm_arch_mmu_enable_log_dirty_pt_masked(struct kvm *kvm, struct kvm_memory_slot *slot, gfn_t gfn_offset, unsigned long mask)

    enable dirty logging for selected PT level pages.

    :param kvm:
        *undescribed*
    :type kvm: struct kvm \*

    :param slot:
        *undescribed*
    :type slot: struct kvm_memory_slot \*

    :param gfn_offset:
        *undescribed*
    :type gfn_offset: gfn_t

    :param mask:
        *undescribed*
    :type mask: unsigned long

.. _`kvm_arch_mmu_enable_log_dirty_pt_masked.description`:

Description
-----------

It calls kvm_mmu_write_protect_pt_masked to write protect selected pages to
enable dirty logging for them.

.. _`kvm_arch_mmu_enable_log_dirty_pt_masked.used-when-we-do-not-need-to-care-about-huge-page-mappings`:

Used when we do not need to care about huge page mappings
---------------------------------------------------------

e.g. during dirty
logging we do not have any such mappings.

.. _`kvm_arch_write_log_dirty`:

kvm_arch_write_log_dirty
========================

.. c:function:: int kvm_arch_write_log_dirty(struct kvm_vcpu *vcpu)

    emulate dirty page logging

    :param vcpu:
        Guest mode vcpu
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_arch_write_log_dirty.description`:

Description
-----------

Emulate arch specific page modification logging for the
nested hypervisor

.. This file was automatic generated / don't edit.

