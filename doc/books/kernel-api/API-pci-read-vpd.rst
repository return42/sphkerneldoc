
.. _API-pci-read-vpd:

============
pci_read_vpd
============

*man pci_read_vpd(9)*

*4.6.0-rc1*

Read one entry from Vital Product Data


Synopsis
========

.. c:function:: ssize_t pci_read_vpd( struct pci_dev * dev, loff_t pos, size_t count, void * buf )

Arguments
=========

``dev``
    pci device struct

``pos``
    offset in vpd space

``count``
    number of bytes to read

``buf``
    pointer to where to store result
