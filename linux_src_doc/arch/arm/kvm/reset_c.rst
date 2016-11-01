.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kvm/reset.c

.. _`kvm_reset_vcpu`:

kvm_reset_vcpu
==============

.. c:function:: int kvm_reset_vcpu(struct kvm_vcpu *vcpu)

    sets core registers and cp15 registers to reset value

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

.. _`kvm_reset_vcpu.description`:

Description
-----------

This function finds the right table above and sets the registers on the
virtual CPU struct to their architecturally defined reset values.

.. This file was automatic generated / don't edit.

