.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-wake-from-d3:

================
pci_wake_from_d3
================

*man pci_wake_from_d3(9)*

*4.6.0-rc5*

enable/disable device to wake up from D3_hot or D3_cold


Synopsis
========

.. c:function:: int pci_wake_from_d3( struct pci_dev * dev, bool enable )

Arguments
=========

``dev``
    PCI device to prepare

``enable``
    True to enable wake-up event generation; false to disable


Description
===========

Many drivers want the device to wake up the system from D3_hot or
D3_cold and this function allows them to set that up cleanly -
``pci_enable_wake`` should not be called twice in a row to enable
wake-up due to PCI PM vs ACPI ordering constraints.

This function only returns error code if the device is not capable of
generating PME# from both D3_hot and D3_cold, and the platform is
unable to enable wake-up power for it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
