
.. _API-pci-clear-mwi:

=============
pci_clear_mwi
=============

*man pci_clear_mwi(9)*

*4.6.0-rc1*

disables Memory-Write-Invalidate for device dev


Synopsis
========

.. c:function:: void pci_clear_mwi( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device to disable


Description
===========

Disables PCI Memory-Write-Invalidate transaction on the device
