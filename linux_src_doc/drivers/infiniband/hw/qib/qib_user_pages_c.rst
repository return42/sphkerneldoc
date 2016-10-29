.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_user_pages.c

.. _`qib_map_page`:

qib_map_page
============

.. c:function:: dma_addr_t qib_map_page(struct pci_dev *hwdev, struct page *page, unsigned long offset, size_t size, int direction)

    a safety wrapper around \ :c:func:`pci_map_page`\ 

    :param struct pci_dev \*hwdev:
        *undescribed*

    :param struct page \*page:
        *undescribed*

    :param unsigned long offset:
        *undescribed*

    :param size_t size:
        *undescribed*

    :param int direction:
        *undescribed*

.. _`qib_map_page.description`:

Description
-----------

A dma_addr of all 0's is interpreted by the chip as "disabled".
Unfortunately, it can also be a valid dma_addr returned on some
architectures.

The powerpc iommu assigns dma_addrs in ascending order, so we don't
have to bother with retries or mapping a dummy page to insure we
don't just get the same mapping again.

I'm sure we won't be so lucky with other iommu's, so FIXME.

.. _`qib_get_user_pages`:

qib_get_user_pages
==================

.. c:function:: int qib_get_user_pages(unsigned long start_page, size_t num_pages, struct page **p)

    lock user pages into memory

    :param unsigned long start_page:
        the start page

    :param size_t num_pages:
        the number of pages

    :param struct page \*\*p:
        the output page structures

.. _`qib_get_user_pages.description`:

Description
-----------

This function takes a given start page (page aligned user virtual
address) and pins it and the following specified number of pages.  For
now, num_pages is always 1, but that will probably change at some point
(because caller is doing expected sends on a single virtually contiguous
buffer, so we can do all pages at once).

.. This file was automatic generated / don't edit.
