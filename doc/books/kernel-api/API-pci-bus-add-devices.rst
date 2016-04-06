
.. _API-pci-bus-add-devices:

===================
pci_bus_add_devices
===================

*man pci_bus_add_devices(9)*

*4.6.0-rc1*

start driver for PCI devices


Synopsis
========

.. c:function:: void pci_bus_add_devices( const struct pci_bus * bus )

Arguments
=========

``bus``
    bus to check for new devices


Description
===========

Start driver for PCI devices and add some sysfs entries.
