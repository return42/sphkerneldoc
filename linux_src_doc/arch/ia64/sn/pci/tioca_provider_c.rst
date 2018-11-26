.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/sn/pci/tioca_provider.c

.. _`tioca_gart_init`:

tioca_gart_init
===============

.. c:function:: int tioca_gart_init(struct tioca_kernel *tioca_kern)

    Initialize SGI TIOCA GART

    :param tioca_kern:
        *undescribed*
    :type tioca_kern: struct tioca_kernel \*

.. _`tioca_gart_init.description`:

Description
-----------

If the indicated tioca has devices present, initialize its associated
GART MMR's and kernel memory.

.. _`tioca_fastwrite_enable`:

tioca_fastwrite_enable
======================

.. c:function:: void tioca_fastwrite_enable(struct tioca_kernel *tioca_kern)

    enable AGP FW for a tioca and its functions

    :param tioca_kern:
        *undescribed*
    :type tioca_kern: struct tioca_kernel \*

.. _`tioca_fastwrite_enable.description`:

Description
-----------

Given a CA, scan all attached functions making sure they all support
FastWrite.  If so, enable FastWrite for all functions and the CA itself.

.. _`tioca_dma_d64`:

tioca_dma_d64
=============

.. c:function:: u64 tioca_dma_d64(unsigned long paddr)

    create a DMA mapping using 64-bit direct mode

    :param paddr:
        system physical address
    :type paddr: unsigned long

.. _`tioca_dma_d64.description`:

Description
-----------

Map \ ``paddr``\  into 64-bit CA bus space.  No device context is necessary.
Bits 53:0 come from the coretalk address.  We just need to mask in the
following optional bits of the 64-bit pci address:

63:60 - Coretalk Packet Type -  0x1 for Mem Get/Put (coherent)
0x2 for PIO (non-coherent)
We will always use 0x1
55:55 - Swap bytes              Currently unused

.. _`tioca_dma_d48`:

tioca_dma_d48
=============

.. c:function:: u64 tioca_dma_d48(struct pci_dev *pdev, u64 paddr)

    create a DMA mapping using 48-bit direct mode

    :param pdev:
        linux pci_dev representing the function
    :type pdev: struct pci_dev \*

    :param paddr:
        system physical address
    :type paddr: u64

.. _`tioca_dma_d48.description`:

Description
-----------

Map \ ``paddr``\  into 64-bit bus space of the CA associated with \ ``pcidev_info``\ .

.. _`tioca_dma_d48.the-ca-agp-48-bit-direct-address-falls-out-as-follows`:

The CA agp 48 bit direct address falls out as follows
-----------------------------------------------------


When direct mapping AGP addresses, the 48 bit AGP address is

.. _`tioca_dma_d48.constructed-as-follows`:

constructed as follows
----------------------


[47:40] - Low 8 bits of the page Node ID extracted from coretalk
address [47:40].  The upper 8 node bits are fixed
and come from the xxx register bits [5:0]
[39:38] - Chiplet ID extracted from coretalk address [39:38]
[37:00] - node offset extracted from coretalk address [37:00]

Since the node id in general will be non-zero, and the chiplet id
will always be non-zero, it follows that the device must support
a dma mask of at least 0xffffffffff (40 bits) to target node 0
and in general should be 0xffffffffffff (48 bits) to target nodes
up to 255.  Nodes above 255 need the support of the xxx register,
and so a given CA can only directly target nodes in the range
xxx - xxx+255.

.. _`tioca_dma_mapped`:

tioca_dma_mapped
================

.. c:function:: dma_addr_t tioca_dma_mapped(struct pci_dev *pdev, unsigned long paddr, size_t req_size)

    create a DMA mapping using a CA GART

    :param pdev:
        linux pci_dev representing the function
    :type pdev: struct pci_dev \*

    :param paddr:
        host physical address to map
    :type paddr: unsigned long

    :param req_size:
        len (bytes) to map
    :type req_size: size_t

.. _`tioca_dma_mapped.description`:

Description
-----------

Map \ ``paddr``\  into CA address space using the GART mechanism.  The mapped
dma_addr_t is guaranteed to be contiguous in CA bus space.

.. _`tioca_dma_unmap`:

tioca_dma_unmap
===============

.. c:function:: void tioca_dma_unmap(struct pci_dev *pdev, dma_addr_t bus_addr, int dir)

    release CA mapping resources

    :param pdev:
        linux pci_dev representing the function
    :type pdev: struct pci_dev \*

    :param bus_addr:
        bus address returned by an earlier tioca_dma_map
    :type bus_addr: dma_addr_t

    :param dir:
        mapping direction (unused)
    :type dir: int

.. _`tioca_dma_unmap.description`:

Description
-----------

Locate mapping resources associated with \ ``bus_addr``\  and release them.
For mappings created using the direct modes (64 or 48) there are no
resources to release.

.. _`tioca_dma_map`:

tioca_dma_map
=============

.. c:function:: u64 tioca_dma_map(struct pci_dev *pdev, unsigned long paddr, size_t byte_count, int dma_flags)

    map pages for PCI DMA

    :param pdev:
        linux pci_dev representing the function
    :type pdev: struct pci_dev \*

    :param paddr:
        host physical address to map
    :type paddr: unsigned long

    :param byte_count:
        bytes to map
    :type byte_count: size_t

    :param dma_flags:
        *undescribed*
    :type dma_flags: int

.. _`tioca_dma_map.description`:

Description
-----------

This is the main wrapper for mapping host physical pages to CA PCI space.
The mapping mode used is based on the devices dma_mask.  As a last resort
use the GART mapped mode.

.. _`tioca_error_intr_handler`:

tioca_error_intr_handler
========================

.. c:function:: irqreturn_t tioca_error_intr_handler(int irq, void *arg)

    SGI TIO CA error interrupt handler

    :param irq:
        unused
    :type irq: int

    :param arg:
        pointer to tioca_common struct for the given CA
    :type arg: void \*

.. _`tioca_error_intr_handler.description`:

Description
-----------

Handle a CA error interrupt.  Simply a wrapper around a SAL call which
defers processing to the SGI prom.

.. _`tioca_bus_fixup`:

tioca_bus_fixup
===============

.. c:function:: void *tioca_bus_fixup(struct pcibus_bussoft *prom_bussoft, struct pci_controller *controller)

    perform final PCI fixup for a TIO CA bus

    :param prom_bussoft:
        Common prom/kernel struct representing the bus
    :type prom_bussoft: struct pcibus_bussoft \*

    :param controller:
        *undescribed*
    :type controller: struct pci_controller \*

.. _`tioca_bus_fixup.description`:

Description
-----------

Replicates the tioca_common pointed to by \ ``prom_bussoft``\  in kernel
space.  Allocates and initializes a kernel-only area for a given CA,
and sets up an irq for handling CA error interrupts.

On successful setup, returns the kernel version of tioca_common back to
the caller.

.. _`tioca_init_provider`:

tioca_init_provider
===================

.. c:function:: int tioca_init_provider( void)

    init SN PCI provider ops for TIO CA

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

