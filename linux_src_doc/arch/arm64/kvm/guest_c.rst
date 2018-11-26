.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kvm/guest.c

.. _`num_timer_regs`:

NUM_TIMER_REGS
==============

.. c:function::  NUM_TIMER_REGS()

.. _`kvm_arm_num_regs`:

kvm_arm_num_regs
================

.. c:function:: unsigned long kvm_arm_num_regs(struct kvm_vcpu *vcpu)

    how many registers do we present via KVM_GET_ONE_REG

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_arm_num_regs.description`:

Description
-----------

This is for all registers.

.. _`kvm_arm_copy_reg_indices`:

kvm_arm_copy_reg_indices
========================

.. c:function:: int kvm_arm_copy_reg_indices(struct kvm_vcpu *vcpu, u64 __user *uindices)

    get indices of all registers.

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

    :param uindices:
        *undescribed*
    :type uindices: u64 __user \*

.. _`kvm_arm_copy_reg_indices.description`:

Description
-----------

We do core registers right here, then we append system regs.

.. _`kvm_arch_vcpu_ioctl_set_guest_debug`:

kvm_arch_vcpu_ioctl_set_guest_debug
===================================

.. c:function:: int kvm_arch_vcpu_ioctl_set_guest_debug(struct kvm_vcpu *vcpu, struct kvm_guest_debug *dbg)

    set up guest debugging

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

    :param dbg:
        *undescribed*
    :type dbg: struct kvm_guest_debug \*

.. _`kvm_arch_vcpu_ioctl_set_guest_debug.description`:

Description
-----------

This sets up and enables the VM for guest debugging. Userspace
passes in a control flag to enable different debug types and
potentially other architecture specific information in the rest of
the structure.

.. This file was automatic generated / don't edit.

