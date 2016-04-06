
.. _API-pcie-get-minimum-link:

=====================
pcie_get_minimum_link
=====================

*man pcie_get_minimum_link(9)*

*4.6.0-rc1*

determine minimum link settings of a PCI device


Synopsis
========

.. c:function:: int pcie_get_minimum_link( struct pci_dev * dev, enum pci_bus_speed * speed, enum pcie_link_width * width )

Arguments
=========

``dev``
    PCI device to query

``speed``
    storage for minimum speed

``width``
    storage for minimum width


Description
===========

This function will walk up the PCI device chain and determine the minimum link width and speed of the device.
