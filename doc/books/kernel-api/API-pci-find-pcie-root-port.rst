
.. _API-pci-find-pcie-root-port:

=======================
pci_find_pcie_root_port
=======================

*man pci_find_pcie_root_port(9)*

*4.6.0-rc1*

return PCIe Root Port


Synopsis
========

.. c:function:: struct pci_dev ⋆ pci_find_pcie_root_port( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to query


Description
===========

Traverse up the parent chain and return the PCIe Root Port PCI Device for a given PCI Device.
