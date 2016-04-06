
.. _API-pci-save-state:

==============
pci_save_state
==============

*man pci_save_state(9)*

*4.6.0-rc1*

save the PCI configuration space of a device before suspending


Synopsis
========

.. c:function:: int pci_save_state( struct pci_dev * dev )

Arguments
=========

``dev``
    - PCI device that we're dealing with
