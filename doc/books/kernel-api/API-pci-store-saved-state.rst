
.. _API-pci-store-saved-state:

=====================
pci_store_saved_state
=====================

*man pci_store_saved_state(9)*

*4.6.0-rc1*

Allocate and return an opaque struct containing the device saved state.


Synopsis
========

.. c:function:: struct pci_saved_state ⋆ pci_store_saved_state( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device that we're dealing with


Description
===========

Return NULL if no state or error.
