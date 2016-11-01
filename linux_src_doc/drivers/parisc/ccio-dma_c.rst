.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parisc/ccio-dma.c

.. _`ccio_alloc_range`:

ccio_alloc_range
================

.. c:function:: int ccio_alloc_range(struct ioc *ioc, struct device *dev, size_t size)

    Allocate pages in the ioc's resource map.

    :param struct ioc \*ioc:
        The I/O Controller.

    :param struct device \*dev:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`ccio_alloc_range.description`:

Description
-----------

This function searches the resource map of the ioc to locate a range
of available pages for the requested size.

.. _`ccio_free_range`:

ccio_free_range
===============

.. c:function:: void ccio_free_range(struct ioc *ioc, dma_addr_t iova, unsigned long pages_mapped)

    Free pages from the ioc's resource map.

    :param struct ioc \*ioc:
        The I/O Controller.

    :param dma_addr_t iova:
        The I/O Virtual Address.

    :param unsigned long pages_mapped:
        The requested number of pages to be freed from the
        I/O Pdir.

.. _`ccio_free_range.description`:

Description
-----------

This function frees the resouces allocated for the iova.

.. _`ccio_io_pdir_entry`:

ccio_io_pdir_entry
==================

.. c:function:: void CCIO_INLINE ccio_io_pdir_entry(u64 *pdir_ptr, space_t sid, unsigned long vba, unsigned long hints)

    Initialize an I/O Pdir.

    :param u64 \*pdir_ptr:
        A pointer into I/O Pdir.

    :param space_t sid:
        The Space Identifier.

    :param unsigned long vba:
        The virtual address.

    :param unsigned long hints:
        The DMA Hint.

.. _`ccio_io_pdir_entry.description`:

Description
-----------

Given a virtual address (vba, arg2) and space id, (sid, arg1),
load the I/O PDIR entry pointed to by pdir_ptr (arg0). Each IO Pdir
entry consists of 8 bytes as shown below (MSB == bit 0):

.. _`ccio_io_pdir_entry.word-0`:

WORD 0
------

+------+----------------+-----------------------------------------------+
\| Phys \| Virtual Index  \|               Phys                            \|
\| 0:3  \|     0:11       \|               4:19                            \|
\|4 bits\|   12 bits      \|              16 bits                          \|
+------+----------------+-----------------------------------------------+

.. _`ccio_io_pdir_entry.word-1`:

WORD 1
------

+-----------------------+-----------------------------------------------+
\|      Phys    \|  Rsvd  \| Prefetch \|Update \|Rsvd  \|Lock  \|Safe  \|Valid  \|
\|     20:39    \|        \| Enable   \|Enable \|      \|Enable\|DMA   \|       \|
\|    20 bits   \| 5 bits \| 1 bit    \|1 bit  \|2 bits\|1 bit \|1 bit \|1 bit  \|
+-----------------------+-----------------------------------------------+

The virtual index field is filled with the results of the LCI
(Load Coherence Index) instruction.  The 8 bits used for the virtual
index are bits 12:19 of the value returned by LCI.

.. _`ccio_clear_io_tlb`:

ccio_clear_io_tlb
=================

.. c:function:: CCIO_INLINE void ccio_clear_io_tlb(struct ioc *ioc, dma_addr_t iovp, size_t byte_cnt)

    Remove stale entries from the I/O TLB.

    :param struct ioc \*ioc:
        The I/O Controller.

    :param dma_addr_t iovp:
        The I/O Virtual Page.

    :param size_t byte_cnt:
        The requested number of bytes to be freed from the I/O Pdir.

.. _`ccio_clear_io_tlb.description`:

Description
-----------

Purge invalid I/O PDIR entries from the I/O TLB.

.. _`ccio_clear_io_tlb.fixme`:

FIXME
-----

Can we change the byte_cnt to pages_mapped?

.. _`ccio_mark_invalid`:

ccio_mark_invalid
=================

.. c:function:: CCIO_INLINE void ccio_mark_invalid(struct ioc *ioc, dma_addr_t iova, size_t byte_cnt)

    Mark the I/O Pdir entries invalid.

    :param struct ioc \*ioc:
        The I/O Controller.

    :param dma_addr_t iova:
        The I/O Virtual Address.

    :param size_t byte_cnt:
        The requested number of bytes to be freed from the I/O Pdir.

.. _`ccio_mark_invalid.description`:

Description
-----------

Mark the I/O Pdir entries invalid and blow away the corresponding I/O
TLB entries.

.. _`ccio_mark_invalid.fixme`:

FIXME
-----

at some threshold it might be "cheaper" to just blow
away the entire I/O TLB instead of individual entries.

Uturn has 256 TLB entries. We don't need to purge every
PDIR entry - just once for each possible TLB entry.
(We do need to maker I/O PDIR entries invalid regardless).

Can we change byte_cnt to pages_mapped?

.. _`ccio_dma_supported`:

ccio_dma_supported
==================

.. c:function:: int ccio_dma_supported(struct device *dev, u64 mask)

    Verify the IOMMU supports the DMA address range.

    :param struct device \*dev:
        The PCI device.

    :param u64 mask:
        A bit mask describing the DMA address range of the device.

.. _`ccio_map_single`:

ccio_map_single
===============

.. c:function:: dma_addr_t ccio_map_single(struct device *dev, void *addr, size_t size, enum dma_data_direction direction)

    Map an address range into the IOMMU.

    :param struct device \*dev:
        The PCI device.

    :param void \*addr:
        The start address of the DMA region.

    :param size_t size:
        The length of the DMA region.

    :param enum dma_data_direction direction:
        The direction of the DMA transaction (to/from device).

.. _`ccio_map_single.description`:

Description
-----------

This function implements the pci_map_single function.

.. _`ccio_unmap_page`:

ccio_unmap_page
===============

.. c:function:: void ccio_unmap_page(struct device *dev, dma_addr_t iova, size_t size, enum dma_data_direction direction, unsigned long attrs)

    Unmap an address range from the IOMMU.

    :param struct device \*dev:
        The PCI device.

    :param dma_addr_t iova:
        *undescribed*

    :param size_t size:
        The length of the DMA region.

    :param enum dma_data_direction direction:
        The direction of the DMA transaction (to/from device).

    :param unsigned long attrs:
        *undescribed*

.. _`ccio_alloc`:

ccio_alloc
==========

.. c:function:: void *ccio_alloc(struct device *dev, size_t size, dma_addr_t *dma_handle, gfp_t flag, unsigned long attrs)

    Allocate a consistent DMA mapping.

    :param struct device \*dev:
        The PCI device.

    :param size_t size:
        The length of the DMA region.

    :param dma_addr_t \*dma_handle:
        The DMA address handed back to the device (not the cpu).

    :param gfp_t flag:
        *undescribed*

    :param unsigned long attrs:
        *undescribed*

.. _`ccio_alloc.description`:

Description
-----------

This function implements the pci_alloc_consistent function.

.. _`ccio_free`:

ccio_free
=========

.. c:function:: void ccio_free(struct device *dev, size_t size, void *cpu_addr, dma_addr_t dma_handle, unsigned long attrs)

    Free a consistent DMA mapping.

    :param struct device \*dev:
        The PCI device.

    :param size_t size:
        The length of the DMA region.

    :param void \*cpu_addr:
        The cpu address returned from the ccio_alloc_consistent.

    :param dma_addr_t dma_handle:
        The device address returned from the ccio_alloc_consistent.

    :param unsigned long attrs:
        *undescribed*

.. _`ccio_free.description`:

Description
-----------

This function implements the pci_free_consistent function.

.. _`ccio_map_sg`:

ccio_map_sg
===========

.. c:function:: int ccio_map_sg(struct device *dev, struct scatterlist *sglist, int nents, enum dma_data_direction direction, unsigned long attrs)

    Map the scatter/gather list into the IOMMU.

    :param struct device \*dev:
        The PCI device.

    :param struct scatterlist \*sglist:
        The scatter/gather list to be mapped in the IOMMU.

    :param int nents:
        The number of entries in the scatter/gather list.

    :param enum dma_data_direction direction:
        The direction of the DMA transaction (to/from device).

    :param unsigned long attrs:
        *undescribed*

.. _`ccio_map_sg.description`:

Description
-----------

This function implements the pci_map_sg function.

.. _`ccio_unmap_sg`:

ccio_unmap_sg
=============

.. c:function:: void ccio_unmap_sg(struct device *dev, struct scatterlist *sglist, int nents, enum dma_data_direction direction, unsigned long attrs)

    Unmap the scatter/gather list from the IOMMU.

    :param struct device \*dev:
        The PCI device.

    :param struct scatterlist \*sglist:
        The scatter/gather list to be unmapped from the IOMMU.

    :param int nents:
        The number of entries in the scatter/gather list.

    :param enum dma_data_direction direction:
        The direction of the DMA transaction (to/from device).

    :param unsigned long attrs:
        *undescribed*

.. _`ccio_unmap_sg.description`:

Description
-----------

This function implements the pci_unmap_sg function.

.. _`ccio_find_ioc`:

ccio_find_ioc
=============

.. c:function:: struct ioc *ccio_find_ioc(int hw_path)

    Find the ioc in the ioc_list

    :param int hw_path:
        The hardware path of the ioc.

.. _`ccio_find_ioc.description`:

Description
-----------

This function searches the ioc_list for an ioc that matches
the provide hardware path.

.. _`ccio_get_iommu`:

ccio_get_iommu
==============

.. c:function:: void *ccio_get_iommu(const struct parisc_device *dev)

    Find the iommu which controls this device

    :param const struct parisc_device \*dev:
        The parisc device.

.. _`ccio_get_iommu.description`:

Description
-----------

This function searches through the registered IOMMU's and returns
the appropriate IOMMU for the device based on its hardware path.

.. _`ccio_ioc_init`:

ccio_ioc_init
=============

.. c:function:: void ccio_ioc_init(struct ioc *ioc)

    Initialize the I/O Controller

    :param struct ioc \*ioc:
        The I/O Controller.

.. _`ccio_ioc_init.description`:

Description
-----------

Initialize the I/O Controller which includes setting up the
I/O Page Directory, the resource map, and initalizing the
U2/Uturn chip into virtual mode.

.. _`ccio_probe`:

ccio_probe
==========

.. c:function:: int ccio_probe(struct parisc_device *dev)

    Determine if ccio should claim this device.

    :param struct parisc_device \*dev:
        The device which has been found

.. _`ccio_probe.description`:

Description
-----------

Determine if ccio should claim this chip (return 0) or not (return 1).
If so, initialize the chip and tell other partners in crime they
have work to do.

.. _`ccio_init`:

ccio_init
=========

.. c:function:: void ccio_init( void)

    ccio initialization procedure.

    :param  void:
        no arguments

.. _`ccio_init.description`:

Description
-----------

Register this driver.

.. This file was automatic generated / don't edit.

