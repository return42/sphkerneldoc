
.. _API-pci-bus-add-device:

==================
pci_bus_add_device
==================

*man pci_bus_add_device(9)*

*4.6.0-rc1*

start driver for a single device


Synopsis
========

.. c:function:: void pci_bus_add_device( struct pci_dev * dev )

Arguments
=========

``dev``
    device to add


Description
===========

This adds add sysfs entries and start device drivers
