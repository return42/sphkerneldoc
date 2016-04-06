
.. _API-pci-write-rom:

=============
pci_write_rom
=============

*man pci_write_rom(9)*

*4.6.0-rc1*

used to enable access to the PCI ROM display


Synopsis
========

.. c:function:: ssize_t pci_write_rom( struct file * filp, struct kobject * kobj, struct bin_attribute * bin_attr, char * buf, loff_t off, size_t count )

Arguments
=========

``filp``
    sysfs file

``kobj``
    kernel object handle

``bin_attr``
    struct bin_attribute for this file

``buf``
    user input

``off``
    file offset

``count``
    number of byte in input


Description
===========

writing anything except 0 enables it
