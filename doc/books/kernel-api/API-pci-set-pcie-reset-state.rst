
.. _API-pci-set-pcie-reset-state:

========================
pci_set_pcie_reset_state
========================

*man pci_set_pcie_reset_state(9)*

*4.6.0-rc1*

set reset state for device dev


Synopsis
========

.. c:function:: int pci_set_pcie_reset_state( struct pci_dev * dev, enum pcie_reset_state state )

Arguments
=========

``dev``
    the PCIe device reset

``state``
    Reset state to enter into


Description
===========

Sets the PCI reset state for the device.
