.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/pci/sta2x11-fixup.c

.. _`p2a`:

p2a
===

.. c:function:: dma_addr_t p2a(dma_addr_t p, struct pci_dev *pdev)

    Translate physical address to STA2x11 AMBA address, used for DMA transfers to STA2x11

    :param dma_addr_t p:
        Physical address

    :param struct pci_dev \*pdev:
        PCI device (must be hosted within the connext)

.. _`a2p`:

a2p
===

.. c:function:: dma_addr_t a2p(dma_addr_t a, struct pci_dev *pdev)

    Translate STA2x11 AMBA address to physical address used for DMA transfers from STA2x11

    :param dma_addr_t a:
        STA2x11 AMBA address

    :param struct pci_dev \*pdev:
        PCI device (must be hosted within the connext)

.. _`dma_capable`:

dma_capable
===========

.. c:function:: bool dma_capable(struct device *dev, dma_addr_t addr, size_t size)

    Check if device can manage DMA transfers (FIXME: kill it)

    :param struct device \*dev:
        device for a PCI device

    :param dma_addr_t addr:
        DMA address

    :param size_t size:
        DMA size

.. _`__phys_to_dma`:

\__phys_to_dma
==============

.. c:function:: dma_addr_t __phys_to_dma(struct device *dev, phys_addr_t paddr)

    Return the DMA AMBA address used for this STA2x11 device

    :param struct device \*dev:
        device for a PCI device

    :param phys_addr_t paddr:
        Physical address

.. _`__dma_to_phys`:

\__dma_to_phys
==============

.. c:function:: phys_addr_t __dma_to_phys(struct device *dev, dma_addr_t daddr)

    Return the physical address used for this STA2x11 DMA address

    :param struct device \*dev:
        device for a PCI device

    :param dma_addr_t daddr:
        STA2x11 AMBA DMA address

.. This file was automatic generated / don't edit.

