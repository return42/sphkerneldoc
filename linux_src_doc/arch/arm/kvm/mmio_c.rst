.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kvm/mmio.c

.. _`kvm_handle_mmio_return`:

kvm_handle_mmio_return
======================

.. c:function:: int kvm_handle_mmio_return(struct kvm_vcpu *vcpu, struct kvm_run *run)

    - Handle MMIO loads after user space emulation or in-kernel IO emulation

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

    :param struct kvm_run \*run:
        The VCPU run struct containing the mmio data

.. This file was automatic generated / don't edit.

