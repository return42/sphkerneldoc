.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kvm/guest.c

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

We do core registers right here, then we append coproc regs.

.. This file was automatic generated / don't edit.

