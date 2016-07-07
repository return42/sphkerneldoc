.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kvm/mmu.c

.. _`kvm_mmu_write_protect_pt_masked`:

kvm_mmu_write_protect_pt_masked
===============================

.. c:function:: void kvm_mmu_write_protect_pt_masked(struct kvm *kvm, struct kvm_memory_slot *slot, gfn_t gfn_offset, unsigned long mask)

    write protect selected PT level pages

    :param struct kvm \*kvm:
        kvm instance

    :param struct kvm_memory_slot \*slot:
        slot to protect

    :param gfn_t gfn_offset:
        start of the BITS_PER_LONG pages we care about

    :param unsigned long mask:
        indicates which pages we should protect

.. _`kvm_mmu_write_protect_pt_masked.used-when-we-do-not-need-to-care-about-huge-page-mappings`:

Used when we do not need to care about huge page mappings
---------------------------------------------------------

e.g. during dirty
logging we do not have any such mappings.

.. _`kvm_mmu_clear_dirty_pt_masked`:

kvm_mmu_clear_dirty_pt_masked
=============================

.. c:function:: void kvm_mmu_clear_dirty_pt_masked(struct kvm *kvm, struct kvm_memory_slot *slot, gfn_t gfn_offset, unsigned long mask)

    clear MMU D-bit for PT level pages

    :param struct kvm \*kvm:
        kvm instance

    :param struct kvm_memory_slot \*slot:
        slot to clear D-bit

    :param gfn_t gfn_offset:
        start of the BITS_PER_LONG pages we care about

    :param unsigned long mask:
        indicates which pages we should clear D-bit

.. _`kvm_mmu_clear_dirty_pt_masked.description`:

Description
-----------

Used for PML to re-log the dirty GPAs after userspace querying dirty_bitmap.

.. _`kvm_arch_mmu_enable_log_dirty_pt_masked`:

kvm_arch_mmu_enable_log_dirty_pt_masked
=======================================

.. c:function:: void kvm_arch_mmu_enable_log_dirty_pt_masked(struct kvm *kvm, struct kvm_memory_slot *slot, gfn_t gfn_offset, unsigned long mask)

    enable dirty logging for selected PT level pages.

    :param struct kvm \*kvm:
        *undescribed*

    :param struct kvm_memory_slot \*slot:
        *undescribed*

    :param gfn_t gfn_offset:
        *undescribed*

    :param unsigned long mask:
        *undescribed*

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

.. This file was automatic generated / don't edit.

