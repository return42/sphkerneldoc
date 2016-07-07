.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/gup.c

.. _`get_user_pages_fast`:

get_user_pages_fast
===================

.. c:function:: int get_user_pages_fast(unsigned long start, int nr_pages, int write, struct page **pages)

    pin user pages in memory

    :param unsigned long start:
        starting user address

    :param int nr_pages:
        number of pages from start to pin

    :param int write:
        whether pages will be written to

    :param struct page \*\*pages:
        array that receives pointers to the pages pinned.
        Should be at least nr_pages long.

.. _`get_user_pages_fast.description`:

Description
-----------

Attempt to pin user pages in memory without taking mm->mmap_sem.
If not successful, it will fall back to taking the lock and
calling \ :c:func:`get_user_pages`\ .

Returns number of pages pinned. This may be fewer than the number
requested. If nr_pages is 0 or negative, returns 0. If no pages
were pinned, returns -errno.

.. This file was automatic generated / don't edit.

