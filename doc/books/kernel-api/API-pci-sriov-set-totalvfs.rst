
.. _API-pci-sriov-set-totalvfs:

======================
pci_sriov_set_totalvfs
======================

*man pci_sriov_set_totalvfs(9)*

*4.6.0-rc1*

- reduce the TotalVFs available


Synopsis
========

.. c:function:: int pci_sriov_set_totalvfs( struct pci_dev * dev, u16 numvfs )

Arguments
=========

``dev``
    the PCI PF device

``numvfs``
    number that should be used for TotalVFs supported


Description
===========

Should be called from PF driver's probe routine with device's mutex held.

Returns 0 if PF is an SRIOV-capable device and value of numvfs valid. If not a PF return -ENOSYS; if numvfs is invalid return -EINVAL; if VFs already enabled, return -EBUSY.
