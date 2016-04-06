
.. _API-pci-stop-and-remove-bus-device:

==============================
pci_stop_and_remove_bus_device
==============================

*man pci_stop_and_remove_bus_device(9)*

*4.6.0-rc1*

remove a PCI device and any children


Synopsis
========

.. c:function:: void pci_stop_and_remove_bus_device( struct pci_dev * dev )

Arguments
=========

``dev``
    the device to remove


Description
===========

Remove a PCI device from the device lists, informing the drivers that the device has been removed. We also remove any subordinate buses and children in a depth-first manner.

For each device we remove, delete the device structure from the device lists, remove the /proc entry, and notify userspace (/sbin/hotplug).
