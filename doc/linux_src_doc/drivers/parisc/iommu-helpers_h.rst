.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parisc/iommu-helpers.h

.. _`iommu_fill_pdir`:

iommu_fill_pdir
===============

.. c:function:: unsigned int iommu_fill_pdir(struct ioc *ioc, struct scatterlist *startsg, int nents, unsigned long hint, void (*iommu_io_pdir_entry)(u64 *, space_t, unsigned long, unsigned long))

    Insert coalesced scatter/gather chunks into the I/O Pdir.

    :param struct ioc \*ioc:
        The I/O Controller.

    :param struct scatterlist \*startsg:
        The scatter/gather list of coalesced chunks.

    :param int nents:
        The number of entries in the scatter/gather list.

    :param unsigned long hint:
        The DMA Hint.

    :param void (\*iommu_io_pdir_entry)(u64 \*, space_t, unsigned long, unsigned long):
        *undescribed*

.. _`iommu_fill_pdir.description`:

Description
-----------

This function inserts the coalesced scatter/gather list chunks into the
I/O Controller's I/O Pdir.

.. This file was automatic generated / don't edit.

