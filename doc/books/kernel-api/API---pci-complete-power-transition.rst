.. -*- coding: utf-8; mode: rst -*-

.. _API---pci-complete-power-transition:

===============================
__pci_complete_power_transition
===============================

*man __pci_complete_power_transition(9)*

*4.6.0-rc5*

Complete power transition of a PCI device


Synopsis
========

.. c:function:: int __pci_complete_power_transition( struct pci_dev * dev, pci_power_t state )

Arguments
=========

``dev``
    PCI device to handle.

``state``
    State to put the device into.


Description
===========

This function should not be called directly by device drivers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
