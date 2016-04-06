
.. _API-pci-read-rom:

============
pci_read_rom
============

*man pci_read_rom(9)*

*4.6.0-rc1*

read a PCI ROM


Synopsis
========

.. c:function:: ssize_t pci_read_rom( struct file * filp, struct kobject * kobj, struct bin_attribute * bin_attr, char * buf, loff_t off, size_t count )

Arguments
=========

``filp``
    sysfs file

``kobj``
    kernel object handle

``bin_attr``
    struct bin_attribute for this file

``buf``
    where to put the data we read from the ROM

``off``
    file offset

``count``
    number of bytes to read


Description
===========

Put ``count`` bytes starting at ``off`` into ``buf`` from the ROM in the PCI device corresponding to ``kobj``.
