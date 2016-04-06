
.. _API-pci-msi-mask-irq:

================
pci_msi_mask_irq
================

*man pci_msi_mask_irq(9)*

*4.6.0-rc1*

Generic irq chip callback to mask PCI/MSI interrupts


Synopsis
========

.. c:function:: void pci_msi_mask_irq( struct irq_data * data )

Arguments
=========

``data``
    pointer to irqdata associated to that interrupt
