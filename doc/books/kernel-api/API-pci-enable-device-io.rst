
.. _API-pci-enable-device-io:

====================
pci_enable_device_io
====================

*man pci_enable_device_io(9)*

*4.6.0-rc1*

Initialize a device for use with IO space


Synopsis
========

.. c:function:: int pci_enable_device_io( struct pci_dev * dev )

Arguments
=========

``dev``
    PCI device to be initialized


Description
===========

Initialize device before it's used by a driver. Ask low-level code to enable I/O resources. Wake up the device if it was suspended. Beware, this function can fail.
