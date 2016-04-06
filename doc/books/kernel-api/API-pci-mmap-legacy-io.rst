
.. _API-pci-mmap-legacy-io:

==================
pci_mmap_legacy_io
==================

*man pci_mmap_legacy_io(9)*

*4.6.0-rc1*

map legacy PCI IO into user memory space


Synopsis
========

.. c:function:: int pci_mmap_legacy_io( struct file * filp, struct kobject * kobj, struct bin_attribute * attr, struct vm_area_struct * vma )

Arguments
=========

``filp``
    open sysfs file

``kobj``
    kobject corresponding to device to be mapped

``attr``
    struct bin_attribute for this file

``vma``
    struct vm_area_struct passed to mmap


Description
===========

Uses an arch specific callback, pci_mmap_legacy_io_page_range, to mmap legacy IO space (first meg of bus space) into application virtual memory space. Returns -ENOSYS if the
operation isn't supported
