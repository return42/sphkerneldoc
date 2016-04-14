.. -*- coding: utf-8; mode: rst -*-

===========
pci_iomap.c
===========

.. _`pci_iomap_range`:

pci_iomap_range
===============

.. c:function:: void __iomem *pci_iomap_range (struct pci_dev *dev, int bar, unsigned long offset, unsigned long maxlen)

    create a virtual mapping cookie for a PCI BAR

    :param struct pci_dev \*dev:
        PCI device that owns the BAR

    :param int bar:
        BAR number

    :param unsigned long offset:
        map memory at the given offset in BAR

    :param unsigned long maxlen:
        max length of the memory to map


.. _`pci_iomap_range.description`:

Description
-----------

Using this function you will get a __iomem address to your device BAR.
You can access it using ioread\*() and iowrite\*(). These functions hide
the details if this is a MMIO or PIO address space and will just do what
you expect from them in the correct way.

``maxlen`` specifies the maximum length to map. If you want to get access to
the complete BAR from offset to the end, pass ``0`` here.


.. _`pci_iomap_wc_range`:

pci_iomap_wc_range
==================

.. c:function:: void __iomem *pci_iomap_wc_range (struct pci_dev *dev, int bar, unsigned long offset, unsigned long maxlen)

    create a virtual WC mapping cookie for a PCI BAR

    :param struct pci_dev \*dev:
        PCI device that owns the BAR

    :param int bar:
        BAR number

    :param unsigned long offset:
        map memory at the given offset in BAR

    :param unsigned long maxlen:
        max length of the memory to map


.. _`pci_iomap_wc_range.description`:

Description
-----------

Using this function you will get a __iomem address to your device BAR.
You can access it using ioread\*() and iowrite\*(). These functions hide
the details if this is a MMIO or PIO address space and will just do what
you expect from them in the correct way. When possible write combining
is used.

``maxlen`` specifies the maximum length to map. If you want to get access to
the complete BAR from offset to the end, pass ``0`` here.


.. _`pci_iomap`:

pci_iomap
=========

.. c:function:: void __iomem *pci_iomap (struct pci_dev *dev, int bar, unsigned long maxlen)

    create a virtual mapping cookie for a PCI BAR

    :param struct pci_dev \*dev:
        PCI device that owns the BAR

    :param int bar:
        BAR number

    :param unsigned long maxlen:
        length of the memory to map


.. _`pci_iomap.description`:

Description
-----------

Using this function you will get a __iomem address to your device BAR.
You can access it using ioread\*() and iowrite\*(). These functions hide
the details if this is a MMIO or PIO address space and will just do what
you expect from them in the correct way.

``maxlen`` specifies the maximum length to map. If you want to get access to
the complete BAR without checking for its length first, pass ``0`` here.


.. _`pci_iomap_wc`:

pci_iomap_wc
============

.. c:function:: void __iomem *pci_iomap_wc (struct pci_dev *dev, int bar, unsigned long maxlen)

    create a virtual WC mapping cookie for a PCI BAR

    :param struct pci_dev \*dev:
        PCI device that owns the BAR

    :param int bar:
        BAR number

    :param unsigned long maxlen:
        length of the memory to map


.. _`pci_iomap_wc.description`:

Description
-----------

Using this function you will get a __iomem address to your device BAR.
You can access it using ioread\*() and iowrite\*(). These functions hide
the details if this is a MMIO or PIO address space and will just do what
you expect from them in the correct way. When possible write combining
is used.

``maxlen`` specifies the maximum length to map. If you want to get access to
the complete BAR without checking for its length first, pass ``0`` here.

