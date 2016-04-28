.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-set-pcie-reset-state:

========================
pci_set_pcie_reset_state
========================

*man pci_set_pcie_reset_state(9)*

*4.6.0-rc5*

set reset state for device dev


Synopsis
========

.. c:function:: int pci_set_pcie_reset_state( struct pci_dev * dev, enum pcie_reset_state state )

Arguments
=========

``dev``
    the PCIe device reset

``state``
    Reset state to enter into


Description
===========

Sets the PCI reset state for the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
