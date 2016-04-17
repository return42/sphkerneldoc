.. -*- coding: utf-8; mode: rst -*-

=============
grant-table.c
=============


.. _`gnttab_alloc_pages`:

gnttab_alloc_pages
==================

.. c:function:: int gnttab_alloc_pages (int nr_pages, struct page **pages)

    alloc pages suitable for grant mapping into

    :param int nr_pages:
        number of pages to alloc

    :param struct page \*\*pages:
        returns the pages



.. _`gnttab_free_pages`:

gnttab_free_pages
=================

.. c:function:: void gnttab_free_pages (int nr_pages, struct page **pages)

    free pages allocated by gnttab_alloc_pages() @nr_pages; number of pages to free

    :param int nr_pages:

        *undescribed*

    :param struct page \*\*pages:
        the pages

