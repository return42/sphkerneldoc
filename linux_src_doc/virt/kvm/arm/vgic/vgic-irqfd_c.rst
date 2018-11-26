.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-irqfd.c

.. _`vgic_irqfd_set_irq`:

vgic_irqfd_set_irq
==================

.. c:function:: int vgic_irqfd_set_irq(struct kvm_kernel_irq_routing_entry *e, struct kvm *kvm, int irq_source_id, int level, bool line_status)

    inject the IRQ corresponding to the irqchip routing entry

    :param e:
        *undescribed*
    :type e: struct kvm_kernel_irq_routing_entry \*

    :param kvm:
        *undescribed*
    :type kvm: struct kvm \*

    :param irq_source_id:
        *undescribed*
    :type irq_source_id: int

    :param level:
        *undescribed*
    :type level: int

    :param line_status:
        *undescribed*
    :type line_status: bool

.. _`vgic_irqfd_set_irq.description`:

Description
-----------

This is the entry point for irqfd IRQ injection

.. _`kvm_set_routing_entry`:

kvm_set_routing_entry
=====================

.. c:function:: int kvm_set_routing_entry(struct kvm *kvm, struct kvm_kernel_irq_routing_entry *e, const struct kvm_irq_routing_entry *ue)

    populate a kvm routing entry from a user routing entry

    :param kvm:
        the VM this entry is applied to
    :type kvm: struct kvm \*

    :param e:
        kvm kernel routing entry handle
    :type e: struct kvm_kernel_irq_routing_entry \*

    :param ue:
        user api routing entry handle
        return 0 on success, -EINVAL on errors.
    :type ue: const struct kvm_irq_routing_entry \*

.. _`kvm_set_msi`:

kvm_set_msi
===========

.. c:function:: int kvm_set_msi(struct kvm_kernel_irq_routing_entry *e, struct kvm *kvm, int irq_source_id, int level, bool line_status)

    inject the MSI corresponding to the MSI routing entry

    :param e:
        *undescribed*
    :type e: struct kvm_kernel_irq_routing_entry \*

    :param kvm:
        *undescribed*
    :type kvm: struct kvm \*

    :param irq_source_id:
        *undescribed*
    :type irq_source_id: int

    :param level:
        *undescribed*
    :type level: int

    :param line_status:
        *undescribed*
    :type line_status: bool

.. _`kvm_set_msi.description`:

Description
-----------

This is the entry point for irqfd MSI injection
and userspace MSI injection.

.. This file was automatic generated / don't edit.

