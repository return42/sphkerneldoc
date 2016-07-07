.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kvm/hyp/tlb.c

.. _`__tlb_flush_vmid`:

__tlb_flush_vmid
================

.. c:function:: void __hyp_text __tlb_flush_vmid(struct kvm *kvm)

    VMID TLBs

    :param struct kvm \*kvm:
        *undescribed*

.. _`__tlb_flush_vmid.description`:

Description
-----------

__kvm_tlb_flush_vmid(struct kvm \*kvm);

We rely on the hardware to broadcast the TLB invalidation to all CPUs
inside the inner-shareable domain (which is the case for all v7
implementations).  If we come across a non-IS SMP implementation, we'll
have to use an IPI based mechanism. Until then, we stick to the simple
hardware assisted version.

As v7 does not support flushing per IPA, just nuke the whole TLB
instead, ignoring the ipa value.

.. This file was automatic generated / don't edit.

