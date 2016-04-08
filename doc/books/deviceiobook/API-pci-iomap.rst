
.. _API-pci-iomap:

=========
pci_iomap
=========

*man pci_iomap(9)*

*4.6.0-rc1*

create a virtual mapping cookie for a PCI BAR


Synopsis
========

.. c:function:: void __iomem ⋆ pci_iomap( struct pci_dev * dev, int bar, unsigned long maxlen )

Arguments
=========

``dev``
    PCI device that owns the BAR

``bar``
    BAR number

``maxlen``
    length of the memory to map


Description
===========

Using this function you will get a __iomem address to your device BAR. You can access it using ioread⋆() and iowrite⋆(). These functions hide the details if this is a MMIO or PIO
address space and will just do what you expect from them in the correct way.

``maxlen`` specifies the maximum length to map. If you want to get access to the complete BAR without checking for its length first, pass ``0`` here.
