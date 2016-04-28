.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-enable-device-mem:

=====================
pci_enable_device_mem
=====================

*man pci_enable_device_mem(9)*

*4.6.0-rc5*

Initialize a device for use with Memory space


Synopsis
========

.. c:function:: int pci_enable_device_mem( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to be initialized


Description
===========

Initialize device before it's used by a driver. Ask low-level code to
enable Memory resources. Wake up the device if it was suspended. Beware,
this function can fail.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
