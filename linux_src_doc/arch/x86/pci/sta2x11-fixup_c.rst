.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/pci/sta2x11-fixup.c

.. _`p2a`:

p2a
===

.. c:function:: dma_addr_t p2a(dma_addr_t p, struct pci_dev *pdev)

    Translate physical address to STA2x11 AMBA address, used for DMA transfers to STA2x11

    :param p:
        Physical address
    :type p: dma_addr_t

    :param pdev:
        PCI device (must be hosted within the connext)
    :type pdev: struct pci_dev \*

.. _`a2p`:

a2p
===

.. c:function:: dma_addr_t a2p(dma_addr_t a, struct pci_dev *pdev)

    Translate STA2x11 AMBA address to physical address used for DMA transfers from STA2x11

    :param a:
        STA2x11 AMBA address
    :type a: dma_addr_t

    :param pdev:
        PCI device (must be hosted within the connext)
    :type pdev: struct pci_dev \*

.. _`dma_capable`:

dma_capable
===========

.. c:function:: bool dma_capable(struct device *dev, dma_addr_t addr, size_t size)

    Check if device can manage DMA transfers (FIXME: kill it)

    :param dev:
        device for a PCI device
    :type dev: struct device \*

    :param addr:
        DMA address
    :type addr: dma_addr_t

    :param size:
        DMA size
    :type size: size_t

.. _`__phys_to_dma`:

\__phys_to_dma
==============

.. c:function:: dma_addr_t __phys_to_dma(struct device *dev, phys_addr_t paddr)

    Return the DMA AMBA address used for this STA2x11 device

    :param dev:
        device for a PCI device
    :type dev: struct device \*

    :param paddr:
        Physical address
    :type paddr: phys_addr_t

.. _`__dma_to_phys`:

\__dma_to_phys
==============

.. c:function:: phys_addr_t __dma_to_phys(struct device *dev, dma_addr_t daddr)

    Return the physical address used for this STA2x11 DMA address

    :param dev:
        device for a PCI device
    :type dev: struct device \*

    :param daddr:
        STA2x11 AMBA DMA address
    :type daddr: dma_addr_t

.. This file was automatic generated / don't edit.

