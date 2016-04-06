
.. _API-pci-load-saved-state:

====================
pci_load_saved_state
====================

*man pci_load_saved_state(9)*

*4.6.0-rc1*

Reload the provided save state into struct pci_dev.


Synopsis
========

.. c:function:: int pci_load_saved_state( struct pci_dev * dev, struct pci_saved_state * state )

Arguments
=========

``dev``
    PCI device that we're dealing with

``state``
    Saved state returned from ``pci_store_saved_state``
