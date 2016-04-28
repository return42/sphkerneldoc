.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-reset-bridge-secondary-bus:

==============================
pci_reset_bridge_secondary_bus
==============================

*man pci_reset_bridge_secondary_bus(9)*

*4.6.0-rc5*

Reset the secondary bus on a PCI bridge.


Synopsis
========

.. c:function:: void pci_reset_bridge_secondary_bus( struct pci_dev * dev )

Arguments
=========

``dev``
    Bridge device


Description
===========

Use the bridge control register to assert reset on the secondary bus.
Devices on the secondary bus are left in power-on state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
