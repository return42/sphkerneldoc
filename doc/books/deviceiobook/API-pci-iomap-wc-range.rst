
.. _API-pci-iomap-wc-range:

==================
pci_iomap_wc_range
==================

*man pci_iomap_wc_range(9)*

*4.6.0-rc1*

create a virtual WC mapping cookie for a PCI BAR


Synopsis
========

.. c:function:: void __iomem ⋆ pci_iomap_wc_range( struct pci_dev * dev, int bar, unsigned long offset, unsigned long maxlen )

Arguments
=========

``dev``
    PCI device that owns the BAR

``bar``
    BAR number

``offset``
    map memory at the given offset in BAR

``maxlen``
    max length of the memory to map


Description
===========

Using this function you will get a __iomem address to your device BAR. You can access it using ioread⋆() and iowrite⋆(). These functions hide the details if this is a MMIO or PIO
address space and will just do what you expect from them in the correct way. When possible write combining is used.

``maxlen`` specifies the maximum length to map. If you want to get access to the complete BAR from offset to the end, pass ``0`` here.
