.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ufs/util.c

.. _`ufs_get_locked_page`:

ufs_get_locked_page
===================

.. c:function:: struct page *ufs_get_locked_page(struct address_space *mapping, pgoff_t index)

    locate, pin and lock a pagecache page, if not exist read it from disk.

    :param struct address_space \*mapping:
        the address_space to search

    :param pgoff_t index:
        the page index

.. _`ufs_get_locked_page.description`:

Description
-----------

Locates the desired pagecache page, if not exist we'll read it,
locks it, increments its reference
count and returns its address.

.. This file was automatic generated / don't edit.

