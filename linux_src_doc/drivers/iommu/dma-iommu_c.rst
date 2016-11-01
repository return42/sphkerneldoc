.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/dma-iommu.c

.. _`iommu_get_dma_cookie`:

iommu_get_dma_cookie
====================

.. c:function:: int iommu_get_dma_cookie(struct iommu_domain *domain)

    Acquire DMA-API resources for a domain

    :param struct iommu_domain \*domain:
        IOMMU domain to prepare for DMA-API usage

.. _`iommu_get_dma_cookie.description`:

Description
-----------

IOMMU drivers should normally call this from their domain_alloc
callback when domain->type == IOMMU_DOMAIN_DMA.

.. _`iommu_put_dma_cookie`:

iommu_put_dma_cookie
====================

.. c:function:: void iommu_put_dma_cookie(struct iommu_domain *domain)

    Release a domain's DMA mapping resources

    :param struct iommu_domain \*domain:
        IOMMU domain previously prepared by \ :c:func:`iommu_get_dma_cookie`\ 

.. _`iommu_put_dma_cookie.description`:

Description
-----------

IOMMU drivers should normally call this from their domain_free callback.

.. _`iommu_dma_init_domain`:

iommu_dma_init_domain
=====================

.. c:function:: int iommu_dma_init_domain(struct iommu_domain *domain, dma_addr_t base, u64 size, struct device *dev)

    Initialise a DMA mapping domain

    :param struct iommu_domain \*domain:
        IOMMU domain previously prepared by \ :c:func:`iommu_get_dma_cookie`\ 

    :param dma_addr_t base:
        IOVA at which the mappable address space starts

    :param u64 size:
        Size of IOVA space

    :param struct device \*dev:
        Device the domain is being initialised for

.. _`iommu_dma_init_domain.description`:

Description
-----------

@base and \ ``size``\  should be exact multiples of IOMMU page granularity to
avoid rounding surprises. If necessary, we reserve the page at address 0
to ensure it is an invalid IOVA. It is safe to reinitialise a domain, but
any change which could make prior IOVAs invalid will fail.

.. _`dma_direction_to_prot`:

dma_direction_to_prot
=====================

.. c:function:: int dma_direction_to_prot(enum dma_data_direction dir, bool coherent)

    Translate DMA API directions to IOMMU API page flags

    :param enum dma_data_direction dir:
        Direction of DMA transfer

    :param bool coherent:
        Is the DMA master cache-coherent?

.. _`dma_direction_to_prot.return`:

Return
------

corresponding IOMMU API page protection flags

.. _`iommu_dma_free`:

iommu_dma_free
==============

.. c:function:: void iommu_dma_free(struct device *dev, struct page **pages, size_t size, dma_addr_t *handle)

    Free a buffer allocated by \ :c:func:`iommu_dma_alloc`\ 

    :param struct device \*dev:
        Device which owns this buffer

    :param struct page \*\*pages:
        Array of buffer pages as returned by \ :c:func:`iommu_dma_alloc`\ 

    :param size_t size:
        Size of buffer in bytes

    :param dma_addr_t \*handle:
        DMA address of buffer

.. _`iommu_dma_free.description`:

Description
-----------

Frees both the pages associated with the buffer, and the array
describing them

.. _`iommu_dma_mmap`:

iommu_dma_mmap
==============

.. c:function:: int iommu_dma_mmap(struct page **pages, size_t size, struct vm_area_struct *vma)

    Map a buffer into provided user VMA

    :param struct page \*\*pages:
        Array representing buffer from \ :c:func:`iommu_dma_alloc`\ 

    :param size_t size:
        Size of buffer in bytes

    :param struct vm_area_struct \*vma:
        VMA describing requested userspace mapping

.. _`iommu_dma_mmap.description`:

Description
-----------

Maps the pages of the buffer in \ ``pages``\  into \ ``vma``\ . The caller is responsible
for verifying the correct size and protection of \ ``vma``\  beforehand.

.. This file was automatic generated / don't edit.

