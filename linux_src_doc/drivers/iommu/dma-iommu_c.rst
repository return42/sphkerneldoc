.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/dma-iommu.c

.. _`iommu_get_dma_cookie`:

iommu_get_dma_cookie
====================

.. c:function:: int iommu_get_dma_cookie(struct iommu_domain *domain)

    Acquire DMA-API resources for a domain

    :param domain:
        IOMMU domain to prepare for DMA-API usage
    :type domain: struct iommu_domain \*

.. _`iommu_get_dma_cookie.description`:

Description
-----------

IOMMU drivers should normally call this from their domain_alloc
callback when domain->type == IOMMU_DOMAIN_DMA.

.. _`iommu_get_msi_cookie`:

iommu_get_msi_cookie
====================

.. c:function:: int iommu_get_msi_cookie(struct iommu_domain *domain, dma_addr_t base)

    Acquire just MSI remapping resources

    :param domain:
        IOMMU domain to prepare
    :type domain: struct iommu_domain \*

    :param base:
        Start address of IOVA region for MSI mappings
    :type base: dma_addr_t

.. _`iommu_get_msi_cookie.description`:

Description
-----------

Users who manage their own IOVA allocation and do not want DMA API support,
but would still like to take advantage of automatic MSI remapping, can use
this to initialise their own domain appropriately. Users should reserve a
contiguous IOVA region, starting at \ ``base``\ , large enough to accommodate the
number of PAGE_SIZE mappings necessary to cover every MSI doorbell address
used by the devices attached to \ ``domain``\ .

.. _`iommu_put_dma_cookie`:

iommu_put_dma_cookie
====================

.. c:function:: void iommu_put_dma_cookie(struct iommu_domain *domain)

    Release a domain's DMA mapping resources

    :param domain:
        IOMMU domain previously prepared by \ :c:func:`iommu_get_dma_cookie`\  or
        \ :c:func:`iommu_get_msi_cookie`\ 
    :type domain: struct iommu_domain \*

.. _`iommu_put_dma_cookie.description`:

Description
-----------

IOMMU drivers should normally call this from their domain_free callback.

.. _`iommu_dma_get_resv_regions`:

iommu_dma_get_resv_regions
==========================

.. c:function:: void iommu_dma_get_resv_regions(struct device *dev, struct list_head *list)

    Reserved region driver helper

    :param dev:
        Device from \ :c:func:`iommu_get_resv_regions`\ 
    :type dev: struct device \*

    :param list:
        Reserved region list from \ :c:func:`iommu_get_resv_regions`\ 
    :type list: struct list_head \*

.. _`iommu_dma_get_resv_regions.description`:

Description
-----------

IOMMU drivers can use this to implement their .get_resv_regions callback
for general non-IOMMU-specific reservations. Currently, this covers GICv3
ITS region reservation on ACPI based ARM platforms that may require HW MSI
reservation.

.. _`iommu_dma_init_domain`:

iommu_dma_init_domain
=====================

.. c:function:: int iommu_dma_init_domain(struct iommu_domain *domain, dma_addr_t base, u64 size, struct device *dev)

    Initialise a DMA mapping domain

    :param domain:
        IOMMU domain previously prepared by \ :c:func:`iommu_get_dma_cookie`\ 
    :type domain: struct iommu_domain \*

    :param base:
        IOVA at which the mappable address space starts
    :type base: dma_addr_t

    :param size:
        Size of IOVA space
    :type size: u64

    :param dev:
        Device the domain is being initialised for
    :type dev: struct device \*

.. _`iommu_dma_init_domain.description`:

Description
-----------

\ ``base``\  and \ ``size``\  should be exact multiples of IOMMU page granularity to
avoid rounding surprises. If necessary, we reserve the page at address 0
to ensure it is an invalid IOVA. It is safe to reinitialise a domain, but
any change which could make prior IOVAs invalid will fail.

.. _`dma_info_to_prot`:

dma_info_to_prot
================

.. c:function:: int dma_info_to_prot(enum dma_data_direction dir, bool coherent, unsigned long attrs)

    Translate DMA API directions and attributes to IOMMU API page flags.

    :param dir:
        Direction of DMA transfer
    :type dir: enum dma_data_direction

    :param coherent:
        Is the DMA master cache-coherent?
    :type coherent: bool

    :param attrs:
        DMA attributes for the mapping
    :type attrs: unsigned long

.. _`dma_info_to_prot.return`:

Return
------

corresponding IOMMU API page protection flags

.. _`iommu_dma_free`:

iommu_dma_free
==============

.. c:function:: void iommu_dma_free(struct device *dev, struct page **pages, size_t size, dma_addr_t *handle)

    Free a buffer allocated by \ :c:func:`iommu_dma_alloc`\ 

    :param dev:
        Device which owns this buffer
    :type dev: struct device \*

    :param pages:
        Array of buffer pages as returned by \ :c:func:`iommu_dma_alloc`\ 
    :type pages: struct page \*\*

    :param size:
        Size of buffer in bytes
    :type size: size_t

    :param handle:
        DMA address of buffer
    :type handle: dma_addr_t \*

.. _`iommu_dma_free.description`:

Description
-----------

Frees both the pages associated with the buffer, and the array
describing them

.. _`iommu_dma_alloc`:

iommu_dma_alloc
===============

.. c:function:: struct page **iommu_dma_alloc(struct device *dev, size_t size, gfp_t gfp, unsigned long attrs, int prot, dma_addr_t *handle, void (*flush_page)(struct device *, const void *, phys_addr_t))

    Allocate and map a buffer contiguous in IOVA space

    :param dev:
        Device to allocate memory for. Must be a real device
        attached to an iommu_dma_domain
    :type dev: struct device \*

    :param size:
        Size of buffer in bytes
    :type size: size_t

    :param gfp:
        Allocation flags
    :type gfp: gfp_t

    :param attrs:
        DMA attributes for this allocation
    :type attrs: unsigned long

    :param prot:
        IOMMU mapping flags
    :type prot: int

    :param handle:
        Out argument for allocated DMA handle
    :type handle: dma_addr_t \*

    :param void (\*flush_page)(struct device \*, const void \*, phys_addr_t):
        Arch callback which must ensure PAGE_SIZE bytes from the
        given VA/PA are visible to the given non-coherent device.

.. _`iommu_dma_alloc.description`:

Description
-----------

If \ ``size``\  is less than PAGE_SIZE, then a full CPU page will be allocated,
but an IOMMU which supports smaller pages might not map the whole thing.

.. _`iommu_dma_alloc.return`:

Return
------

Array of struct page pointers describing the buffer,
or NULL on failure.

.. _`iommu_dma_mmap`:

iommu_dma_mmap
==============

.. c:function:: int iommu_dma_mmap(struct page **pages, size_t size, struct vm_area_struct *vma)

    Map a buffer into provided user VMA

    :param pages:
        Array representing buffer from \ :c:func:`iommu_dma_alloc`\ 
    :type pages: struct page \*\*

    :param size:
        Size of buffer in bytes
    :type size: size_t

    :param vma:
        VMA describing requested userspace mapping
    :type vma: struct vm_area_struct \*

.. _`iommu_dma_mmap.description`:

Description
-----------

Maps the pages of the buffer in \ ``pages``\  into \ ``vma``\ . The caller is responsible
for verifying the correct size and protection of \ ``vma``\  beforehand.

.. This file was automatic generated / don't edit.

