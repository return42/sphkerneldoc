.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kvm/vz.c

.. _`kvm_vz_should_use_htimer`:

kvm_vz_should_use_htimer
========================

.. c:function:: bool kvm_vz_should_use_htimer(struct kvm_vcpu *vcpu)

    Find whether to use the VZ hard guest timer.

    :param vcpu:
        Virtual CPU.
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_vz_should_use_htimer.return`:

Return
------

true if the VZ GTOffset & real guest CP0_Count should be used
instead of software emulation of guest timer.
false otherwise.

.. _`_kvm_vz_restore_stimer`:

\_kvm_vz_restore_stimer
=======================

.. c:function:: void _kvm_vz_restore_stimer(struct kvm_vcpu *vcpu, u32 compare, u32 cause)

    Restore soft timer state.

    :param vcpu:
        Virtual CPU.
    :type vcpu: struct kvm_vcpu \*

    :param compare:
        CP0_Compare register value, restored by caller.
    :type compare: u32

    :param cause:
        CP0_Cause register to restore.
    :type cause: u32

.. _`_kvm_vz_restore_stimer.description`:

Description
-----------

Restore VZ state relating to the soft timer. The hard timer can be enabled
later.

.. _`_kvm_vz_restore_htimer`:

\_kvm_vz_restore_htimer
=======================

.. c:function:: void _kvm_vz_restore_htimer(struct kvm_vcpu *vcpu, u32 compare, u32 cause)

    Restore hard timer state.

    :param vcpu:
        Virtual CPU.
    :type vcpu: struct kvm_vcpu \*

    :param compare:
        CP0_Compare register value, restored by caller.
    :type compare: u32

    :param cause:
        CP0_Cause register to restore.
    :type cause: u32

.. _`_kvm_vz_restore_htimer.description`:

Description
-----------

Restore hard timer Guest.Count & Guest.Cause taking care to preserve the
value of Guest.CP0_Cause.TI while restoring Guest.CP0_Cause.

.. _`kvm_vz_restore_timer`:

kvm_vz_restore_timer
====================

.. c:function:: void kvm_vz_restore_timer(struct kvm_vcpu *vcpu)

    Restore timer state.

    :param vcpu:
        Virtual CPU.
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_vz_restore_timer.description`:

Description
-----------

Restore soft timer state from saved context.

.. _`kvm_vz_acquire_htimer`:

kvm_vz_acquire_htimer
=====================

.. c:function:: void kvm_vz_acquire_htimer(struct kvm_vcpu *vcpu)

    Switch to hard timer state.

    :param vcpu:
        Virtual CPU.
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_vz_acquire_htimer.description`:

Description
-----------

Restore hard timer state on top of existing soft timer state if possible.

Since hard timer won't remain active over preemption, preemption should be
disabled by the caller.

.. _`_kvm_vz_save_htimer`:

\_kvm_vz_save_htimer
====================

.. c:function:: void _kvm_vz_save_htimer(struct kvm_vcpu *vcpu, u32 *out_compare, u32 *out_cause)

    Switch to software emulation of guest timer.

    :param vcpu:
        Virtual CPU.
    :type vcpu: struct kvm_vcpu \*

    :param out_compare:
        *undescribed*
    :type out_compare: u32 \*

    :param out_cause:
        *undescribed*
    :type out_cause: u32 \*

.. _`_kvm_vz_save_htimer.description`:

Description
-----------

Save VZ guest timer state and switch to software emulation of guest CP0
timer. The hard timer must already be in use, so preemption should be
disabled.

.. _`kvm_vz_save_timer`:

kvm_vz_save_timer
=================

.. c:function:: void kvm_vz_save_timer(struct kvm_vcpu *vcpu)

    Save guest timer state.

    :param vcpu:
        Virtual CPU.
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_vz_save_timer.description`:

Description
-----------

Save VZ guest timer state and switch to soft guest timer if hard timer was in
use.

.. _`kvm_vz_lose_htimer`:

kvm_vz_lose_htimer
==================

.. c:function:: void kvm_vz_lose_htimer(struct kvm_vcpu *vcpu)

    Ensure hard guest timer is not in use.

    :param vcpu:
        Virtual CPU.
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_vz_lose_htimer.description`:

Description
-----------

Transfers the state of the hard guest timer to the soft guest timer, leaving
guest state intact so it can continue to be used with the soft timer.

.. _`is_eva_access`:

is_eva_access
=============

.. c:function:: bool is_eva_access(union mips_instruction inst)

    Find whether an instruction is an EVA memory accessor.

    :param inst:
        32-bit instruction encoding.
    :type inst: union mips_instruction

.. _`is_eva_access.description`:

Description
-----------

Finds whether \ ``inst``\  encodes an EVA memory access instruction, which would
indicate that emulation of it should access the user mode address space
instead of the kernel mode address space. This matters for MUSUK segments
which are TLB mapped for user mode but unmapped for kernel mode.

.. _`is_eva_access.return`:

Return
------

Whether \ ``inst``\  encodes an EVA accessor instruction.

.. _`is_eva_am_mapped`:

is_eva_am_mapped
================

.. c:function:: bool is_eva_am_mapped(struct kvm_vcpu *vcpu, unsigned int am, bool eu)

    Find whether an access mode is mapped.

    :param vcpu:
        KVM VCPU state.
    :type vcpu: struct kvm_vcpu \*

    :param am:
        3-bit encoded access mode.
    :type am: unsigned int

    :param eu:
        Segment becomes unmapped and uncached when Status.ERL=1.
    :type eu: bool

.. _`is_eva_am_mapped.description`:

Description
-----------

Decode \ ``am``\  to find whether it encodes a mapped segment for the current VCPU
state. Where necessary \ ``eu``\  and the actual instruction causing the fault are
taken into account to make the decision.

.. _`is_eva_am_mapped.return`:

Return
------

Whether the VCPU faulted on a TLB mapped address.

.. _`kvm_vz_gva_to_gpa`:

kvm_vz_gva_to_gpa
=================

.. c:function:: int kvm_vz_gva_to_gpa(struct kvm_vcpu *vcpu, unsigned long gva, unsigned long *gpa)

    Convert valid GVA to GPA.

    :param vcpu:
        KVM VCPU state.
    :type vcpu: struct kvm_vcpu \*

    :param gva:
        Guest virtual address to convert.
    :type gva: unsigned long

    :param gpa:
        Output guest physical address.
    :type gpa: unsigned long \*

.. _`kvm_vz_gva_to_gpa.description`:

Description
-----------

Convert a guest virtual address (GVA) which is valid according to the guest
context, to a guest physical address (GPA).

.. _`kvm_vz_gva_to_gpa.return`:

Return
------

0 on success.
-errno on failure.

.. _`kvm_vz_badvaddr_to_gpa`:

kvm_vz_badvaddr_to_gpa
======================

.. c:function:: int kvm_vz_badvaddr_to_gpa(struct kvm_vcpu *vcpu, unsigned long badvaddr, unsigned long *gpa)

    Convert GVA BadVAddr from root exception to GPA.

    :param vcpu:
        KVM VCPU state.
    :type vcpu: struct kvm_vcpu \*

    :param badvaddr:
        Root BadVAddr.
    :type badvaddr: unsigned long

    :param gpa:
        Output guest physical address.
    :type gpa: unsigned long \*

.. _`kvm_vz_badvaddr_to_gpa.description`:

Description
-----------

VZ implementations are permitted to report guest virtual addresses (GVA) in
BadVAddr on a root exception during guest execution, instead of the more
convenient guest physical addresses (GPA). When we get a GVA, this function
converts it to a GPA, taking into account guest segmentation and guest TLB
state.

.. _`kvm_vz_badvaddr_to_gpa.return`:

Return
------

0 on success.
-errno on failure.

.. _`kvm_trap_vz_handle_cop_unusable`:

kvm_trap_vz_handle_cop_unusable
===============================

.. c:function:: int kvm_trap_vz_handle_cop_unusable(struct kvm_vcpu *vcpu)

    Guest used unusable coprocessor.

    :param vcpu:
        Virtual CPU context.
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_trap_vz_handle_cop_unusable.description`:

Description
-----------

Handle when the guest attempts to use a coprocessor which hasn't been allowed
by the root context.

.. _`kvm_trap_vz_handle_msa_disabled`:

kvm_trap_vz_handle_msa_disabled
===============================

.. c:function:: int kvm_trap_vz_handle_msa_disabled(struct kvm_vcpu *vcpu)

    Guest used MSA while disabled in root.

    :param vcpu:
        Virtual CPU context.
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_trap_vz_handle_msa_disabled.description`:

Description
-----------

Handle when the guest attempts to use MSA when it is disabled in the root
context.

.. _`kvm_vz_resize_guest_vtlb`:

kvm_vz_resize_guest_vtlb
========================

.. c:function:: unsigned int kvm_vz_resize_guest_vtlb(unsigned int size)

    Attempt to resize guest VTLB.

    :param size:
        Number of guest VTLB entries (0 < \ ``size``\  <= root VTLB entries).
    :type size: unsigned int

.. _`kvm_vz_resize_guest_vtlb.description`:

Description
-----------

Attempt to resize the guest VTLB by writing guest Config registers. This is
necessary for cores with a shared root/guest TLB to avoid overlap with wired
entries in the root VTLB.

.. _`kvm_vz_resize_guest_vtlb.return`:

Return
------

The resulting guest VTLB size.

.. This file was automatic generated / don't edit.

