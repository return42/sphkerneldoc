.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/controller/dwc/pci-keystone.c

.. _`ks_pcie_legacy_irq_handler`:

ks_pcie_legacy_irq_handler
==========================

.. c:function:: void ks_pcie_legacy_irq_handler(struct irq_desc *desc)

    Handle legacy interrupt

    :param struct irq_desc \*desc:
        Pointer to irq descriptor

.. _`ks_pcie_legacy_irq_handler.description`:

Description
-----------

Traverse through pending legacy interrupts and invoke handler for each. Also
takes care of interrupt controller level mask/ack operation.

.. This file was automatic generated / don't edit.

