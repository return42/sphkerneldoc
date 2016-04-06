
.. _API-pci-sriov-get-totalvfs:

======================
pci_sriov_get_totalvfs
======================

*man pci_sriov_get_totalvfs(9)*

*4.6.0-rc1*

- get total VFs supported on this device


Synopsis
========

.. c:function:: int pci_sriov_get_totalvfs( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI PF device


Description
===========

For a PCIe device with SRIOV support, return the PCIe SRIOV capability value of TotalVFs or the value of driver_max_VFs if the driver reduced it. Otherwise 0.
