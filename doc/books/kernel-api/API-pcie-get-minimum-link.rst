.. -*- coding: utf-8; mode: rst -*-

.. _API-pcie-get-minimum-link:

=====================
pcie_get_minimum_link
=====================

*man pcie_get_minimum_link(9)*

*4.6.0-rc5*

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

This function will walk up the PCI device chain and determine the
minimum link width and speed of the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
