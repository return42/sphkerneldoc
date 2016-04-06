
.. _API-pci-release-region:

==================
pci_release_region
==================

*man pci_release_region(9)*

*4.6.0-rc1*

Release a PCI bar


Synopsis
========

.. c:function:: void pci_release_region( struct pci_dev * pdev, int bar )

Arguments
=========

``pdev``
    PCI device whose resources were previously reserved by pci_request_region

``bar``
    BAR to release


Description
===========

Releases the PCI I/O and memory resources previously reserved by a successful call to pci_request_region. Call this function only after all use of the PCI regions has ceased.
