
.. _API-pci-request-selected-regions:

============================
pci_request_selected_regions
============================

*man pci_request_selected_regions(9)*

*4.6.0-rc1*

Reserve selected PCI I/O and memory resources


Synopsis
========

.. c:function:: int pci_request_selected_regions( struct pci_dev * pdev, int bars, const char * res_name )

Arguments
=========

``pdev``
    PCI device whose resources are to be reserved

``bars``
    Bitmask of BARs to be requested

``res_name``
    Name to be associated with resource
