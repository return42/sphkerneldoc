
.. _API-pci-msi-unmask-irq:

==================
pci_msi_unmask_irq
==================

*man pci_msi_unmask_irq(9)*

*4.6.0-rc1*

Generic irq chip callback to unmask PCI/MSI interrupts


Synopsis
========

.. c:function:: void pci_msi_unmask_irq( struct irq_data * data )

Arguments
=========

``data``
    pointer to irqdata associated to that interrupt
