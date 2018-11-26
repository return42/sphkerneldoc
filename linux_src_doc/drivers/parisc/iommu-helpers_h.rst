.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parisc/iommu-helpers.h

.. _`iommu_fill_pdir`:

iommu_fill_pdir
===============

.. c:function:: unsigned int iommu_fill_pdir(struct ioc *ioc, struct scatterlist *startsg, int nents, unsigned long hint, void (*iommu_io_pdir_entry)(u64 *, space_t, unsigned long, unsigned long))

    Insert coalesced scatter/gather chunks into the I/O Pdir.

    :param ioc:
        The I/O Controller.
    :type ioc: struct ioc \*

    :param startsg:
        The scatter/gather list of coalesced chunks.
    :type startsg: struct scatterlist \*

    :param nents:
        The number of entries in the scatter/gather list.
    :type nents: int

    :param hint:
        The DMA Hint.
    :type hint: unsigned long

    :param void (\*iommu_io_pdir_entry)(u64 \*, space_t, unsigned long, unsigned long):
        *undescribed*

.. _`iommu_fill_pdir.description`:

Description
-----------

This function inserts the coalesced scatter/gather list chunks into the
I/O Controller's I/O Pdir.

.. This file was automatic generated / don't edit.

