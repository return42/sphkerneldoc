.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/sn/pci/tioce_provider.c

.. _`tioce_d64_min`:

TIOCE_D64_MIN
=============

.. c:function::  TIOCE_D64_MIN()

.. _`tioce_dma_d64`:

tioce_dma_d64
=============

.. c:function:: u64 tioce_dma_d64(unsigned long ct_addr, int dma_flags)

    create a DMA mapping using 64-bit direct mode

    :param unsigned long ct_addr:
        system coretalk address

    :param int dma_flags:
        *undescribed*

.. _`tioce_dma_d64.description`:

Description
-----------

Map \ ``ct_addr``\  into 64-bit CE bus space.  No device context is necessary
and no CE mapping are consumed.

Bits 53:0 come from the coretalk address.  The remaining bits are set as

.. _`tioce_dma_d64.follows`:

follows
-------


63    - must be 1 to indicate d64 mode to CE hardware
62    - barrier bit ... controlled with \ :c:func:`tioce_dma_barrier`\ 
61    - msi bit ... specified through dma_flags
60:54 - reserved, MBZ

.. _`pcidev_to_tioce`:

pcidev_to_tioce
===============

.. c:function:: void pcidev_to_tioce(struct pci_dev *pdev, struct tioce __iomem **base, struct tioce_kernel **kernel, int *port)

    return misc ce related pointers given a pci_dev

    :param struct pci_dev \*pdev:
        *undescribed*

    :param struct tioce __iomem \*\*base:
        ptr to store struct tioce_mmr \* for the CE holding this device

    :param struct tioce_kernel \*\*kernel:
        ptr to store struct tioce_kernel \* for the CE holding this device

    :param int \*port:
        ptr to store the CE port number that this device is on

.. _`pcidev_to_tioce.description`:

Description
-----------

Return pointers to various CE-related structures for the CE upstream of
\ ``pci_dev``\ .

.. _`tioce_alloc_map`:

tioce_alloc_map
===============

.. c:function:: u64 tioce_alloc_map(struct tioce_kernel *ce_kern, int type, int port, u64 ct_addr, int len, int dma_flags)

    Given a coretalk address, map it to pcie bus address space using one of the various ATE-based address modes.

    :param struct tioce_kernel \*ce_kern:
        tioce context

    :param int type:
        map mode to use

    :param int port:
        0-based port that the requesting device is downstream of

    :param u64 ct_addr:
        the coretalk address to map

    :param int len:
        number of bytes to map

    :param int dma_flags:
        *undescribed*

.. _`tioce_alloc_map.description`:

Description
-----------

Given the addressing type, set up various parameters that define the
ATE pool to use.  Search for a contiguous block of entries to cover the
length, and if enough resources exist, fill in the ATEs and construct a
tioce_dmamap struct to track the mapping.

.. _`tioce_dma_d32`:

tioce_dma_d32
=============

.. c:function:: u64 tioce_dma_d32(struct pci_dev *pdev, u64 ct_addr, int dma_flags)

    create a DMA mapping using 32-bit direct mode

    :param struct pci_dev \*pdev:
        linux pci_dev representing the function

    :param u64 ct_addr:
        *undescribed*

    :param int dma_flags:
        *undescribed*

.. _`tioce_dma_d32.description`:

Description
-----------

Map \ ``paddr``\  into 32-bit bus space of the CE associated with \ ``pcidev_info``\ .

.. _`tioce_dma_barrier`:

tioce_dma_barrier
=================

.. c:function:: u64 tioce_dma_barrier(u64 bus_addr, int on)

    swizzle a TIOCE bus address to include or exclude the barrier bit.

    :param u64 bus_addr:
        bus address to swizzle

    :param int on:
        *undescribed*

.. _`tioce_dma_barrier.description`:

Description
-----------

Given a TIOCE bus address, set the appropriate bit to indicate barrier
attributes.

.. _`tioce_dma_unmap`:

tioce_dma_unmap
===============

.. c:function:: void tioce_dma_unmap(struct pci_dev *pdev, dma_addr_t bus_addr, int dir)

    release CE mapping resources

    :param struct pci_dev \*pdev:
        linux pci_dev representing the function

    :param dma_addr_t bus_addr:
        bus address returned by an earlier tioce_dma_map

    :param int dir:
        mapping direction (unused)

.. _`tioce_dma_unmap.description`:

Description
-----------

Locate mapping resources associated with \ ``bus_addr``\  and release them.
For mappings created using the direct modes there are no resources
to release.

.. _`tioce_do_dma_map`:

tioce_do_dma_map
================

.. c:function:: u64 tioce_do_dma_map(struct pci_dev *pdev, u64 paddr, size_t byte_count, int barrier, int dma_flags)

    map pages for PCI DMA

    :param struct pci_dev \*pdev:
        linux pci_dev representing the function

    :param u64 paddr:
        host physical address to map

    :param size_t byte_count:
        bytes to map

    :param int barrier:
        *undescribed*

    :param int dma_flags:
        *undescribed*

.. _`tioce_do_dma_map.description`:

Description
-----------

This is the main wrapper for mapping host physical pages to CE PCI space.
The mapping mode used is based on the device's dma_mask.

.. _`tioce_dma`:

tioce_dma
=========

.. c:function:: u64 tioce_dma(struct pci_dev *pdev, unsigned long paddr, size_t byte_count, int dma_flags)

    standard pci dma map interface

    :param struct pci_dev \*pdev:
        pci device requesting the map

    :param unsigned long paddr:
        system physical address to map into pci space

    :param size_t byte_count:
        # bytes to map

    :param int dma_flags:
        *undescribed*

.. _`tioce_dma.description`:

Description
-----------

Simply call \ :c:func:`tioce_do_dma_map`\  to create a map with the barrier bit clear
in the address.

.. _`tioce_dma_consistent`:

tioce_dma_consistent
====================

.. c:function:: u64 tioce_dma_consistent(struct pci_dev *pdev, unsigned long paddr, size_t byte_count, int dma_flags)

    consistent pci dma map interface

    :param struct pci_dev \*pdev:
        pci device requesting the map

    :param unsigned long paddr:
        system physical address to map into pci space

    :param size_t byte_count:
        # bytes to map

    :param int dma_flags:
        *undescribed*

.. _`tioce_dma_consistent.description`:

Description
-----------

Simply call \ :c:func:`tioce_do_dma_map`\  to create a map with the barrier bit set
in the address.

.. _`tioce_error_intr_handler`:

tioce_error_intr_handler
========================

.. c:function:: irqreturn_t tioce_error_intr_handler(int irq, void *arg)

    SGI TIO CE error interrupt handler

    :param int irq:
        unused

    :param void \*arg:
        pointer to tioce_common struct for the given CE

.. _`tioce_error_intr_handler.description`:

Description
-----------

Handle a CE error interrupt.  Simply a wrapper around a SAL call which
defers processing to the SGI prom.

.. _`tioce_reserve_m32`:

tioce_reserve_m32
=================

.. c:function:: void tioce_reserve_m32(struct tioce_kernel *ce_kern, u64 base, u64 limit)

    reserve M32 ATEs for the indicated address range

    :param struct tioce_kernel \*ce_kern:
        *undescribed*

    :param u64 base:
        starting bus address to reserve

    :param u64 limit:
        last bus address to reserve

.. _`tioce_reserve_m32.description`:

Description
-----------

If base/limit falls within the range of bus space mapped through the
M32 space, reserve the resources corresponding to the range.

.. _`tioce_kern_init`:

tioce_kern_init
===============

.. c:function:: struct tioce_kernel *tioce_kern_init(struct tioce_common *tioce_common)

    init kernel structures related to a given TIOCE

    :param struct tioce_common \*tioce_common:
        ptr to a cached tioce_common struct that originated in prom

.. _`tioce_force_interrupt`:

tioce_force_interrupt
=====================

.. c:function:: void tioce_force_interrupt(struct sn_irq_info *sn_irq_info)

    implement altix \ :c:func:`force_interrupt`\  backend for CE

    :param struct sn_irq_info \*sn_irq_info:
        sn asic irq that we need an interrupt generated for

.. _`tioce_force_interrupt.description`:

Description
-----------

Given an sn_irq_info struct, set the proper bit in ce_adm_force_int to
force a secondary interrupt to be generated.  This is to work around an
asic issue where there is a small window of opportunity for a legacy device
interrupt to be lost.

.. _`tioce_target_interrupt`:

tioce_target_interrupt
======================

.. c:function:: void tioce_target_interrupt(struct sn_irq_info *sn_irq_info)

    implement set_irq_affinity for tioce resident functions.  Note:  only applies to line interrupts, not MSI's.

    :param struct sn_irq_info \*sn_irq_info:
        SN IRQ context

.. _`tioce_target_interrupt.description`:

Description
-----------

Given an sn_irq_info, set the associated CE device's interrupt destination
register.  Since the interrupt destination registers are on a per-ce-slot
basis, this will retarget line interrupts for all functions downstream of
the slot.

.. _`tioce_bus_fixup`:

tioce_bus_fixup
===============

.. c:function:: void *tioce_bus_fixup(struct pcibus_bussoft *prom_bussoft, struct pci_controller *controller)

    perform final PCI fixup for a TIO CE bus

    :param struct pcibus_bussoft \*prom_bussoft:
        Common prom/kernel struct representing the bus

    :param struct pci_controller \*controller:
        *undescribed*

.. _`tioce_bus_fixup.description`:

Description
-----------

Replicates the tioce_common pointed to by \ ``prom_bussoft``\  in kernel
space.  Allocates and initializes a kernel-only area for a given CE,
and sets up an irq for handling CE error interrupts.

On successful setup, returns the kernel version of tioce_common back to
the caller.

.. _`tioce_init_provider`:

tioce_init_provider
===================

.. c:function:: int tioce_init_provider( void)

    init SN PCI provider ops for TIO CE

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

