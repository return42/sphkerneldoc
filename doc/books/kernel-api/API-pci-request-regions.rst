.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-request-regions:

===================
pci_request_regions
===================

*man pci_request_regions(9)*

*4.6.0-rc5*

Reserved PCI I/O and memory resources


Synopsis
========

.. c:function:: int pci_request_regions( struct pci_dev * pdev, const char * res_name )

Arguments
=========

``pdev``
    PCI device whose resources are to be reserved

``res_name``
    Name to be associated with resource.


Description
===========

Mark all PCI regions associated with PCI device ``pdev`` as being
reserved by owner ``res_name``. Do not access any address inside the PCI
regions unless this call returns successfully.

Returns 0 on success, or ``EBUSY`` on error. A warning message is also
printed on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
