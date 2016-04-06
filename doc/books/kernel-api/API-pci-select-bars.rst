
.. _API-pci-select-bars:

===============
pci_select_bars
===============

*man pci_select_bars(9)*

*4.6.0-rc1*

Make BAR mask from the type of resource


Synopsis
========

.. c:function:: int pci_select_bars( struct pci_dev * dev, unsigned long flags )

Arguments
=========

``dev``
    the PCI device for which BAR mask is made

``flags``
    resource type mask to be selected


Description
===========

This helper routine makes bar mask from the type of resource.
