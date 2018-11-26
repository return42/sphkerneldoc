.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/swap.c

.. _`put_pages_list`:

put_pages_list
==============

.. c:function:: void put_pages_list(struct list_head *pages)

    release a list of pages

    :param pages:
        list of pages threaded on page->lru
    :type pages: struct list_head \*

.. _`put_pages_list.description`:

Description
-----------

Release a list of pages which are strung together on page.lru.  Currently
used by \ :c:func:`read_cache_pages`\  and related error recovery code.

.. _`lru_cache_add_anon`:

lru_cache_add_anon
==================

.. c:function:: void lru_cache_add_anon(struct page *page)

    add a page to the page lists

    :param page:
        the page to add
    :type page: struct page \*

.. _`lru_cache_add`:

lru_cache_add
=============

.. c:function:: void lru_cache_add(struct page *page)

    add a page to a page list

    :param page:
        the page to be added to the LRU.
    :type page: struct page \*

.. _`lru_cache_add.description`:

Description
-----------

Queue the page for addition to the LRU via pagevec. The decision on whether
to add the page to the [in]active [file\|anon] list is deferred until the
pagevec is drained. This gives a chance for the caller of \ :c:func:`lru_cache_add`\ 
have the page added to the active list using \ :c:func:`mark_page_accessed`\ .

.. _`lru_cache_add_active_or_unevictable`:

lru_cache_add_active_or_unevictable
===================================

.. c:function:: void lru_cache_add_active_or_unevictable(struct page *page, struct vm_area_struct *vma)

    :param page:
        the page to be added to LRU
    :type page: struct page \*

    :param vma:
        vma in which page is mapped for determining reclaimability
    :type vma: struct vm_area_struct \*

.. _`lru_cache_add_active_or_unevictable.description`:

Description
-----------

Place \ ``page``\  on the active or unevictable LRU list, depending on its
evictability.  Note that if the page is not evictable, it goes
directly back onto it's zone's unevictable list, it does NOT use a
per cpu pagevec.

.. _`deactivate_file_page`:

deactivate_file_page
====================

.. c:function:: void deactivate_file_page(struct page *page)

    forcefully deactivate a file page

    :param page:
        page to deactivate
    :type page: struct page \*

.. _`deactivate_file_page.description`:

Description
-----------

This function hints the VM that \ ``page``\  is a good reclaim candidate,
for example if its invalidation fails due to the page being dirty
or under writeback.

.. _`mark_page_lazyfree`:

mark_page_lazyfree
==================

.. c:function:: void mark_page_lazyfree(struct page *page)

    make an anon page lazyfree

    :param page:
        page to deactivate
    :type page: struct page \*

.. _`mark_page_lazyfree.description`:

Description
-----------

\ :c:func:`mark_page_lazyfree`\  moves \ ``page``\  to the inactive file list.
This is done to accelerate the reclaim of \ ``page``\ .

.. _`release_pages`:

release_pages
=============

.. c:function:: void release_pages(struct page **pages, int nr)

    batched \ :c:func:`put_page`\ 

    :param pages:
        array of pages to release
    :type pages: struct page \*\*

    :param nr:
        number of pages
    :type nr: int

.. _`release_pages.description`:

Description
-----------

Decrement the reference count on all the pages in \ ``pages``\ .  If it
fell to zero, remove the page from the LRU and free it.

.. _`pagevec_lookup_entries`:

pagevec_lookup_entries
======================

.. c:function:: unsigned pagevec_lookup_entries(struct pagevec *pvec, struct address_space *mapping, pgoff_t start, unsigned nr_entries, pgoff_t *indices)

    gang pagecache lookup

    :param pvec:
        Where the resulting entries are placed
    :type pvec: struct pagevec \*

    :param mapping:
        The address_space to search
    :type mapping: struct address_space \*

    :param start:
        The starting entry index
    :type start: pgoff_t

    :param nr_entries:
        The maximum number of pages
    :type nr_entries: unsigned

    :param indices:
        The cache indices corresponding to the entries in \ ``pvec``\ 
    :type indices: pgoff_t \*

.. _`pagevec_lookup_entries.description`:

Description
-----------

\ :c:func:`pagevec_lookup_entries`\  will search for and return a group of up
to \ ``nr_pages``\  pages and shadow entries in the mapping.  All
entries are placed in \ ``pvec``\ .  \ :c:func:`pagevec_lookup_entries`\  takes a
reference against actual pages in \ ``pvec``\ .

The search returns a group of mapping-contiguous entries with
ascending indexes.  There may be holes in the indices due to
not-present entries.

\ :c:func:`pagevec_lookup_entries`\  returns the number of entries which were
found.

.. _`pagevec_remove_exceptionals`:

pagevec_remove_exceptionals
===========================

.. c:function:: void pagevec_remove_exceptionals(struct pagevec *pvec)

    pagevec exceptionals pruning

    :param pvec:
        The pagevec to prune
    :type pvec: struct pagevec \*

.. _`pagevec_remove_exceptionals.description`:

Description
-----------

\ :c:func:`pagevec_lookup_entries`\  fills both pages and exceptional radix
tree entries into the pagevec.  This function prunes all
exceptionals from \ ``pvec``\  without leaving holes, so that it can be
passed on to page-only pagevec operations.

.. _`pagevec_lookup_range`:

pagevec_lookup_range
====================

.. c:function:: unsigned pagevec_lookup_range(struct pagevec *pvec, struct address_space *mapping, pgoff_t *start, pgoff_t end)

    gang pagecache lookup

    :param pvec:
        Where the resulting pages are placed
    :type pvec: struct pagevec \*

    :param mapping:
        The address_space to search
    :type mapping: struct address_space \*

    :param start:
        The starting page index
    :type start: pgoff_t \*

    :param end:
        The final page index
    :type end: pgoff_t

.. _`pagevec_lookup_range.description`:

Description
-----------

\ :c:func:`pagevec_lookup_range`\  will search for & return a group of up to PAGEVEC_SIZE
pages in the mapping starting from index \ ``start``\  and upto index \ ``end``\ 
(inclusive).  The pages are placed in \ ``pvec``\ .  \ :c:func:`pagevec_lookup`\  takes a
reference against the pages in \ ``pvec``\ .

The search returns a group of mapping-contiguous pages with ascending
indexes.  There may be holes in the indices due to not-present pages. We
also update \ ``start``\  to index the next page for the traversal.

\ :c:func:`pagevec_lookup_range`\  returns the number of pages which were found. If this
number is smaller than PAGEVEC_SIZE, the end of specified range has been
reached.

.. This file was automatic generated / don't edit.

