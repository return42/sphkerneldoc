
.. _API-pci-mmap-resource:

=================
pci_mmap_resource
=================

*man pci_mmap_resource(9)*

*4.6.0-rc1*

map a PCI resource into user memory space


Synopsis
========

.. c:function:: int pci_mmap_resource( struct kobject * kobj, struct bin_attribute * attr, struct vm_area_struct * vma, int write_combine )

Arguments
=========

``kobj``
    kobject for mapping

``attr``
    struct bin_attribute for the file being mapped

``vma``
    struct vm_area_struct passed into the mmap

``write_combine``
    1 for write_combine mapping


Description
===========

Use the regular PCI mapping routines to map a PCI resource into userspace.
