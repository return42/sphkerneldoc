
.. _API-pci-write-vpd:

=============
pci_write_vpd
=============

*man pci_write_vpd(9)*

*4.6.0-rc1*

Write entry to Vital Product Data


Synopsis
========

.. c:function:: ssize_t pci_write_vpd( struct pci_dev * dev, loff_t pos, size_t count, const void * buf )

Arguments
=========

``dev``
    pci device struct

``pos``
    offset in vpd space

``count``
    number of bytes to write

``buf``
    buffer containing write data
