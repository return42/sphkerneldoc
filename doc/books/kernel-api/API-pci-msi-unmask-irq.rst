.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-msi-unmask-irq:

==================
pci_msi_unmask_irq
==================

*man pci_msi_unmask_irq(9)*

*4.6.0-rc5*

Generic irq chip callback to unmask PCI/MSI interrupts


Synopsis
========

.. c:function:: void pci_msi_unmask_irq( struct irq_data * data )

Arguments
=========

``data``
    pointer to irqdata associated to that interrupt


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
