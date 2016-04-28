.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-find-capability:

===================
pci_find_capability
===================

*man pci_find_capability(9)*

*4.6.0-rc5*

query for devices' capabilities


Synopsis
========

.. c:function:: int pci_find_capability( struct pci_dev * dev, int cap )

Arguments
=========

``dev``
    PCI device to query

``cap``
    capability code


Description
===========

Tell if a device supports a given PCI capability. Returns the address of
the requested capability structure within the device's PCI configuration
space or 0 in case the device does not support it. Possible values for
``cap``:

``PCI_CAP_ID_PM`` Power Management ``PCI_CAP_ID_AGP`` Accelerated
Graphics Port ``PCI_CAP_ID_VPD`` Vital Product Data
``PCI_CAP_ID_SLOTID`` Slot Identification ``PCI_CAP_ID_MSI`` Message
Signalled Interrupts ``PCI_CAP_ID_CHSWP`` CompactPCI HotSwap
``PCI_CAP_ID_PCIX`` PCI-X ``PCI_CAP_ID_EXP`` PCI Express


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
