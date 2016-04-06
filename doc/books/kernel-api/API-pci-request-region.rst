
.. _API-pci-request-region:

==================
pci_request_region
==================

*man pci_request_region(9)*

*4.6.0-rc1*

Reserve PCI I/O and memory resource


Synopsis
========

.. c:function:: int pci_request_region( struct pci_dev * pdev, int bar, const char * res_name )

Arguments
=========

``pdev``
    PCI device whose resources are to be reserved

``bar``
    BAR to be reserved

``res_name``
    Name to be associated with resource


Description
===========

Mark the PCI region associated with PCI device ``pdev`` BAR ``bar`` as being reserved by owner ``res_name``. Do not access any address inside the PCI regions unless this call
returns successfully.

Returns 0 on success, or ``EBUSY`` on error. A warning message is also printed on failure.
