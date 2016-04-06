
.. _API-pci-enable-device:

=================
pci_enable_device
=================

*man pci_enable_device(9)*

*4.6.0-rc1*

Initialize device before it's used by a driver.


Synopsis
========

.. c:function:: int pci_enable_device( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to be initialized


Description
===========

Initialize device before it's used by a driver. Ask low-level code to enable I/O and memory. Wake up the device if it was suspended. Beware, this function can fail.

Note we don't actually enable the device many times if we call this function repeatedly (we just increment the count).
