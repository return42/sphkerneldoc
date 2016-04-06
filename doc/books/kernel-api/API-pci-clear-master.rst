
.. _API-pci-clear-master:

================
pci_clear_master
================

*man pci_clear_master(9)*

*4.6.0-rc1*

disables bus-mastering for device dev


Synopsis
========

.. c:function:: void pci_clear_master( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device to disable
