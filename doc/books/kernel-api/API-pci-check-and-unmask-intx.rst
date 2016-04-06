
.. _API-pci-check-and-unmask-intx:

=========================
pci_check_and_unmask_intx
=========================

*man pci_check_and_unmask_intx(9)*

*4.6.0-rc1*

unmask INTx if no interrupt is pending


Synopsis
========

.. c:function:: bool pci_check_and_unmask_intx( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device to operate on


Description
===========

Check if the device dev has its INTx line asserted, unmask it if not and return true. False is returned and the mask remains active if there was still an interrupt pending.
