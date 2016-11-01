.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/swap.c

.. _`put_pages_list`:

put_pages_list
==============

.. c:function:: void put_pages_list(struct list_head *pages)

    release a list of pages

    :param struct list_head \*pages:
        list of pages threaded on page->lru

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

    :param struct page \*page:
        the page to add

.. _`lru_cache_add`:

lru_cache_add
=============

.. c:function:: void lru_cache_add(struct page *page)

    add a page to a page list

    :param struct page \*page:
        the page to be added to the LRU.

.. _`lru_cache_add.description`:

Description
-----------

Queue the page for addition to the LRU via pagevec. The decision on whether
to add the page to the [in]active [file\|anon] list is deferred until the
pagevec is drained. This gives a chance for the caller of \ :c:func:`lru_cache_add`\ 
have the page added to the active list using \ :c:func:`mark_page_accessed`\ .

.. _`add_page_to_unevictable_list`:

add_page_to_unevictable_list
============================

.. c:function:: void add_page_to_unevictable_list(struct page *page)

    add a page to the unevictable list

    :param struct page \*page:
        the page to be added to the unevictable list

.. _`add_page_to_unevictable_list.description`:

Description
-----------

Add page directly to its zone's unevictable list.  To avoid races with
tasks that might be making the page evictable, through eg. munlock,
munmap or exit, while it's not on the lru, we want to add the page
while it's locked or otherwise "invisible" to other tasks.  This is
difficult to do when using the pagevec cache, so bypass that.

.. _`lru_cache_add_active_or_unevictable`:

lru_cache_add_active_or_unevictable
===================================

.. c:function:: void lru_cache_add_active_or_unevictable(struct page *page, struct vm_area_struct *vma)

    :param struct page \*page:
        the page to be added to LRU

    :param struct vm_area_struct \*vma:
        vma in which page is mapped for determining reclaimability

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

    :param struct page \*page:
        page to deactivate

.. _`deactivate_file_page.description`:

Description
-----------

This function hints the VM that \ ``page``\  is a good reclaim candidate,
for example if its invalidation fails due to the page being dirty
or under writeback.

.. _`deactivate_page`:

deactivate_page
===============

.. c:function:: void deactivate_page(struct page *page)

    deactivate a page

    :param struct page \*page:
        page to deactivate

.. _`deactivate_page.description`:

Description
-----------

deactivate_page() moves \ ``page``\  to the inactive list if \ ``page``\  was on the active
list and was not an unevictable page.  This is done to accelerate the reclaim
of \ ``page``\ .

.. _`release_pages`:

release_pages
=============

.. c:function:: void release_pages(struct page **pages, int nr, bool cold)

    batched \ :c:func:`put_page`\ 

    :param struct page \*\*pages:
        array of pages to release

    :param int nr:
        number of pages

    :param bool cold:
        whether the pages are cache cold

.. _`release_pages.description`:

Description
-----------

Decrement the reference count on all the pages in \ ``pages``\ .  If it
fell to zero, remove the page from the LRU and free it.

.. _`pagevec_lookup_entries`:

pagevec_lookup_entries
======================

.. c:function:: unsigned pagevec_lookup_entries(struct pagevec *pvec, struct address_space *mapping, pgoff_t start, unsigned nr_pages, pgoff_t *indices)

    gang pagecache lookup

    :param struct pagevec \*pvec:
        Where the resulting entries are placed

    :param struct address_space \*mapping:
        The address_space to search

    :param pgoff_t start:
        The starting entry index

    :param unsigned nr_pages:
        *undescribed*

    :param pgoff_t \*indices:
        The cache indices corresponding to the entries in \ ``pvec``\ 

.. _`pagevec_lookup_entries.description`:

Description
-----------

pagevec_lookup_entries() will search for and return a group of up
to \ ``nr_entries``\  pages and shadow entries in the mapping.  All
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

    :param struct pagevec \*pvec:
        The pagevec to prune

.. _`pagevec_remove_exceptionals.description`:

Description
-----------

pagevec_lookup_entries() fills both pages and exceptional radix
tree entries into the pagevec.  This function prunes all
exceptionals from \ ``pvec``\  without leaving holes, so that it can be
passed on to page-only pagevec operations.

.. _`pagevec_lookup`:

pagevec_lookup
==============

.. c:function:: unsigned pagevec_lookup(struct pagevec *pvec, struct address_space *mapping, pgoff_t start, unsigned nr_pages)

    gang pagecache lookup

    :param struct pagevec \*pvec:
        Where the resulting pages are placed

    :param struct address_space \*mapping:
        The address_space to search

    :param pgoff_t start:
        The starting page index

    :param unsigned nr_pages:
        The maximum number of pages

.. _`pagevec_lookup.description`:

Description
-----------

pagevec_lookup() will search for and return a group of up to \ ``nr_pages``\  pages
in the mapping.  The pages are placed in \ ``pvec``\ .  \ :c:func:`pagevec_lookup`\  takes a
reference against the pages in \ ``pvec``\ .

The search returns a group of mapping-contiguous pages with ascending
indexes.  There may be holes in the indices due to not-present pages.

\ :c:func:`pagevec_lookup`\  returns the number of pages which were found.

.. This file was automatic generated / don't edit.

