
.. _API-pci-back-from-sleep:

===================
pci_back_from_sleep
===================

*man pci_back_from_sleep(9)*

*4.6.0-rc1*

turn PCI device on during system-wide transition into working state


Synopsis
========

.. c:function:: int pci_back_from_sleep( struct pci_dev * dev )

Arguments
=========

``dev``
    Device to handle.


Description
===========

Disable device's system wake-up capability and put it into D0.
