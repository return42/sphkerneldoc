.. -*- coding: utf-8; mode: rst -*-

======
page.c
======


.. _`fscache_mark_page_cached`:

fscache_mark_page_cached
========================

.. c:function:: void fscache_mark_page_cached (struct fscache_retrieval *op, struct page *page)

    Mark a page as being cached

    :param struct fscache_retrieval \*op:
        The retrieval op pages are being marked for

    :param struct page \*page:
        The page to be marked



.. _`fscache_mark_page_cached.description`:

Description
-----------

Mark a netfs page as being cached.  After this is called, the netfs
must call :c:func:`fscache_uncache_page` to remove the mark.



.. _`fscache_mark_pages_cached`:

fscache_mark_pages_cached
=========================

.. c:function:: void fscache_mark_pages_cached (struct fscache_retrieval *op, struct pagevec *pagevec)

    Mark pages as being cached

    :param struct fscache_retrieval \*op:
        The retrieval op pages are being marked for

    :param struct pagevec \*pagevec:
        The pages to be marked



.. _`fscache_mark_pages_cached.description`:

Description
-----------

Mark a bunch of netfs pages as being cached.  After this is called,
the netfs must call :c:func:`fscache_uncache_page` to remove the mark.

