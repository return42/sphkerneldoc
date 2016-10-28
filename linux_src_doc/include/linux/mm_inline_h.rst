.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mm_inline.h

.. _`page_is_file_cache`:

page_is_file_cache
==================

.. c:function:: int page_is_file_cache(struct page *page)

    should the page be on a file LRU or anon LRU?

    :param struct page \*page:
        the page to test

.. _`page_is_file_cache.description`:

Description
-----------

Returns 1 if \ ``page``\  is page cache page backed by a regular filesystem,
or 0 if \ ``page``\  is anonymous, tmpfs or otherwise ram or swap backed.
Used by functions that manipulate the LRU lists, to sort a page
onto the right LRU list.

We would like to get this info without a page flag, but the state
needs to survive until the page is last deleted from the LRU, which
could be as far down as \__page_cache_release.

.. _`page_lru_base_type`:

page_lru_base_type
==================

.. c:function:: enum lru_list page_lru_base_type(struct page *page)

    which LRU list type should a page be on?

    :param struct page \*page:
        the page to test

.. _`page_lru_base_type.description`:

Description
-----------

Used for LRU list index arithmetic.

Returns the base LRU type - file or anon - \ ``page``\  should be on.

.. _`page_off_lru`:

page_off_lru
============

.. c:function:: enum lru_list page_off_lru(struct page *page)

    which LRU list was page on? clearing its lru flags.

    :param struct page \*page:
        the page to test

.. _`page_off_lru.description`:

Description
-----------

Returns the LRU list a page was on, as an index into the array of LRU
lists; and clears its Unevictable or Active flags, ready for freeing.

.. _`page_lru`:

page_lru
========

.. c:function:: enum lru_list page_lru(struct page *page)

    which LRU list should a page be on?

    :param struct page \*page:
        the page to test

.. _`page_lru.description`:

Description
-----------

Returns the LRU list a page should be on, as an index
into the array of LRU lists.

.. This file was automatic generated / don't edit.

