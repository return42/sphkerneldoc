.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kvm/tlb.c

.. _`clear_root_gid`:

clear_root_gid
==============

.. c:function:: void clear_root_gid( void)

    Set GuestCtl1.RID for normal root operation.

    :param void:
        no arguments
    :type void: 

.. _`set_root_gid_to_guest_gid`:

set_root_gid_to_guest_gid
=========================

.. c:function:: void set_root_gid_to_guest_gid( void)

    Set GuestCtl1.RID to match GuestCtl1.ID.

    :param void:
        no arguments
    :type void: 

.. _`set_root_gid_to_guest_gid.description`:

Description
-----------

Sets the root GuestID to match the current guest GuestID, for TLB operation
on the GPA->RPA mappings in the root TLB.

The caller must be sure to disable HTW while the root GID is set, and
possibly longer if TLB registers are modified.

.. _`kvm_vz_guest_tlb_lookup`:

kvm_vz_guest_tlb_lookup
=======================

.. c:function:: int kvm_vz_guest_tlb_lookup(struct kvm_vcpu *vcpu, unsigned long gva, unsigned long *gpa)

    Lookup a guest VZ TLB mapping.

    :param vcpu:
        KVM VCPU pointer.
    :type vcpu: struct kvm_vcpu \*

    :param gva:
        *undescribed*
    :type gva: unsigned long

    :param gpa:
        Ponter to output guest physical address it maps to.
    :type gpa: unsigned long \*

.. _`kvm_vz_guest_tlb_lookup.description`:

Description
-----------

Converts a guest virtual address in a guest TLB mapped segment to a guest
physical address, by probing the guest TLB.

.. _`kvm_vz_guest_tlb_lookup.return`:

Return
------

0 if guest TLB mapping exists for \ ``gva``\ . \*@gpa will have been
written.
-EFAULT if no guest TLB mapping exists for \ ``gva``\ . \*@gpa may not
have been written.

.. _`kvm_vz_local_flush_roottlb_all_guests`:

kvm_vz_local_flush_roottlb_all_guests
=====================================

.. c:function:: void kvm_vz_local_flush_roottlb_all_guests( void)

    Flush all root TLB entries for guests.

    :param void:
        no arguments
    :type void: 

.. _`kvm_vz_local_flush_roottlb_all_guests.description`:

Description
-----------

Invalidate all entries in root tlb which are GPA mappings.

.. _`kvm_vz_local_flush_guesttlb_all`:

kvm_vz_local_flush_guesttlb_all
===============================

.. c:function:: void kvm_vz_local_flush_guesttlb_all( void)

    Flush all guest TLB entries.

    :param void:
        no arguments
    :type void: 

.. _`kvm_vz_local_flush_guesttlb_all.description`:

Description
-----------

Invalidate all entries in guest tlb irrespective of guestid.

.. _`kvm_vz_save_guesttlb`:

kvm_vz_save_guesttlb
====================

.. c:function:: void kvm_vz_save_guesttlb(struct kvm_mips_tlb *buf, unsigned int index, unsigned int count)

    Save a range of guest TLB entries.

    :param buf:
        Buffer to write TLB entries into.
    :type buf: struct kvm_mips_tlb \*

    :param index:
        Start index.
    :type index: unsigned int

    :param count:
        Number of entries to save.
    :type count: unsigned int

.. _`kvm_vz_save_guesttlb.description`:

Description
-----------

Save a range of guest TLB entries. The caller must ensure interrupts are
disabled.

.. _`kvm_vz_load_guesttlb`:

kvm_vz_load_guesttlb
====================

.. c:function:: void kvm_vz_load_guesttlb(const struct kvm_mips_tlb *buf, unsigned int index, unsigned int count)

    Save a range of guest TLB entries.

    :param buf:
        Buffer to read TLB entries from.
    :type buf: const struct kvm_mips_tlb \*

    :param index:
        Start index.
    :type index: unsigned int

    :param count:
        Number of entries to load.
    :type count: unsigned int

.. _`kvm_vz_load_guesttlb.description`:

Description
-----------

Load a range of guest TLB entries. The caller must ensure interrupts are
disabled.

.. _`kvm_mips_suspend_mm`:

kvm_mips_suspend_mm
===================

.. c:function:: void kvm_mips_suspend_mm(int cpu)

    Suspend the active mm. \ ``cpu``\          The CPU we're running on.

    :param cpu:
        *undescribed*
    :type cpu: int

.. _`kvm_mips_suspend_mm.description`:

Description
-----------

Suspend the active_mm, ready for a switch to a KVM guest virtual address
space. This is left active for the duration of guest context, including time
with interrupts enabled, so we need to be careful not to confuse e.g. cache
management IPIs.

\ :c:func:`kvm_mips_resume_mm`\  should be called before context switching to a different
process so we don't need to worry about reference counting.

This needs to be in static kernel code to avoid exporting init_mm.

.. _`kvm_mips_resume_mm`:

kvm_mips_resume_mm
==================

.. c:function:: void kvm_mips_resume_mm(int cpu)

    Resume the current process mm. \ ``cpu``\          The CPU we're running on.

    :param cpu:
        *undescribed*
    :type cpu: int

.. _`kvm_mips_resume_mm.description`:

Description
-----------

Resume the mm of the current process, after a switch back from a KVM guest
virtual address space (see \ :c:func:`kvm_mips_suspend_mm`\ ).

.. This file was automatic generated / don't edit.

