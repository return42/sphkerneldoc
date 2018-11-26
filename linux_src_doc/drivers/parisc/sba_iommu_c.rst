.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parisc/sba_iommu.c

.. _`sba_dump_ranges`:

sba_dump_ranges
===============

.. c:function:: void sba_dump_ranges(void __iomem *hpa)

    debugging only - print ranges assigned to this IOA

    :param hpa:
        base address of the sba
    :type hpa: void __iomem \*

.. _`sba_dump_ranges.description`:

Description
-----------

Print the MMIO and IO Port address ranges forwarded by an Astro/Ike/RIO
IO Adapter (aka Bus Converter).

.. _`sba_dump_tlb`:

sba_dump_tlb
============

.. c:function:: void sba_dump_tlb(void __iomem *hpa)

    debugging only - print IOMMU operating parameters

    :param hpa:
        base address of the IOMMU
    :type hpa: void __iomem \*

.. _`sba_dump_tlb.description`:

Description
-----------

Print the size/location of the IO MMU PDIR.

.. _`sba_dump_pdir_entry`:

sba_dump_pdir_entry
===================

.. c:function:: void sba_dump_pdir_entry(struct ioc *ioc, char *msg, uint pide)

    debugging only - print one IOMMU PDIR entry

    :param ioc:
        IO MMU structure which owns the pdir we are interested in.
    :type ioc: struct ioc \*

    :param msg:
        text to print ont the output line.
    :type msg: char \*

    :param pide:
        pdir index.
    :type pide: uint

.. _`sba_dump_pdir_entry.description`:

Description
-----------

Print one entry of the IO MMU PDIR in human readable form.

.. _`sba_check_pdir`:

sba_check_pdir
==============

.. c:function:: int sba_check_pdir(struct ioc *ioc, char *msg)

    debugging only - consistency checker

    :param ioc:
        IO MMU structure which owns the pdir we are interested in.
    :type ioc: struct ioc \*

    :param msg:
        text to print ont the output line.
    :type msg: char \*

.. _`sba_check_pdir.description`:

Description
-----------

Verify the resource map and pdir state is consistent

.. _`sba_dump_sg`:

sba_dump_sg
===========

.. c:function:: void sba_dump_sg(struct ioc *ioc, struct scatterlist *startsg, int nents)

    debugging only - print Scatter-Gather list

    :param ioc:
        IO MMU structure which owns the pdir we are interested in.
    :type ioc: struct ioc \*

    :param startsg:
        head of the SG list
    :type startsg: struct scatterlist \*

    :param nents:
        number of entries in SG list
    :type nents: int

.. _`sba_dump_sg.description`:

Description
-----------

print the SG list so we can verify it's correct by hand.

.. _`sba_search_bitmap`:

sba_search_bitmap
=================

.. c:function:: SBA_INLINE unsigned long sba_search_bitmap(struct ioc *ioc, struct device *dev, unsigned long bits_wanted)

    find free space in IO PDIR resource bitmap

    :param ioc:
        IO MMU structure which owns the pdir we are interested in.
    :type ioc: struct ioc \*

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param bits_wanted:
        number of entries we need.
    :type bits_wanted: unsigned long

.. _`sba_search_bitmap.description`:

Description
-----------

Find consecutive free bits in resource bitmap.
Each bit represents one entry in the IO Pdir.

.. _`sba_search_bitmap.cool-perf-optimization`:

Cool perf optimization
----------------------

search for log2(size) bits at a time.

.. _`sba_alloc_range`:

sba_alloc_range
===============

.. c:function:: int sba_alloc_range(struct ioc *ioc, struct device *dev, size_t size)

    find free bits and mark them in IO PDIR resource bitmap

    :param ioc:
        IO MMU structure which owns the pdir we are interested in.
    :type ioc: struct ioc \*

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param size:
        number of bytes to create a mapping for
    :type size: size_t

.. _`sba_alloc_range.description`:

Description
-----------

Given a size, find consecutive unmarked and then mark those bits in the
resource bit map.

.. _`sba_free_range`:

sba_free_range
==============

.. c:function:: SBA_INLINE void sba_free_range(struct ioc *ioc, dma_addr_t iova, size_t size)

    unmark bits in IO PDIR resource bitmap

    :param ioc:
        IO MMU structure which owns the pdir we are interested in.
    :type ioc: struct ioc \*

    :param iova:
        IO virtual address which was previously allocated.
    :type iova: dma_addr_t

    :param size:
        number of bytes to create a mapping for
    :type size: size_t

.. _`sba_free_range.description`:

Description
-----------

clear bits in the ioc's resource map

.. _`sba_io_pdir_entry`:

sba_io_pdir_entry
=================

.. c:function:: void SBA_INLINE sba_io_pdir_entry(u64 *pdir_ptr, space_t sid, unsigned long vba, unsigned long hint)

    fill in one IO PDIR entry

    :param pdir_ptr:
        pointer to IO PDIR entry
    :type pdir_ptr: u64 \*

    :param sid:
        process Space ID - currently only support KERNEL_SPACE
    :type sid: space_t

    :param vba:
        Virtual CPU address of buffer to map
    :type vba: unsigned long

    :param hint:
        DMA hint set to use for this mapping
    :type hint: unsigned long

.. _`sba_io_pdir_entry.description`:

Description
-----------

SBA Mapping Routine

Given a virtual address (vba, arg2) and space id, (sid, arg1)
\ :c:func:`sba_io_pdir_entry`\  loads the I/O PDIR entry pointed to by
pdir_ptr (arg0).
Using the bass-ackwards HP bit numbering, Each IO Pdir entry
for Astro/Ike looks like:


0                    19                                 51   55       63
+-+---------------------+----------------------------------+----+--------+
\|V\|        U            \|            PPN[43:12]            \| U  \|   VI   \|
+-+---------------------+----------------------------------+----+--------+

Pluto is basically identical, supports fewer physical address bits:

0                       23                              51   55       63
+-+------------------------+-------------------------------+----+--------+
\|V\|        U               \|         PPN[39:12]            \| U  \|   VI   \|
+-+------------------------+-------------------------------+----+--------+

V  == Valid Bit  (Most Significant Bit is bit 0)
U  == Unused
PPN == Physical Page Number
VI  == Virtual Index (aka Coherent Index)

LPA instruction output is put into PPN field.
LCI (Load Coherence Index) instruction provides the "VI" bits.

We pre-swap the bytes since PCX-W is Big Endian and the
IOMMU uses little endian for the pdir.

.. _`sba_mark_invalid`:

sba_mark_invalid
================

.. c:function:: SBA_INLINE void sba_mark_invalid(struct ioc *ioc, dma_addr_t iova, size_t byte_cnt)

    invalidate one or more IO PDIR entries

    :param ioc:
        IO MMU structure which owns the pdir we are interested in.
    :type ioc: struct ioc \*

    :param iova:
        IO Virtual Address mapped earlier
    :type iova: dma_addr_t

    :param byte_cnt:
        number of bytes this mapping covers.
    :type byte_cnt: size_t

.. _`sba_mark_invalid.description`:

Description
-----------

Marking the IO PDIR entry(ies) as Invalid and invalidate
corresponding IO TLB entry. The Ike PCOM (Purge Command Register)
is to purge stale entries in the IO TLB when unmapping entries.

The PCOM register supports purging of multiple pages, with a minium
of 1 page and a maximum of 2GB. Hardware requires the address be
aligned to the size of the range being purged. The size of the range
must be a power of 2. The "Cool perf optimization" in the
allocation routine helps keep that true.

.. _`sba_dma_supported`:

sba_dma_supported
=================

.. c:function:: int sba_dma_supported(struct device *dev, u64 mask)

    PCI driver can query DMA support

    :param dev:
        instance of PCI owned by the driver that's asking
    :type dev: struct device \*

    :param mask:
        number of address bits this PCI device can handle
    :type mask: u64

.. _`sba_dma_supported.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_map_single`:

sba_map_single
==============

.. c:function:: dma_addr_t sba_map_single(struct device *dev, void *addr, size_t size, enum dma_data_direction direction)

    map one buffer and return IOVA for DMA

    :param dev:
        instance of PCI owned by the driver that's asking.
    :type dev: struct device \*

    :param addr:
        driver buffer to map.
    :type addr: void \*

    :param size:
        number of bytes to map in driver buffer.
    :type size: size_t

    :param direction:
        R/W or both.
    :type direction: enum dma_data_direction

.. _`sba_map_single.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_unmap_page`:

sba_unmap_page
==============

.. c:function:: void sba_unmap_page(struct device *dev, dma_addr_t iova, size_t size, enum dma_data_direction direction, unsigned long attrs)

    unmap one IOVA and free resources

    :param dev:
        instance of PCI owned by the driver that's asking.
    :type dev: struct device \*

    :param iova:
        IOVA of driver buffer previously mapped.
    :type iova: dma_addr_t

    :param size:
        number of bytes mapped in driver buffer.
    :type size: size_t

    :param direction:
        R/W or both.
    :type direction: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`sba_unmap_page.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_alloc`:

sba_alloc
=========

.. c:function:: void *sba_alloc(struct device *hwdev, size_t size, dma_addr_t *dma_handle, gfp_t gfp, unsigned long attrs)

    allocate/map shared mem for DMA

    :param hwdev:
        instance of PCI owned by the driver that's asking.
    :type hwdev: struct device \*

    :param size:
        number of bytes mapped in driver buffer.
    :type size: size_t

    :param dma_handle:
        IOVA of new buffer.
    :type dma_handle: dma_addr_t \*

    :param gfp:
        *undescribed*
    :type gfp: gfp_t

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`sba_alloc.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_free`:

sba_free
========

.. c:function:: void sba_free(struct device *hwdev, size_t size, void *vaddr, dma_addr_t dma_handle, unsigned long attrs)

    free/unmap shared mem for DMA

    :param hwdev:
        instance of PCI owned by the driver that's asking.
    :type hwdev: struct device \*

    :param size:
        number of bytes mapped in driver buffer.
    :type size: size_t

    :param vaddr:
        virtual address IOVA of "consistent" buffer.
    :type vaddr: void \*

    :param dma_handle:
        *undescribed*
    :type dma_handle: dma_addr_t

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`sba_free.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_map_sg`:

sba_map_sg
==========

.. c:function:: int sba_map_sg(struct device *dev, struct scatterlist *sglist, int nents, enum dma_data_direction direction, unsigned long attrs)

    map Scatter/Gather list

    :param dev:
        instance of PCI owned by the driver that's asking.
    :type dev: struct device \*

    :param sglist:
        array of buffer/length pairs
    :type sglist: struct scatterlist \*

    :param nents:
        number of entries in list
    :type nents: int

    :param direction:
        R/W or both.
    :type direction: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`sba_map_sg.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_unmap_sg`:

sba_unmap_sg
============

.. c:function:: void sba_unmap_sg(struct device *dev, struct scatterlist *sglist, int nents, enum dma_data_direction direction, unsigned long attrs)

    unmap Scatter/Gather list

    :param dev:
        instance of PCI owned by the driver that's asking.
    :type dev: struct device \*

    :param sglist:
        array of buffer/length pairs
    :type sglist: struct scatterlist \*

    :param nents:
        number of entries in list
    :type nents: int

    :param direction:
        R/W or both.
    :type direction: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`sba_unmap_sg.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_get_iommu`:

sba_get_iommu
=============

.. c:function:: void *sba_get_iommu(struct parisc_device *pci_hba)

    Assign the iommu pointer for the pci bus controller.

    :param pci_hba:
        *undescribed*
    :type pci_hba: struct parisc_device \*

.. _`sba_get_iommu.description`:

Description
-----------

Returns the appropriate IOMMU data for the given parisc PCI controller.
This is cached and used later for PCI DMA Mapping.

.. _`sba_directed_lmmio`:

sba_directed_lmmio
==================

.. c:function:: void sba_directed_lmmio(struct parisc_device *pci_hba, struct resource *r)

    return first directed LMMIO range routed to rope

    :param pci_hba:
        *undescribed*
    :type pci_hba: struct parisc_device \*

    :param r:
        resource PCI host controller wants start/end fields assigned.
    :type r: struct resource \*

.. _`sba_directed_lmmio.description`:

Description
-----------

For the given parisc PCI controller, determine if any direct ranges
are routed down the corresponding rope.

.. _`sba_distributed_lmmio`:

sba_distributed_lmmio
=====================

.. c:function:: void sba_distributed_lmmio(struct parisc_device *pci_hba, struct resource *r)

    return portion of distributed LMMIO range

    :param pci_hba:
        *undescribed*
    :type pci_hba: struct parisc_device \*

    :param r:
        resource PCI host controller wants start/end fields assigned.
    :type r: struct resource \*

.. _`sba_distributed_lmmio.description`:

Description
-----------

For the given parisc PCI controller, return portion of distributed LMMIO
range. The distributed LMMIO is always present and it's just a question
of the base address and size of the range.

.. This file was automatic generated / don't edit.

