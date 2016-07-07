.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kvm/handle_exit.c

.. _`kvm_handle_wfx`:

kvm_handle_wfx
==============

.. c:function:: int kvm_handle_wfx(struct kvm_vcpu *vcpu, struct kvm_run *run)

    handle a wait-for-interrupts or wait-for-event instruction executed by a guest

    :param struct kvm_vcpu \*vcpu:
        the vcpu pointer

    :param struct kvm_run \*run:
        *undescribed*

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

.. _`kvm_handle_guest_debug`:

kvm_handle_guest_debug
======================

.. c:function:: int kvm_handle_guest_debug(struct kvm_vcpu *vcpu, struct kvm_run *run)

    handle a debug exception instruction

    :param struct kvm_vcpu \*vcpu:
        the vcpu pointer

    :param struct kvm_run \*run:
        access to the kvm_run structure for results

.. _`kvm_handle_guest_debug.description`:

Description
-----------

We route all debug exceptions through the same handler. If both the
guest and host are using the same debug facilities it will be up to
userspace to re-inject the correct exception for guest delivery.

.. This file was automatic generated / don't edit.

