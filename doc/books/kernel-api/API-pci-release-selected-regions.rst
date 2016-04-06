
.. _API-pci-release-selected-regions:

============================
pci_release_selected_regions
============================

*man pci_release_selected_regions(9)*

*4.6.0-rc1*

Release selected PCI I/O and memory resources


Synopsis
========

.. c:function:: void pci_release_selected_regions( struct pci_dev * pdev, int bars )

Arguments
=========

``pdev``
    PCI device whose resources were previously reserved

``bars``
    Bitmask of BARs to be released


Description
===========

Release selected PCI I/O and memory resources previously reserved. Call this function only after all use of the PCI regions has ceased.
