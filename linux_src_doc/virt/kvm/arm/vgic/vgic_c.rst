.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic.c

.. _`vgic_target_oracle`:

vgic_target_oracle
==================

.. c:function:: struct kvm_vcpu *vgic_target_oracle(struct vgic_irq *irq)

    compute the target vcpu for an irq

    :param irq:
        The irq to route. Must be already locked.
    :type irq: struct vgic_irq \*

.. _`vgic_target_oracle.description`:

Description
-----------

Based on the current state of the interrupt (enabled, pending,
active, vcpu and target_vcpu), compute the next vcpu this should be
given to. Return NULL if this shouldn't be injected at all.

Requires the IRQ lock to be held.

.. _`kvm_vgic_inject_irq`:

kvm_vgic_inject_irq
===================

.. c:function:: int kvm_vgic_inject_irq(struct kvm *kvm, int cpuid, unsigned int intid, bool level, void *owner)

    Inject an IRQ from a device to the vgic

    :param kvm:
        The VM structure pointer
    :type kvm: struct kvm \*

    :param cpuid:
        The CPU for PPIs
    :type cpuid: int

    :param intid:
        The INTID to inject a new state to.
    :type intid: unsigned int

    :param level:
        Edge-triggered:  true:  to trigger the interrupt
        false: to ignore the call
        Level-sensitive  true:  raise the input signal
        false: lower the input signal
    :type level: bool

    :param owner:
        The opaque pointer to the owner of the IRQ being raised to verify
        that the caller is allowed to inject this IRQ.  Userspace
        injections will have owner == NULL.
    :type owner: void \*

.. _`kvm_vgic_inject_irq.description`:

Description
-----------

The VGIC is not concerned with devices being active-LOW or active-HIGH for
level-sensitive interrupts.  You can think of the level parameter as 1
being HIGH and 0 being LOW and all devices being active-HIGH.

.. _`kvm_vgic_reset_mapped_irq`:

kvm_vgic_reset_mapped_irq
=========================

.. c:function:: void kvm_vgic_reset_mapped_irq(struct kvm_vcpu *vcpu, u32 vintid)

    Reset a mapped IRQ

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

    :param vintid:
        The INTID of the interrupt
    :type vintid: u32

.. _`kvm_vgic_reset_mapped_irq.description`:

Description
-----------

Reset the active and pending states of a mapped interrupt.  Kernel
subsystems injecting mapped interrupts should reset their interrupt lines
when we are doing a reset of the VM.

.. _`kvm_vgic_set_owner`:

kvm_vgic_set_owner
==================

.. c:function:: int kvm_vgic_set_owner(struct kvm_vcpu *vcpu, unsigned int intid, void *owner)

    Set the owner of an interrupt for a VM

    :param vcpu:
        Pointer to the VCPU (used for PPIs)
    :type vcpu: struct kvm_vcpu \*

    :param intid:
        The virtual INTID identifying the interrupt (PPI or SPI)
    :type intid: unsigned int

    :param owner:
        Opaque pointer to the owner
    :type owner: void \*

.. _`kvm_vgic_set_owner.description`:

Description
-----------

Returns 0 if intid is not already used by another in-kernel device and the
owner is set, otherwise returns an error code.

.. _`vgic_prune_ap_list`:

vgic_prune_ap_list
==================

.. c:function:: void vgic_prune_ap_list(struct kvm_vcpu *vcpu)

    Remove non-relevant interrupts from the list

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

.. _`vgic_prune_ap_list.description`:

Description
-----------

Go over the list of "interesting" interrupts, and prune those that we
won't have to consider in the near future.

.. This file was automatic generated / don't edit.

