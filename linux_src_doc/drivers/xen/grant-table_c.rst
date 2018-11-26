.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/xen/grant-table.c

.. _`gnttab_alloc_pages`:

gnttab_alloc_pages
==================

.. c:function:: int gnttab_alloc_pages(int nr_pages, struct page **pages)

    alloc pages suitable for grant mapping into

    :param nr_pages:
        number of pages to alloc
    :type nr_pages: int

    :param pages:
        returns the pages
    :type pages: struct page \*\*

.. _`gnttab_free_pages`:

gnttab_free_pages
=================

.. c:function:: void gnttab_free_pages(int nr_pages, struct page **pages)

    free pages allocated by \ :c:func:`gnttab_alloc_pages`\  \ ``nr_pages``\ ; number of pages to free

    :param nr_pages:
        *undescribed*
    :type nr_pages: int

    :param pages:
        the pages
    :type pages: struct page \*\*

.. _`gnttab_dma_alloc_pages`:

gnttab_dma_alloc_pages
======================

.. c:function:: int gnttab_dma_alloc_pages(struct gnttab_dma_alloc_args *args)

    alloc DMAable pages suitable for grant mapping into

    :param args:
        arguments to the function
    :type args: struct gnttab_dma_alloc_args \*

.. _`gnttab_dma_free_pages`:

gnttab_dma_free_pages
=====================

.. c:function:: int gnttab_dma_free_pages(struct gnttab_dma_alloc_args *args)

    free DMAable pages

    :param args:
        arguments to the function
    :type args: struct gnttab_dma_alloc_args \*

.. This file was automatic generated / don't edit.

