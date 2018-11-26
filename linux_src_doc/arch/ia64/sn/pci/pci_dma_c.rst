.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/sn/pci/pci_dma.c

.. _`sn_dma_supported`:

sn_dma_supported
================

.. c:function:: int sn_dma_supported(struct device *dev, u64 mask)

    test a DMA mask

    :param dev:
        device to test
    :type dev: struct device \*

    :param mask:
        DMA mask to test
    :type mask: u64

.. _`sn_dma_supported.description`:

Description
-----------

Return whether the given PCI device DMA address mask can be supported
properly.  For example, if your device can only drive the low 24-bits
during PCI bus mastering, then you would pass 0x00ffffff as the mask to
this function.  Of course, SN only supports devices that have 32 or more
address bits when using the PMU.

.. _`sn_dma_set_mask`:

sn_dma_set_mask
===============

.. c:function:: int sn_dma_set_mask(struct device *dev, u64 dma_mask)

    set the DMA mask

    :param dev:
        device to set
    :type dev: struct device \*

    :param dma_mask:
        new mask
    :type dma_mask: u64

.. _`sn_dma_set_mask.description`:

Description
-----------

Set \ ``dev``\ 's DMA mask if the hw supports it.

.. _`sn_dma_alloc_coherent`:

sn_dma_alloc_coherent
=====================

.. c:function:: void *sn_dma_alloc_coherent(struct device *dev, size_t size, dma_addr_t *dma_handle, gfp_t flags, unsigned long attrs)

    allocate memory for coherent DMA

    :param dev:
        device to allocate for
    :type dev: struct device \*

    :param size:
        size of the region
    :type size: size_t

    :param dma_handle:
        DMA (bus) address
    :type dma_handle: dma_addr_t \*

    :param flags:
        memory allocation flags
    :type flags: gfp_t

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`sn_dma_alloc_coherent.description`:

Description
-----------

\ :c:func:`dma_alloc_coherent`\  returns a pointer to a memory region suitable for
coherent DMA traffic to/from a PCI device.  On SN platforms, this means
that \ ``dma_handle``\  will have the \ ``PCIIO_DMA_CMD``\  flag set.

This interface is usually used for "command" streams (e.g. the command
queue for a SCSI controller).  See Documentation/DMA-API.txt for
more information.

.. _`sn_dma_free_coherent`:

sn_dma_free_coherent
====================

.. c:function:: void sn_dma_free_coherent(struct device *dev, size_t size, void *cpu_addr, dma_addr_t dma_handle, unsigned long attrs)

    free memory associated with coherent DMAable region

    :param dev:
        device to free for
    :type dev: struct device \*

    :param size:
        size to free
    :type size: size_t

    :param cpu_addr:
        kernel virtual address to free
    :type cpu_addr: void \*

    :param dma_handle:
        DMA address associated with this region
    :type dma_handle: dma_addr_t

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`sn_dma_free_coherent.description`:

Description
-----------

Frees the memory allocated by \ :c:func:`dma_alloc_coherent`\ , potentially unmapping
any associated IOMMU mappings.

.. _`sn_dma_map_page`:

sn_dma_map_page
===============

.. c:function:: dma_addr_t sn_dma_map_page(struct device *dev, struct page *page, unsigned long offset, size_t size, enum dma_data_direction dir, unsigned long attrs)

    map a single page for DMA

    :param dev:
        device to map for
    :type dev: struct device \*

    :param page:
        *undescribed*
    :type page: struct page \*

    :param offset:
        *undescribed*
    :type offset: unsigned long

    :param size:
        size of the region
    :type size: size_t

    :param dir:
        *undescribed*
    :type dir: enum dma_data_direction

    :param attrs:
        optional dma attributes
    :type attrs: unsigned long

.. _`sn_dma_map_page.description`:

Description
-----------

Map the region pointed to by \ ``cpu_addr``\  for DMA and return the
DMA address.

We map this to the one step pcibr_dmamap_trans interface rather than
the two step pcibr_dmamap_alloc/pcibr_dmamap_addr because we have
no way of saving the dmamap handle from the alloc to later free
(which is pretty much unacceptable).

mappings with the DMA_ATTR_WRITE_BARRIER get mapped with
\ :c:func:`dma_map_consistent`\  so that writes force a flush of pending DMA.
(See "SGI Altix Architecture Considerations for Linux Device Drivers",

.. _`sn_dma_map_page.document-number`:

Document Number
---------------

007-4763-001)

.. _`sn_dma_map_page.todo`:

TODO
----

simplify our interface;
figure out how to save dmamap handle so can use two step.

.. _`sn_dma_unmap_page`:

sn_dma_unmap_page
=================

.. c:function:: void sn_dma_unmap_page(struct device *dev, dma_addr_t dma_addr, size_t size, enum dma_data_direction dir, unsigned long attrs)

    unamp a DMA mapped page

    :param dev:
        device to sync
    :type dev: struct device \*

    :param dma_addr:
        DMA address to sync
    :type dma_addr: dma_addr_t

    :param size:
        size of region
    :type size: size_t

    :param dir:
        *undescribed*
    :type dir: enum dma_data_direction

    :param attrs:
        optional dma attributes
    :type attrs: unsigned long

.. _`sn_dma_unmap_page.description`:

Description
-----------

This routine is supposed to sync the DMA region specified
by \ ``dma_handle``\  into the coherence domain.  On SN, we're always cache
coherent, so we just need to free any ATEs associated with this mapping.

.. _`sn_dma_unmap_sg`:

sn_dma_unmap_sg
===============

.. c:function:: void sn_dma_unmap_sg(struct device *dev, struct scatterlist *sgl, int nhwentries, enum dma_data_direction dir, unsigned long attrs)

    unmap a DMA scatterlist

    :param dev:
        device to unmap
    :type dev: struct device \*

    :param sgl:
        *undescribed*
    :type sgl: struct scatterlist \*

    :param nhwentries:
        number of scatterlist entries
    :type nhwentries: int

    :param dir:
        *undescribed*
    :type dir: enum dma_data_direction

    :param attrs:
        optional dma attributes
    :type attrs: unsigned long

.. _`sn_dma_unmap_sg.description`:

Description
-----------

Unmap a set of streaming mode DMA translations.

.. _`sn_dma_map_sg`:

sn_dma_map_sg
=============

.. c:function:: int sn_dma_map_sg(struct device *dev, struct scatterlist *sgl, int nhwentries, enum dma_data_direction dir, unsigned long attrs)

    map a scatterlist for DMA

    :param dev:
        device to map for
    :type dev: struct device \*

    :param sgl:
        *undescribed*
    :type sgl: struct scatterlist \*

    :param nhwentries:
        number of entries
    :type nhwentries: int

    :param dir:
        *undescribed*
    :type dir: enum dma_data_direction

    :param attrs:
        optional dma attributes
    :type attrs: unsigned long

.. _`sn_dma_map_sg.description`:

Description
-----------

mappings with the DMA_ATTR_WRITE_BARRIER get mapped with
\ :c:func:`dma_map_consistent`\  so that writes force a flush of pending DMA.
(See "SGI Altix Architecture Considerations for Linux Device Drivers",

.. _`sn_dma_map_sg.document-number`:

Document Number
---------------

007-4763-001)

Maps each entry of \ ``sg``\  for DMA.

.. This file was automatic generated / don't edit.

