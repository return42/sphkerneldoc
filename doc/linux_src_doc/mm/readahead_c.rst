.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/readahead.c

.. _`read_cache_pages`:

read_cache_pages
================

.. c:function:: int read_cache_pages(struct address_space *mapping, struct list_head *pages, int (*) filler (void *, struct page *, void *data)

    populate an address space with some pages & start reads against them

    :param struct address_space \*mapping:
        the address_space

    :param struct list_head \*pages:
        The address of a list_head which contains the target pages.  These
        pages have their ->index populated and are otherwise uninitialised.

    :param (int (\*) filler (void \*, struct page \*):
        callback routine for filling a single page.

    :param void \*data:
        private data for the callback routine.

.. _`read_cache_pages.description`:

Description
-----------

Hides the details of the LRU cache etc from the filesystems.

.. _`page_cache_sync_readahead`:

page_cache_sync_readahead
=========================

.. c:function:: void page_cache_sync_readahead(struct address_space *mapping, struct file_ra_state *ra, struct file *filp, pgoff_t offset, unsigned long req_size)

    generic file readahead

    :param struct address_space \*mapping:
        address_space which holds the pagecache and I/O vectors

    :param struct file_ra_state \*ra:
        file_ra_state which holds the readahead state

    :param struct file \*filp:
        passed on to ->\ :c:func:`readpage`\  and ->\ :c:func:`readpages`\ 

    :param pgoff_t offset:
        start offset into \ ``mapping``\ , in pagecache page-sized units

    :param unsigned long req_size:
        hint: total size of the read which the caller is performing in
        pagecache pages

.. _`page_cache_sync_readahead.description`:

Description
-----------

\ :c:func:`page_cache_sync_readahead`\  should be called when a cache miss happened:
it will submit the read.  The readahead logic may decide to piggyback more
pages onto the read request if access patterns suggest it will improve
performance.

.. _`page_cache_async_readahead`:

page_cache_async_readahead
==========================

.. c:function:: void page_cache_async_readahead(struct address_space *mapping, struct file_ra_state *ra, struct file *filp, struct page *page, pgoff_t offset, unsigned long req_size)

    file readahead for marked pages

    :param struct address_space \*mapping:
        address_space which holds the pagecache and I/O vectors

    :param struct file_ra_state \*ra:
        file_ra_state which holds the readahead state

    :param struct file \*filp:
        passed on to ->\ :c:func:`readpage`\  and ->\ :c:func:`readpages`\ 

    :param struct page \*page:
        the page at \ ``offset``\  which has the PG_readahead flag set

    :param pgoff_t offset:
        start offset into \ ``mapping``\ , in pagecache page-sized units

    :param unsigned long req_size:
        hint: total size of the read which the caller is performing in
        pagecache pages

.. _`page_cache_async_readahead.description`:

Description
-----------

\ :c:func:`page_cache_async_readahead`\  should be called when a page is used which
has the PG_readahead flag; this is a marker to suggest that the application
has used up enough of the readahead window that we should start pulling in
more pages.

.. This file was automatic generated / don't edit.

