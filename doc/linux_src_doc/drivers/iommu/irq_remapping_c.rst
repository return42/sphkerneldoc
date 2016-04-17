.. -*- coding: utf-8; mode: rst -*-

===============
irq_remapping.c
===============


.. _`irq_remapping_get_ir_irq_domain`:

irq_remapping_get_ir_irq_domain
===============================

.. c:function:: struct irq_domain *irq_remapping_get_ir_irq_domain (struct irq_alloc_info *info)

    Get the irqdomain associated with the IOMMU device serving request @info

    :param struct irq_alloc_info \*info:
        interrupt allocation information, used to identify the IOMMU device



.. _`irq_remapping_get_ir_irq_domain.description`:

Description
-----------

It's used to get parent irqdomain for HPET and IOAPIC irqdomains.
Returns pointer to IRQ domain, or NULL on failure.



.. _`irq_remapping_get_irq_domain`:

irq_remapping_get_irq_domain
============================

.. c:function:: struct irq_domain *irq_remapping_get_irq_domain (struct irq_alloc_info *info)

    Get the irqdomain serving the request @info

    :param struct irq_alloc_info \*info:
        interrupt allocation information, used to identify the IOMMU device



.. _`irq_remapping_get_irq_domain.description`:

Description
-----------

There will be one PCI MSI/MSIX irqdomain associated with each interrupt
remapping device, so this interface is used to retrieve the PCI MSI/MSIX
irqdomain serving request ``info``\ .
Returns pointer to IRQ domain, or NULL on failure.

