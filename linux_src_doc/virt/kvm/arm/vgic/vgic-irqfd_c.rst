.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/vgic/vgic-irqfd.c

.. _`vgic_irqfd_set_irq`:

vgic_irqfd_set_irq
==================

.. c:function:: int vgic_irqfd_set_irq(struct kvm_kernel_irq_routing_entry *e, struct kvm *kvm, int irq_source_id, int level, bool line_status)

    inject the IRQ corresponding to the irqchip routing entry

    :param struct kvm_kernel_irq_routing_entry \*e:
        *undescribed*

    :param struct kvm \*kvm:
        *undescribed*

    :param int irq_source_id:
        *undescribed*

    :param int level:
        *undescribed*

    :param bool line_status:
        *undescribed*

.. _`vgic_irqfd_set_irq.description`:

Description
-----------

This is the entry point for irqfd IRQ injection

.. _`kvm_set_routing_entry`:

kvm_set_routing_entry
=====================

.. c:function:: int kvm_set_routing_entry(struct kvm *kvm, struct kvm_kernel_irq_routing_entry *e, const struct kvm_irq_routing_entry *ue)

    populate a kvm routing entry from a user routing entry

    :param struct kvm \*kvm:
        the VM this entry is applied to

    :param struct kvm_kernel_irq_routing_entry \*e:
        kvm kernel routing entry handle

    :param const struct kvm_irq_routing_entry \*ue:
        user api routing entry handle
        return 0 on success, -EINVAL on errors.

.. _`kvm_set_msi`:

kvm_set_msi
===========

.. c:function:: int kvm_set_msi(struct kvm_kernel_irq_routing_entry *e, struct kvm *kvm, int irq_source_id, int level, bool line_status)

    inject the MSI corresponding to the MSI routing entry

    :param struct kvm_kernel_irq_routing_entry \*e:
        *undescribed*

    :param struct kvm \*kvm:
        *undescribed*

    :param int irq_source_id:
        *undescribed*

    :param int level:
        *undescribed*

    :param bool line_status:
        *undescribed*

.. _`kvm_set_msi.description`:

Description
-----------

This is the entry point for irqfd MSI injection
and userspace MSI injection.

.. This file was automatic generated / don't edit.

