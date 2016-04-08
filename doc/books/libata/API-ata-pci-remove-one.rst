
.. _API-ata-pci-remove-one:

==================
ata_pci_remove_one
==================

*man ata_pci_remove_one(9)*

*4.6.0-rc1*

PCI layer callback for device removal


Synopsis
========

.. c:function:: void ata_pci_remove_one( struct pci_dev * pdev )

Arguments
=========

``pdev``
    PCI device that was removed


Description
===========

PCI layer indicates to libata via this hook that hot-unplug or module unload event has occurred. Detach all ports. Resource release is handled via devres.


LOCKING
=======

Inherited from PCI layer (may sleep).
