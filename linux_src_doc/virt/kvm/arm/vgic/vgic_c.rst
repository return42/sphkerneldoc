.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic.c

.. _`vgic_target_oracle`:

vgic_target_oracle
==================

.. c:function:: struct kvm_vcpu *vgic_target_oracle(struct vgic_irq *irq)

    compute the target vcpu for an irq

    :param struct vgic_irq \*irq:
        The irq to route. Must be already locked.

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

.. c:function:: int kvm_vgic_inject_irq(struct kvm *kvm, int cpuid, unsigned int intid, bool level)

    Inject an IRQ from a device to the vgic

    :param struct kvm \*kvm:
        The VM structure pointer

    :param int cpuid:
        The CPU for PPIs

    :param unsigned int intid:
        The INTID to inject a new state to.

    :param bool level:
        Edge-triggered:  true:  to trigger the interrupt
        false: to ignore the call
        Level-sensitive  true:  raise the input signal
        false: lower the input signal

.. _`kvm_vgic_inject_irq.description`:

Description
-----------

The VGIC is not concerned with devices being active-LOW or active-HIGH for
level-sensitive interrupts.  You can think of the level parameter as 1
being HIGH and 0 being LOW and all devices being active-HIGH.

.. _`vgic_prune_ap_list`:

vgic_prune_ap_list
==================

.. c:function:: void vgic_prune_ap_list(struct kvm_vcpu *vcpu)

    Remove non-relevant interrupts from the list

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

.. _`vgic_prune_ap_list.description`:

Description
-----------

Go over the list of "interesting" interrupts, and prune those that we
won't have to consider in the near future.

.. This file was automatic generated / don't edit.
