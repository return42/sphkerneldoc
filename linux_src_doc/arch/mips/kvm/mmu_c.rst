.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kvm/mmu.c

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

.. This file was automatic generated / don't edit.

