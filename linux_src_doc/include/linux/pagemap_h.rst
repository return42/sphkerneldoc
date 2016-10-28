.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/pagemap.h

.. _`find_get_page`:

find_get_page
=============

.. c:function:: struct page *find_get_page(struct address_space *mapping, pgoff_t offset)

    find and get a page reference

    :param struct address_space \*mapping:
        the address_space to search

    :param pgoff_t offset:
        the page index

.. _`find_get_page.description`:

Description
-----------

Looks up the page cache slot at \ ``mapping``\  & \ ``offset``\ .  If there is a
page cache page, it is returned with an increased refcount.

Otherwise, \ ``NULL``\  is returned.

.. _`find_lock_page`:

find_lock_page
==============

.. c:function:: struct page *find_lock_page(struct address_space *mapping, pgoff_t offset)

    locate, pin and lock a pagecache page pagecache_get_page - find and get a page reference

    :param struct address_space \*mapping:
        the address_space to search

    :param pgoff_t offset:
        the page index

.. _`find_lock_page.description`:

Description
-----------

Looks up the page cache slot at \ ``mapping``\  & \ ``offset``\ .  If there is a
page cache page, it is returned locked and with an increased
refcount.

Otherwise, \ ``NULL``\  is returned.

\ :c:func:`find_lock_page`\  may sleep.

.. _`find_or_create_page`:

find_or_create_page
===================

.. c:function:: struct page *find_or_create_page(struct address_space *mapping, pgoff_t offset, gfp_t gfp_mask)

    locate or add a pagecache page

    :param struct address_space \*mapping:
        the page's address_space

    :param pgoff_t offset:
        *undescribed*

    :param gfp_t gfp_mask:
        page allocation mode

.. _`find_or_create_page.description`:

Description
-----------

Looks up the page cache slot at \ ``mapping``\  & \ ``offset``\ .  If there is a
page cache page, it is returned locked and with an increased
refcount.

If the page is not present, a new page is allocated using \ ``gfp_mask``\ 
and added to the page cache and the VM's LRU list.  The page is
returned locked and with an increased refcount.

On memory exhaustion, \ ``NULL``\  is returned.

\ :c:func:`find_or_create_page`\  may sleep, even if \ ``gfp_flags``\  specifies an
atomic allocation!

.. _`grab_cache_page_nowait`:

grab_cache_page_nowait
======================

.. c:function:: struct page *grab_cache_page_nowait(struct address_space *mapping, pgoff_t index)

    returns locked page at given index in given cache

    :param struct address_space \*mapping:
        target address_space

    :param pgoff_t index:
        the page index

.. _`grab_cache_page_nowait.description`:

Description
-----------

Same as \ :c:func:`grab_cache_page`\ , but do not wait if the page is unavailable.
This is intended for speculative data generators, where the data can
be regenerated if the page couldn't be grabbed.  This routine should
be safe to call while holding the lock for another page.

Clear \__GFP_FS when allocating the page to avoid recursion into the fs
and deadlock against the caller's locked page.

.. This file was automatic generated / don't edit.

