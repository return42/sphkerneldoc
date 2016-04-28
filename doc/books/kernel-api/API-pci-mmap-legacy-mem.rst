.. -*- coding: utf-8; mode: rst -*-

.. _API-pci-mmap-legacy-mem:

===================
pci_mmap_legacy_mem
===================

*man pci_mmap_legacy_mem(9)*

*4.6.0-rc5*

map legacy PCI memory into user memory space


Synopsis
========

.. c:function:: int pci_mmap_legacy_mem( struct file * filp, struct kobject * kobj, struct bin_attribute * attr, struct vm_area_struct * vma )

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

Uses an arch specific callback, pci_mmap_legacy_mem_page_range, to
mmap legacy memory space (first meg of bus space) into application
virtual memory space.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
