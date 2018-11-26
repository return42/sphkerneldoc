.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/hp/common/sba_iommu.c

.. _`sba_dump_tlb`:

sba_dump_tlb
============

.. c:function:: void sba_dump_tlb(char *hpa)

    debugging only - print IOMMU operating parameters

    :param hpa:
        base address of the IOMMU
    :type hpa: char \*

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

.. _`get_iovp_order`:

get_iovp_order
==============

.. c:function:: SBA_INLINE int get_iovp_order(unsigned long size)

    to PAGE_SIZE being the minimum mapping alignment and TC flush granularity. It only incurs about 1 clock cycle to use this one with the static variable and makes the code more intuitive.

    :param size:
        *undescribed*
    :type size: unsigned long

.. _`sba_search_bitmap`:

sba_search_bitmap
=================

.. c:function:: SBA_INLINE unsigned long sba_search_bitmap(struct ioc *ioc, struct device *dev, unsigned long bits_wanted, int use_hint)

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

    :param use_hint:
        use res_hint to indicate where to start looking
    :type use_hint: int

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

.. c:function::  sba_io_pdir_entry( pdir_ptr,  vba)

    fill in one IO PDIR entry

    :param pdir_ptr:
        pointer to IO PDIR entry
    :type pdir_ptr: 

    :param vba:
        Virtual CPU address of buffer to map
    :type vba: 

.. _`sba_io_pdir_entry.description`:

Description
-----------

SBA Mapping Routine

Given a virtual address (vba, arg1) \ :c:func:`sba_io_pdir_entry`\ 
loads the I/O PDIR entry pointed to by pdir_ptr (arg0).
Each IO Pdir entry consists of 8 bytes as shown below
(LSB == bit 0):

63                    40                                 11    7        0
+-+---------------------+----------------------------------+----+--------+
\|V\|        U            \|            PPN[39:12]            \| U  \|   FF   \|
+-+---------------------+----------------------------------+----+--------+

V  == Valid Bit
U  == Unused
PPN == Physical Page Number

The physical address fields are filled with the results of \ :c:func:`virt_to_phys`\ 
on the vba.

.. _`mark_clean`:

mark_clean
==========

.. c:function:: void mark_clean(void *addr, size_t size)

    cache coherent, any (complete) pages that were written via DMA can be marked as "clean" so that \ :c:func:`lazy_mmu_prot_update`\  doesn't have to flush them when they get mapped into an executable vm-area.

    :param addr:
        *undescribed*
    :type addr: void \*

    :param size:
        *undescribed*
    :type size: size_t

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
corresponding IO TLB entry. The PCOM (Purge Command Register)
is to purge stale entries in the IO TLB when unmapping entries.

The PCOM register supports purging of multiple pages, with a minium
of 1 page and a maximum of 2GB. Hardware requires the address be
aligned to the size of the range being purged. The size of the range
must be a power of 2. The "Cool perf optimization" in the
allocation routine helps keep that true.

.. _`sba_map_page`:

sba_map_page
============

.. c:function:: dma_addr_t sba_map_page(struct device *dev, struct page *page, unsigned long poff, size_t size, enum dma_data_direction dir, unsigned long attrs)

    map one buffer and return IOVA for DMA

    :param dev:
        instance of PCI owned by the driver that's asking.
    :type dev: struct device \*

    :param page:
        *undescribed*
    :type page: struct page \*

    :param poff:
        *undescribed*
    :type poff: unsigned long

    :param size:
        number of bytes to map in driver buffer.
    :type size: size_t

    :param dir:
        R/W or both.
    :type dir: enum dma_data_direction

    :param attrs:
        optional dma attributes
    :type attrs: unsigned long

.. _`sba_map_page.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_unmap_page`:

sba_unmap_page
==============

.. c:function:: void sba_unmap_page(struct device *dev, dma_addr_t iova, size_t size, enum dma_data_direction dir, unsigned long attrs)

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

    :param dir:
        R/W or both.
    :type dir: enum dma_data_direction

    :param attrs:
        optional dma attributes
    :type attrs: unsigned long

.. _`sba_unmap_page.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_alloc_coherent`:

sba_alloc_coherent
==================

.. c:function:: void *sba_alloc_coherent(struct device *dev, size_t size, dma_addr_t *dma_handle, gfp_t flags, unsigned long attrs)

    allocate/map shared mem for DMA

    :param dev:
        instance of PCI owned by the driver that's asking.
    :type dev: struct device \*

    :param size:
        number of bytes mapped in driver buffer.
    :type size: size_t

    :param dma_handle:
        IOVA of new buffer.
    :type dma_handle: dma_addr_t \*

    :param flags:
        *undescribed*
    :type flags: gfp_t

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`sba_alloc_coherent.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_free_coherent`:

sba_free_coherent
=================

.. c:function:: void sba_free_coherent(struct device *dev, size_t size, void *vaddr, dma_addr_t dma_handle, unsigned long attrs)

    free/unmap shared mem for DMA

    :param dev:
        instance of PCI owned by the driver that's asking.
    :type dev: struct device \*

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

.. _`sba_free_coherent.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_fill_pdir`:

sba_fill_pdir
=============

.. c:function:: SBA_INLINE int sba_fill_pdir(struct ioc *ioc, struct scatterlist *startsg, int nents)

    write allocated SG entries into IO PDIR

    :param ioc:
        IO MMU structure which owns the pdir we are interested in.
    :type ioc: struct ioc \*

    :param startsg:
        list of IOVA/size pairs
    :type startsg: struct scatterlist \*

    :param nents:
        number of entries in startsg list
    :type nents: int

.. _`sba_fill_pdir.description`:

Description
-----------

Take preprocessed SG list and write corresponding entries
in the IO PDIR.

.. _`sba_coalesce_chunks`:

sba_coalesce_chunks
===================

.. c:function:: SBA_INLINE int sba_coalesce_chunks(struct ioc *ioc, struct device *dev, struct scatterlist *startsg, int nents)

    preprocess the SG list

    :param ioc:
        IO MMU structure which owns the pdir we are interested in.
    :type ioc: struct ioc \*

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param startsg:
        list of IOVA/size pairs
    :type startsg: struct scatterlist \*

    :param nents:
        number of entries in startsg list
    :type nents: int

.. _`sba_coalesce_chunks.description`:

Description
-----------

First pass is to walk the SG list and determine where the breaks are
in the DMA stream. Allocates PDIR entries but does not fill them.
Returns the number of DMA chunks.

Doing the fill separate from the coalescing/allocation keeps the
code simpler. Future enhancement could make one pass through
the sglist do both.

.. _`sba_map_sg_attrs`:

sba_map_sg_attrs
================

.. c:function:: int sba_map_sg_attrs(struct device *dev, struct scatterlist *sglist, int nents, enum dma_data_direction dir, unsigned long attrs)

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

    :param dir:
        R/W or both.
    :type dir: enum dma_data_direction

    :param attrs:
        optional dma attributes
    :type attrs: unsigned long

.. _`sba_map_sg_attrs.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. _`sba_unmap_sg_attrs`:

sba_unmap_sg_attrs
==================

.. c:function:: void sba_unmap_sg_attrs(struct device *dev, struct scatterlist *sglist, int nents, enum dma_data_direction dir, unsigned long attrs)

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

    :param dir:
        R/W or both.
    :type dir: enum dma_data_direction

    :param attrs:
        optional dma attributes
    :type attrs: unsigned long

.. _`sba_unmap_sg_attrs.description`:

Description
-----------

See Documentation/DMA-API-HOWTO.txt

.. This file was automatic generated / don't edit.

