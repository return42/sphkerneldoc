
.. _API-pci-disable-device:

==================
pci_disable_device
==================

*man pci_disable_device(9)*

*4.6.0-rc1*

Disable PCI device after use


Synopsis
========

.. c:function:: void pci_disable_device( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to be disabled


Description
===========

Signal to the system that the PCI device is not in use by the system anymore. This only involves disabling PCI bus-mastering, if active.

Note we don't actually disable the device until all callers of ``pci_enable_device`` have called ``pci_disable_device``.
