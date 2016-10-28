.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parisc/sba_iommu.c

.. _`sba_dump_ranges`:

sba_dump_ranges
===============

.. c:function:: void sba_dump_ranges(void __iomem *hpa)

    debugging only - print ranges assigned to this IOA

    :param void __iomem \*hpa:
        base address of the sba

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

    :param void __iomem \*hpa:
        base address of the IOMMU

.. _`sba_dump_tlb.description`:

Description
-----------

Print the size/location of the IO MMU PDIR.

.. _`sba_dump_pdir_entry`:

sba_dump_pdir_entry
===================

.. c:function:: void sba_dump_pdir_entry(struct ioc *ioc, char *msg, uint pide)

    debugging only - print one IOMMU PDIR entry

    :param struct ioc \*ioc:
        IO MMU structure which owns the pdir we are interested in.

    :param char \*msg:
        text to print ont the output line.

    :param uint pide:
        pdir index.

.. _`sba_dump_pdir_entry.description`:

Description
-----------

Print one entry of the IO MMU PDIR in human readable form.

.. _`sba_check_pdir`:

sba_check_pdir
==============

.. c:function:: int sba_check_pdir(struct ioc *ioc, char *msg)

    debugging only - consistency checker

    :param struct ioc \*ioc:
        IO MMU structure which owns the pdir we are interested in.

    :param char \*msg:
        text to print ont the output line.

.. _`sba_check_pdir.description`:

Description
-----------

Verify the resource map and pdir state is consistent

.. _`sba_dump_sg`:

sba_dump_sg
===========

.. c:function:: void sba_dump_sg(struct ioc *ioc, struct scatterlist *startsg, int nents)

    debugging only - print Scatter-Gather list

    :param struct ioc \*ioc:
        IO MMU structure which owns the pdir we are interested in.

    :param struct scatterlist \*startsg:
        head of the SG list

    :param int nents:
        number of entries in SG list

.. _`sba_dump_sg.description`:

Description
-----------

print the SG list so we can verify it's correct by hand.

.. _`sba_search_bitmap`:

sba_search_bitmap
=================

.. c:function:: SBA_INLINE unsigned long sba_search_bitmap(struct ioc *ioc, struct device *dev, unsigned long bits_wanted)

    find free space in IO PDIR resource bitmap

    :param struct ioc \*ioc:
        IO MMU structure which owns the pdir we are interested in.

    :param struct device \*dev:
        *undescribed*

    :param unsigned long bits_wanted:
        number of entries we need.

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

    :param struct ioc \*ioc:
        IO MMU structure which owns the pdir we are interested in.

    :param struct device \*dev:
        *undescribed*

    :param size_t size:
        number of bytes to create a mapping for

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

    :param struct ioc \*ioc:
        IO MMU structure which owns the pdir we are interested in.

    :param dma_addr_t iova:
        IO virtual address which was previously allocated.

    :param size_t size:
        number of bytes to create a mapping for

.. _`sba_free_range.description`:

Description
-----------

clear bits in the ioc's resource map

.. _`sba_io_pdir_entry`:

sba_io_pdir_entry
=================

.. c:function:: void SBA_INLINE sba_io_pdir_entry(u64 *pdir_ptr, space_t sid, unsigned long vba, unsigned long hint)

    fill in one IO PDIR entry

    :param u64 \*pdir_ptr:
        pointer to IO PDIR entry

    :param space_t sid:
        process Space ID - currently only support KERNEL_SPACE

    :param unsigned long vba:
        Virtual CPU address of buffer to map

    :param unsigned long hint:
        DMA hint set to use for this mapping

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

    :param struct ioc \*ioc:
        IO MMU structure which owns the pdir we are interested in.

    :param dma_addr_t iova:
        IO Virtual Address mapped earlier

    :param size_t byte_cnt:
        number of bytes this mapping covers.

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

    :param struct device \*dev:
        instance of PCI owned by the driver that's asking

    :param u64 mask:
        number of address bits this PCI device can handle

.. _`sba_dma_supported.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_map_single`:

sba_map_single
==============

.. c:function:: dma_addr_t sba_map_single(struct device *dev, void *addr, size_t size, enum dma_data_direction direction)

    map one buffer and return IOVA for DMA

    :param struct device \*dev:
        instance of PCI owned by the driver that's asking.

    :param void \*addr:
        driver buffer to map.

    :param size_t size:
        number of bytes to map in driver buffer.

    :param enum dma_data_direction direction:
        R/W or both.

.. _`sba_map_single.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_unmap_page`:

sba_unmap_page
==============

.. c:function:: void sba_unmap_page(struct device *dev, dma_addr_t iova, size_t size, enum dma_data_direction direction, struct dma_attrs *attrs)

    unmap one IOVA and free resources

    :param struct device \*dev:
        instance of PCI owned by the driver that's asking.

    :param dma_addr_t iova:
        IOVA of driver buffer previously mapped.

    :param size_t size:
        number of bytes mapped in driver buffer.

    :param enum dma_data_direction direction:
        R/W or both.

    :param struct dma_attrs \*attrs:
        *undescribed*

.. _`sba_unmap_page.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_alloc`:

sba_alloc
=========

.. c:function:: void *sba_alloc(struct device *hwdev, size_t size, dma_addr_t *dma_handle, gfp_t gfp, struct dma_attrs *attrs)

    allocate/map shared mem for DMA

    :param struct device \*hwdev:
        instance of PCI owned by the driver that's asking.

    :param size_t size:
        number of bytes mapped in driver buffer.

    :param dma_addr_t \*dma_handle:
        IOVA of new buffer.

    :param gfp_t gfp:
        *undescribed*

    :param struct dma_attrs \*attrs:
        *undescribed*

.. _`sba_alloc.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_free`:

sba_free
========

.. c:function:: void sba_free(struct device *hwdev, size_t size, void *vaddr, dma_addr_t dma_handle, struct dma_attrs *attrs)

    free/unmap shared mem for DMA

    :param struct device \*hwdev:
        instance of PCI owned by the driver that's asking.

    :param size_t size:
        number of bytes mapped in driver buffer.

    :param void \*vaddr:
        virtual address IOVA of "consistent" buffer.

    :param dma_addr_t dma_handle:
        *undescribed*

    :param struct dma_attrs \*attrs:
        *undescribed*

.. _`sba_free.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_map_sg`:

sba_map_sg
==========

.. c:function:: int sba_map_sg(struct device *dev, struct scatterlist *sglist, int nents, enum dma_data_direction direction, struct dma_attrs *attrs)

    map Scatter/Gather list

    :param struct device \*dev:
        instance of PCI owned by the driver that's asking.

    :param struct scatterlist \*sglist:
        array of buffer/length pairs

    :param int nents:
        number of entries in list

    :param enum dma_data_direction direction:
        R/W or both.

    :param struct dma_attrs \*attrs:
        *undescribed*

.. _`sba_map_sg.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_unmap_sg`:

sba_unmap_sg
============

.. c:function:: void sba_unmap_sg(struct device *dev, struct scatterlist *sglist, int nents, enum dma_data_direction direction, struct dma_attrs *attrs)

    unmap Scatter/Gather list

    :param struct device \*dev:
        instance of PCI owned by the driver that's asking.

    :param struct scatterlist \*sglist:
        array of buffer/length pairs

    :param int nents:
        number of entries in list

    :param enum dma_data_direction direction:
        R/W or both.

    :param struct dma_attrs \*attrs:
        *undescribed*

.. _`sba_unmap_sg.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_get_iommu`:

sba_get_iommu
=============

.. c:function:: void *sba_get_iommu(struct parisc_device *pci_hba)

    Assign the iommu pointer for the pci bus controller.

    :param struct parisc_device \*pci_hba:
        *undescribed*

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

    :param struct parisc_device \*pci_hba:
        *undescribed*

    :param struct resource \*r:
        resource PCI host controller wants start/end fields assigned.

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

    :param struct parisc_device \*pci_hba:
        *undescribed*

    :param struct resource \*r:
        resource PCI host controller wants start/end fields assigned.

.. _`sba_distributed_lmmio.description`:

Description
-----------

For the given parisc PCI controller, return portion of distributed LMMIO
range. The distributed LMMIO is always present and it's just a question
of the base address and size of the range.

.. This file was automatic generated / don't edit.

