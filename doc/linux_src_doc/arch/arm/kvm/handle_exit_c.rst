.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kvm/handle_exit.c

.. _`kvm_handle_wfx`:

kvm_handle_wfx
==============

.. c:function:: int kvm_handle_wfx(struct kvm_vcpu *vcpu, struct kvm_run *run)

    handle a WFI or WFE instructions trapped in guests

    :param struct kvm_vcpu \*vcpu:
        the vcpu pointer

    :param struct kvm_run \*run:
        the kvm_run structure pointer

.. _`kvm_handle_wfx.wfe`:

WFE
---

Yield the CPU and come back to this vcpu when the scheduler
decides to.

.. _`kvm_handle_wfx.wfi`:

WFI
---

Simply call \ :c:func:`kvm_vcpu_block`\ , which will halt execution of
world-switches and schedule other host processes until there is an
incoming IRQ or FIQ to the VM.

.. This file was automatic generated / don't edit.

