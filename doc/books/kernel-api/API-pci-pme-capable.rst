
.. _API-pci-pme-capable:

===============
pci_pme_capable
===============

*man pci_pme_capable(9)*

*4.6.0-rc1*

check the capability of PCI device to generate PME#


Synopsis
========

.. c:function:: bool pci_pme_capable( struct pci_dev * dev, pci_power_t state )

Arguments
=========

``dev``
    PCI device to handle.

``state``
    PCI state from which device will issue PME#.
