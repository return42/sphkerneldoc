.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-rescan-bus:

==============
pci_rescan_bus
==============

*man pci_rescan_bus(9)*

*4.6.0-rc5*

scan a PCI bus for devices.


Synopsis
========

.. c:function:: unsigned int pci_rescan_bus( struct pci_bus * bus )

Arguments
=========

``bus``
    PCI bus to scan


Description
===========

Scan a PCI bus and child buses for new devices, adds them, and enables
them.

Returns the max number of subordinate bus discovered.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
