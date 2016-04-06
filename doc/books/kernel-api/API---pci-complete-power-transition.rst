
.. _API---pci-complete-power-transition:

===============================
__pci_complete_power_transition
===============================

*man __pci_complete_power_transition(9)*

*4.6.0-rc1*

Complete power transition of a PCI device


Synopsis
========

.. c:function:: int __pci_complete_power_transition( struct pci_dev * dev, pci_power_t state )

Arguments
=========

``dev``
    PCI device to handle.

``state``
    State to put the device into.


Description
===========

This function should not be called directly by device drivers.
