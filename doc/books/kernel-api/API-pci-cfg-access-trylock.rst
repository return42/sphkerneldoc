
.. _API-pci-cfg-access-trylock:

======================
pci_cfg_access_trylock
======================

*man pci_cfg_access_trylock(9)*

*4.6.0-rc1*

try to lock PCI config reads/writes


Synopsis
========

.. c:function:: bool pci_cfg_access_trylock( struct pci_dev * dev )

Arguments
=========

``dev``
    pci device struct


Description
===========

Same as pci_cfg_access_lock, but will return 0 if access is already locked, 1 otherwise. This function can be used from atomic contexts.
