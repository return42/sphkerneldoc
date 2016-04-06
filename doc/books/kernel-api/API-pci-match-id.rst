
.. _API-pci-match-id:

============
pci_match_id
============

*man pci_match_id(9)*

*4.6.0-rc1*

See if a pci device matches a given pci_id table


Synopsis
========

.. c:function:: const struct pci_device_id ⋆ pci_match_id( const struct pci_device_id * ids, struct pci_dev * dev )

Arguments
=========

``ids``
    array of PCI device id structures to search in

``dev``
    the PCI device structure to match against.


Description
===========

Used by a driver to check whether a PCI device present in the system is in its list of supported devices. Returns the matching pci_device_id structure or ``NULL`` if there is no
match.

Deprecated, don't use this as it will not catch any dynamic ids that a driver might want to check for.
