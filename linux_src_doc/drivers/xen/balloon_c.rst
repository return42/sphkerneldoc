.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/xen/balloon.c

.. _`alloc_xenballooned_pages`:

alloc_xenballooned_pages
========================

.. c:function:: int alloc_xenballooned_pages(int nr_pages, struct page **pages)

    get pages that have been ballooned out

    :param nr_pages:
        Number of pages to get
    :type nr_pages: int

    :param pages:
        pages returned
        \ ``return``\  0 on success, error otherwise
    :type pages: struct page \*\*

.. _`free_xenballooned_pages`:

free_xenballooned_pages
=======================

.. c:function:: void free_xenballooned_pages(int nr_pages, struct page **pages)

    return pages retrieved with get_ballooned_pages

    :param nr_pages:
        Number of pages
    :type nr_pages: int

    :param pages:
        pages to return
    :type pages: struct page \*\*

.. This file was automatic generated / don't edit.

