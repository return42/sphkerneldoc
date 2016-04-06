
.. _API-pci-cfg-access-unlock:

=====================
pci_cfg_access_unlock
=====================

*man pci_cfg_access_unlock(9)*

*4.6.0-rc1*

Unlock PCI config reads/writes


Synopsis
========

.. c:function:: void pci_cfg_access_unlock( struct pci_dev * dev )

Arguments
=========

``dev``
    pci device struct


Description
===========

This function allows PCI config accesses to resume.
