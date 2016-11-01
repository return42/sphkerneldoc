.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kvm/reset.c

.. _`kvm_arch_dev_ioctl_check_extension`:

kvm_arch_dev_ioctl_check_extension
==================================

.. c:function:: int kvm_arch_dev_ioctl_check_extension(struct kvm *kvm, long ext)

    :param struct kvm \*kvm:
        *undescribed*

    :param long ext:
        *undescribed*

.. _`kvm_arch_dev_ioctl_check_extension.description`:

Description
-----------

We currently assume that the number of HW registers is uniform
across all CPUs (see cpuinfo_sanity_check).

.. _`kvm_reset_vcpu`:

kvm_reset_vcpu
==============

.. c:function:: int kvm_reset_vcpu(struct kvm_vcpu *vcpu)

    sets core registers and sys_regs to reset value

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

.. _`kvm_reset_vcpu.description`:

Description
-----------

This function finds the right table above and sets the registers on
the virtual CPU struct to their architecturally defined reset
values.

.. This file was automatic generated / don't edit.

