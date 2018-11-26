.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/mmio.c

.. _`kvm_handle_mmio_return`:

kvm_handle_mmio_return
======================

.. c:function:: int kvm_handle_mmio_return(struct kvm_vcpu *vcpu, struct kvm_run *run)

    - Handle MMIO loads after user space emulation or in-kernel IO emulation

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

    :param run:
        The VCPU run struct containing the mmio data
    :type run: struct kvm_run \*

.. This file was automatic generated / don't edit.

