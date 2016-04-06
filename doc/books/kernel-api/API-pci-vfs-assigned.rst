
.. _API-pci-vfs-assigned:

================
pci_vfs_assigned
================

*man pci_vfs_assigned(9)*

*4.6.0-rc1*

returns number of VFs are assigned to a guest


Synopsis
========

.. c:function:: int pci_vfs_assigned( struct pci_dev * dev )

Arguments
=========

``dev``
    the PCI device


Description
===========

Returns number of VFs belonging to this device that are assigned to a guest. If device is not a physical function returns 0.
