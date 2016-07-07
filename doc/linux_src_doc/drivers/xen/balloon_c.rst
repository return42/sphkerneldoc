.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/xen/balloon.c

.. _`alloc_xenballooned_pages`:

alloc_xenballooned_pages
========================

.. c:function:: int alloc_xenballooned_pages(int nr_pages, struct page **pages)

    get pages that have been ballooned out

    :param int nr_pages:
        Number of pages to get

    :param struct page \*\*pages:
        pages returned
        \ ``return``\  0 on success, error otherwise

.. _`free_xenballooned_pages`:

free_xenballooned_pages
=======================

.. c:function:: void free_xenballooned_pages(int nr_pages, struct page **pages)

    return pages retrieved with get_ballooned_pages

    :param int nr_pages:
        Number of pages

    :param struct page \*\*pages:
        pages to return

.. This file was automatic generated / don't edit.

