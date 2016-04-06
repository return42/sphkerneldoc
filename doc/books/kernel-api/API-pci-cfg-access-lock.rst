
.. _API-pci-cfg-access-lock:

===================
pci_cfg_access_lock
===================

*man pci_cfg_access_lock(9)*

*4.6.0-rc1*

Lock PCI config reads/writes


Synopsis
========

.. c:function:: void pci_cfg_access_lock( struct pci_dev * dev )

Arguments
=========

``dev``
    pci device struct


Description
===========

When access is locked, any userspace reads or writes to config space and concurrent lock requests will sleep until access is allowed via pci_cfg_access_unlocked again.
